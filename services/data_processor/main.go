package main

import (
    "encoding/json"
    "log"
    "net/http"
)

type DataProcessor struct {
    Features []string
    Values   []float64
}

func (dp *DataProcessor) PreProcess(w http.ResponseWriter, r *http.Request) {
    var data map[string]interface{}
    if err := json.NewDecoder(r.Body).Decode(&data); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    // Process financial data
    processed := processFinancialData(data)
    
    json.NewEncoder(w).Encode(processed)
}

func main() {
    http.HandleFunc("/process", (&DataProcessor{}).PreProcess)
    log.Fatal(http.ListenAndServe(":8081", nil))
}