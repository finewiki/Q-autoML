use pyo3::prelude::*;
use statrs::statistics::Statistics;

#[pyfunction]
pub fn volatility(data: Vec<f64>) -> PyResult<f64> {
    let returns: Vec<f64> = data.windows(2)
        .map(|w| (w[1] - w[0]) / w[0])
        .collect();
        
    let std_dev = returns.std_dev();
    Ok(std_dev * (252.0_f64).sqrt()) // Annualized volatility
}

#[pyfunction]
pub fn z_score(data: Vec<f64>) -> PyResult<Vec<f64>> {
    let mean = data.mean();
    let std_dev = data.std_dev();
    
    let result: Vec<f64> = data.iter()
        .map(|&x| (x - mean) / std_dev)
        .collect();
        
    Ok(result)
}