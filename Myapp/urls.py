from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('',views .login,name='login'),
    path('register',views.register,name='register'),
    path('otp',views.otp),
    path('fpass',views.fpass,name='fpass'),
    # path('newpass',views.newpass,name='newpass'),

    path('logout', views.logout,name='logout'),
    path('forgot', views.forgot,name='forgot'),
    path('p404',views.p404,name='p404'),
    path('p500',views.p500,name='p500'),
    path('addcourse',views.addcourse,name='addcourse'),
    
    path('accordion',views.accordion,name='accordion'),
    path('adddepartment',views.adddepartment,name='adddepartment'),
    path('addlibraryassets',views.addlibraryassets,name='addlibraryassets'),
    path('addprofessor',views.addprofessor,name='addprofessor'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('advanceformelement',views.advanceformelement,name='advanceformelement'),
    path('alerts',views.alerts,name='alerts'),

    path('allcourses',views.allcourses,name='allcourses'),
    path('allprofessors',views.allprofessors,name='allprofessors'),
    path('allstudents',views.allstudents,name='allstudents'),
    path('analytics',views.analytics,name='analytics'),
    path('areacharts',views.areacharts,name='areacharts'),  
    path('barcharts',views.barcharts,name='barcharts'),
    path('basicformelement',views.basicformelement,name='basicformelement'),
    path('buttons',views.buttons,name='buttons'),
    path('c3',views.c3,name='c3'),
    path('codeeditor',views.codeeditor,name='codeeditor'),
    path('courseinfo',views.courseinfo,name='courseinfo'),
    path('coursepayment',views.coursepayment,name='coursepayment'),

    path('datamaps',views.datamaps,name='datamaps'),
    path('datatable',views.datatable,name='datatable'),
    path('departments',views.departments,name='departments'),
    path('duallistbox',views.duallistbox,name='duallistbox'),

    path('editcourse',views.editcourse,name='editcourse'),
    path('editdepartment',views.editdepartment,name='editdepartment'),
    path('editlibraryassets',views.editlibraryassets,name='editlibraryassets'),
    path('editprofessor',views.editprofessor,name='editprofessor'),
    path('editstudent',views.editstudent,name='editstudent'),
    path('events',views.events,name='events'),
    
    path('googlemap',views.googlemap,name='googlemap'),
    path('imagescropper',views.imagescropper,name='imagescropper'),
    path('libraryassets',views.libraryassets,name='libraryassets'),
    path('linecharts',views.linecharts,name='linecharts'),
    path('lock',views.lock,name='lock'),
    path('mailbox',views.mailbox,name='mailbox'),
    path('myprofile',views.myprofile,name='myprofile'),

    path('mailboxcompose',views.mailboxcompose,name='mailboxcompose'),
    path('mailboxview',views.mailboxview,name='mailboxview'),
    path('modals',views.modals,name='modals'),
    path('multiupload',views.multiupload,name='multiupload'),
    path('notifications',views.notifications,name='notifications'),
    path('passwordmeter',views.passwordmeter,name='passwordmeter'),
    path('passwordrecovery',views.passwordrecovery,name='passwordrecovery'),
    path('pdfviewer',views.pdfviewer,name='pdfviewer'),
    path('preloader',views.preloader,name='preloader'),
    path('professorprofile',views.professorprofile,name='professorprofile'),
    path('roundedchart',views.roundedchart,name='roundedchart'),
    path('sparkline',views.sparkline,name='sparkline'),
    path('statictable',views.statictable,name='statictable'),
    path('mailbox',views.mailbox,name='mailbox'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('tabs',views.tabs,name='tabs'),
    path('tinymc',views.tinymc,name='tinymc'),
    path('treeview',views.treeview,name='treeview'),
    path('widgets',views.widgets,name='widgets'),
    path('xeditable',views.xeditable,name='xeditable'),
    path('peity',views.peity,name='peity'),
]
