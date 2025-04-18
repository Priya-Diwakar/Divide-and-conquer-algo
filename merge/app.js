import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [numbers, setNumbers] = useState('');
    const [sortedNumbers, setSortedNumbers] = useState([]);
    const [algorithm, setAlgorithm] = useState('merge');

    const handleSort = async () => {
        const numArray = numbers.split(',').map(num => parseInt(num.trim(), 10));
        const response = await axios.post('http://127.0.0.1:5000/sort', {
            numbers: numArray,
            algorithm: algorithm
        });

        setSortedNumbers(response.data.sorted_numbers);
    };

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Sorting Visualizer</h1>
            <input 
                type="text" 
                placeholder="Enter numbers separated by commas" 
                value={numbers} 
                onChange={(e) => setNumbers(e.target.value)}
            />
            <br />
            <select onChange={(e) => setAlgorithm(e.target.value)}>
                <option value="merge">Merge Sort</option>
                <option value="quick">Quick Sort</option>
            </select>
            <br />
            <button onClick={handleSort}>Sort</button>
            <h2>Sorted Numbers:</h2>
            <p>{sortedNumbers.join(', ')}</p>
        </div>
    );
}

export default App;
