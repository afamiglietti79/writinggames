from django.urls import path
from . import views

app_name = "feud"
urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('newprompt', views.newPrompt.as_view(), name="newprompt"),
    path('<int:prompt_id>/displayprompt', views.displayPrompt.as_view(), name="displayprompt"),
    path('<int:prompt_id>/editprompt', views.editPrompt.as_view(), name="editprompt"),
    path('<int:prompt_id>/listResponses', views.listResponses.as_view(), name="listresponses"),
    path('<int:prompt_id>/ajaxresponses', views.ajaxResponses, name="ajaxresponses"),
    path('<int:prompt_id>/toggleVote', views.toggleVoteStatus, name="togglevote"),
    path('<int:response_id>/vote', views.vote, name="vote"),
    path('<int:prompt_id>/deleteprompt', views.deletePrompt, name="deleteprompt")
]
