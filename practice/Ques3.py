# Enumerate and F-strings.

lst = ["Hatty Potter", "Macbeth", "Julius & Caesaer", "Pride & Prejudice", "Wuthering Heights", "Jane Eyre", "Hamlet", "The Tempest", "The Merchant of Venice"]

for index, item in enumerate(lst):
    print(f"Book {index+1}: {item}")