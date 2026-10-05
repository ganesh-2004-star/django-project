from django.db import models



class TodoList(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)




































# Create your models here.
#TABLE:NOTE#note is table name aND WRITTEN AFTER CLASS 
#FIELDS:ID,TITLE,CONTENT,SUBJECT,Program(Science,management,course_names),crated_at


# models.py file create models -> migration file(models details) -> database reflect

    #id is auto defined

# orm obj reln mapping 
# way to interact with databasse using progtamming langaueg obj/class instead of sql directly 

# sql:select from note #get all data from noyte table whose ititle is writing

# get all daata from table
   #orm;model_name or table name.objects


#    select * from note where title ;writing;

    # add or create data
    # NOTE.objects.create(title="first",content="this is the first note",created_at="2026-09-28")
    # note.objects.all().values()
    
    # retrieve access/get single data
    # modelname.obj.get(id =1)

    # update:
    # a.title="newdata"
    # a.save()
    # delete:
    # a.delete()
    # 

    # filter
    # modelname.objects.filter(title="smthg")
    
    
    
    
    
    #inside django db models inside model  