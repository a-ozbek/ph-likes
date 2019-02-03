import os
import pickle
import numpy as np
from scipy.spatial.distance import cosine
from ph_likes.util import settings


class CosinePostSimilarity:
    """
    Post similarity model based on 
    cosine distance and CF matrix
    """
    def __init__(self, silent=True):
        self.silent = silent
        self._print_msg("Loading data/models ...")
        self.cf = np.load(os.path.join(settings.LOCAL_MODELS_PATH, 'CF.npy'))
        # post_ids
        self.post_ids2index = pickle.load(open(os.path.join(settings.LOCAL_MODELS_PATH, 'post_ids2index.pkl'), 'rb'))
        self.index2post_ids = pickle.load(open(os.path.join(settings.LOCAL_MODELS_PATH, 'index2post_ids.pkl'), 'rb'))
        # user_ids
        self.user_ids2index = pickle.load(open(os.path.join(settings.LOCAL_MODELS_PATH, 'user_ids2index.pkl'), 'rb'))
        self.index2user_ids = pickle.load(open(os.path.join(settings.LOCAL_MODELS_PATH, 'index2user_ids.pkl'), 'rb'))
        self._print_msg("Loading done.")
    
    def _print_msg(self, msg):
        if not self.silent:
            print(msg)
    
    def get_similarity(self, post_id_1, post_id_2):
        """
        Returns a similarity between to `post_id`s
        """
        # get item_id indices
        post_index_1 = self.post_ids2index[post_id_1]
        post_index_2 = self.post_ids2index[post_id_2]
        
        # get vectors
        v1 = self.cf[:, post_index_1]
        v2 = self.cf[:, post_index_2]
        
        return 1.0 - cosine(v1, v2)

    