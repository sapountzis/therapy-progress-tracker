from typing import Any

from pydantic import BaseModel, Field


class Symptom(BaseModel):
    description: str = Field(
        alias="Description",
        description="Description of the symptom.",
        default_factory=str,
    )
    onset: str = Field(
        alias="Onset",
        description="Describes when the symptom first started.",
        default_factory=str,
    )
    frequency: str = Field(
        alias="Frequency",
        description="Describes how often the symptom occurs.",
        default_factory=str,
    )
    ascendance: str = Field(
        alias="Ascendance",
        description="Describes any improvements or progress with the symptom.",
        default_factory=str,
    )
    intensity: str = Field(
        alias="Intensity",
        description="Describes severity of the symptom.",
        default_factory=str,
    )
    duration: str = Field(
        alias="Duration",
        description="Describes how long the symptom has been present.",
        default_factory=str,
    )
    quote_symptom: str = Field(
        alias="Quote (Symptom)",
        description="Presents a client quote about the symptom.",
        default_factory=str,
    )


class Diagnosis(BaseModel):
    description: str = Field(
        alias="Description",
        description="Identifies the most accurate DSM-5 diagnosis.",
        default_factory=str,
    )
    dsm_code: str = Field(
        alias="DSM- Code",
        description="Provides the DSM-5 code for the diagnosis.",
        default_factory=str,
    )
    icd_code: str = Field(
        alias="ICD- Code",
        description="Provides the ICD-10 code for the diagnosis.",
        default_factory=str,
    )
    reasoning: str = Field(
        alias="Reasoning",
        description="Explains why the diagnosis fits the client.",
        default_factory=str,
    )


class AssessmentTool(BaseModel):
    description: str = Field(
        alias="Description",
        description="Description of the assessment tool.",
        default_factory=str,
    )
    purpose: str = Field(
        alias="Purpose",
        description="Describes the purpose of using this assessment.",
        default_factory=str,
    )
    results: str = Field(
        alias="Results",
        description="Summarizes assessment results and significance.",
        default_factory=str,
    )
    status: str = Field(
        alias="Status",
        description="Describes status of assessments.",
        default_factory=str,
    )


class Presentation(BaseModel):
    chief_complaint: str = Field(
        alias="Chief Complaint",
        description="Details the primary problems or symptoms that brought the client to therapy.",
        default_factory=str,
    )
    quote_chief_complaint: str = Field(
        alias="Quote (Chief Complaint)",
        description="Presents a client quote about their presenting problem(s).",
        default_factory=str,
    )
    impairments_and_challenges: str = Field(
        alias="Impairments and Challenges",
        description="Details areas of impairment and their impact on client's life.",
        default_factory=str,
    )
    family_dynamics: str = Field(
        alias="Family Dynamics",
        description="Describes relationships and interactions between family members.",
        default_factory=str,
    )


class PsychologicalFactors(BaseModel):
    family_mental_health_history: str = Field(
        alias="Family Mental Health History",
        description="Describes family mental health issues and impact.",
        default_factory=str,
    )
    previous_mental_health_treatments: str = Field(
        alias="Previous Mental Health Treatments",
        description="Summarizes previous mental health treatment details.",
        default_factory=str,
    )
    previous_mental_health_assessments: str = Field(
        alias="Previous Mental Health Assessments",
        description="Summarizes previous mental health assessments and diagnoses.",
        default_factory=str,
    )
    symptoms: dict[str, Symptom] = Field(
        alias="Symptoms",
        description="Lists symptoms experienced by the client.",
        default_factory=dict,
    )


class BiologicalFactors(BaseModel):
    allergies: str = Field(
        alias="Allergies",
        description="Summarizes any allergies reported.",
        default_factory=str,
    )
    family_medical_history: str = Field(
        alias="Family Medical History",
        description="Describes relevant family medical history.",
        default_factory=str,
    )
    medical_conditions: str = Field(
        alias="Medical Conditions",
        description="Describes chronic health conditions and any possible somatic disorders.",
        default_factory=str,
    )
    sleep: str = Field(
        alias="Sleep",
        description="Describes sleep patterns and related issues.",
        default_factory=str,
    )
    nutrition: str = Field(
        alias="Nutrition",
        description="Describes diet, nutrition, and any related eating disorders.",
        default_factory=str,
    )
    physical_activity: str = Field(
        alias="Physical Activity",
        description="Describes physical activity and its effects.",
        default_factory=str,
    )
    sexual_activity: str = Field(
        alias="Sexual Activity",
        description="Describes any relevant sexual activity.",
        default_factory=str,
    )
    substances: str = Field(
        alias="Substances",
        description="Describes substance use details.",
        default_factory=str,
    )


class SocialFactors(BaseModel):
    work_or_school: str = Field(
        alias="Work or School",
        description="Describes work/school activities and any related issues.",
        default_factory=str,
    )
    relationships: str = Field(
        alias="Relationships",
        description="Describes key relationships and any difficulties.",
        default_factory=str,
    )
    recreation: str = Field(
        alias="Recreation",
        description="Describes recreational activities and their effects.",
        default_factory=str,
    )
    family_social_history: str = Field(
        alias="Family Social History",
        description="Describes family relationship history and stressors.",
        default_factory=str,
    )
    cultural_considerations: str = Field(
        alias="Cultural Considerations",
        description="Describes other relevant social factors.",
        default_factory=str,
    )
    traumatic_experiences: str = Field(
        alias="Traumatic Experiences",
        description="Describes any traumatic experiences and impact.",
        default_factory=str,
    )
    quote_traumatic_experiences: str = Field(
        alias="Quote (Traumatic Experiences)",
        description="Presents a client quote about the traumatic experience.",
        default_factory=str,
    )


