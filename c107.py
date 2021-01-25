import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

mean = df.groupby("student_id", as_index=False).mean()

fig = px.scatter(mean, x="student_id", y="attempt", color="attempt")
fig.show()
