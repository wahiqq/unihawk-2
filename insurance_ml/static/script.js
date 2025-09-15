// Constants
const API_URL = 'http://localhost:5000/api';
const FORM_ID = 'prediction-form';
const LOADING_ID = 'loading';
const RESULTS_ID = 'results';
const ERROR_ID = 'error-message';
const PREDICTED_COST_ID = 'predicted-cost';
const MODEL_USED_ID = 'model-used';
const FACTOR_LIST_ID = 'factor-list';
const RESULTS_PANEL_ID = 'results-panel';

// Main functionality
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById(FORM_ID);
    
    // Handle form submission
    form.addEventListener('submit', handleFormSubmit);
    
    // Scroll to results on smaller screens when the prediction is done
    document.getElementById(FORM_ID).addEventListener('submit', (e) => {
        if (window.innerWidth < 768) {
            setTimeout(() => {
                document.getElementById(RESULTS_PANEL_ID).scrollIntoView({
                    behavior: 'smooth'
                });
            }, 500);
        }
    });
});

// Handle form submission
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Show loading state and hide any previous results or errors
    toggleElement(LOADING_ID, true);
    toggleElement(RESULTS_ID, false);
    toggleElement(ERROR_ID, false);
    
    // Get form data
    const formData = new FormData(event.target);
    const data = {
        age: formData.get('age'),
        sex: formData.get('sex'),
        bmi: formData.get('bmi'),
        children: formData.get('children'),
        smoker: formData.get('smoker'),
        region: formData.get('region'),
        model_name: formData.get('model')
    };
    
    try {
        // Send request to API
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        // Hide loading state
        toggleElement(LOADING_ID, false);
        
        if (response.ok) {
            const result = await response.json();
            displayResults(result, data);
        } else {
            const errorData = await response.json();
            displayError(errorData.error || 'An error occurred during prediction');
        }
    } catch (error) {
        console.error('API request error:', error);
        toggleElement(LOADING_ID, false);
        displayError('Could not connect to the prediction service');
    }
}

// Display results
function displayResults(result, inputData) {
    // Update cost and model info
    document.getElementById(PREDICTED_COST_ID).textContent = 
        `$${result.prediction.toLocaleString('en-US', {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
    
    document.getElementById(MODEL_USED_ID).textContent = 
        formatModelName(result.model_used);
    
    // Generate factors that affect the cost
    generateFactorList(inputData);
    
    // Show results
    toggleElement(RESULTS_ID, true);
}

// Generate a list of factors that affect the cost
function generateFactorList(data) {
    const factorList = document.getElementById(FACTOR_LIST_ID);
    factorList.innerHTML = '';
    
    // Create list items for each factor with descriptive text
    const factors = [
        {
            key: 'smoker',
            label: 'Smoking Status',
            description: data.smoker === 'yes' 
                ? 'Being a smoker significantly increases insurance costs'
                : 'Non-smokers typically have lower insurance costs'
        },
        {
            key: 'age',
            label: 'Age',
            description: `Age (${data.age} years) - Insurance costs generally increase with age`
        },
        {
            key: 'bmi',
            label: 'BMI',
            description: getBmiDescription(data.bmi)
        },
        {
            key: 'children',
            label: 'Dependents',
            description: `Having ${data.children} dependent${data.children !== '1' ? 's' : ''} can affect insurance pricing`
        },
        {
            key: 'region',
            label: 'Region',
            description: `Your location (${formatRegion(data.region)}) affects insurance costs due to regional healthcare pricing`
        },
        {
            key: 'sex',
            label: 'Sex',
            description: `Biological sex (${data.sex}) can influence health risk factors and insurance costs`
        }
    ];
    
    // Add each factor to the list
    factors.forEach(factor => {
        const li = document.createElement('li');
        li.innerHTML = `<strong>${factor.label}:</strong> ${factor.description}`;
        factorList.appendChild(li);
    });
}

// Get descriptive text for BMI values
function getBmiDescription(bmi) {
    const bmiValue = parseFloat(bmi);
    let category = '';
    
    if (bmiValue < 18.5) {
        category = 'underweight';
    } else if (bmiValue < 25) {
        category = 'normal weight';
    } else if (bmiValue < 30) {
        category = 'overweight';
    } else {
        category = 'obesity';
    }
    
    return `BMI of ${bmiValue} (${category}) - Higher BMI values may increase insurance costs`;
}

// Display error message
function displayError(message) {
    const errorElement = document.getElementById(ERROR_ID);
    errorElement.textContent = message;
    toggleElement(ERROR_ID, true);
}

// Helper functions
function toggleElement(elementId, show) {
    const element = document.getElementById(elementId);
    element.classList.toggle('hidden', !show);
}

function formatModelName(modelName) {
    return modelName
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function formatRegion(region) {
    return region.charAt(0).toUpperCase() + region.slice(1);
}