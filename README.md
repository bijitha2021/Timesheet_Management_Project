# Timesheet_Management_Project
Good progress. Like that you are trying to capture the signals during user creation. I have commented on model name policy in models.py. Humm, the idea behind using those signals is that when you are creating a user/Profile/Doctor, we also want to create the auth.user, since there is onetoone relation between 2. That's why we capture the signal of user creation and then insert the record in our custom user/doctor/profile table as well.
I can detail on it during session. - Kanchan, 02/09
