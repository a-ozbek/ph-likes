from flask import Flask
from flask import request, jsonify
from ph_likes.post_similarity.cosine_post_similarity import CosinePostSimilarity


app = Flask(__name__)

# Load Models
COSINE_POST_SIMILARITY_MODEL = CosinePostSimilarity(silent=False)


@app.route('/get_post_similarity', methods=['POST'])
def get_post_similarity():
    data = request.get_json()
    post_id_1 = int(data['post_id_1'])
    post_id_2 = int(data['post_id_2'])    
    similarity = COSINE_POST_SIMILARITY_MODEL.get_similarity(post_id_1, post_id_2)    
    return jsonify(similarity)


if __name__ == "__main__":
    app.run(debug=False)