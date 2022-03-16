const $form = $("#cupcakeForm");
const baseUrl = "/api/cupcakes";

$("#cupcakeSubmit").click(postCupcakes);

async function postCupcakes(evt) {
  evt.preventDefault();
  const newCupcake = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image: $("#image").val(),
  };
  if (newCupcake.image == "") {
    delete newCupcake.image;
  }
  resp = await axios.post(baseUrl, newCupcake);
  $("#cupcakeList").append(makeListItem(resp.data.cupcake));
}

async function getCupcakes() {
  const response = await axios.get("/api/cupcakes");

  const cupcakes = response.data.cupcakes;

  return cupcakes;
}

async function populatePage() {
  const cupcakes = await getCupcakes();
  for (let cupcake of cupcakes) {
    // console.log(cupcake);
    $("#cupcakeList").append(makeListItem(cupcake));
  }
}

function makeListItem(cupcake) {
  return `<div class="col col-md-4" id="${cupcake.id}">
            <div class="card mb-3">
                <img src="${cupcake.image}" class="card-img-top">
                <div class="card-body">
                    <h5 class="card-title">${cupcake.flavor}</h5>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">${cupcake.size}</li>
                        <li class="list-group-item">${cupcake.rating}</li>
                    </ul>
                </div>
            </div>
        </div>`;
}

populatePage();
