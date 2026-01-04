# sigmoid_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Sigmoid Activation Function")

st.write("Sigmoid Function: f(x) = 1 / (1 + e⁻ˣ)")

x = np.linspace(-5, 5, 50)
z = 1 / (1 + np.exp(-x))

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, z)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.grid(True)

st.pyplot(fig)
