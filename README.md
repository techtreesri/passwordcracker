🔐 Brute Force Password Cracker (Python)

This is a simple brute-force password cracker written in Python. It attempts to guess a user-provided password by generating every possible combination of characters until it matches.

📂 Project Structure

```
brute_force_password_cracker/
├── password_cracker.py
└── README.md
```

🧠 How It Works

* The user enters a target password.
* The program uses `itertools.product()` to generate all combinations of lowercase letters, numbers, and symbols of the same length as the target.
* Each generated combination is compared to the target.
* The process continues until the password is found.


💻 Demo

```bash
$ python password_cracker.py
Enter a Target : abc
...
password found :abc
Time Taken: 2.35 seconds
Total attempts : 875
```

🔎 Features

* Brute-force cracking for any string made of:

  * Lowercase alphabets (`a-z`)
  * Digits (`0-9`)
  * Common symbols (`!@#$%^&*()+_=-`)
  * Space
* Reports:

  * Total time taken
  * Total number of attempts made
* Educational demonstration of how brute-force works


⚙️ Requirements

* Python 3.x
* No external libraries needed (only standard libraries used)



📄 Code Overview

```python
posible_value = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()+_=- "
for guess in itertools.product(posible_value, repeat=max_lenght):
    guess = "".join(guess)
    if guess == target:
        # Match found
```

⚠️ Limitations

* Only supports passwords of **fixed length equal to the target**.
* Exponential time complexity: not efficient for passwords longer than 4–5 characters.
* Not intended for real-world password cracking — **educational use only**.


🛑 Disclaimer

> This tool is for **educational purposes only**.
> Do not use it to attempt unauthorized access to systems.
> The author is **not responsible** for any misuse.


📜 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).
