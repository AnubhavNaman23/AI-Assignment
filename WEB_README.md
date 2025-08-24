# 🌐 LQT AI Assignment - Web Application

## Project Overview

This project is a comprehensive **AI Developer Portfolio** built as a web application for the LQT AI Assignment. It demonstrates advanced machine learning capabilities, data visualization, and modern web development practices through an interactive dashboard.

### 🎯 Key Features

- **Interactive Web Dashboard**: Professional web interface with real-time analytics
- **Machine Learning Models**: Multiple algorithms with performance comparison
- **Data Visualization**: Dynamic charts and plots using Matplotlib/Seaborn
- **REST API**: RESTful endpoints for data operations and predictions
- **Responsive Design**: Bootstrap 5 with mobile-first approach
- **Real-time Processing**: AJAX-powered frontend with live updates

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip package manager
- Modern web browser

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/lqt-ai-assignment.git
cd lqt-ai-assignment
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python src/api/app.py
```

4. **Open in browser**
```
http://localhost:5000
```

## 🏗️ Architecture

### Backend (Flask)
- **Framework**: Flask with RESTful API design
- **ML Pipeline**: Scikit-learn for model training and predictions
- **Visualization**: Matplotlib/Seaborn for dynamic chart generation
- **Data Processing**: Pandas/NumPy for data manipulation

### Frontend (Web)
- **Framework**: Bootstrap 5 for responsive design
- **JavaScript**: Vanilla JS with async/await for API calls
- **Styling**: Custom CSS with animations and transitions
- **Charts**: Dynamic visualization integration

### Project Structure
```
LQT AI assignment/
├── src/
│   ├── api/
│   │   └── app.py              # Main Flask application
│   ├── data/
│   │   └── data_loader.py      # Data generation utilities
│   ├── models/
│   │   └── classification.py   # ML model implementations
│   └── visualization/
│       └── plots.py           # Chart generation
├── templates/
│   ├── index.html             # Landing page
│   └── dashboard.html         # Main dashboard
├── static/
│   ├── css/
│   │   └── style.css          # Custom styling
│   └── js/
│       ├── app.js             # Main application JS
│       └── dashboard.js       # Dashboard functionality
├── requirements.txt           # Python dependencies
└── test_web_app.py           # Web application tests
```

## 🔧 API Endpoints

### Core Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page |
| `/dashboard` | GET | Main dashboard |
| `/api/health` | GET | API health check |

### Data & ML Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/generate_data` | POST | Generate sample dataset |
| `/api/train_models` | POST | Train ML models |
| `/api/predict` | POST | Make predictions |
| `/api/visualize/<type>` | GET | Generate visualizations |

### Example API Usage

**Generate Data:**
```bash
curl -X POST http://localhost:5000/api/generate_data \
  -H "Content-Type: application/json" \
  -d '{"samples": 1000}'
```

**Train Models:**
```bash
curl -X POST http://localhost:5000/api/train_models
```

**Make Prediction:**
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 30,
    "income": 55000,
    "education_years": 16,
    "experience": 8.5,
    "satisfaction_score": 7.5,
    "performance_rating": 4
  }'
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_web_app.py
```

The test suite covers:
- ✅ Web page accessibility
- ✅ API health checks
- ✅ Data generation
- ✅ Model training
- ✅ Prediction accuracy
- ✅ Visualization rendering

## 🎨 Features Walkthrough

### 1. Landing Page (`/`)
- Professional hero section with animated background
- Feature showcase with interactive cards
- Technology stack display
- Call-to-action for dashboard access

### 2. AI Dashboard (`/dashboard`)
- **Data Generation**: Create synthetic datasets with custom parameters
- **Model Training**: Train multiple ML algorithms simultaneously
- **Performance Analysis**: Compare model metrics with visualization
- **Real-time Predictions**: Interactive prediction interface
- **Dynamic Visualizations**: Correlation, distribution, and performance charts

### 3. Machine Learning Models
- **Logistic Regression**: Linear classification with probability scores
- **Random Forest**: Ensemble method with feature importance
- **Support Vector Machine**: Non-linear classification with kernel methods

### 4. Visualization Types
- **Correlation Matrix**: Feature relationship heatmap
- **Distribution Plots**: Data distribution analysis
- **Pair Plots**: Multi-dimensional scatter plots
- **Performance Charts**: Model accuracy comparison

## 🔐 Technical Specifications

### Dependencies
```
Flask==2.3.3
pandas==2.1.1
numpy==1.24.3
scikit-learn==1.3.0
matplotlib==3.7.2
seaborn==0.12.2
```

### Browser Compatibility
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

### Performance Metrics
- Page load time: <2s
- API response time: <500ms
- Model training time: <10s (1000 samples)

## 🚢 Deployment

### Local Development
```bash
python src/api/app.py
```

### Production (Docker)
```bash
docker build -t lqt-ai-assignment .
docker run -p 5000:5000 lqt-ai-assignment
```

## 📊 Monitoring & Analytics

The application includes:
- Real-time API health monitoring
- Performance metrics tracking
- Error logging and reporting
- User interaction analytics

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**LQT AI Assignment**
- Portfolio demonstration of AI/ML web development skills
- Modern full-stack architecture with Python/Flask and vanilla JavaScript
- Professional deployment-ready web application

## 🔗 Links

- **Live Demo**: [Coming Soon]
- **API Documentation**: Available at `/api/health`
- **Repository**: [GitHub Repository]

---

**Built with ❤️ for the LQT AI Assignment**

*Demonstrating modern web development, machine learning integration, and professional software engineering practices.*
