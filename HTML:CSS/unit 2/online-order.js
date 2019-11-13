let cartTable;


function makeCartRow(item, price) {
    const row = document.createElement("tr");
    const itemData = document.createElement("td");
    itemData.innerText = item;
    row.appendChild(itemData);
    const priceData = document.createElement("td");
    priceData.innerText = price;
    row.appendChild(priceData);
    return row;
}

let exampleArray = [{ item: "soup", price: 3 },
    { item: "salad", price: 3 },
    { item: "sandwich", price: 5 }
]

const rowFromItem = function(value) {
    cartTable.appendChild(makeCartRow(value.name, '$' + value.price));
}


const updateCart = async function(array) {
    cartTable = document.getElementById("cart-content"); // step 1: get parent element
    console.log("called updateCart");
    console.dir(cartTable);
    cartTable.innerHTML = "";
    const headerRow = document.createElement("tr");
    const itemHeader = document.createElement("th");
    const amountHeader = document.createElement("th");
    itemHeader.innerText = "Item";
    amountHeader.innerText = "Amount";
    headerRow.appendChild(itemHeader);
    headerRow.appendChild(amountHeader);
    cartTable.appendChild(headerRow);
    // add the example items
    // cartTable.appendChild(makeCartRow("soup", "$3"));
    // cartTable.appendChild(makeCartRow("salad", "$3"));
    // cartTable.appendChild(makeCartRow("sandwich", "$5"));
    if (!array) {
        array = [];
    }
    array.forEach(rowFromItem);
    const totalRow = document.createElement("tr"); // step 2 new element
    const totalHeader = document.createElement("th");
    const totalAmount = document.createElement("th");
    let sum = 0;
    array.forEach(function(item) {
        sum += item.price;
    })
    totalAmount.innerText = '$' + sum;
    totalHeader.innerText = "Total: ";
    totalRow.appendChild(totalHeader);
    totalRow.appendChild(totalAmount);
    cartTable.appendChild(totalRow);
}

// updateCart = function() {
//     console.log("3");
// }

// this is always called when the page loads