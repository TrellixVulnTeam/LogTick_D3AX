from django.db import models
from django.contrib.auth.models import User
from Main.main_models.Current_Status import Current_Status
import datetime

class ProcessData(models.Model):
    process_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    start_time = models.BigIntegerField()
    end_time = models.BigIntegerField()
    user_id = models.BigIntegerField()
    weekend_id = models.BigIntegerField()
    duration = models.BigIntegerField()
    image_data = models.TextField()
    
    
    def __str__(self):
        return self.process_id
