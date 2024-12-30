import { ip } from "./common.js";
import { API_getItems, API_getMoneySymbol } from "./REST.js";

// VARIABLES GENERALES
var filtersElements = {
    "cathegory-food": {
        state: false,
        label: "comida"
    },
    "cathegory-tools": {
        state: false,
        label: "herramientas"
    },
    "cathegory-redstone": {
        state: false,
        label: "redstone"
    },
    "cathegory-minerals": {
        state: false,
        label: "minerales"
    }
};

var minPrice = null;
var maxPrice = null;

var moneySymbol = "€";

// Filtros estáticos provisionales. Deberían ser dinámicos.
document.getElementById("cathegory-food").addEventListener("click", function () {
    toogleCheckFilter(this.id);
    getItems();
});
document.getElementById("cathegory-tools").addEventListener("click", function () {
    toogleCheckFilter(this.id);
    getItems();
});
document.getElementById("cathegory-redstone").addEventListener("click", function () {
    toogleCheckFilter(this.id);
    getItems();
});
document.getElementById("cathegory-minerals").addEventListener("click", function () {
    toogleCheckFilter(this.id);
    getItems();
});
document.getElementById("filter-min-price").addEventListener("input", function () {
    let value = this.value;
    this.parentNode.querySelector("label").innerText = "Precio mínimo: " + value.toString() + moneySymbol;
    document.getElementById("filter-max-price").min = value;
});
document.getElementById("filter-max-price").addEventListener("input", function () {
    let value = this.value;
    this.parentNode.querySelector("label").innerText = "Precio máximo: " + value.toString() + moneySymbol;
    document.getElementById("filter-min-price").max = value;
});
document.getElementById("filter-apply").addEventListener("click", getItems);

window.addEventListener("load", init);

async function init() {
    for (const [key, value] of Object.entries(filtersElements)) {
        getFilterElement(key);
    }

    await getItems();

    document.getElementById("filter-min-price").value = minPrice;
    document.getElementById("filter-max-price").value = maxPrice;

    document.getElementById("filter-min-price").parentNode.querySelector("label").innerText = "Precio mínimo: " + document.getElementById("filter-min-price").value.toString() + moneySymbol;
    document.getElementById("filter-max-price").parentNode.querySelector("label").innerText = "Precio máximo: " + document.getElementById("filter-max-price").value.toString() + moneySymbol;
}

async function getItems() {
    await getMoneySymbol();
    
    document.getElementById("store-section-items").innerHTML = "";
    let filters = {};

    let filterLabels = [];
    for (const [key, value] of Object.entries(filtersElements)) {
        if (value.state) {
            filterLabels.push(value.label);
        } else if (filterLabels.includes(value.label)) {
            filterLabels.slice(filterLabels.indexOf(value.label), 1)
        }
        
        filters["labels"] = filterLabels;
        if (filters["labels"].length == 0) {
            delete filters.labels;
        }
    }

    let filterName = document.getElementById("filter-name").value;
    if (filterName) {
        filters["name"] = filterName;
    }

    let filterMinPrice = document.getElementById("filter-min-price").value;
    let filterMaxPrice = document.getElementById("filter-max-price").value;

    filters["price"] = {};
    if (minPrice != null || minPrice != filterMinPrice) {
        filters.price["min_price"] = parseInt(filterMinPrice);
    }

    if (maxPrice != null || maxPrice != filterMaxPrice) {
        filters.price["max_price"] = parseInt(filterMaxPrice);
    }

    if (filters.price == {}) {
        delete filters.price;
    }

    // Obtenemos los items
    let items = await API_getItems(ip, { "item_filters": filters })
    for (let i = 0; i < items.length; i++) {
        let ammount = 1; // La cantidad ofrecida podría ser indicada por el servidor
        let name = items[i].name;
        let description = items[i].description;
        let price = items[i].price;
        let image = items[i].image;

        document.getElementById("store-section-items").appendChild(buildItem(ammount, name, description, price, image));
    }

    document.getElementById("filter-min-price").min = minPrice;
    document.getElementById("filter-max-price").max = maxPrice;
    
    document.getElementById("filter-min-price").max = document.getElementById("filter-max-price").value;
    document.getElementById("filter-max-price").min = document.getElementById("filter-min-price").value;
}

