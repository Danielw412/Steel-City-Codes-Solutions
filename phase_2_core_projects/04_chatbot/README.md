# Chatbot: Solutions

Phase 2 (Core Projects, always first). Student starter code and requirements: [Steel-City-Codes-Starter-Code/phase_2_core_projects/04_chatbot](https://github.com/Danielw412/Steel-City-Codes-Starter-Code/tree/main/phase_2_core_projects/04_chatbot)

These solutions show what a finished project can look like. Students should write their own code. Use these files to answer questions, unblock a stuck student, or check that a project meets the requirements.

## Solution Files

| File | What it demonstrates |
|---|---|
| `solution_1_basic.py` | One loop and an `if`/`elif` chain of substring checks such as `"python" in message`. |
| `solution_2_random_responses.py` | Each topic has several replies, chosen with `random.choice()`. A `contains_topic()` helper handles simple plurals. |
| `solution_3_dictionary.py` | Topics and replies stored in a dictionary. The message is split into words with punctuation removed, so adding a topic means adding one dictionary entry. |

## What to Look For in Student Code

- `.lower()` before checking keywords, so `PYTHON` works.
- Singular and plural checks, such as `bear` and `bears`.
- A fallback reply that lists the topics the bot knows.
- A blank-input check and an exit command.
- Note for volunteers: a substring check like `"hi" in message` also matches words such as `this`. That is a good discussion point and a reason to split the message into words, as solution 3 does.
