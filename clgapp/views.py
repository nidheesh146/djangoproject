from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from clgapp.models import Addcourse,Student,Teacher
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def admin_panel(request):
    return render(request,'admin_panel.html')

def login(request):
    return render(request, 'login.html')

def logout_view(request):
    auth.logout(request)  
    messages.info(request, 'You have been logged out.')  
    return redirect('login') 

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                return redirect('admin_panel')
            else:
                messages.info(request, f'Welcome "{username}"')
                return redirect('teach_home')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'login.html')


@login_required(login_url='login')
def add_course(request):
    if request.method=='POST':
        coursename=request.POST.get('coursename')
        coursefee= request.POST.get('coursefee')
        
        if coursename and coursefee:
            Addcourse.objects.create(coursename=coursename,coursefee=coursefee)
            messages.success(request,'Course added successfully!')
            return redirect('add_course')
        else:
            messages.error(request,'please fill all fields')
    return render(request,'add_course.html')

@login_required(login_url='login')
def add_student(request):
    courses=Addcourse.objects.all()
    #print(courses)
    if request.method == 'POST':
        stdname = request.POST.get('stdname')
        address = request.POST.get('address')
        age = request.POST.get('age')
        date = request.POST.get('date')
        course_id = request.POST.get('course')  

        course=Addcourse.objects.get(id=course_id)
        
        Student.objects.create(stdname=stdname,address=address,age=age,date=date,course=course)
       
        messages.success(request,'student added successfully')
        return redirect('add_student')
    return render(request,'add_student.html',{'courses':courses})


def teacher_reg(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        address = request.POST['address']
        age = request.POST['age']
        email = request.POST['email']
        contact = request.POST['contact']
        course_id = request.POST['course']

        if course_id == '':
            messages.info(request, 'Please select a course')
            return redirect('teacher_reg')

        if password != cpassword:
            messages.info(request, 'Passwords do not match')
            return redirect('teacher_reg')

        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists. Please choose a different one.')
            return redirect('teacher_reg')

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
        )
        user.save()
        

        teacher = Teacher(
            user=user,
            name=name,
            username=username,
            address=address,
            age=age,
            email=email,
            contact=contact,
            course=Addcourse.objects.get(id=course_id)
        )

        try:
            teacher.save()
            messages.success(request, 'Teacher registered successfully')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error saving teacher: {str(e)}')
            return redirect('teacher_reg')
        
    courses=Addcourse.objects.all()
    return render(request,'add_teacher.html', {'courses': courses})

def show_teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'show_teachers.html', {'teachers': teachers})

   
@login_required(login_url='login')
def teach_home(request):
    teachers=Teacher.objects.all()
    return render(request,'teach_home.html',{'teachers':teachers})

def edit_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk) 

    if request.method == 'POST':
        teacher.user.username = request.POST.get('user')
        teacher.name = request.POST.get('user')
        teacher.email = request.POST.get('email')
        teacher.address = request.POST.get('address')
        teacher.age = request.POST.get('age')
        teacher.contact = request.POST.get('contact')

        new_password = request.POST.get('password')
        if new_password:  
            teacher.password = new_password
        
        course_id = request.POST.get('course')
        teacher.course = Addcourse.objects.get(id=course_id)

        if request.FILES.get('image'):
            teacher.image = request.FILES['image']

        teacher.save()  
        messages.success(request, 'Teacher details updated successfully!')
        return redirect('show_teachers') 

    courses = Addcourse.objects.all()  
    return render(request,'editteacher.html', {'teacher': teacher, 'courses': courses})

@login_required(login_url='login')
def editstudent(request, pk):
    student = Student.objects.get(id=pk)  

    if request.method == 'POST':
        student.stdname = request.POST.get('stdname')
        student.address = request.POST.get('address')
        student.age = request.POST.get('age')
        student.date = request.POST.get('date')

        course_id = request.POST.get('course')
        student.course = Addcourse.objects.get(id=course_id)  
        student.save()  
        messages.success(request, 'Student details updated successfully!')
        return redirect('show_students')  

    courses = Addcourse.objects.all()  
    return render(request, 'editstudent.html', {'student': student, 'courses': courses})


def show_students(request):
    students = Student.objects.all()

    if request.method == "POST":
  
        pass

    return render(request, 'show_students.html', {
        'students': students,
        'messages': messages.get_messages(request),
    })
@login_required(login_url='login')
def delete_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    messages.success(request, "Student deleted successfully.")
    return redirect('show_students')


@login_required(login_url='login')
def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    

    if request.method == 'POST':
        teacher.delete()
        
        
        if teacher.user:
           teacher.user.delete()
        
        messages.success(request, 'Teacher has been deleted successfully.')
        return redirect('show_teachers')  
    return render(request, 'delete_confirmation.html', {'teacher': teacher})

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def teacher_profile(request):
    teacher = Teacher.objects.get(user=request.user)
    return render(request, 'teacher_profile.html', {'teacher': teacher})