function buildItem(ammount, name, description, price, image) {
    if (minPrice == null || minPrice > price) {
        minPrice = price;
    }
    if (maxPrice == null || maxPrice < price) {
        maxPrice = price;
    }

    let item = document.createElement("div");
    item.classList.add("item");
    item.classList.add("mc-inventory-bg");

    let itemIcons = document.createElement("div");
    itemIcons.classList.add("item-icons");
    // Se supone que pueden haber mas items. Por ahora aparecerá solo 1
    let itemIconsIcon = document.createElement("div");
    itemIconsIcon.classList.add("item-icon");
    let itemIconsIconImg = document.createElement("img");
    itemIconsIconImg.setAttribute("src", "../static/assets/images/" + image + ".png");
    let itemIconsIconAmmount = document.createElement("div");
    itemIconsIconAmmount.classList.add("item-ammount");
    if (ammount > 1) {
        itemIconsIconAmmount.innerText = ammount.toString();
    }

    let itemData = document.createElement("div");
    itemData.classList.add("item-data");
    let itemDataName = document.createElement("p");
    itemDataName.classList.add("item-data-name");
    itemDataName.innerText = name.toString();
    let itemDataDescription = document.createElement("p");
    itemDataDescription.classList.add("item-data-description");
    itemDataDescription.innerText = description.toString();
    let itemDataPrice = document.createElement("h3");
    itemDataPrice.classList.add("item-data-price");
    itemDataPrice.innerText = price.toString() + moneySymbol;

    let itemActions = document.createElement("div");
    itemActions.classList.add("item-actions");
    let itemActionsAdd = document.createElement("input");
    itemActionsAdd.classList.add("mc-button");
    itemActionsAdd.setAttribute("type", "button");
    itemActionsAdd.setAttribute("value", "Añadir al carro");

    item.appendChild(itemIcons);
    item.appendChild(itemData);
    item.appendChild(itemActions);

    itemIcons.appendChild(itemIconsIcon);

    itemIconsIcon.appendChild(itemIconsIconImg);
    itemIconsIcon.appendChild(itemIconsIconAmmount);

    itemData.appendChild(itemDataName);
    if (itemDataDescription.innerText != "") {
        itemData.appendChild(itemDataDescription);
    }
    itemData.appendChild(itemDataPrice);

    itemActions.appendChild(itemActionsAdd);

    return item;
}

function getFilterElement(filterID) {
    let filter = document.getElementById(filterID);
    let filterCheck = filter.querySelector(".mc-chekbox");

    if (filterCheck.classList.contains("mc-chekbox-deactive")) {
        filtersElements[filterID].state = false;
    } else if (filterCheck.classList.contains("mc-chekbox-active")) {
        filtersElements[filterID].state = true;
    }
}

function toogleCheckFilter(filterID) {
    let activeClass = "mc-chekbox-active";
    let deactiveClass = "mc-chekbox-deactive";
    filtersElements[filterID].state = !filtersElements[filterID].state;
    if (filtersElements[filterID].state) {
        document.getElementById(filterID).querySelector(".mc-chekbox").classList.remove(deactiveClass);
        document.getElementById(filterID).querySelector(".mc-chekbox").classList.add(activeClass);
    } else {
        document.getElementById(filterID).querySelector(".mc-chekbox").classList.remove(activeClass);
        document.getElementById(filterID).querySelector(".mc-chekbox").classList.add(deactiveClass);
    }
}

async function getMoneySymbol() {
    let data = await API_getMoneySymbol(ip);
    moneySymbol = data.symbol;
}