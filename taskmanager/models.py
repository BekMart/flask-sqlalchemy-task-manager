from taskmanager import db # import db form main taskmanager package to define the database


# create tables representing class-based models using SQLAlchemy ORM..
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True) # unique id - primary_key=True and set to integer - this will increment with each instance
    category_name = db.Column(db.String(25), unique=True, nullable=False) # (25) = max character count, each new category is unique, nullable=False = required field
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True) # this links the foreign key and enables ondelete=cascade

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True) # unique id - primary_key=True and set to integer - this will increment with each instance
    task_name = db.Column(db.String(50), unique=True, nullable=False) # max characters = 50/unique for each record/required field
    task_description = db.Column(db.Text, nullable=False) # db.Text = allows longer strings to be used
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False) # links this table to content in category table/ondelete = cascade means that if a category is deleted , it will be reflected elsewhere

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
    