class ClinicalAssessment(BaseModel):
    clinical_conceptualization: str = Field(
        alias="Clinical Conceptualization",
        description="Summarizes contributing biopsychosocial factors.",
        default_factory=str,
    )
    diagnoses: dict[str, Diagnosis] = Field(
        alias="Diagnoses",
        description="Diagnosis details.",
        default_factory=dict,
    )
    assessment_tools: dict[str, AssessmentTool] = Field(
        alias="Assessment Tools",
        description="Identifies assessments used.",
        default_factory=dict,
    )


class MentalStatusExam(BaseModel):
    mood_and_affect: str = Field(
        alias="Mood and Affect",
        description="Describes current mood and affect.",
        default_factory=str,
    )
    speech_and_language: str = Field(
        alias="Speech and Language",
        description="Describes speech and language abilities.",
        default_factory=str,
    )
    thought_process_and_content: str = Field(
        alias="Thought Process and Content",
        description="Describes thought process and content.",
        default_factory=str,
    )
    orientation: str = Field(
        alias="Orientation",
        description="Describes orientation to surroundings.",
        default_factory=str,
    )
    perceptual_disturbances: str = Field(
        alias="Perceptual Disturbances",
        description="Describes any perceptual disturbances.",
        default_factory=str,
    )
    cognition: str = Field(
        alias="Cognition",
        description="Describes cognitive abilities and memory impairments.",
        default_factory=str,
    )
    insight: str = Field(
        alias="Insight",
        description="The client demonstrated insight into their stress and its impact on their life.",
        default_factory=str,
    )


class RiskAssessment(BaseModel):
    risks_or_safety_concerns: str = Field(
        alias="Risks or Safety Concerns",
        description="Describes risks identified, if any.",
        default_factory=str,
    )
    hopelessness: str = Field(
        alias="Hopelessness",
        description="Describes level of hopelessness and systemic depression.",
        default_factory=str,
    )
    suicidal_thoughts_or_attempts: str = Field(
        alias="Suicidal Thoughts or Attempts",
        description="Describes any suicidal thoughts/attempts.",
        default_factory=str,
    )
    self_harm: str = Field(
        alias="Self Harm",
        description="Describes any self-harm instances.",
        default_factory=str,
    )
    dangerous_to_others: str = Field(
        alias="Dangerous to Others",
        description="Describes danger to self/others.",
        default_factory=str,
    )
    quote_risk: str = Field(
        alias="Quote (Risk)",
        description="Presents a client quote about risks.",
        default_factory=str,
    )
    safety_plan: str = Field(
        alias="Safety Plan",
        description="Describes any safety plans in place.",
        default_factory=str,
    )


class StrengthsAndResources(BaseModel):
    internal_strengths: str = Field(
        alias="Internal Strengths",
        description="Describes internal coping strengths.",
        default_factory=str,
    )
    external_resources: str = Field(
        alias="External Resources",
        description="Describes external support resources.",
        default_factory=str,
    )
    quote_resources: str = Field(
        alias="Quote (Resources)",
        description="Presents a client quote about strengths/resources.",
        default_factory=str,
    )


class ProgressAndResponse(BaseModel):
    response_to_treatment: str = Field(
        alias="Response to Treatment",
        description="Describes client's response to treatment so far.",
        default_factory=str,
    )
    specific_examples_or_instances: str = Field(
        alias="Specific Examples or Instances",
        description="Describes examples for progress.",
        default_factory=str,
    )
    challenges_to_progress: str = Field(
        alias="Challenges to Progress",
        description="Identifies concerns about therapy process.",
        default_factory=str,
    )
    practitioners_observations_and_reflections: str = Field(
        alias="Practitioner's Observations and Reflections",
        description="Describes observations and insights.",
        default_factory=str,
    )


class TherapySessionSummary(BaseModel):
    brief_summary_of_session: str = Field(
        alias="Brief Summary of Session",
        description="Provides a concise summary of key session topics, emotions, interventions, and progress.",
        default_factory=str,
    )
    presentation: Presentation = Field(
        alias="Presentation",
        default_factory=Presentation,
    )
    psychological_factors: PsychologicalFactors = Field(
        alias="Psychological Factors",
        default_factory=PsychologicalFactors,
    )
    biological_factors: BiologicalFactors = Field(
        alias="Biological Factors",
        default_factory=BiologicalFactors,
    )
    social_factors: SocialFactors = Field(
        alias="Social Factors",
        default_factory=SocialFactors,
    )
    clinical_assessment: ClinicalAssessment = Field(
        alias="Clinical Assessment",
        default_factory=ClinicalAssessment,
    )
    mental_status_exam: MentalStatusExam = Field(
        alias="Mental Status Exam",
        default_factory=MentalStatusExam,
    )
    risk_assessment: RiskAssessment = Field(
        alias="Risk Assessment",
        default_factory=RiskAssessment,
    )
    strengths_and_resources: StrengthsAndResources = Field(
        alias="Strengths and Resources",
        default_factory=StrengthsAndResources,
    )
    progress_and_response: ProgressAndResponse = Field(
        alias="Progress and Response",
        default_factory=ProgressAndResponse,
    )

    class Config:
        populate_by_name = True

    def _to_human(self, data: dict[str, Any], indent: int = 0) -> str:
        yaml_lines = []

        def format_line(key: str, value: str, indent_level: int) -> str:
            return f"{'  ' * indent_level}{key}: {value}"

        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    yaml_lines.append(f"{'  ' * indent}{key}:")
                    yaml_lines.append(self._to_human(value, indent + 1))
                elif isinstance(value, str):
                    yaml_lines.append(format_line(key, value, indent))
        return "\n".join(yaml_lines)

    def to_human(self) -> str:
        data = self.model_dump(by_alias=True)
        return self._to_human(data)
