library(ggplot2)
library(plotly)
library(corrplot)

create_price_plot <- function(data) {
    ggplot(data, aes(x = Date, y = Close)) +
        geom_line(color = "blue") +
        geom_line(aes(y = SMA_20), color = "red", linetype = "dashed") +
        theme_minimal() +
        labs(title = "Stock Price with 20-day Moving Average",
             x = "Date",
             y = "Price")
}

create_volume_plot <- function(data) {
    ggplot(data, aes(x = Date, y = Volume)) +
        geom_bar(stat = "identity", fill = "darkblue", alpha = 0.7) +
        theme_minimal() +
        labs(title = "Trading Volume",
             x = "Date",
             y = "Volume")
}

create_correlation_heatmap <- function(data) {
    cor_matrix <- cor(data[c("Close", "Volume", "High", "Low", "SMA_20", "RSI")])
    corrplot(cor_matrix, 
            method = "color",
            type = "upper",
            addCoef.col = "black",
            tl.col = "black",
            tl.srt = 45)
}