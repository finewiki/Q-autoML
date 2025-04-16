package com.automl.processor;

import java.util.*;
import java.io.*;
import java.nio.file.*;
import com.fasterxml.jackson.databind.ObjectMapper;

public class DataProcessor {
    private static final ObjectMapper mapper = new ObjectMapper();
    
    public static class FinancialData {
        public String symbol;
        public List<Double> prices;
        public List<Double> volumes;
        
        // Getters and setters
    }
    
    public FinancialData processData(String jsonData) throws IOException {
        FinancialData data = mapper.readValue(jsonData, FinancialData.class);
        
        // Remove null values
        data.prices.removeIf(Objects::isNull);
        data.volumes.removeIf(Objects::isNull);
        
        // Calculate moving averages
        List<Double> sma = calculateSMA(data.prices, 20);
        
        // Process volumes
        List<Double> normalizedVolumes = normalizeVolumes(data.volumes);
        
        return data;
    }
    
    private List<Double> calculateSMA(List<Double> prices, int window) {
        List<Double> sma = new ArrayList<>();
        for (int i = 0; i < prices.size(); i++) {
            if (i < window - 1) {
                sma.add(null);
                continue;
            }
            double sum = 0;
            for (int j = 0; j < window; j++) {
                sum += prices.get(i - j);
            }
            sma.add(sum / window);
        }
        return sma;
    }
    
    private List<Double> normalizeVolumes(List<Double> volumes) {
        double max = Collections.max(volumes);
        double min = Collections.min(volumes);
        return volumes.stream()
            .map(v -> (v - min) / (max - min))
            .collect(Collectors.toList());
    }
}