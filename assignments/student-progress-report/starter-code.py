"""Starter code for Student Progress Report Generator assignment."""


def load_scores(filename):
    """Read name,score lines from a file and return a list of (name, score)."""
    # TODO: Open the file and parse each line into (name, int(score)).
    # Example line: Ava,88
    return []


def calculate_average(scores):
    """Return the average score as a float."""
    # TODO: Compute and return the average score.
    return 0.0


def count_passing(scores, passing_score=70):
    """Return how many students have score >= passing_score."""
    # TODO: Count and return passing students.
    return 0


def highest_score(scores):
    """Return (name, score) for the highest-scoring student."""
    # TODO: Find and return the highest-scoring student.
    # Hint: built-in max with a key can help.
    return ("", 0)


def print_report(scores):
    """Print a formatted class progress report."""
    # TODO: Use helper functions and print a summary.
    pass


def main():
    scores = load_scores("scores.txt")
    print_report(scores)


if __name__ == "__main__":
    main()
