import { APIGET, APIPOST, APIPUT, APIDELETE } from "./GenericREST.js";

/*
EJEMPLO:

// GET
export function nombreFuncion1(ip) {
    //... mas codigo ...
    return APIGET(ip + '/');
}

// POST
export function nombreFuncion2(ip, data) {
    //... mas codigo ...
    return APIPOST(ip + '/users', data);
}

// PUT
export function nombreFuncion3(ip, data) {
    //... mas codigo ...
    return APIPUT(ip + '/users', data);
}

// DELETE
export function nombreFuncion4(ip) {
    //... mas codigo ...
    return APIDELETE(ip + '/');
}
*/

export function API_getItems(ip, data) {
    return APIPOST(ip + '/api/items', data);
}

export function API_getMoneySymbol(ip) {
    return APIGET(ip + '/api/money/symbol');
}