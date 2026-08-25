# Test Cases

| ID | Test Case | Expected Result |
|---|---|---|
| TC01 | Valid trainee ID | Accepted |
| TC02 | Empty trainee ID | Rejected |
| TC03 | Empty trainee name | Rejected |
| TC04 | Valid specialization | Accepted |
| TC05 | Invalid specialization | Rejected |
| TC06 | Attendance between 0 and 100 | Accepted |
| TC07 | Attendance outside range | Rejected |
| TC08 | Invalid attendance text | Rejected |
| TC09 | Score between 0 and 100 | Accepted |
| TC10 | Score outside range | Rejected |
| TC11 | Invalid assignment status | Rejected |
| TC12 | Duplicate trainee ID | Rejected |
| TC13 | Valid CSV record | Inserted into PostgreSQL |
| TC14 | Invalid CSV record | Written to rejected records |
| TC15 | Eligibility check | Correct eligibility returned |
| TC16 | Performance rating | Correct rating returned |
| TC17 | Report generation | Correct report returned |

## Automated Test Result

The current automated test suite contains:

`23 tests`

Result:

`23 passed`