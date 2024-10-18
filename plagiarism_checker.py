import textract
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file_with_textract(file_path):
    """Read text from various file formats using textract."""
    try:
        text = textract.process(file_path).decode('utf-8', errors='replace')
        return text
    except Exception as e:
        print(f"Error reading {file_path} with textract: {e}")
        return None

def check_plagiarism(text1, text2):
    """Check the similarity between two texts using cosine similarity."""
    vectorizer = CountVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    return cosine_sim[0][1] * 100 
