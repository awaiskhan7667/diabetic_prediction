import gradio as gr
import joblib
import numpy as np
import matplotlib.pyplot as plt

# Load Model
model = joblib.load("model.pkl")

# ----------- Chart Functions -----------

def plot_glucose_trend(value):
    plt.figure(figsize=(4, 2.5))
    x = [1, 2, 3, 4]
    y = [85, 95, 110, value]  # last value = user's glucose
    plt.plot(x, y, marker='o')
    plt.title("Glucose Trend (mg/dL)")
    plt.xlabel("Time Points")
    plt.ylabel("Glucose Level")
    plt.tight_layout()
    return plt.gcf()

def plot_bmi_scale(bmi):
    plt.figure(figsize=(4, 1.7))
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    limits = [18.5, 24.9, 29.9, 40]
    colors = ["blue", "green", "orange", "red"]

    for i in range(4):
        plt.barh(0, limits[i], color=colors[i], alpha=0.4)

    plt.axvline(bmi, color="black", linewidth=2)
    plt.text(bmi + 0.1, 0, f"{bmi} BMI", va='center')

    plt.yticks([])
    plt.xlabel("BMI Scale")
    plt.title("BMI Position")
    plt.tight_layout()
    return plt.gcf()

# ------------- Prediction Function -------------

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age):
    data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age]])
    
    pred = model.predict(data)[0]
    
    # Probability score
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(data)[0][1]
    else:
        prob = None
    
    result = "🔴 Diabetic" if pred == 1 else "🟢 Not Diabetic"
    
    # Charts
    glucose_chart = plot_glucose_trend(Glucose)
    bmi_chart = plot_bmi_scale(BMI)
    
    return result, f"{prob*100:.2f} % Chance of Diabetes", glucose_chart, bmi_chart

# ----------------- UI DESIGN -----------------

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown(
        """
        <div style='text-align:center'>
            <h1 style="color:#2C3E50;">🩺 Diabetes Prediction App</h1>
            <p style="font-size:18px; color:#7F8C8D;">
                Enter patient details below to check diabetes risk with charts & probability.
            </p>
        </div>
        """
    )

    with gr.Row():
        Pregnancies = gr.Number(label="Pregnancies (count)", value=2)
        Glucose = gr.Number(label="Glucose (mg/dL)", value=120)
        BloodPressure = gr.Number(label="Blood Pressure (mmHg)", value=70)
        SkinThickness = gr.Number(label="Skin Thickness (mm)", value=20)

    with gr.Row():
        Insulin = gr.Number(label="Insulin (µU/mL)", value=80)
        BMI = gr.Number(label="BMI (kg/m²)", value=28)
        DPF = gr.Number(label="Diabetes Pedigree Function", value=0.45)
        Age = gr.Number(label="Age (years)", value=35)

    submit_btn = gr.Button("🔍 Predict Diabetes", variant="primary")
    
    result = gr.Textbox(label="Prediction")
    probability = gr.Textbox(label="Probability Score")
    
    glucose_plot = gr.Plot(label="Glucose Trend")
    bmi_plot = gr.Plot(label="BMI Scale View")

    submit_btn.click(
        fn=predict_diabetes,
        inputs=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DPF, Age],
        outputs=[result, probability, glucose_plot, bmi_plot]
    )

demo.launch()
