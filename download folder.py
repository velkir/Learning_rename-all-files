import gdown

url = 'https://drive.google.com/drive/folders/1sa1GJzLzwSDQyQPqzaIjzOD90kHnZe2E'
gdown.download_folder(url, quiet=True, use_cookies=False)