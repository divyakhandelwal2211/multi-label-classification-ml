from sklearn.metrics import f1_score, accuracy_score

def evaluate_model(model, X_test, y_test):

    y_pred = model.predict(X_test)

    # Micro F1 Score
    micro_f1 = f1_score(y_test, y_pred, average='micro')

    # Accuracy Score (subset accuracy in multi-label)
    accuracy = accuracy_score(y_test, y_pred)

    print("Micro F1 Score:", micro_f1)
    print("Accuracy Score:", accuracy)