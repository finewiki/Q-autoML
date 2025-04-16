library(tidyverse)
library(tseries)
library(quantmod)
library(TTR)

analyze_financial_data <- function(data) {
    # Basic statistics
    stats <- list(
        mean = mean(data$Close),
        median = median(data$Close),
        std_dev = sd(data$Close),
        skewness = moments::skewness(data$Close),
        kurtosis = moments::kurtosis(data$Close)
    )
    
    # Stationarity test
    adf_result <- adf.test(data$Close)
    
    # Calculate returns
    returns <- diff(log(data$Close))
    
    # Volatility analysis
    volatility <- sd(returns) * sqrt(252)
    
    # Correlation analysis
    cor_matrix <- cor(data[c("Close", "Volume", "High", "Low")])
    
    list(
        basic_stats = stats,
        stationarity = adf_result,
        volatility = volatility,
        correlation = cor_matrix
    )
}

calculate_technical_indicators <- function(data) {
    # Add technical indicators
    data$SMA_20 <- SMA(data$Close, n = 20)
    data$RSI <- RSI(data$Close)
    data$MACD <- MACD(data$Close)
    
    data
}