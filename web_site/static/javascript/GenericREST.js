// funcion genérica para hacer GET
export function APIGET(path) {
    return fetch(path, {
        method: 'GET',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(jsonData => jsonData.json())
        .then(data => { return data });
}

// funcion genérica para hacer POST
export function APIPOST(path, data) {
    return fetch(path, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(jsonData => jsonData.json())
        .then(data => { return data });
}

// funcion genérica para hacer PUT
export function APIPUT(path, data) {
    return fetch(path, {
        method: 'PUT',
        mode: 'cors',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(jsonData => jsonData.json())
        .then(data => { return data });
}

// funcion genérica para hacer DELETE
export function APIDELETE(path) {
    return fetch(path, {
        method: 'DELETE',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(jsonData => jsonData.json())
        .then(data => { return data });
}