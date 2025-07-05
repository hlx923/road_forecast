from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def build_lstm(input_shape):
    # ... existing code ...
    model = Sequential()
    model.add(LSTM(64, input_shape=input_shape))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    return model

def train_lstm(model, X_train, y_train, epochs=10):
    # ... existing code ...
    model.fit(X_train, y_train, epochs=epochs, batch_size=32)
    return model

# ... existing code ...