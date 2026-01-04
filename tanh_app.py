# tanh_app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tanh Activation Function")

st.write("Hyperbolic Tangent (Tanh): f(x) = tanh(x)")

x = np.linspace(-5, 5, 50)
z = np.tanh(x)

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, z)
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output")
ax.grid(True)

st.pyplot(fig)
