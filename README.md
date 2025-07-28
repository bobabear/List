# List Utilities for Reaction Data

A Python module of list‑and‑dictionary utilities for processing reaction/engagement data:

- **`filter_popular(reacts_2D, names, threshold)`**  
  Return a list of user names whose total reactions meet or exceed `threshold`.

- **`gather_engagement(names, reacts, grouping)`**  
  Group individual reaction counts into sub‑lists by user, producing a 2D list where each row is `[user, r1, r2, …]`.

- **`clear_zeros(reacts_2D)`**  
  Remove all zero‑entries and any empty rows from a 2D reaction list.

- **`form_reactions_list(react_dict1, react_dict2)`**  
  Merge two reaction dictionaries into a list of `[reaction_type, total_count]` for each unique reaction.

- **`form_reactions_dict(reacts_2D)`**  
  Convert a 2D list of `[reaction_type, count]` pairs into a dictionary and append a `"total"` key summing all counts.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or newer

### Installation

```bash
git clone https://github.com/your-username/List-main.git
cd List-main
```

## How to Use

from achu4_211_PA4 import ( <br>
    filter_popular, <br>
    gather_engagement, <br>
    clear_zeros, <br>
    form_reactions_list, <br>
    form_reactions_dict <br>
)

### 1. filter_popular
reacts_2D = [<br>
    [5, 0, 2],<br>
    [1, 1, 1],<br>
    [0, 0, 0]<br>
]<br>
names     = ['Alice', 'Bob', 'Cara']<br>
print(filter_popular(reacts_2D, names, threshold=5))
→ ['Alice']

### 2. gather_engagement
names    = ['Alice', 'Bob']<br>
reacts   = [10, 20, 30, 40]<br>
grouping = [2, 2]<br>
**Groups first two reacts for Alice, next two for Bob**<br>
print(gather_engagement(names, reacts, grouping))
→ [['Alice', 10, 20], ['Bob', 30, 40]]

### 3. clear_zeros
reacts_2D = [[0, 2, 0], [0, 0], [1, 3]]<br>
print(clear_zeros(reacts_2D))
→ [[2], [1, 3]]

### 4. form_reactions_list
r1 = {'like': 5, 'love': 2}<br>
r2 = {'like': 3, 'haha': 4}<br>
print(form_reactions_list(r1, r2))
→ [['love', 2], ['haha', 4], ['like', 8]]  (order may vary)

### 5. form_reactions_dict
reacts_2D = [['like', 8], ['love', 2], ['haha', 4]]<br>
print(form_reactions_dict(reacts_2D))
→ {'like': 8, 'love': 2, 'haha': 4, 'total': 14}

## Run Test Cases

**Test with Tester**
python3 tester4.py achu4_211_PA4.py

**Test a specific function**
python3 tester4.py achu4_211_PA4.py filter_popular form_reactions_dict

