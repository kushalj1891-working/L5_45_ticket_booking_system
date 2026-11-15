# Reflection

> The supplied handout refers to four reflection questions, but neither the uploaded PDF nor the assigned repository README contains their wording. The prompts below are representative questions based on the lab objectives; they are not quoted from the handout.

## 1. Which static analysis tool was most useful, and why?

Bandit was most useful for surfacing risks that can be easy to overlook in a small script. It identified the dynamic `eval`, weak MD5 digest, predictable PIN generator, and shell command. Those findings made it clear that code can appear to work while still exposing security problems.

## 2. Which finding was most important to fix?

The use of `eval` was especially important because an expression supplied by a caller could execute arbitrary Python code. I replaced the expression string with a numeric discount rate, checked that it is between 0 and 1, and calculated the price directly. I also removed the shell invocation that used the export filename.

## 3. What did the tools miss, and what are their limits?

Static analysis checks source patterns; it does not prove that booking behavior matches every requirement or that every edge case works at runtime. For example, the original script's mutable default list can retain state across calls, and its report alone does not show the user-facing consequences. Manual review and runtime checks are still needed alongside the tools.

## 4. How will static analysis affect your future coding workflow?

I will run the tools early and again after changes, then review each finding in context instead of treating the output as a substitute for understanding the code. Pylint helps with maintainability and likely bugs, Flake8 catches formatting problems, and Bandit focuses attention on security-sensitive patterns. Keeping the final reports makes it easier to confirm that fixes removed the reported issues.
