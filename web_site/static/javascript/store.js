import { ip } from "./common.js";
import { API_getItems } from "./REST.js";

// VARIABLES GENERALES
var filtersElements = {
    "cathegory-food": {
        state: true,
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

window.addEventListener("load", init);

function init() {
    for (const [key, value] of Object.entries(filtersElements)) {
        getFilterElement(key);
    }

    getItems();
}

async function getItems() {
    document.getElementById("store-section-items").innerHTML = "";
    let filters = {};

    let filterLabels = [];
    for (const [key, value] of Object.entries(filtersElements)) {
        if (value.state) {
            console.log(value.label);
            filterLabels.push(value.label);
        } else if (filterLabels.includes(value.label)) {
            filterLabels.slice(filterLabels.indexOf(value.label), 1)
        }
        
        filters["labels"] = filterLabels;
        if (filters["labels"].length == 0) {
            delete filters.labels;
        }
    }

    let items = await API_getItems(ip, { "item_filters": filters })
    for (let i = 0; i < items.length; i++) {
        let ammount = 1;
        let name = items[i].name;
        let price = items[i].price;
        let image = items[i].image;

        document.getElementById("store-section-items").appendChild(buildItem(ammount, name, price, image));
    }
}

function buildItem(ammount, name, price, image) {
    let item = document.createElement("div");
    item.classList.add("item");
    item.classList.add("mc-inventory-bg");

    let itemIcons = document.createElement("div");
    itemIcons.classList.add("item-icons");
    // Se supone que pueden haber mas items. Por ahora solo aparecerá solo 1
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
    let itemDataPrice = document.createElement("h3");
    itemDataPrice.classList.add("item-data-price");
    itemDataPrice.innerText = price.toString() + " €";

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