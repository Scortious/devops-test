document.addEventListener("DOMContentLoaded", () => {
    const tableBody = document.querySelector("#stock-table tbody");
    const updateButton = document.getElementById("update-prices");

    async function fetchStocks() {
        const response = await fetch("/stocks");
        const stocks = await response.json();
        tableBody.innerHTML = "";
        stocks.forEach(stock => {
            const row = `<tr>
                <td>${stock.symbol}</td>
                <td>${stock.price}</td>
            </tr>`;
            tableBody.innerHTML += row;
        });
    }

    async function updatePrices() {
        await fetch("/update_prices", { method: "PUT" });
        fetchStocks();
    }

    updateButton.addEventListener("click", updatePrices);

    // Initial load
    fetchStocks();
});
