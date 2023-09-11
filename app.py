import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.summary import summary_body
from app_pages.project_hypothesis import project_hypothesis_body
from app_pages.leaves_visualiser import leaves_visualiser_body
from app_pages.ml_performance import ml_performance_body
from app_pages.mildew_detector import mildew_detector_body

app = MultiPage(app_name="Mildew Detector")

app.app_page("Summary", summary_body)
app.app_page("Project Hypothesis", project_hypothesis_body)
app.app_page("Leaves Visualiser", leaves_visualiser_body)
app.app_page("Machine Learning Performance", ml_performance_body)
app.app_page("Mildew Detector", mildew_detector_body)

app.run()
