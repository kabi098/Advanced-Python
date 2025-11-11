# List of exam scores
scores = [35, 55, 60, 72, 88, 90, 45, 99, 67, 82]

# Filter out scores below the passing mark (50)
passing_scores = list(filter(lambda s: s >= 50, scores))

# Map remaining scores to letter grades
letter_grades = list(map(
    lambda s: 'A' if s >= 90 else
              'B' if s >= 80 else
              'C' if s >= 70 else
              'D' if s >= 60 else
              'E',
    passing_scores
))

# Display results
print("Original Scores:", scores)
print("Passing Scores (>= 50):", passing_scores)
print("Letter Grades:", letter_grades)
