# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The game had a minimalistic UI/UX experience, nothing complex really nice to use.
- List at least two concrete bugs you noticed at the start 
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Expected to happen - Expected the score to compute appropriately in increasing manner
     Actually happened - The Score computed in a uncomprehensive way

  2. Expected to happen = I expected the hint message to be accurate.
      Actually happened - The hint is in accurate, it asked me to go higher on 100

  3. Expected to happen = The easy guess is supposed to be form 0 - 20
      Actually happened - The easy guess is supposed to be form 0 - 20, when i choose a higher number hint says go higher
      

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used AI like a helper to point me to possible problems in my code and to give me ideas for what to check.
It was useful for speeding up my thinking, but I still had to test everything myself in the game.

One correct suggestion was that the hint problem was likely caused by the comparison logic in my conditions.
I checked the code and tested values like 20 and 100, and that helped me confirm and fix the wrong hint behavior.

One misleading suggestion was that the score problem could be fixed by only changing where the score updates happen.
After testing several rounds, I saw the real issue was also in the scoring logic itself, so I had to adjust that part too.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed only when the code looked correct and the game also behaved the way I expected.
If the game still gave strange results during play, then I knew the bug was not fully fixed yet.

One test I ran was entering different numbers to check if the hints made sense, especially at the edges of the range.
This showed me that the hint message was wrong before the fix and accurate after I corrected the conditions.

I also tested the score by playing multiple rounds and watching how it changed after each guess.
That showed me whether the score was increasing in a clear way or still behaving in a confusing manner.

AI also helped me think about what kinds of tests to run, especially checking edge cases and unusual inputs.
That made it easier for me to understand whether my fixes were actually working or not.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
