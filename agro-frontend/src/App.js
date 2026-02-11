import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { LayoutDashboard, FileText, Send, Loader2, Leaf, Languages } from 'lucide-react';
import Dashboard from './Dashboard';
import { translations } from './translations';
import './App.css';

function App() {
  const [lang, setLang] = useState('en');
  const t = translations[lang];

  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });

  React.useEffect(() => {
    const handleMouseMove = (e) => {
      setMousePos({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  const [formData, setFormData] = useState({
    area: 0, rainfall: 0, temperature: 0, fertilizer_cost: 0,
    previous_yield: 0, previous_profit: 0, current_cost: 0,
    fertilizer: 0, irrigation: 0, month: 1, last_price: 0, demand_index: 0
  });
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('input');

  const handleChange = (e) => {
    const value = e.target.type === 'number' ? parseFloat(e.target.value) : e.target.value;
    setFormData({ ...formData, [e.target.name]: value || 0 });
  };

  const toggleLang = () => {
    setLang(lang === 'en' ? 'hi' : 'en');
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const apiUrl = process.env.REACT_APP_API_URL.startsWith('http')
        ? process.env.REACT_APP_API_URL
        : `https://${process.env.REACT_APP_API_URL}`;

      const response = await fetch(`${apiUrl}/report/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      setReport(data);
      setActiveTab('dashboard');
    } catch (error) {
      alert(t.error.backend);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-wrapper classy-gradient">
      <div
        className="mouse-torch"
        style={{
          left: `${mousePos.x}px`,
          top: `${mousePos.y}px`
        }}
      />
      <div className="bg-glow" />

      <div className="content-container">
        <header className="app-header glass">
          <div className="logo-section">
            <Leaf className="logo-icon" size={32} />
            <h1 className="text-gradient">{t.title}</h1>
          </div>

          <nav className="tab-nav">
            <button
              className={`nav-btn ${activeTab === 'input' ? 'active' : ''}`}
              onClick={() => setActiveTab('input')}
            >
              <FileText size={18} />
              <span>{t.inputTab}</span>
            </button>
            <button
              className={`nav-btn ${activeTab === 'dashboard' ? 'active' : ''}`}
              disabled={!report}
              onClick={() => setActiveTab('dashboard')}
            >
              <LayoutDashboard size={18} />
              <span>{t.analyticsTab}</span>
            </button>
            <div className="divider" />
            <button className="nav-btn lang-toggle" onClick={toggleLang}>
              <Languages size={18} />
              <span style={{ minWidth: '60px' }}>{t.langToggle}</span>
            </button>
          </nav>
        </header>

        <main className="main-content">
          <AnimatePresence mode="wait">
            {activeTab === 'input' ? (
              <motion.div
                key="form"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ duration: 0.3 }}
              >
                <form onSubmit={handleSubmit} className="input-form glass">
                  <div className="form-header">
                    <h2>{t.formHeader}</h2>
                    <p>{t.formSubheader}</p>
                  </div>

                  <div className="form-grid">
                    {Object.keys(formData).map((key) => (
                      <div key={key} className="input-group">
                        <label>
                          {t.fields[key]}
                          <span className="unit-label">({t.units[key]})</span>
                        </label>
                        <input
                          name={key}
                          type="number"
                          step="any"
                          onChange={handleChange}
                          placeholder="0.0"
                          required
                        />
                      </div>
                    ))}
                  </div>

                  <button type="submit" className="glow-btn submit-btn" disabled={loading}>
                    {loading ? (
                      <><Loader2 className="animate-spin" size={20} /> {t.analyzingBtn}</>
                    ) : (
                      <><Send size={20} /> {t.generateBtn}</>
                    )}
                  </button>
                </form>
              </motion.div>
            ) : (
              <Dashboard key="dashboard" data={report} t={t} lang={lang} inputData={formData} />
            )}
          </AnimatePresence>
        </main>
      </div>

      <footer className="app-footer">
        <p>{t.footer}</p>
      </footer>
    </div>
  );
}

export default App;