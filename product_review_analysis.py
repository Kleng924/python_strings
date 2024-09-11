# 1. Product Review Analysis
# Task 1: Keyword Highlighter
# Write a program that searches through reviews list and looks for keywords such as "good", 
# "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. 
# Print out each review with the keywords in uppercase so they stand out.

# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. I'm impressed with its quality."

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "excellent", "bad", "poor", "average"]

def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews

highlighted_reviews = highlight_keywords(reviews, keywords)

for review in highlighted_reviews:
    print(review)

user_input = int(input("Enter 2 for Task 2: "))

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.
    
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def sentiment_tally(review, positive_words, negative_words):
    positive_words_count = 0
    negative_words_count = 0

    for word in positive_words:
        positive_words_count += review.lower().count(word)
    for word in negative_words:
        negative_words_count += review.lower().count(word)

    return positive_words_count, negative_words_count

for review in reviews:
    positive_count, negative_count = sentiment_tally(review, positive_words, negative_words)
    print(f"Review: {review}")
    print(f"Positive Reviews: {positive_count} vs Negative Reviews: {negative_count}")

next_task = int(input("Enter 3, for Task 3: "))

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.
# Example: "This product is really good. I'm...",

def summarize_reviews(reviews):
    summaries = []
    for review in reviews:
        if len(review) > 35:
            cutoff_index = review[:35].rfind(' ')
            summary = review[:cutoff_index] + "…"
        else:
            summary = review
        summaries.append(summary)
    return summaries

summarized_reviews = summarize_reviews(reviews)
print(summarized_reviews)