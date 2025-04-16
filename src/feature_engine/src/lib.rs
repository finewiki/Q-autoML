use pyo3::prelude::*;
use ndarray::Array2;

#[pyfunction]
fn calculate_financial_ratios(data: Vec<f64>) -> PyResult<Vec<f64>> {
    let mut ratios = Vec::new();
    
    // Calculate common financial ratios
    for window in data.windows(2) {
        if window[1] != 0.0 {
            ratios.push(window[0] / window[1]);
        }
    }
    
    Ok(ratios)
}

#[pymodule]
fn feature_engine(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(calculate_financial_ratios, m)?)?;
    Ok(())
}