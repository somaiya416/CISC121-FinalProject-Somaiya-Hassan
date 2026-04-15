# Project Title
Scholarship Shortlist Sorter — Merge Sort Visualization

---

## Chosen Problem
This project simulates ranking scholarship applicants by computing a final evaluation score based on GPA, volunteer hours, and essay performance. The application helps visualize how candidates are ordered fairly using a sorting algorithm.

---

## Chosen Algorithm
**Merge Sort**

Merge Sort was selected because it provides predictable performance (O(n log n)) and naturally demonstrates divide-and-conquer computational thinking. It is well suited for ranking applicants because stability and consistent ordering are important when comparing similar scores.

### Assumptions / Preconditions
- GPA is on a 0–4.3 scale.
- Essay scores range from 0–100.
- Volunteer hours are capped at 100 for fairness.
- Higher final score = higher ranking.

---

## Demo
The screenshots are in separate folders in this file. I tried really hard to put a link here but I couldn't. So they are not IN README but in the FinalProject file. 

---

## Problem Breakdown & Computational Thinking

### Decomposition
- Parse applicant input
- Compute weighted score
- Apply Merge Sort
- Display ranking and steps
- Visualize algorithm execution

### Pattern Recognition
- Sorting repeatedly compares elements.
- Lists can be divided into smaller sublists.
- Similar merging logic applies recursively.

### Abstraction
- Applicants represented as objects.
- Only final score matters during comparisons.
- UI separated from sorting logic.

### Algorithm Design
1. Divide list into halves recursively.
2. Sort each half.
3. Merge sorted halves while comparing scores.
4. Record steps for visualization.


---

## Steps to Run

1. Clone repository or download files.
2. Create a virtual environment:
python3 -m venv env
source env/bin/activate
3. Install dependencies:
pip install -r requirements.txt
4. Run application:
python app.py
5. Open browser at the local Gradio URL shown in Terminal.

---

## Hugging Face Link
http://127.0.0.1:7860

---

## Testing

### Tested Inputs
- Normal applicant lists (5–10 entries)
- Already sorted inputs
- Reverse sorted inputs
- Equal scores
- Invalid formatting

### Edge Cases
| Case | Expected Result | Actual Result |
|------|----------------|---------------|
| Empty input | Error message | Correct |
| Missing fields | Validation error | Correct |
| Large volunteer hours | Capped at 100 | Correct |
| Single applicant | No sorting needed | Correct |

---

## Author & Acknowledgment
Author: Somaiya Hassan

This project was developed for CISC 121 coursework.

This project was developed with the assistance of AI (Google Gemini/ChatGPT) in the following capacities:
GUI Development: AI was used to help structure the Gradio interface and handle the yield generators for visualization.
Debugging: AI assisted in troubleshooting the Python virtual environment and library installation errors on macOS. ChatGPT assisted in debugging the code body as well. 
Documentation: AI helped format the README.md to ensure it aligned with the grading rubric requirements.
Core Logic: The Merge/Quick Sort algorithm was implemented by the author based on class concepts, with AI providing guidance on how to step through the visualization.
