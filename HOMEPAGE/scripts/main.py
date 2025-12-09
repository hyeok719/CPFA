# CPFA: Climate Prediction For All
# Skeleton Code based on the Pangu-Weather model
# Author: [jang junhyeok]

import pandas as pd
import numpy as np
import onnxruntime as ort
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def load_pangu_model(model_path="pangu_weather.onnx"):
    """Load the pretrained Pangu-Weather ONNX model."""
    try:
        session = ort.InferenceSession(model_path)
        print("Model loaded successfully.")
        return session
    except Exception:
        print("Model file not found.")
        return None


def load_dataset(filepath):
    """Load dataset and extract variables such as temperature, latitude, longitude, and time."""
    try:
        data = pd.read_csv(filepath)  # Placeholder (will use xarray for NetCDF later)
        print(f"Dataset loaded: {len(data)} records")
        return data
    except Exception:
        print("Dataset not found or incompatible format.")
        return None


def run_inference(session, data):
    """Run prediction using the loaded model."""
    if session is None or data is None:
        print("Missing model or data.")
        return None

    # Placeholder for actual ONNX model inference
    preds = np.random.randn(10, 10)
    print("Inference completed (placeholder).")
    return preds


def visualize_results(predictions):
    """Visualize predicted data on a world map."""
    if predictions is None:
        print("No predictions to visualize.")
        return

    plt.figure(figsize=(8, 4))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()
    ax.set_title("Predicted Surface Temperature")
    plt.contourf(np.linspace(0, 360, predictions.shape[1]),
                 np.linspace(-90, 90, predictions.shape[0]),
                 predictions,
                 cmap="RdBu_r",
                 transform=ccrs.PlateCarree())
    plt.colorbar(label="Temperature (°C)")
    plt.show()


def main():
    """Main workflow: load model, load data, predict, and visualize."""
    print("Starting CPFA pipeline...")
    session = load_pangu_model()
    data = load_dataset("example_input.csv")

    if session and data is not None:
        preds = run_inference(session, data)
        visualize_results(preds)
    else:
        print("Inference skipped.")


if __name__ == "__main__":
    main()
