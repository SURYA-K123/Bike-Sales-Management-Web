function getDetails(event) 
{
    var xhr = new XMLHttpRequest();
    var url = "/send-message";
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card');
    var idTag = bikeCard.querySelector('.id');
    var id = idTag.textContent;
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location = '/details/' + id;
        }
    };
    xhr.send(JSON.stringify({"message": id}));
}
function editBranch(event) {
    var xhr = new XMLHttpRequest();
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card');
    var idTag = bikeCard.querySelector('#branch-id');
    var id = idTag.textContent;
    var url = "/editbranch";
    console.log(id)
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location = '/editbranchpage/' + id
        }
    };
    xhr.send(JSON.stringify({ "id": id }));
}

const displayBtn = document.getElementById('add-button');
displayBtn.addEventListener('click', () => {
  window.location.href = '/openaddbranch';
});


function deleteBranch(event) {
    a=confirm("Are you sure want to delete")
    if(a===true)
    {
    var xhr = new XMLHttpRequest();
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card');
    var idTag = bikeCard.querySelector('#branch-id');
    var id = idTag.textContent;
    var url = "/deletebranch/" + id;
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location = "/vbranch"
        }
    };
    xhr.send(JSON.stringify({ "branchid": id }));
}
}

function viewBikesAvailable(event) {
    var xhr = new XMLHttpRequest();
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card');
    var idTag = bikeCard.querySelector('#branch-id');
    var id = idTag.textContent;
    var url = "/viewbranchbike";
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location = "/viewbranchbike/"+id
        }
    };
    xhr.send(JSON.stringify({"id": id }));
}


function editBike(event) {
    var xhr = new XMLHttpRequest();
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card1');
    var idTag = bikeCard.querySelector('.id');
    var id = idTag.textContent;
    var url = "/openeditbike";
    console.log(id)
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            window.location = '/editbike/' + id
        }
    };
    xhr.send(JSON.stringify({ "id": id }));
}

function deleteBike(event) {
    a=confirm("Are you sure want to delete")
    if(a===true)
    {
    var xhr = new XMLHttpRequest();
    var method = "POST";
    var bikeCard = event.target.closest('.bike-card1');
    var idTag = bikeCard.querySelector('.id');
    var id = idTag.textContent;
    var url = "/deletebike/" + id;
    xhr.open(method, url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        window.location = "/bikesadmin";
      }
    };
    xhr.send(JSON.stringify({ "id": id }));
  }
}
  

function generatePdf()
{
    const doc = new jsPDF();
    doc.text('Hello World!', 10, 10);
    doc.save('hello_world.pdf');
}

