const axios = require('axios');

async function testPrediction() {
    const data = {
    state_code: 0,
    category_code: 8,
    age_first_funding_year: 2.0,
    age_last_funding_year: 6.0,
    relationships: 3,
    funding_rounds: 4,
    funding_total_usd: 15000000,
    milestones: 2,
    is_CA: 1,
    is_NY: 0,
    is_MA: 0,
    is_TX: 0,
    is_otherstate: 0,
    is_software: 1,
    is_web: 1,
    is_mobile: 0,
    is_enterprise: 0,
    is_advertising: 0,
    is_gamesvideo: 0,
    is_ecommerce: 1,
    is_biotech: 0,
    is_consulting: 0,
    is_othercategory: 0,
    has_VC: 1,
    has_angel: 1,
    has_roundA: 1,
    has_roundB: 0,
    has_roundC: 0,
    has_roundD: 0,
    avg_participants: 1.5,
    is_top500: 1,
    labels: 1
};

    try {
        const response = await axios.post('http://127.0.0.1:8000/predict', data, {
            headers: {
                'Content-Type': 'application/json',
                'Origin': 'http://localhost:3000'
            }
        });
        console.log('Prediction:', response.data.prediction);
    } catch (error) {
        console.error('Error:', error.response?.data || error.message);
    }
}

testPrediction();