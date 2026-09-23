let expenses = JSON.parse(localStorage.getItem("expenses")) || [];

const form = document.getElementById("expenseForm");
const expenseList = document.getElementById("expenseList");
const total = document.getElementById("total");
const count = document.getElementById("count");
const emptyMessage = document.getElementById("emptyMessage");
const clearBtn = document.getElementById("clearBtn");

function displayExpenses() {
    expenseList.innerHTML = "";

    let totalAmount = 0;

    expenses.forEach((expense, index) => {
        totalAmount += Number(expense.amount);

        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${expense.date}</td>
            <td>${expense.description}</td>
            <td>${expense.category}</td>
            <td>₹${Number(expense.amount).toFixed(2)}</td>
            <td>
                <button class="delete-btn" onclick="deleteExpense(${index})">
                    Delete
                </button>
            </td>
        `;

        expenseList.appendChild(row);
    });

    total.textContent = `₹${totalAmount.toFixed(2)}`;
    count.textContent = expenses.length;

    emptyMessage.style.display =
        expenses.length === 0 ? "block" : "none";
}

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const date = document.getElementById("date").value;
    const description = document.getElementById("description").value;
    const category = document.getElementById("category").value;
    const amount = document.getElementById("amount").value;

    const expense = {
        date: date,
        description: description,
        category: category,
        amount: amount
    };

    expenses.push(expense);

    localStorage.setItem("expenses", JSON.stringify(expenses));

    form.reset();

    displayExpenses();
});

function deleteExpense(index) {
    expenses.splice(index, 1);

    localStorage.setItem("expenses", JSON.stringify(expenses));

    displayExpenses();
}

clearBtn.addEventListener("click", function() {
    expenses = [];

    localStorage.removeItem("expenses");

    displayExpenses();
});

displayExpenses();
