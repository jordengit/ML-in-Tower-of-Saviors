# Environment

## Action
- ['u', 'd', 'l', 'r', 'e'] up/down/left/right/empty(no move)

## Reward function
- hit wall -> score -1
- bigger than limit_steps -> score - (steps-limit_steps) * 0.5
- combos -> score + combos * 5

## Stop condition
- step to 'e' (means didn't move)
- combos equal max_combo
