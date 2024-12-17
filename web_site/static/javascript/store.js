import { ip } from "./common.js";
import { API_getItems } from "./REST.js";

window.addEventListener("load", getItems);

function init() {
    let items = getItems();

    for (let i = 0; i < items.length; i++) {
        console.log(items[i]);
    }
}

async function getItems() {
    document.getElementById("store-section-items").innerHTML = "";
    let items = await API_getItems(ip, { "item_filters": {} })
    for (let i = 0; i < items.length; i++) {
        let ammount = 5;
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
    itemIconsIconImg.setAttribute("src", "../static/assets/images/items/" + image + ".png");
    let itemIconsIconAmmount = document.createElement("div");
    itemIconsIconAmmount.classList.add("item-ammount");
    itemIconsIconAmmount.innerText = ammount.toString();

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