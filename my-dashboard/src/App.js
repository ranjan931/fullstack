import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Plot from 'react-plotly.js';

function App() {
    const [data, setData] = useState([]);
    const [yearFilter, setYearFilter] = useState('');
    const [countryFilter, setCountryFilter] = useState('');

    useEffect(() => {
        const params = {};
        if (yearFilter) {
            params.year = yearFilter;
        }
        if (countryFilter) {
            params.country = countryFilter;
        }
        axios.get('http://127.0.0.1:5000/api/data', { params })
            .then(response => {
                setData(response.data);
            })
            .catch(error => {
                console.error('There was an error fetching the data!', error);
            });
    }, [yearFilter, countryFilter]);

    return (
        <div className="App">
            <h1>Data Visualization Dashboard</h1>
            <div>
                <label>
                    Filter by Year:
                    <input
                        type="number"
                        value={yearFilter}
                        onChange={e => setYearFilter(e.target.value)}
                        placeholder="Year"
                    />
                </label>
                <label>
                    Filter by Country:
                    <input
                        type="text"
                        value={countryFilter}
                        onChange={e => setCountryFilter(e.target.value)}
                        placeholder="Country"
                    />
                </label>
            </div>
            <Plot
                data={[
                    {
                        x: data.map(d => d.year),
                        y: data.map(d => d.intensity),
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'red' },
                    },
                ]}
                layout={{ title: 'Intensity Over Years' }}
            />
        </div>
    );
}

export default App;
