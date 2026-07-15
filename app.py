import re
import pickle
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.set_page_config(page_title="Stock Sentiment Classifier", page_icon="📈", layout="centered")

MAX_LEN = 200


@st.cache_resource
def load_artifacts():
    model = load_model("best_model.keras")
    with open("stock_tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    return model, tokenizer

model, tokenizer = load_artifacts()

# ---- Same cleaning function used during training ----
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def predict_sentiment(text):
    cleaned = clean_text(text)
    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post", truncating="post")
    prob = model.predict(padded, verbose=0)[0][0]
    label = "Positive" if prob > 0.5 else "Negative"
    return label, float(prob)

# ---------------- Streamlit UI ----------------
st.title("📈 Stock Sentiment Classifier")
st.write("Powered by a GRU neural network trained on stock-related tweets")

text = st.text_area(
    "Enter a stock-related tweet or comment:",
    height=150,
    placeholder="e.g. AAPL breaking out above resistance, looking strong for Q3..."
)

if st.button("Predict Sentiment"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        label, prob = predict_sentiment(text)
        confidence = prob if label == "Positive" else 1 - prob

        if label == "Positive":
            st.success(f"**{label}** (confidence: {confidence:.2%})")
        else:
            st.error(f"**{label}** (confidence: {confidence:.2%})")

        st.progress(float(prob))
        st.caption(f"Raw model output (probability of positive): {prob:.4f}")