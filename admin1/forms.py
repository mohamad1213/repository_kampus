from django.forms import ModelForm
from django import forms
from .models import *
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    class Meta:
         model = User
         fields = ['username', 'password1']
class UploadForm(ModelForm):
    class Meta:
         model = Upload
         exclude = ['owner','favourite']
         widgets = {
            'judul_laporan': forms.TextInput({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'tahun_penyelesaian': forms.TextInput({'class': 'form-control form-control-sm', 'type':'number','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'abstrak': forms.Textarea({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'nama_penulis': forms.TextInput({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'nim_siswa': forms.TextInput({'class': 'form-control form-control-sm', 'type':'number','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'prodi': forms.Select({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'jenis_laporan': forms.Select({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
        }
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['prodi'].empty_label = 'Select Prodi ...'
        self.fields['jenis_laporan'].empty_label = 'Select Jenis Journal ...'
        self.fields['upload'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
class UploadSkripsiForm(ModelForm):
    class Meta:
         model = UploadSkripsi
         exclude = ['owner','favourite']
         widgets = {
            'judul_laporan': forms.TextInput({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'tahun_penyelesaian': forms.TextInput({'class': 'form-control form-control-sm', 'type':'number','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'abstrak': forms.Textarea({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'nama_penulis': forms.TextInput({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'nim_siswa': forms.TextInput({'class': 'form-control form-control-sm', 'type':'number','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
            'prodi': forms.Select({'class': 'form-control form-control-sm', 'type':'text','style':'padding:6px 10px ;border: 1px solid #ced4da'}),
        }
    def __init__(self, *args, **kwargs):
        super(UploadSkripsiForm, self).__init__(*args, **kwargs)
        self.fields['prodi'].empty_label = 'Select Prodi ...'
        self.fields['lampiran'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['cover'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['daftarisi'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['bab1'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['bab2'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['bab3'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['bab4'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['bab5'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
        self.fields['dapus'].widget.attrs.update({ 'class': 'form-control','type':'file', 'accept':'application/pdf','style':'padding:6px 10px ;border: 1px solid #ced4da'})
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({ 'class': 'form-control', 'type': 'email' })
        self.fields['alamat'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['name'].widget.attrs.update({ 'class': 'form-control', 'type': 'text' })
        self.fields['profile_pic'].widget.attrs.update({ 'class': 'form-control', 'type': 'file' })
        self.fields['phone'].widget.attrs.update({ 'class': 'form-control', 'type': 'number' })

class EditProfileForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    phone = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    alamat = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio','phone','alamat']

def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg