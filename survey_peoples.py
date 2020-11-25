from csv_process import write_result
from dotenv import load_dotenv
import os
from survey.survey_one_people import survey_one_people


def survey_peoples(survey_people):
    load_dotenv()
    api_token = os.environ['api_token']
    i = 0
    while i < survey_people:
        result = survey_one_people(api_token)
        write_result(result)
        i += 1

survey_peoples(100)