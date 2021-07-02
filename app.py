import os
import streamlit as st
import numpy as np
import pandas as pd
import time

# https://plotly.com/python/plotly-express/
import plotly.express as px

from teachablehub.clients import TeachableHubPredictAPI

teachable = TeachableHubPredictAPI(
    teachable=os.environ.get('TH_TEACHABLE', 'user/teachable'),
    environment=os.environ.get('TH_ENVIRONMENT', 'experiments'),
    serving_key=os.environ.get('TH_SERVING_KEY', 'you-serving-key')
)

st.markdown("""
# TeachableHub Ludwig BBC Classifier

This is a Interactive Application Interface integrated with the Teachable Prediction API for Realtime Cloud predictions from every device.

## **Features**
""")

txt = st.text_area('Text to classify',
    '''wilkinson fit to face edinburgh england captain jonny wilkinson will make his long-awaited return from injury against edinburgh on saturday.  wilkinson  who has not played since injuring his bicep on 17 october  took part in full-contact training with newcastle falcons on wednesday. and the 25-year-old fly-half will start saturday s heineken cup match at murrayfield on the bench. but newcastle director of rugby rob andrew said:  he s fine and we hope to get him into the game at some stage.  the 25-year-old missed england s autumn internationals after aggravating the haematoma in his upper right arm against saracens. he was subsequently replaced as england captain by full-back jason robinson. sale s charlie hodgson took over the number 10 shirt in the internationals against canada  south africa and australia. wilkinson s year has been disrupted by injury as his muscle problem followed eight months on the sidelines with a shoulder injury sustained in the world cup final.''',
     height=250)

features = {"text": txt}
predictions = teachable.predict(features)

classes = []
probabilities = []

for prediction in predictions:
    classes.append(prediction['className'])
    probabilities.append(prediction['probability'])

chart_data = pd.DataFrame({
    "Probablities": probabilities,
    "Classes": classes,
})

# https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
state_total_graph = px.bar(
    chart_data.sort_values(by=['Classes']),
    x='Probablities',
    y='Classes',
    color='Classes')
st.plotly_chart(state_total_graph)
