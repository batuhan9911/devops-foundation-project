Task1

devops-foundation-project klasörü oluşturdum. git init ile klasörü Git repository yaptım. app, docker, docs ve scripts klasörlerini oluşturdum. Git boş klasörleri takip edemediğini öğrendim. Bunun çin boş klasörlere .gitkeep eklendiğini öğrendim. git add . ile dosyaları staging area'ya aldım. git commit ile ilk kaydı oluşturdum. GitHubda devops-foundation-project repositorysini oluşturdum. git remote add origin ile local repositoryi GitHuba bağladım. git push ile commiti GitHuba gönderdim.










Task3 
Uygulama için app.py dosyası oluşturdum ai’a flask uygulaması yaptırdım txt dosyasına uygulama için flaskı ekledim. Dockerfile oluşturdum python 3.12slim image kullandım. WORKDIR ve klasörü /app’e koydum. Buraları ai’a sora sora yaptım. Portunu 8080 olarak yaptım. docker build ile devops-demo-app:1.0 image'ını oluşturdum. docker images ile imageın oluştuğunu kontrol ettim. Bunları yaparken docker deamona bağlanamadım docker desktop bozulmuş tekrar yükledim sorun düzeldi.  







Task4  Soruda yazılanları terminale girdim, DevOps Foundation Project is running!  Çıktısını aldım.  








task5

Önce çalışan devops-demo-app containerını kaldırdım docker rm -f devops-demo-app. Sonra bilerek yanlış portta çalıştırdım 
docker run -d \
  --name devops-demo-app \
  -p 9090:8080 \
  devops-demo-app:1.0
Sonra curl http://localhost:8080 yaparak bağlantı hatası aldım. containerı kaldırıp portu düzgün girdim düzeldi.  







task6  devops-network adında bir Docker network oluşturdum.
PostgreSQL, Redis ve uygulama containerını aynı networke bağladım. docker network ls ve docker network inspect ile üçününde bağlanıp bağlanmadığını kontrol ettim.  







task7  PostgreSQL containerını devops-network üzerinde çalıştırdım. users tablosunu id, name, email ve created_at alanlarıyla oluşturdum.
\d users ile tabloyu kontrol ettim.  







task8  PostgreSQL için postgres-data valime oluşturdum. Database ali, veli ve Ahmet isimlerini ekledim. PostgreSQL containerini sildim sonra valumu yeniden oluşturdum, SELECT * FROM users; ile kontrol ettiğimde isimler hala duruyordu burada container silinse bile valoumun hala kaldığını gördüm.  







task9  .env dosyası oluşturdum ve database ile Redis bilgilerini environment variable olarak tanımladım.
.env dosyasını .gitignore’a ekleyerek gite gitmesini engelledim.
 








task10  Aidan yardım aldım  







task11  App, PostgreSQL ve Redis servislerine healthcheck eklerken aidan yardım aldım. App için /health endpointini ve healthcheck yapısını oluştururken aidan yardım aldım.
docker compose ps ile üç servisin de healthy olduğunu doğruladım.









Task12  App processini bilerek durdurarak crash testi yaptım.
Containerın otomatik olarak yeniden başladığını ve tekrar healthy olduğunu doğruladım.  







task13  cevap1 : hata olup olmadığını ve gelen istekler için log oluşturur. cevap2: docker logs tek bir containerin loglarına bakar, docker compose logs compose projesindeki servislerin loglarına bakar. cevap3: docker logs --tail 100 devops-demo-app bunu bilmiyodum baktım cevap4: docker logs --timestamps devops-demo-app şeklindeymiş. cevap5: docker logs devops-demo-app çünkü uygulama neden kapanıyor hata var mı diye bakabiliyoruz. docker inspect devops-demo-app ile de restart atıyor mu atmıyo mu çalışanları komutları görebiliyoruz.  











task14 

A: PostgreSQL bağlantısını bozdum: sed -i '' 's/DATABASE_HOST=postgres/DATABASE_HOST=localhost/' .env

Düzeltmek için: sed -i '' 's/DATABASE_HOST=localhost/DATABASE_HOST=postgres/' .env


B: Redis bağlantısını bozdum: sed -i '' 's/REDIS_HOST=redis/REDIS_HOST=wrong-host/' .env

Düzeltmek için: sed -i '' 's/REDIS_HOST=wrong-host/REDIS_HOST=redis/' .env


C: task5in aynısıydı

D: PostgreSQL'i durdurdum: docker kill postgres
Tekrar çalıştırdım: docker start postgres  










task15


PostgreSQL veritabanının backupını pg_dump ile backup.sql dosyasına aldım.
docker exec postgres pg_dump -U devops -d devopsdb > backup.sql
devopsdb database'ini sildim ve yeniden oluşturdum.
Backup'ı geri yükledim: cat backup.sql | docker exec -i postgres psql -U devops -d devopsdb burada anladığım backup.sql ve psql devopsdb içine tekrar yükleniyor.
SELECT * FROM users; ile kontrol ettim ali, veli ve ahmet verilerinin geri geldiğini gördüm.  











task16 

develop ve feature/docker-compose branchlerini oluşturdum. Feature yeni özellik geliştirmek debugfix hata düzeltirken kullanıldığını gördüm.
Feature branchinde değişiklikleri kaydettim:
git add .
git commit -m "Add docker compose stack"

Feature branchini GitHuba gönderdim:
git push origin feature/docker-compose

GitHubda feature/docker-compose develop için pull sonra merge yaptım.

Son olarak develop branchini main ile birleştirip GitHuba gönderdim:
git merge develop
git push origin main









Task17

Anlamlılar   








task18

Bu taskda aidan yardım aldım. Kısa yol oluşturuyoruz chmod +x kullanarak.
 ./scripts/start.sh başlatmak için stop, log, backup ve status olarak da ayarladım kısaca docker komutları kullanmak yerine bu scriptleri kullanıyoruz.  






task19 
task14le benzerdi.  







task20

Killercoda üzerinde yeni bir Ubuntu Linux ortamı kullandım.
Git ve Dockerı kontrol ettim. Docker Compose kurulu olmadığı için kurdum.
Projeyi GitHubdan clone ettim: git clone https://github.com/batuhan9911/devops-foundation-project.git
.env dosyasını oluşturdum. Sistemi tek komutla çalıştırdım: docker compose up -d
docker compose ps ile app, PostgreSQL ve Redis'in healthy olduğunu gördüm. Sistemi yeni bir Linux ortamında sıfırdan ayağa kaldırabildim.
