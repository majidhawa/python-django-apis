from django.shortcuts import render
from api.serializer import Class_PeriodSerializer, CourseSerializer, ClassroomSerializer, StudentSerializer, TeacherSerializer
from classperiod.models import Class_Period
from classroom.models import Classroom
from course.models import Courses
from rest_framework import status
from student.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from teacher.models import Teacher
# Create your views here.

class StudentListViews(APIView):
    def get(self, request):
        students = Student.objects.all()
        first_name = request.query_params.get("first_name")
        if first_name:
            students = students.filter(first_name=first_name)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
class CourseListViews(APIView):
    def get(self, request):
        course = Courses.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
class ClassroomListViews(APIView):
    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
class Class_PeriodListViews(APIView):
    def get(self, request):
        class_period = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_period, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = Class_PeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data) 
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get( id = id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class TeacherDetailView(APIView):
    def get(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    def put(self, request, id):
        teacher = Teacher.objects.get(id = id)
        serializer = TeacherSerializer(teacher, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        teacher = Teacher.objects.get( id = id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class CourseDetailView(APIView):
    def get(self, request, id):
        course = Courses.objects.get(id = id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    def put(self, request, id):
        course = Courses.objects.get(id = id)
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        course = Courses.objects.get( id = id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassroomDetailView(APIView):
    def get(self, request, id):
        classroom = Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data)
    def put(self, request, id):
        classroom = Classroom.objects.get(id = id)
        serializer = ClassroomSerializer(classroom, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        classroom = Classroom.objects.get( id = id)
        classroom.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class Class_PeriodDetailView(APIView):
    def get(self, request, id):
        class_period = Class_Period.objects.get(id = id)
        serializer = Class_PeriodSerializer(class_period)
        return Response(serializer.data)
    def put(self, request, id):
        class_period = Class_Period.objects.get(id = id)
        serializer = Class_PeriodSerializer(class_period, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        class_period= Class_Period.objects.get( id = id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class AssignStudentToClass(APIView):
    def post(self, request, class_period_id):
        try:
            class_period = Class_Period.objects.get(id=class_period_id)
        except Class_Period.DoesNotExist:
            return Response({'error': 'Class period not found'}, status=status.HTTP_404_NOT_FOUND)

        student_id = request.data.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        class_period.student = student
        class_period.save()

        serializer = Class_PeriodSerializer(class_period)
        return Response(serializer.data, status=status.HTTP_200_OK)
class AssignTeacherToCourse(APIView):
    def post(self, request, course_id):
        try:
            course = Courses.objects.get(id=course_id)
        except Courses.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        teacher_id = request.data.get('teacher_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        course.teacher = teacher
        course.save()

        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AssignTeacherToClassroom(APIView):
    def post(self, request, classroom_id):
        try:
            classroom = Classroom.objects.get(id=classroom_id)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)

        teacher_id = request.data.get('teacher_id')
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        classroom.class_teacher = teacher
        classroom.save()

        serializer = ClassroomSerializer(classroom)
        return Response(serializer.data, status=status.HTTP_200_OK)
class WeeklyTimetable(APIView):
    def get(self, request):
        class_periods = Class_Period.objects.all()
        serializer = Class_PeriodSerializer(class_periods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

