from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict
from pure_pagination import PageNotAnInteger, Paginator  # 分页
from .forms import UserAskForm
from django.http import HttpResponse
import json


# organization list
class OrgListView(View):
    def get(self, request):
        allOrg = CourseOrg.objects.all()
        allCity = CityDict.objects.all()

        # 筛选
        cityID = request.GET.get('city', '')
        category = request.GET.get('ct', '')
        sortType = request.GET.get('sort', '')
        if cityID:
            allOrg = allOrg.filter(city_id=int(cityID))
        if category:
            allOrg = allOrg.filter(category=category)
        if sortType:
            allOrg = allOrg.order_by('-' + sortType)
        hotOrg = allOrg.order_by("clickNum")[:3]
        orgNum = allOrg.count()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(allOrg, 1, request=request)
        orgs = p.page(page)

        return render(request, "org-list.html", {
            'allOrg': orgs,
            'allCity': allCity,
            'orgNum': orgNum,
            'cityID': cityID,
            'category': category,
            'hotOrg': hotOrg,
            'sortType': sortType
        })


# 用户添加咨询
class UserAskView(View):
    def post(self, request):
        userAskForm = UserAskForm(request.POST)
        if userAskForm.is_valid():
            userAsk = userAskForm.save(commit=True)
            return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
        else:
            return HttpResponse(json.dumps({'status': 'fail', 'msg': "Input Incorrect!"}),
                                content_type='application/json')


class OrgHomeView(View):
    def get(self, request, orgName):
        currentPage = "home"
        courseOrg = CourseOrg.objects.get(name=orgName)
        allCourses = courseOrg.course_set.all()[:3]
        allTeachers = courseOrg.teacher_set.all()[:1]
        return render(request, 'org-detail-homepage.html', {
            "allCourses": allCourses,
            "allTeachers": allTeachers,
            "courseOrg": courseOrg,
            "currentPage": currentPage
        })


class OrgCourseView(View):
    def get(self, request, orgName):
        currentPage = "course"
        courseOrg = CourseOrg.objects.get(name=orgName)
        allCourses = courseOrg.course_set.all()

        return render(request, 'org-detail-course.html', {
            "courseOrg": courseOrg,
            "allCourses": allCourses,
            "currentPage": currentPage
        })


class OrgDescView(View):
    def get(self, request, orgName):
        currentPage = "desc"
        courseOrg = CourseOrg.objects.get(name=orgName)

        return render(request, 'org-detail-desc.html', {
            "courseOrg": courseOrg,
            "currentPage": currentPage
        })


class OrgTeacherView(View):
    def get(self, request, orgName):
        currentPage = "teacher"
        courseOrg = CourseOrg.objects.get(name=orgName)
        allTeachers = courseOrg.teacher_set.all()

        return render(request, 'org-detail-teachers.html', {
            "courseOrg": courseOrg,
            "currentPage": currentPage,
            'allTeachers': allTeachers
        })
