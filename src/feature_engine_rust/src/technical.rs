use pyo3::prelude::*;
use ndarray::Array1;

#[pyfunction]
pub fn moving_average(data: Vec<f64>, window: usize) -> PyResult<Vec<f64>> {
    let n = data.len();
    let mut result = vec![0.0; n];
    
    for i in window-1..n {
        let sum: f64 = data[i-window+1..=i].iter().sum();
        result[i] = sum / window as f64;
    }
    
    Ok(result)
}

#[pyfunction]
pub fn exponential_moving_average(data: Vec<f64>, alpha: f64) -> PyResult<Vec<f64>> {
    let mut result = vec![0.0; data.len()];
    result[0] = data[0];
    
    for i in 1..data.len() {
        result[i] = alpha * data[i] + (1.0 - alpha) * result[i-1];
    }
    
    Ok(result)
}