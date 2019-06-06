#coding = utf-8


# 文件上传
class UploadFile:
    # 上传路径
    UPLOAD_FOLODER = "static/file"
    # 所有能够通过的数据类型
    ALLOWED_EXTENIONS = ["jpg","png","gif","bmp"]
    # 文件大小
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB


config = {
    'fileupload':UploadFile
}
