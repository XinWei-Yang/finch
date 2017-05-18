from mlp_clf import MLPClassifier
import numpy as np
import tensorflow as tf


if __name__ == '__main__':
    (X_train, y_train), (X_test, y_test) = tf.contrib.keras.datasets.cifar10.load_data()

    X_train = (X_train/255.0).mean(axis=3).reshape(-1, 32*32)
    X_test = (X_test/255.0).mean(axis=3).reshape(-1, 32*32)
    Y_train = tf.contrib.keras.utils.to_categorical(y_train)
    Y_test = tf.contrib.keras.utils.to_categorical(y_test)

    clf = MLPClassifier(32*32, 10)
    log = clf.fit(X_train, Y_train, val_data=(X_test,Y_test))
    pred = clf.predict(X_test)

    final_acc = np.equal(np.argmax(pred,1), np.argmax(Y_test,1)).astype(float).mean()
    print("final testing accuracy: %.4f" % final_acc)
