from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Course
from .forms import CourseForm
TIMES = [('08:10','09:00'),('09:10','10:00'),('10:10','11:00'),('11:10','12:00'),('13:30','14:20'),('14:25','15:15'),('15:25','16:15'),('16:20','17:10'),('17:15','18:05')]
def weekly(request):
    courses = list(Course.objects.order_by('weekday', 'start'))
    for course in courses:
        course.time_start = TIMES[course.start - 1][0]
        course.time_end = TIMES[course.end - 1][1]
    rows = []
    for period, times in enumerate(TIMES, 1):
        cells = []
        for day in range(1, 8):
            course = next((c for c in courses if c.weekday == day and c.start <= period <= c.end), None)
            if course and course.start != period and period != 5: continue
            segment_end = min(course.end, 4) if course and period <= 4 else (course.end if course else period)
            cells.append({'course':course, 'span': segment_end - period + 1 if course else 1})
        rows.append({'period':period, 'start':times[0], 'end':times[1], 'cells':cells})
    return render(request, 'weekly.html', {'rows':rows, 'count':len(courses)})
def detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'detail.html', {'course': course, 'time_start': TIMES[course.start - 1][0], 'time_end': TIMES[course.end - 1][1]})
def edit(request, pk=None):
    course = get_object_or_404(Course, pk=pk) if pk else None
    form = CourseForm(request.POST or None, instance=course)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('weekly')
    return render(request, 'form.html', {'form':form, 'course':course})
def delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('weekly')
    return render(request, 'delete.html', {'course':course})
