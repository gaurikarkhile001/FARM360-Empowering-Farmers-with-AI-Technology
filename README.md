

# FARM360 - Empowering Farmers with AI Technology 🌾

FARM360 is an AI-powered platform designed to empower farmers with intelligent solutions to enhance agricultural productivity and decision-making. The platform integrates cutting-edge AI and IoT technologies to provide actionable insights and recommendations, helping farmers make informed choices about their crops, fertilizers, and market strategies.

---

## Features 🚜

1. **Crop Recommendation** 🌱  
   Get AI-driven crop recommendations based on soil data, weather patterns, and market demand.

2. **Market Price** 💰  
   Access real-time market prices for various crops, helping farmers maximize their profits.

3. **Plant Disease Prediction** 🦠  
   Identify plant diseases early and receive actionable advice to manage and prevent damage.

4. **Fertilizer Suggestions** 🌾  
   Receive customized fertilizer recommendations tailored to crop type and soil health.

---

## Deployment 🛠️

### Docker Image  
This project is containerized using Docker for portability and scalability.  
The Docker image is publicly available on Docker Hub:  
**[https://hub.docker.com/u/gaurikarkhile](https://hub.docker.com/u/gaurikarkhile)**

### Deployment on AWS EC2  
FARM360 is deployed on an AWS EC2 instance for high availability and scalability.  
You can access the platform at: **[(http://your-ec2-public-ip)](http://your-ec2-public-ip)**

---

## Getting Started 🚀

### Prerequisites
- Docker installed locally
- AWS account with EC2 setup
- Python 3.8+ (if running locally)

### Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/gaurikarkhile001/FARM360-Empowering-Farmers-with-AI-Technology.git
   cd FARM360
   ```

2. **Build the Docker Image**  
   ```bash
   docker build -t flask-mlops-app:latest .
   ```

3. **Run the Docker Container**  
   ```bash
   docker run -p 8000:8000 flask-mlops-app:latest
   ```

4. **Push the Docker Image to Docker Hub**  
   ```bash
   docker tag flask-mlops-app:latest gaurikarkhile/flask-mlops-app:latest
   docker push gaurikarkhile/flask-mlops-app:latest
   ```

5. **Deploy on AWS EC2**  
   - Pull the Docker image from Docker Hub on the EC2 instance:  
     ```bash
     docker pull gaurikarkhile/flask-mlops-app:latest
     ```
   - Run the container on the EC2 instance:  
     ```bash
     docker run -d -p 80:8000 gaurikarkhile/flask-mlops-app:latest
     ```

---

## Technologies Used 🛠️

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Models:** TensorFlow, Scikit-learn  
- **Containerization:** Docker  
- **Cloud:** AWS EC2  

---

## How It Works 🔍

1. **Crop Recommendation**  
   - Analyzes soil type, weather data, and historical patterns to recommend the most suitable crops.

2. **Market Price**  
   - Integrates APIs to fetch real-time market data for crops.

3. **Plant Disease Prediction**  
   - Uses AI models to classify diseases based on leaf images uploaded by users.

4. **Fertilizer Suggestions**  
   - Suggests the best fertilizers based on crop needs and soil condition.

---

## Future Scope ✨

- Integration with IoT sensors for real-time crop monitoring.  
- Addition of weather forecasting for precise farming.  
- Expansion to include livestock management features.  
- Mobile app for accessibility.

---

## Contributing 🤝

We welcome contributions from the community!  
Feel free to fork the repository and submit a pull request.  

---

## License 📜

This project is licensed under the [MIT License](LICENSE).

---

## Contact 📧

For any queries or support, please contact:  
**Gauri Karkhile**  
- **Email:** [gaurikarkhile1@gmail.com](mailto:gaurikarkhile1@gmail.com)  
```
