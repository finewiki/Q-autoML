use pyo3::prelude::*;

#[pyfunction]
pub fn clean_data(data: Vec<f64>) -> PyResult<Vec<f64>> {
    let cleaned: Vec<f64> = data.into_iter()
        .filter(|&x| !x.is_nan() && !x.is_infinite())
        .collect();
        
    Ok(cleaned)
}

pub fn normalize_data(data: Vec<f64>) -> Vec<f64> {
    let min = data.iter().fold(f64::INFINITY, |a, &b| a.min(b));
    let max = data.iter().fold(f64::NEG_INFINITY, |a, &b| a.max(b));
    let range = max - min;
    
    data.iter().map(|&x| (x - min) / range).collect()
}