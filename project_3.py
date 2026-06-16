# TF-IDF Recommendation System

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# 1. DATA INGESTION
items = [
    {
        "name": "Machine Learning Course",
        "description": "Artificial Intelligence machine learning data science algorithms"
    },
    {
        "name": "Python Programming Projects",
        "description": "Python coding programming software development projects"
    },
    {
        "name": "Deep Learning Tutorial",
        "description": "AI neural networks deep learning computer vision"
    },
    {
        "name": "Java Language Course",
        "description": "Java programming language software development"
    },
    {
        "name": "GitHub Learning Course",
        "description": "GitHub version control collaboration software development"
    },
    {
        "name": "MySQL Tutorial",
        "description": "MySQL Database Tutorial & SQL queries data management"
    }
]


# Extract descriptions
item_descriptions = []

for item in items:
    item_descriptions.append(item["description"])

# 2. USER INPUT
# Minimum 4 preferences
print("Recommendation System")
preferences = []

for i in range(4):
    user_input = input(f"Enter interest {i+1}: ")
    preferences.append(user_input)


# Convert user preferences into single query
user_profile = " ".join(preferences)

# 3. TF-IDF MODEL
# Combine user profile with items
documents = item_descriptions + [user_profile]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# 4. SCORING
# Cosine similarity
similarity_scores = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)
scores = similarity_scores[0]

# 5. FILTERING
# Remove low similarity results
recommendations = []
threshold = 0.05
for index, score in enumerate(scores):

    if score >= threshold:
        recommendations.append(
            {
                "name": items[index]["name"],
                "score": score
            }
        )

# 6. SORTING
# Highest score first
recommendations = sorted(
    recommendations,
    key=lambda x: x["score"],
    reverse=True
)

# OUTPUT
print("\nRecommended Items:")

if len(recommendations) == 0:
    print("No matching recommendations found.")

else:

    for item in recommendations:
        print(
            f"{item['name']}  --> Match Score: {round(item['score'],3)}"
        )
