

async function getCupcakes() {
    const response = await axios.get('/api/cupcakes');

    const cupcakes = response.data.cupcakes;

    return cupcakes;
}

async function populatePage() {
    const cupcakes = await getCupcakes();
    for (let cupcake of cupcakes){
        // console.log(cupcake);
        $('#cupcakeList').append(makeListItem(cupcake));

    }
}

function makeListItem(cupcake) {
    return `<div class="col col-md-4" id="${cupcake.id}">
            <div class="card">
                <img src="${cupcake.image}" class="card-img-top">
                <h5 class="card-title">${cupcake.flavor}</h5>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">${cupcake.size}</li>
                    <li class="list-group-item">${cupcake.rating}</li>
                </ul>
            </div>
        </div>`
}

populatePage()