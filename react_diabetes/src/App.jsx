import { useState, useRef } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import "./App.css";

const initialForm = {
  HighBP: 0,
  HighChol: 0,
  CholCheck: 0,
  BMI: 0,
  Smoker: 0,
  Stroke: 0,
  HeartDiseaseorAttack: 0,
  PhysActivity: 0,
  Fruits: 0,
  Veggies: 0,
  HvyAlcoholConsump: 0,
  AnyHealthcare: 0,
  NoDocbcCost: 0,
  GenHlth: 0,
  MentHlth: 0,
  PhysHlth: 0,
  DiffWalk: 0,
  Sex: 0,
  Age: 0,
  Education: 0,
  Income: 0,
};

function HomeSection() {
  return (
    <div className="home-section">
      <img
        src="https://www.tissupath.com.au//wp-content/uploads/Diabetes-Overview-1-768x768.png"
        alt="Futuristic diabetes overview"
        className="home-image"
      />
      <h1>Diabetes Health Predictor</h1>
      <p>
        Welcome to the Diabetes Health Predictor! This web application leverages advanced machine learning algorithms to help you assess your risk of developing diabetes based on a variety of health indicators. By entering your personal health data—such as blood pressure, cholesterol levels, BMI, lifestyle habits, and more—you will receive an instant prediction about your diabetes risk category.
      </p>
      <p>
        Our goal is to empower you with personalized insights that can support early detection and prevention. The prediction is generated using a model trained on real-world health data, but it is not a substitute for professional medical advice. For any health concerns, please consult a healthcare provider.
      </p>
      <p>
        To get started, simply navigate to the Prediction section, fill in the required fields, and click "Calculate" to see your result. Your privacy is important to us—no data is stored or shared.
      </p>
    </div>
  );
}

function PredictionSection() {
  const [form, setForm] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const formRef = useRef(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: Number(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    try {
      const res = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const data = await res.json();
      setResult(data.prediction);
    } catch (err) {
      setResult("Server connection error!");
    }
    setLoading(false);
  };

  return (
    <>
      <img
        src="https://cdn.analyticsvidhya.com/wp-content/uploads/2022/01/30738medtec-futuristic-650-672c56a896ab7.webp"
        alt="Futuristic AI diabetes prediction"
        className="prediction-image"
      />
      <h1>Diabetes Prediction</h1>
      <form ref={formRef} onSubmit={handleSubmit} className="form-grid">
        {Object.keys(initialForm).map((key) => (
          <div key={key}>
            <label>
              {key}:
              <input
                type="number"
                name={key}
                value={form[key]}
                onChange={handleChange}
                required
              />
            </label>
          </div>
        ))}
        <button type="submit" disabled={loading}>
          {loading ? "Calculating..." : "Calculate"}
        </button>
      </form>
      {result !== null && (
        <div className="result-box">
          <strong>Prediction:</strong> {result}
        </div>
      )}
    </>
  );
}

function ContactSection() {
  return (
    <div className="contact-section">
      <h1>Contact</h1>
      <p>For questions or feedback, please contact us at <a href="https://github.com/popaalex1">https://github.com/popaalex1</a>.</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <nav className="navbar">
        <Link to="/">Home</Link>
        <Link to="/prediction">Prediction</Link>
        <Link to="/contact">Contact</Link>
      </nav>
      <div className="app-container">
        <Routes>
          <Route path="/" element={<HomeSection />} />
          <Route path="/prediction" element={<PredictionSection />} />
          <Route path="/contact" element={<ContactSection />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App; 