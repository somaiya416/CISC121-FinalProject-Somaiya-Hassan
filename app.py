"""
CISC 121 Project
Scholarship Shortlist Sorter
Algorithm: Merge Sort (implemented from scratch)

This application sorts scholarship applicants based on a computed
final score using GPA, volunteer hours, and essay score.

Visualization shows step-by-step Merge Sort progress.
"""

import gradio as gr
import time

# ---------------------------------------------------
# DATA MODEL
# ---------------------------------------------------

class Applicant:
    """
    Represents one scholarship applicant.
    """

    def __init__(self, name, gpa, volunteer_hours, essay_score):
        self.name = name
        self.gpa = float(gpa)
        self.volunteer_hours = float(volunteer_hours)
        self.essay_score = float(essay_score)
        self.final_score = self.compute_score()

    def compute_score(self):
        """
        Compute weighted scholarship score.
        Assumptions:
        GPA max = 4.3
        Essay max = 100
        Volunteer hours scaled to 100
        """
        volunteer_scaled = min(self.volunteer_hours, 100)

        return (
            0.5 * (self.gpa / 4.3 * 100) +
            0.3 * volunteer_scaled +
            0.2 * self.essay_score
        )

    def __repr__(self):
        return f"{self.name} ({self.final_score:.2f})"


# ---------------------------------------------------
# MERGE SORT (FROM SCRATCH)
# ---------------------------------------------------

def merge(left, right, steps):
    """
    Merge two sorted lists while recording steps.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        steps.append(f"Comparing {left[i]} and {right[j]}")

        if left[i].final_score >= right[j].final_score:
            result.append(left[i])
            steps.append(f"→ Taking {left[i]}")
            i += 1
        else:
            result.append(right[j])
            steps.append(f"→ Taking {right[j]}")
            j += 1

    while i < len(left):
        result.append(left[i])
        steps.append(f"Appending remaining {left[i]}")
        i += 1

    while j < len(right):
        result.append(right[j])
        steps.append(f"Appending remaining {right[j]}")
        j += 1

    return result


def merge_sort(applicants, steps):
    """
    Recursive Merge Sort implementation.
    """
    if len(applicants) <= 1:
        return applicants

    mid = len(applicants) // 2
    left = merge_sort(applicants[:mid], steps)
    right = merge_sort(applicants[mid:], steps)

    steps.append(
        f"Merging {[a.name for a in left]} "
        f"and {[a.name for a in right]}"
    )

    return merge(left, right, steps)


# ---------------------------------------------------
# INPUT PARSING
# ---------------------------------------------------

def parse_input(text):
    """
    Expected format per line:
    Name,GPA,VolunteerHours,EssayScore
    """
    applicants = []

    lines = text.strip().split("\n")

    for line in lines:
        parts = line.split(",")

        if len(parts) != 4:
            raise ValueError(
                "Each line must contain: Name,GPA,Hours,EssayScore"
            )

        name, gpa, hours, essay = parts
        applicants.append(Applicant(name, gpa, hours, essay))

    return applicants


# ---------------------------------------------------
# SORT + VISUALIZATION
# ---------------------------------------------------

def run_sort(text):
    try:
        applicants = parse_input(text)
    except Exception as e:
        return f"❌ Input Error:\n{str(e)}"

    steps = []

    sorted_list = merge_sort(applicants, steps)

    output = "=== STEP-BY-STEP MERGE SORT ===\n\n"

    for step in steps:
        output += step + "\n"
        time.sleep(0.02)

    output += "\n=== FINAL RANKING ===\n"

    rank = 1
    for applicant in sorted_list:
        output += (
            f"{rank}. {applicant.name} "
            f"(Score: {applicant.final_score:.2f})\n"
        )
        rank += 1

    return output


# ---------------------------------------------------
# GRADIO UI
# ---------------------------------------------------

DESCRIPTION = """
## 🎓 Scholarship Shortlist Sorter

Enter applicants in the format:

Name,GPA,VolunteerHours,EssayScore

Example:
Alice,4.0,50,90
Bob,3.8,120,85

The app will visualize Merge Sort step-by-step.
"""

demo = gr.Interface(
    fn=run_sort,
    inputs=gr.Textbox(
        lines=10,
        placeholder="Enter applicant data here..."
    ),
    outputs=gr.Textbox(lines=20),
    title="CISC 121 — Merge Sort Visualization",
    description=DESCRIPTION,
)

if __name__ == "__main__":
    demo.launch()