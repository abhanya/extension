from django.urls import path
from . import views

urlpatterns = [
    path('master',views.extension_master,name='mast'),
    path('',views.extension_home,name='home'),
    path('about',views.extension_about,name='about'),
    # path('contact',views.extension_,name='contact'),
    # path('new',views.extension_new,name="new"),
    path('images',views.extension_image,name="image"),
    path('baabtra',views.extension_baabtra,name="baabtra"),
    path('newpage',views.extension_newpage,name="newpage"),
    path('cssbox',views.extension_cssbox,name="cssbox"),
    path('cssrule',views.extension_cssrule,name="rule"),
    path('grid',views.extension_grid,name="grid"),
    path('gridalign',views.extension_gridalign,name="grida"),
    # path('modal',views.extension_modal,name="mod"),
    path('java',views.extension_java,name="ja"),
    path('javan',views.extension_javan,name="jav"),
    path('func',views.extension_fun,name="jav"),
    path('newjava',views.extension_new,name="jav"),
    path('jswork',views.extension_work,name="work"),
    path('dom',views.extension_dom,name="dm"),
    path('domnew',views.extension_domnew,name="dm"),
    path('domwrk',views.extension_domwork,name="dm"),
    path('jwrk',views.extension_jsworknw,name="dm"),
    path('wrk',views.extension_work,name="dm"),
    path('neww',views.extension_newjv,name="dm"),
    path('newwork',views.extension_newwork,name="dm"),
    path('local',views.extension_localstor,name="dm"),
    path('tra',views.extension_traverse,name="dm"),
    path('jq',views.extension_signup,name="dm"),
    path('test',views.extension_test,name="dm"),
    path('pr',views.extension_pot,name="dm"),












    
]