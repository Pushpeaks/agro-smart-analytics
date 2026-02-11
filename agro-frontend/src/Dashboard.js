import {
    LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
    BarChart, Bar, PieChart, Pie, Cell
} from 'recharts';
import { motion } from 'framer-motion';
import { TrendingUp, DollarSign, Sprout, Leaf, AlertTriangle, CheckCircle } from 'lucide-react';

const Dashboard = ({ data, t, lang, inputData }) => {
    if (!data) return null;

    const trendData = [
        { name: t.results.previous, yield: data.previous_yield || 4.2, profit: data.previous_profit || 12000 },
        { name: t.results.predicted, yield: data.yield, profit: data.profit },
    ];

    const pieData = [
        { name: t.costLabel, value: inputData?.current_cost || 5000, color: '#ff4d4d' },
        { name: t.profitLabel, value: data.profit, color: 'var(--primary)' }
    ];

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="dashboard-container"
            style={{ display: 'flex', flexDirection: 'column', gap: '24px', marginTop: '40px' }}
        >
            {/* Row 1: Key Metrics */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px' }}>
                <MetricCard
                    icon={<Sprout size={24} color="var(--primary)" />}
                    label={t.yield}
                    value={`${data.yield} ${t.units.previous_yield}`}
                    sub={t.results.basedOnParams}
                />
                <MetricCard
                    icon={<DollarSign size={24} color="var(--accent-gold)" />}
                    label={t.profit}
                    value={`₹${data.profit}`}
                    sub={`${t.marketPrice}: ₹${data.price}`}
                />
                <MetricCard
                    icon={data.recommendation === "Optimal" ? <CheckCircle size={24} color="var(--primary)" /> : <AlertTriangle size={24} color="#ff6b6b" />}
                    label={t.risk}
                    value={data.recommendation === "Optimal" ? t.results.optimal : t.results.highRisk}
                    sub={t.results.stabilityScore}
                    accent={data.recommendation === "Optimal" ? "var(--primary)" : "#ff6b6b"}
                />
                <MetricCard
                    icon={<Leaf size={24} color="var(--primary)" />}
                    label={t.bestCrop}
                    value={t.crops[data.recommended_crop]}
                    sub={lang === 'en' ? "For Maximum Profit" : "अधिकतम लाभ के लिए"}
                />
            </div>

            {/* Row 2: Visual Insights */}
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '20px' }}>
                {/* Cost vs Profit Breakdown */}
                <div className="glass" style={{ padding: '24px', height: '350px', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <h3 style={{ alignSelf: 'flex-start', marginTop: 0, color: 'var(--text-dim)', fontSize: '14px' }}>{t.profitBreakdown}</h3>
                    <ResponsiveContainer width="100%" height="80%">
                        <PieChart>
                            <Pie
                                data={pieData}
                                cx="50%"
                                cy="50%"
                                innerRadius={60}
                                outerRadius={80}
                                paddingAngle={5}
                                dataKey="value"
                            >
                                {pieData.map((entry, index) => (
                                    <Cell key={`cell-${index}`} fill={entry.color} />
                                ))}
                            </Pie>
                            <Tooltip
                                contentStyle={{ background: 'rgba(0,0,0,0.8)', border: '1px solid var(--surface-border)', borderRadius: '8px' }}
                                itemStyle={{ color: 'var(--primary)' }}
                            />
                        </PieChart>
                    </ResponsiveContainer>
                    <div style={{ display: 'flex', gap: '20px', fontSize: '12px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><div style={{ width: 10, height: 10, borderRadius: '50%', background: '#ff4d4d' }} /> {t.costLabel}</div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}><div style={{ width: 10, height: 10, borderRadius: '50%', background: 'var(--primary)' }} /> {t.profitLabel}</div>
                    </div>
                </div>

                {/* Performance Gauge */}
                <div className="glass" style={{ padding: '24px', height: '350px' }}>
                    <h3 style={{ marginTop: 0, color: 'var(--text-dim)', fontSize: '14px' }}>{t.comparisonChart}</h3>
                    <ResponsiveContainer width="100%" height="90%">
                        <BarChart data={trendData}>
                            <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" vertical={false} />
                            <XAxis dataKey="name" stroke="var(--text-dim)" fontSize={12} />
                            <YAxis stroke="var(--text-dim)" fontSize={12} />
                            <Tooltip
                                cursor={{ fill: 'rgba(255, 255, 255, 0.5)' }}
                                contentStyle={{ background: 'rgba(0,0,0,0.8)', border: '1px solid var(--surface-border)', borderRadius: '8px' }}
                                itemStyle={{ color: 'var(--primary)' }}
                            />
                            <Bar name={t.yield} dataKey="yield" fill="var(--primary)" radius={[4, 4, 0, 0]} />
                            <Bar name={t.profit} dataKey="profit" fill="#90EE90" radius={[4, 4, 0, 0]} />
                        </BarChart>
                    </ResponsiveContainer>
                </div>
            </div>

            {/* Row 3: Trends */}
            <div className="glass" style={{ padding: '24px', height: '300px' }}>
                <h3 style={{ marginTop: 0, color: 'var(--text-dim)', fontSize: '14px' }}>{t.priceTrendChart}</h3>
                <ResponsiveContainer width="100%" height="90%">
                    <LineChart data={trendData}>
                        <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.1)" vertical={false} />
                        <XAxis dataKey="name" stroke="var(--text-dim)" fontSize={12} />
                        <YAxis stroke="var(--text-dim)" fontSize={12} />
                        <Tooltip
                            contentStyle={{ background: 'rgba(0,0,0,0.8)', border: '1px solid var(--surface-border)', borderRadius: '8px' }}
                        />
                        <Line name={t.yield} type="monotone" dataKey="yield" stroke="var(--primary)" strokeWidth={3} dot={{ fill: 'var(--primary)' }} />
                    </LineChart>
                </ResponsiveContainer>
            </div>
        </motion.div>
    );
};

const MetricCard = ({ icon, label, value, sub, accent }) => (
    <motion.div
        whileHover={{ translateY: -5 }}
        className="glass"
        style={{ padding: '20px', borderLeft: accent ? `4px solid ${accent}` : '1px solid var(--surface-border)' }}
    >
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '12px' }}>
            {icon}
            <span style={{ color: 'var(--text-dim)', fontSize: '12px', fontWeight: 600 }}>{label}</span>
        </div>
        <div style={{ fontSize: '24px', fontWeight: 700, color: accent || 'var(--text-main)' }}>{value}</div>
        <div style={{ color: 'var(--text-dim)', fontSize: '11px', marginTop: '4px' }}>{sub}</div>
    </motion.div>
);

export default Dashboard;
