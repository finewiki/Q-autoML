use pyo3::prelude::*;
mod technical;
mod statistics;
mod utils;

use technical::{moving_average, exponential_moving_average};
use statistics::{volatility, z_score};
use utils::clean_data;

#[pymodule]
fn feature_engine_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(moving_average, m)?)?;
    m.add_function(wrap_pyfunction!(exponential_moving_average, m)?)?;
    m.add_function(wrap_pyfunction!(volatility, m)?)?;
    m.add_function(wrap_pyfunction!(z_score, m)?)?;
    m.add_function(wrap_pyfunction!(clean_data, m)?)?;
    Ok(())
}