# **MODEL SELECTION**

In order to find the best suited model to fit the data, different optimers 
were explored.  Three optimisers were used, **adam** (v1), **Adadelta** (v2) 
and **Adagrad** (v3).  Outlines of the models and their perfomamce are 
detailed below.

![Cherry Trees in blossom](/assets/images/pedro-sanz-fd4KegLUgOA.jpg)

***

## **Table of Contents**

- [**MODEL SELECTION**](#model-selection)
  - [**Model v1**](#model-v1)
    - [**v1 Outline**](#v1-outline)
    - [**v1 Performance**](#v1-performance)
    - [**v1 Conclusion**](#v1-conclusion)
  - [**model v2**](#model-v2)
    - [**v2 Outline**](#v2-outline)
    - [**v2 Performance**](#v2-performance)
    - [**v2 Conclusion**](#v2-conclusion)
  - [**Model v3**](#model-v3)
    - [**v3 Outline**](#v3-outline)
    - [**v3 Performance**](#v3-performance)
    - [**v3 Conclusion**](#v3-conclusion)
  - [**Conclusion**](#conclusion)

***

## **Model v1**

### **v1 Outline**

    def create_tf_model():
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(128, activation = 'relu'))

    model.add(Dropout(0.5))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    
    return model

***

    Model: "sequential"
    _________________________________________________________________

    Layer (type)                 Output Shape              Param #
    =================================================================

    conv2d (Conv2D)              (None, 254, 254, 32)      896
    _________________________________________________________________
    max_pooling2d (MaxPooling2D) (None, 127, 127, 32)      0
    _________________________________________________________________
    conv2d_1 (Conv2D)            (None, 125, 125, 64)      18496
    _________________________________________________________________
    max_pooling2d_1 (MaxPooling2 (None, 62, 62, 64)        0
    _________________________________________________________________
    conv2d_2 (Conv2D)            (None, 60, 60, 64)        36928
    _________________________________________________________________
    max_pooling2d_2 (MaxPooling2 (None, 30, 30, 64)        0
    _________________________________________________________________
    flatten (Flatten)            (None, 57600)             0
    _________________________________________________________________
    dense (Dense)                (None, 128)               7372928
    _________________________________________________________________
    dropout (Dropout)            (None, 128)               0
    _________________________________________________________________

    dense_1 (Dense)              (None, 1)                 129
    =================================================================

    Total params: 7,429,377
    Trainable params: 7,429,377
    Non-trainable params: 0
    _________________________________________________________________

### **v1 Performance**

![V1 Accuracy](/outputs/v1/model_training_acc.png)

![V1 Loss](/outputs/v1/model_training_losses.png)

    evaluation = model.evaluate(test_set)
    43/43 [==============================]
    18s 404ms/step
    loss: 0.0169
    accuracy: 0.9953

![V1 Confusion Matrix](/outputs/v1/confusion_matrix.png)

### **v1 Conclusion**

Overfitting

***

## **model v2**

### **v2 Outline**

    def create_tf_model():
        model = Sequential()

        model.add(Conv2D(filters=32, kernel_size=(3,3),input_shape=image_shape,
        activation='relu',))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
        activation='relu',))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
        activation='relu',))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(128, activation = 'relu'))

        model.add(Dropout(0.5))
        model.add(Dense(units=1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='Adadelta',
                      metrics=['accuracy'])
    
        return model

***

    Model: "sequential"
    _________________________________________________________________

    Layer (type)                 Output Shape              Param #
    =================================================================

    conv2d (Conv2D)              (None, 254, 254, 32)      896
    _________________________________________________________________
    max_pooling2d (MaxPooling2D) (None, 127, 127, 32)      0
    _________________________________________________________________
    conv2d_1 (Conv2D)            (None, 125, 125, 64)      18496
    _________________________________________________________________
    max_pooling2d_1 (MaxPooling2 (None, 62, 62, 64)        0
    _________________________________________________________________
    conv2d_2 (Conv2D)            (None, 60, 60, 64)        36928
    _________________________________________________________________
    max_pooling2d_2 (MaxPooling2 (None, 30, 30, 64)        0
    _________________________________________________________________
    flatten (Flatten)            (None, 57600)             0
    _________________________________________________________________
    dense (Dense)                (None, 128)               7372928
    _________________________________________________________________
    dropout (Dropout)            (None, 128)               0
    _________________________________________________________________

    dense_1 (Dense)              (None, 1)                 129
    =================================================================

    Total params: 7,429,377
    Trainable params: 7,429,377
    Non-trainable params: 0

### **v2 Performance**

![V2 Accuracy](/outputs/v1/model_training_acc.png)

![V1 Loss](/outputs/v1/model_training_losses.png)

    evaluation = model.evaluate(test_set)


![V2 Confusion Matrix](/outputs/v2/confusion_matrix.png)

### **v2 Conclusion**

***


## **Model v3**

- Adagrad is an optimizer with parameter-specific learning rates, which are 
  adapted relative to how frequently a parameter gets updated during training. 
  The more updates a parameter receives, the smaller the updates.

### **v3 Outline**

    def create_tf_model():
    model = Sequential()

    model.add(Conv2D(filters=32, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(filters=64, kernel_size=(3,3),input_shape=image_shape,
    activation='relu',))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(128, activation = 'relu'))

    model.add(Dropout(0.5))
    model.add(Dense(1, activation = 'sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer='adagrad',
                  metrics=['accuracy'])
    
    return model

***

    Model: "sequential"
    _________________________________________________________________

    Layer (type)                 Output Shape              Param #
    =================================================================

    conv2d (Conv2D)              (None, 254, 254, 32)      896
    _________________________________________________________________
    max_pooling2d (MaxPooling2D) (None, 127, 127, 32)      0
    _________________________________________________________________
    conv2d_1 (Conv2D)            (None, 125, 125, 64)      18496
    _________________________________________________________________
    max_pooling2d_1 (MaxPooling2 (None, 62, 62, 64)        0
    _________________________________________________________________
    conv2d_2 (Conv2D)            (None, 60, 60, 64)        36928
    _________________________________________________________________
    max_pooling2d_2 (MaxPooling2 (None, 30, 30, 64)        0
    _________________________________________________________________
    flatten (Flatten)            (None, 57600)             0
    _________________________________________________________________
    dense (Dense)                (None, 128)               7372928
    _________________________________________________________________
    dropout (Dropout)            (None, 128)               0
    _________________________________________________________________

    dense_1 (Dense)              (None, 1)                 129
    =================================================================

    Total params: 7,429,377
    Trainable params: 7,429,377
    Non-trainable params: 0
    _________________________________________________________________

### **v3 Performance**

![V3 Accuracy](/outputs/v3/model_training_acc.png)

![V3 Loss](/outputs/v3/model_training_losses.png)

    evaluation = model.evaluate(test_set)
    43/43 [==============================]
    18s 404ms/step
    loss: 0.0169
    accuracy: 0.9953

![V3 Confusion Matrix](/outputs/v3/confusion_matrix.png)

### **v3 Conclusion**

***

## Conclusion

V3 selected. Doesn't overfit. Accuracy meets target.