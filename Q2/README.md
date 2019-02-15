## Description
### Files
- q2.py
- data_json.json
  - **Columns** (Keys,Type)
    - user_id,string
    - product_id,string
    - quantity,count

### Code
**q2.py** <br>
- function `def popular(filename = 'data_json.json')`
  - Parameter JSON filename (string) default "data_json.json"
  - Output in Console
    - [Most popular product(s) based on the quantity of goods sold](https://github.com/coolkp/moloco/blob/master/Q2/q2.py#L45)
    - [Most popular product(s) based on the number of purchasers](https://github.com/coolkp/moloco/blob/master/Q2/q2.py#L46)
- Complexity
  - Parameters(N json messages, U unique users, and P unique products)
    - **Runtime Complexity**
      - Loop traversal 1 Pass i.e O(N)
      - Lookup for most and others O(1)
      - Outputting O(1)
    - **Space Complexity**
      - Unique Products => Quantity O(P)
      - Unique Products => Unique Users O(P x U)
      - Output => Worst Case O(P) + O(P)
