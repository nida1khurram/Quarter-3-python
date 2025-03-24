# import streamlit as st
# import pandas as pd
# import numpy as np

# data = pd.DataFrame(
#     np.random.randn(50,3),
#     columns=["A","B","C"]
# )
# # st.line_chart(data)
# # st.bar_chart(data)
# st.area_chart(data)
# ______________2_________________

# import streamlit as st
# import pandas as pd
# #pip install plotly
# import plotly.express as px 
# data = pd.DataFrame(
#     {
#         "Fruit":["Apple","Mango","Cherries"],
#         "Amount":[10,20,30]
#     }
# )
# fig = px.bar(data, x="Fruit", y= "Amount", title="Fruit sale")
# st.plotly_chart(fig)
# ____________3___________________
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.DataFrame(
    np.random.randn(100,3),
    columns=["A","B","C"]
)
plt.figure(figsize=(10,6))
sns.scatterplot(x = data["A"], y = data["B"])
plt.title("Scatter plot of A & B")
st.pyplot(plt)