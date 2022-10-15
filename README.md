# Report Viewer 

一個基於Django MTV架構的報表檢視服務，連結PostgreSQL資料庫。並透過Docker解決不同環境下的佈署問題。


## 環境需求

需在有Docker與docker-compose的環境執行

## 佈署服務

1. 將專案從Server載到本機環境
```
git clone https://github.com/chialatte2129/report-viewer.git
```
2. 進入專案資料夾
```
cd report-viewer
```
3. 使用docker-compose啟動服務
```
docker-compose up
```
4. 確定container有正常啟動，並複製container id
```
docker ps
```
5. 首次啟動後，執行資料庫初始化，先創建資料庫異動檔。 <your_container_id>請填入上一步複製的container id
```
docker exec -ti <your_container_id> python manage.py makemigrations
```
6. 執行資料庫異動檔
```
docker exec -ti <your_container_id> python manage.py migrate
```
7. 創建管理員帳號
```
docker exec -ti <your_container_id> python manage.py createsuperuser
```
8. 服務會啟在 http://127.0.0.1:8000/
9. 後台管理網址 http://127.0.0.1:8000/admin
10. 停止服務
```
docker-compose down
```
