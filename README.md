# Automated-Birthday-Wisher-Emailer

Tech Stack: Python, Pandas, SMTP, datetime, File I/O

Developed an automated Python script that reads birthday data from a CSV file and sends personalized birthday emails to individuals on their special day.

Key Features:
Parsed CSV data with pandas to retrieve names, emails, and birth dates.

Compared current date with birthdays to trigger email sending only on matching days.

Selected a random birthday letter template, replaced placeholders dynamically with the recipient’s name.
Sent emails securely using SMTP protocol with TLS encryption and Gmail SMTP server.

Logged into email account programmatically to automate outgoing messages.

Included error handling to print notification if no birthdays occur on the current day.
