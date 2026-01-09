
import streamlit as st
import pandas as pd
from core import compute_wellness

st.title("Wellness Score Calculator")

file = st.file_uploader("Upload CSV")

if file:
    df = pd.read_csv(file)
    df['wellness_score']=df.apply(compute_wellness, axis=1)
    st.write(df)
    df.to_csv("scored.csv", index=False)
    st.download_button("Download Scored CSV", data=df.to_csv(index=False), file_name="scored.csv")
