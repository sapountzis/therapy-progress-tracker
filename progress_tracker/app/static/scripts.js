function switchTab(tabName) {
  
    document.querySelectorAll('.tab').forEach(tab => {
        tab.classList.remove('active');
    });
    
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    
    const selectedTab = document.querySelector(`#${tabName}Tab`);
    const selectedContent = document.querySelector(`#${tabName}`);
    
    selectedTab.classList.add('active');
    selectedContent.classList.add('active');
}

document.addEventListener('DOMContentLoaded', function() {
    switchTab('manageSessions');
});


function loadSessionsForComparison(clientId) {
    if (!clientId) return;
    
    fetch(`/api/clients/${clientId}/sessions`)
        .then(response => response.json())
        .then(sessions => {
            const session1Select = document.getElementById('session1');
            const session2Select = document.getElementById('session2');
            
            const options = sessions.map(session => `
                <option value="${session.id}">
                    ${new Date(session.timestamp).toLocaleDateString()}
                </option>
            `).join('');
            
            session1Select.innerHTML = '<option value="">Select session...</option>' + options;
            session2Select.innerHTML = '<option value="">Select session...</option>' + options;
        });
}

function handleCompareSubmit(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    const session1 = formData.get('session1_id');
    const session2 = formData.get('session2_id');
    const clientId = formData.get('client_id');

    const progressSection = document.querySelector('.progress-summary');
    progressSection.innerHTML = `
        <div class="loading-container">
            <div class="loading-bar">
                <div class="loading-progress"></div>
            </div>
            <p>Comparing sessions...</p>
        </div>
    `;

    const requestFormData = new FormData();
    requestFormData.append('client_id', clientId);
    requestFormData.append('session_ids', session1);
    requestFormData.append('session_ids', session2);

    fetch('/api/compare-sessions', {
        method: 'POST',
        body: requestFormData
    })
    .then(response => response.json())
    .then(data => {
        const progressSection = document.querySelector('.progress-summary');
        const clientInfo = document.querySelector('.client-info');
        
        clientInfo.innerHTML = `
            <p>Comparing sessions from ${data.session_dates.map(date => 
                new Date(date).toLocaleDateString()
            ).join(' and ')}</p>
        `;

        progressSection.innerHTML = `
            <h3>Progress Summary:</h3>
            <p>${data.progress}</p>
            <h4>Reason:</h4>
            <p>${data.reason}</p>
        `;
    })
    .catch(error => {
        console.error('Error comparing sessions:', error);
        progressSection.innerHTML = `
            <div class="error-message">
                <p>Error comparing sessions. Please try again.</p>
            </div>
        `;
    });
}

async function handleClientSubmit(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    try {
        const response = await fetch('/api/clients', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            window.location.reload();
        } else {
            alert('Failed to create client');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while creating the client');
    }
}

async function handleSessionUpload(event) {
    event.preventDefault();
    
    const formData = new FormData(event.target);
    try {
        const response = await fetch('/api/sessions', {
            method: 'POST',
            body: formData
        });
        
        if (response.ok) {
            window.location.reload();
        } else {
            alert('Failed to upload session');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while uploading the session');
    }
}

async function loadClientSessions(clientId) {
    if (!clientId) {
        document.querySelector('.session-list').innerHTML = '';
        return;
    }

    try {
        const response = await fetch(`/api/clients/${clientId}/sessions`);
        if (!response.ok) {
            throw new Error('Failed to fetch sessions');
        }
        
        const sessions = await response.json();
        const sessionListHtml = sessions.length ? sessions.map((session, index) => {
            const sessionData = session.data;
            return `
                <div class="accordion-item">
                    <button class="accordion-header" onclick="toggleAccordion(${index})">
                        Session from ${new Date(session.timestamp).toLocaleDateString()}
                        <span class="accordion-icon">+</span>
                    </button>
                    <div class="accordion-content">
                        <div class="session-summary">
                            <h5>Brief Summary:</h5>
                            <p>${sessionData["Brief Summary of Session"] || 'No summary available'}</p>
                            
                            <h5>Clinical Assessment:</h5>
                            <p>${sessionData["Clinical Assessment"]?.["Clinical Conceptualization"] || 'No assessment available'}</p>
                            
                            <h5>Diagnoses:</h5>
                            <ul>
                                ${Object.entries(sessionData["Clinical Assessment"]?.["Diagnosiss"] || {})
                                    .map(([name, diagnosis]) => `
                                        <li>
                                            <strong>${diagnosis.Description}:</strong>
                                            ${diagnosis.Reasoning}
                                            (DSM: ${diagnosis["DSM- Code"]})
                                        </li>
                                    `).join('')}
                            </ul>

                            <h5>Symptoms:</h5>
                            <ul>
                                ${Object.entries(sessionData["Psychological Factors"]?.["Symptoms"] || {})
                                    .map(([name, symptom]) => `
                                        <li>
                                            <strong>${symptom.Description}:</strong><br>
                                            Onset: ${symptom.Onset}<br>
                                            Frequency: ${symptom.Frequency}<br>
                                            Intensity: ${symptom.Intensity}
                                        </li>
                                    `).join('')}
                            </ul>

                            <h5>Assessment Tools:</h5>
                            <ul>
                                ${Object.entries(sessionData["Clinical Assessment"]?.["Assessment Tools"] || {})
                                    .map(([name, tool]) => `
                                        <li>
                                            <strong>${tool.Description}:</strong>
                                            ${tool.Results}
                                        </li>
                                    `).join('')}
                            </ul>
                        </div>
                    </div>
                </div>
            `;
        }).join('') : '<p>No sessions found for this client.</p>';

        document.querySelector('.session-list').innerHTML = sessionListHtml;
        document.getElementById('existingClient').value = clientId;
    } catch (error) {
        console.error('Error loading sessions:', error);
        document.querySelector('.session-list').innerHTML = 
            '<p class="error">Error loading sessions</p>';
    }
}

function toggleAccordion(index) {
    const accordionItems = document.querySelectorAll('.accordion-item');
    const clickedItem = accordionItems[index];
    const content = clickedItem.querySelector('.accordion-content');
    const icon = clickedItem.querySelector('.accordion-icon');
    
    accordionItems.forEach((item, idx) => {
        if (idx !== index) {
            item.querySelector('.accordion-content').style.maxHeight = null;
            item.querySelector('.accordion-icon').textContent = '+';
            item.classList.remove('active');
        }
    });
    
    clickedItem.classList.toggle('active');
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
        icon.textContent = '+';
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
        icon.textContent = '−';
    }
}