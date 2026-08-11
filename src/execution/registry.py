from automation.task_runner import run_task
from automation.file_organizer import organize_test

from projects.business_ai_tools.lead_analyzer.analyzer import LeadAnalyzer
from projects.business_ai_tools.lead_analyzer.models import Lead


def first_test_task():
    return run_task("first_test")


def lead_analysis_task():

    lead = Lead(
        name="Luxury Furniture Co",
        message="Need a 3D product animation for our furniture line",
        budget="$2000",
        deadline="3 weeks"
    )

    analyzer = LeadAnalyzer()

    return analyzer.analyze(lead)


TASKS = {

    "first_test": first_test_task,

    "file_scan": organize_test,

    "lead_analysis": lead_analysis_task,

}


def get_task(name):
    return TASKS.get(name)