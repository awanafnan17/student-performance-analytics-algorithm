def analyze_scores(scores):
    """
    Analyze a list of numeric scores and return the average and performance classification.
    The function uses a loop to sum the scores and a series of if-elif statements to
    classify the average into performance categories: Excellent, Good, Average, or Needs Improvement.

    Args:
        scores (list of float): A list of numerical scores.

    Returns:
        tuple: The average score and a string representing the performance category.
    """
    total = 0
    count = 0
    # Iterate through each score to compute total and count
    for score in scores:
            # Skip negative scores
    if score < 0:
        continue
    total += score
    count += 1
    # Avoid division by zero
    average = total / count if count > 0 else 0
    # Classify performance based on average score
    if average >= 80:
        performance = "Excellent"
    elif average >= 65
        performance = "Good"
    elif average >= 40:
        performance = "Average"
    else:
        performance = "Needs Improvement"
    return average, performance

# Example usage when the script is run directly
if __name__ == '__main__':
    # Example list of scores
    sample_scores = [85, 90, 78, 92, 88]
    avg, perf = analyze_scores(sample_scores)
    print(f"Average: {avg:.2f}, Performance: {perf}")
