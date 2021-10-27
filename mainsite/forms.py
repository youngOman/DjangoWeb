from django.contrib.auth.forms import UserCreationForm
from django.db.models.enums import Choices
from django.forms import fields
from mainsite.models import User,Post,Category
from django import forms
class Loginform(forms.Form):
    account=forms.CharField(label="帳號", max_length=25, required=True,widget=forms.TextInput(attrs={'placeholder':'帳號...'}))
    password=forms.CharField(label="密碼", max_length=20,required=True,widget=forms.PasswordInput(attrs={'placeholder':'密碼...'}))
class Userregisterform(UserCreationForm):#繼承UserCreationForm類別
    username = forms.CharField(label="帳號",widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="電子郵件",widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密碼",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="密碼確認",widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2'] # User類別內的instance   

# choices=[(),(),()] 寫死的寫法
Choices=Category.objects.all().values_list('Category_name','Category_name') #成雙固定寫法
choice_list=[]
for item in Choices:
    choice_list.append(item)
class Postform(forms.ModelForm): #繼承forms.ModelForm類別
    class Meta:
        model=Post
        fields=['pub_title','title_tag','author','category','pub_body',]
        widgets={
            'pub_title':forms.TextInput(attrs={'class': 'form-control'}), #,'id':'exampleFormControlInput1'
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-select'}),
            'category':forms.Select(choices=choice_list,attrs={'class': 'form-select'}),
            'pub_body':forms.Textarea(attrs={'class': 'form-control','placeholder':'今天我想婆.....'})
        }
    def __init__(self,*args, **kwargs):
        super(Postform,self).__init__(*args, **kwargs) #能避免覆寫父類別(ModelForm)的method
        self.fields['pub_title'].label='文章標題'
        self.fields['pub_body'].label='內容'
        self.fields['author'].label='作者'
        self.fields['category'].label='分類'
        
class EditForm(forms.ModelForm): #繼承forms.ModelForm類別
    class Meta:
        model=Post
        fields=['pub_title','title_tag','pub_body']
        widgets={
            'pub_title':forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag':forms.TextInput(attrs={'class': 'form-control'}),
            'pub_body':forms.Textarea(attrs={'class': 'form-control'})
        }
        labels={
            'pub_title':'文章標題',
            'pub_body':'內容',
        }
        




