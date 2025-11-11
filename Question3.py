# List of customer feedback messages
feedback_list = [
    "Great service!",
    "The product qUality was excelLent and delivery was fast.",
    "Okay.",
    "CusTomer suPport was helpful anD poLite.",
    "Too expensive!",
    "Absolutely love it!"
]

# Filter out feedback shorter than 20 characters
filtered_feedback = list(filter(lambda msg: len(msg) >= 20, feedback_list))

# Convert the remaining feedback to lowercase
lowercase_feedback = list(map(lambda msg: msg.lower(), filtered_feedback))

# Display results
print("Original Feedback List:")
print(feedback_list)
print("\nFiltered Feedback (>= 20 chars):")
print(filtered_feedback)
print("\nLowercase Feedback:")
print(lowercase_feedback)
