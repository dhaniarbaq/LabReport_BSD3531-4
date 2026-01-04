# relu_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("ReLU Activation Function")

st.write("Rectified Linear Unit (ReLU): f(x) = max(0, x)")

x = np.linspace(-5, 5, 50)
z = np.maximum(0, x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, z)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.grid(True)

st.pyplot(fig)
