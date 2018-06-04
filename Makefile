run: 
	@echo 'Building API Image'
	docker build -t interview_api_image .

	@echo 'Starting the Container' 
	docker run -d --name api_container -p 3000:3000 -v /tmp/logs/:/tmp/logs interview_api_image
