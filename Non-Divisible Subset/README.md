
| Challenge info | info   |
| ----       | -----     |
| Author     | zxqfd555 |
| Difficulty | Medium    |
| Challenge link | [link](https://www.hackerrank.com/challenges/non-divisible-subset/problem) |

 
This is really an interesting challenge.

The idea behind this challenge is "exclusive".

`A + B` can be evenly divided by `k` means `A % k + B % k = 0 or k`.

We can confirm this by rewriting `A + B` to `ak + a_left + bk + b_left`.

So in this case, given a set `{A % k}`, the exclusive set is `{k - A % k}`.
And we can only add either of them to the result set.

For example:

    given input:
    4 3
    1 7 2 4
    
    Because k == 3, so there are only one exclusive sets pair:
    {A % 3 == 1} and {A % 3 == 2}
    As 1 7 4 are in {A % 3 == 1} and 2 in {A % 3 == 2},
    if we take {1, 7, 4}, then we cannot take {2}.
    