class Job:
    def __init__(self,jobId,title):
        self.jobId = jobId
        self.title = title
        self.assignedTo = ""
    
    @classmethod
    def assign_job(cls,user):
        jobId = int(input("Enter the JobId you want to assign yourself: "))
        for job in Manager.job_list:
            if job.jobId == jobId:
                print("Job Assigned")
                job.assignedTo = user.userId
                User.assign_job(user,job)
            else:
                print("Job Not Found")
        
        
        
class User:
    
    def __init__(self,userId):
        self.userId = userId
        self.jobAssigned = []
    
    @classmethod
    def login(cls):
        userId = input("Enter User ID you want to login as: ")
        for user in Manager.user_list:
            if user.userId == userId:
                print("found user")
                return user
            else:
                print("Cannor find user")
    
    @classmethod
    def assign_job(cls,user,job):
        user.jobAssigned.append(job)
        
       
    

    
    
    
    
class Manager:
    
    user_list = []
    job_list = []
    
    def __init__(self):
        pass
    
    def add_job(self):
        jobId = int(input("Enter the Job Id: "))
        title = input("What is the Job About: ")
        Manager.job_list.append(Job(jobId,title))
            
    
    def add_user(self):
        userId = input("What is the User ID: ")
        Manager.user_list.append(User(userId))
             
    
    @classmethod
    def show_all_jobs(cls):
        for index,job in enumerate(Manager.job_list, start=1):
            print(f"{index}. jobId: {job.jobId}, Title: {job.title}, Assigned To: {job.assignedTo}")
            
    @classmethod
    def show_all_user(cls):
        for index,user in enumerate(Manager.user_list, start=1):
            print(f"{index}. User ID: {user.userId}")
            for uJobs in user.jobAssigned:
                  print(f"Job Assigned: {uJobs.jobId}")
                  
    @classmethod
    def show_all_unassigned_job(cls):
        for index,job in enumerate(Manager.job_list, start=1):
            if job.assignedTo == "":
                print(f"{index}. jobId: {job.jobId}, Title: {job.title}, Assigned To: {job.assignedTo}")
            