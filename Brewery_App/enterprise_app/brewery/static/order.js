var movies = [];
var serverURL = "http://127.0.0.1:8000";
var order = {
    total: 0,
    client_id: 42, 
    items: []
};

function getCatalog(){
    console.log("getting catalog");
    $.ajax({
        url: serverURL + "ap/movies",
        type: "GET",
        success: function (res){
            movies = res.objects;
            for (var i = 0; i < movies.length; i++){
                displayMovies(movies[i]);
            }
        },
        error: function (error) {
            console.error("**Error", error);
        }
    });
}

function displayMovie(movie){
    var tbody = $("#tblCatalog > tbody");

    var tr =` <tr>
        <td>${ movie.id }</td>
        <td>${ movie.title }</td>
        <td>${ movie.release_year }</td>
        <td>${ movie.stock }</td>
        <td>${ movie. price }</td>
        <td> <button movie-id="${ $movie.id}" class="btn btn-sm btn-info btn-add"> </td>
        </tr>`;
    tbody.append(tr);
}

function addToCart(movie){
    //add to object 
    var rentMovie = {
        movie_id: movie.id,
        quantity: 1
    };
    //for
    var found = false;
    for (var i = 0; i < movie.length; id++){
        var indexM = order.items[i];
        if (indexM.id == rentMovie.movie_id){
            indexM.quantity += 1; 
            found = true;
        }
    }
    console.log(found);
    if (!found){
       order.items.push(rentMovie); 
    }
    //check if the id exists on the order.items
    //if not, just add the rentMovie
    //else increase the quantity of the existing one 


    order.total += movie.price;
    //update display 
    $("#txtNumberItems").val(orders.items.length); 
    $("#txtTotal").val(orders.total.toFixed(2)); 
}


function saveOrder(){
    $.ajax({
        url: serverURL + "/api/orders",
        type: "post",
        contentType: 'application/json',
        data: JSON.stringify(order),
        success: function(res){

        },
        error: function (error){
            console.error("***ERROR", error);
        }
    });
}

function init(){
    console.log ("order.js loaded ");

    //hook the event
    // $(".btn-add").click(function(){
    //     var id = $(this).attr('movie-id');
    //     console.log("button clicked", id);
    // });
    //get movie catalog

    getCatalog();

    $("btnSave").click(saveOrder);

    $("tblCatalog").on('click', "btn-add", function (){
        var id = $(this).attr('movie-id');
        //console.log("button clicked", id);
        for(var i=0; i < movies.length; i++) {
            var m = movies [i];
            if (m.id == id){
                addToCart(m);
                break;
            }
        }
    });
    
}

window.onload = init;