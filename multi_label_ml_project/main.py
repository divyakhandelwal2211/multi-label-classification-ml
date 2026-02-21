import os
from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.model import train_model, save_model
from src.evaluate import evaluate_model


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(BASE_DIR, "data", "multi_label_dataset_1000_rows.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "trained_model.pkl")

LABEL_COLUMNS = ["label_A", "label_B", "label_C"]


def main():

    df = load_data(DATA_PATH)

    X_train, X_test, y_train, y_test, scaler = preprocess_data(
        df, LABEL_COLUMNS
    )

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    save_model(model, MODEL_PATH)

    print("Model saved successfully ✅")


if __name__ == "__main__":
    main()