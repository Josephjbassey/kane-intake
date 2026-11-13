# Kane CLI Verification Objective: Invoice Extraction

## Objective
Go to {{base_url}}, click on the "Run Mock Invoice Flow (₦12,500)" button, and verify the total shows ₦12,500.

## Assertion Criteria
1. Web page renders cleanly with header "Kane Intake".
2. Clicking the mock invoice flow triggers HTMX extraction without page reload.
3. The extraction result card appears.
4. The element with id `extracted-total` contains `₦12,500`.
5. Vendor name shows `Lagos Freight & Logistics Ltd`.

## Command Line Execution
```bash
kane-cli run "Go to http://localhost:8000, click on the 'Run Mock Invoice Flow (₦12,500)' button, and verify the total shows ₦12,500" --agent --headless --timeout 120
```
