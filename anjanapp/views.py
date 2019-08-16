import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse
from anjanapp.form import LoginForm,Calculation,LoginPass,FormName,PostForm,DocumentForm,MailForm
from anjanapp.models import Employee,Document
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

#view1
def view1(request):
    txt = "<center><h1>hello how are you</h1></center>"
    return HttpResponse(txt)

#view2
def view2(request):
    today = datetime.datetime.now().date()
    return render(request, "datetime.html", {"TODAY":today})

#view3
def view3(request):
    return redirect("http://www.facebook.com")


#view4
def view4(request):
    li=['apple','orange','grape']
    return render(request, "fruits.html", {"FRUITS":li})

#view5
def view5(request):

 username=""

 if request.method=="POST":
    obj1 = LoginForm(request.POST)
    if obj1.is_valid():
     username = obj1.cleaned_data['txt']
    else:
        obj1 = LoginForm(initial={'user':username})
    return render(request, "response.html", {"USER":username.upper()})

#view6
def view6(request):
   sum = ""

   if request.method =="POST":
      obj2 = Calculation(request.POST)
      if obj2.is_valid():
         try:
           a = obj2.cleaned_data['adda']
           b = obj2.cleaned_data['addb']
           sum = int(a) + int(b)
         except:
          print("Addition")
   return render(request, 'addresult.html', {"TOTAL": sum})

#view7
def view7(request):
    usr=""
    psw=""
    res=""

    if request.method=="POST":
        obj3 = LoginPass(request.POST)
        if obj3.is_valid():
            usr = obj3.cleaned_data['log']
            psw = obj3.cleaned_data['pas']
            try:
             if usr == psw or psw == usr[::-1]:
               res = "Login Sucess"
             else:
               res = "Login Failed"
            except usr == "" or psw == " ":
               res = "Login Failed"
    return render(request, "logpass.html", {"RESULT": res})

#view8
def form_name_view8(request):
    form = FormName(request.POST)
    if form.is_valid():
        print("validation sucess")
        print('name='+form.cleaned_data['name'])
        print('Email='+form.cleaned_data['email'])
        print('text='+form.cleaned_data['text'])
    return render(request, "form_page.html", {"FORM":form})

#view8
def post_form_upload(request):
    name = "not logged in "
    li=[]
    s= ""

    if request.method == "POST":
        obj4 = PostForm(request.POST)

        if obj4.is_valid():
            name=len(obj4.cleaned_data['tab'])
            n = int(name)
            for i in range(1, 10, 1):
                s = (str)(n)+ ' * ' +(str)(i)+ ' = ' +(str)(n*i)
                li.append(s)

            else:
                obj4 = PostForm(initial={'user:name'})
    return render(request, "display.html", {"TABLE":li})

#view9 (models) dont forget to add this in --> "admin.py" --> admin.site.register()
def employee_record(request):
    userlist = Employee.objects.order_by('eno')
    return render(request, 'employee.html', {"EMPLOYEE":userlist})

#view10 (forms)
def insertemployee(request):
    var = employee_record(request)
    if request.method == 'POST':
        empno = request.POST['eno']
        empname = request.POST['ename']
        empemail = request.POST['email']
        obj5 = Employee(eno=empno, ename=empname,email=empemail)
        obj5.save()
        msg = """<center>Employee Record Successfully Inserted</center>"""
    return HttpResponse(var)

def home(request):
    documents = Document.objects.all()
    return render(request, "home.html", {'documents':documents})

def model_form_upload(request):

      if request.method=="POST":
          form = DocumentForm(request.POST,request.FILES)
          if form.is_valid():
              form.save()
      else:
         form = DocumentForm()
      return render(request, "model_form_upload.html", {'form':form})

#view11
def send_email(request):
    if request.method == "POST":
        obj6 = MailForm(request.POST)
        if obj6.is_valid():
            sub = obj6.cleaned_data['subject']
            msg = obj6.cleaned_data['message']
            to = obj6.cleaned_data['to']
            res = send_mail(sub, msg, settings.EMAIL_HOST_USER, [to])
            if res == 1:
                msg = "Mail sent Successfuly"
            else:
                msg = "Mail could not sent"
    return render(request, "confirmationpage.html", {"MSG":msg})

#view12
def circular_nav(request):
    return render(request, 'index.html')

