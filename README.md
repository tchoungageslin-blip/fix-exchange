# 💰 Lab: The Price Calculator Fix

**Scenario:** We have a price formatting function that works for some prices but gives wrong results for others (try testing with 19.99). Also, the currency converter is completely missing!

**Your Job:** Fork the repo, fix the rounding bug, implement the currency converter, and pass the GitHub Action check.

---

## 🧪 Instructions:

1.  **Fork & Clone** the repository.

2.  **Create a Branch:**

    ```bash
    git checkout -b fix/price-calculator
    ```

3.  **Run Tests Locally:**

    ```bash
    python -m unittest discover tests
    ```

    - _Observation:_ You will see `AssertionError: 19 != 20`. Read the error message carefully!

4.  **Fix `src/pricing.py`:**

    - **Step A:** Fix the `format_price` function. It currently uses `int(price)` which truncates the decimal. It _should_ use `round(price)` to properly round prices to the nearest integer.

    - **Step B:** Implement `convert_currency` so it returns `amount * exchange_rate`.

5.  **Commit & Push:**

    ```bash
    git commit -am "fix: corrected rounding and added currency converter"
    git push origin fix/price-calculator
    ```

6.  **Open Pull Request:**
    - Go to GitHub and create a Pull Request from your branch
    - Watch the "Price Calculator Checker" run
    - If it turns Green ✅, you are done!

---

## 📁 Project Structure

```
prices/
├── src/
│   └── pricing.py      # 👈 Fix this file!
├── tests/
│   └── test_pricing.py # 📋 Tests that verify your fixes
├── .github/
│   └── workflows/
│       └── check_pricing.yml  # 🤖 GitHub Action
└── README.md
```

---

## 💡 Hints

- `int(19.99)` returns `19` (truncates)
- `round(19.99)` returns `20` (rounds properly)
- Currency conversion is simple multiplication: `100 USD * 0.85 = 85 EUR`

---

## ✅ Success Criteria

All tests must pass:

- `test_format_price_rounds_up` - 19.99 should become 20
- `test_format_price_rounds_down` - 19.49 should become 19
- `test_format_price_exact` - 25.00 should become 25
- `test_convert_currency` - 100 \* 0.85 should equal 85.0
- `test_convert_currency_reverse` - 50 \* 1.18 should equal 59.0

Good luck! 🍀
