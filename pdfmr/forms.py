from django import forms
from django.conf import settings
from django.core.files.storage import default_storage
import os, random, string

class UploadForm(forms.Form):
    """
    PDFアップロード用フォームの定義
    saveメソッドはアップロードしたPDFを一時フォルダに保存する。
    """
    
    # <input type = "upload">の形式でフォームを生成 --> documentでアップロードされたファイルにアクセス可能となる
    document = forms.FileField(label = "PDFアップロード",
                                widget = forms.ClearableFileInput(attrs = {'multiple' : True}),
    )

    def save(self):
        # request.FILESの中で、アップロードされたファイルは管理されており、フォーム側からはself.files.getlist()でアクセスできる
        upload_files = self.files.getlist('document')
        # 途中ファイル保存用のパスを生成する
        temp_dir = os.path.join(settings.MEDIA_ROOT, self.create_dir(10))
        
        for pdf in upload_files:
            # default_storage.save()で任意のファイルをローカルに保存できる
            default_storage.save(os.path.join(temp_dir, pdf.name), pdf)
        return temp_dir
    
    def create_dir(self,n):
        """一時フォルダ生成関数"""
        return 'pdf/' + ''.join(random.choices(string.ascii_letters + string.digits, k = n))