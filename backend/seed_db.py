from app import create_app
from models import db, User, Task
from datetime import datetime, timedelta, timezone

# Create the flask application context
app = create_app()

# Open the app context
with app.app_context(): 
    # add mock users
    user1 = User(username="elm", password="alicepassword") 
    user2 = User(username="frank", password="bobpassword")

    db.session.add_all([user1, user2])
    db.session.commit()

    # add mock tasks
    task1 = Task(
        title="Learn Flask",
        description="Learn how to use Flask for web development.",
        due_date=datetime.now(timezone.utc) + timedelta(days=7),
        user_id=user1.id,
    )
    task2 = Task(
        title="LeetCode",
        description="Solve LeetCode problems.",
        due_date=datetime.now(timezone.utc) + timedelta(days=14),
        user_id=user2.id,
    )
    
    db.session.add_all([task1, task2])
    db.session.commit()

    print("Mock data inserted successfully!")
