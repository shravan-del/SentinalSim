# SentinelSim: Defense AI for Drone Threat Detection

A sophisticated AI-powered defense system that demonstrates advanced object tracking and threat prediction capabilities. This project showcases the integration of machine learning with real-world defense applications.

## 🎯 Features

- Real-time drone and object detection using YOLOv5
- Threat level assessment and scoring
- Interactive web interface for image upload and analysis
- Visual threat detection mapping
- Advanced statistical analysis of detected objects

## 🛠️ Technology Stack

- **Backend**: Python, PyTorch, OpenCV
- **ML Model**: YOLOv5 (pre-trained)
- **Frontend**: Streamlit
- **Data Processing**: NumPy, Pandas
- **Visualization**: Matplotlib

## 🚀 Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SentinelSim.git
cd SentinelSim
```

2. Create and activate a virtual environment:
```bash
python -m venv sentinelsim-env
source sentinelsim-env/bin/activate  # On Windows: sentinelsim-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## 📊 Usage

1. Access the web interface at `http://localhost:8501`
2. Upload an aerial image containing potential threats
3. The system will:
   - Detect objects using YOLOv5
   - Calculate threat levels
   - Display visual analysis
   - Provide threat assessment scores

## 🔒 Security Note

This is a simulation project intended for educational and demonstration purposes only. It should not be used in real-world defense applications without proper validation and security measures.

## 📝 License

MIT License - see LICENSE file for details 