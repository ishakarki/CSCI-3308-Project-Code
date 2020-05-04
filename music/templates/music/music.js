var songs = [
   
];

function loadSongs()
{
    var i;
    for(i = 0; i < songs.length; i++)
    {
        var a = document.createElement("a");
        var newSong = document.createElement("li");
        var element = document.getElementById("playlist");

        // getting the song title without the .mp3
        var length = songs[i].length;
        var title = songs[i].substr(0,length-4);

        if(i==0)
        {
            newSong.className = "current-song";
        }

        a.textContent = title;
        a.setAttribute('href',songs[i]);
        newSong.appendChild(a);
        element.appendChild(newSong);
    }
}

// function credits to https://github.com/NelsWebDev/HTML5AudioPlaylist.git

function audioPlayer(){
    var currentSong = 0;
    $("#audioPlayer")[0].src = $("#playlist li a")[0];

    $("#playlist li a").click(function(e){
        // prevents it from doing that weird thing
       e.preventDefault(); 
       $("#audioPlayer")[0].src = this;
       $("#audioPlayer")[0].play();
       $("#playlist li").removeClass("current-song");
        currentSong = $(this).parent().index();
        $(this).parent().addClass("current-song");
    });
    
    $("#audioPlayer")[0].addEventListener("ended", function(){
       currentSong++;
        if(currentSong == $("#playlist li a").length)
            currentSong = 0;
        $("#playlist li").removeClass("current-song");
        $("#playlist li:eq("+currentSong+")").addClass("current-song");
        $("#audioPlayer")[0].src = $("#playlist li a")[currentSong].href;
        $("#audioPlayer")[0].play();
    });
}