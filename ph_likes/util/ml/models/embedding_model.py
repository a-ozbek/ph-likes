from keras import layers
from keras import models


def get_embedding_model(n_users, n_posts, embedding_dim=16):
    """
    Embedding model
    """
    input_user = layers.Input(shape=(1,))
    input_post = layers.Input(shape=(1,))
    x1 = layers.Embedding(input_dim=n_users, output_dim=embedding_dim)(input_user)
    x2 = layers.Embedding(input_dim=n_posts, output_dim=embedding_dim)(input_post)
    x = layers.multiply([x1, x2])
    x = layers.Flatten()(x)
    x = layers.Dense(1, activation='sigmoid')(x)
    model = models.Model(inputs=[input_user, input_post], outputs=x)
    
    return model