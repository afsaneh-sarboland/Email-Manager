const red = $('#red')
        const yellow = $('#yellow')
        const green = $('#green')
        const pink = $('#pink')
        const blue = $('#blue')
        const plant = $('#plant')
        const circls = $(".change_color")
        $(document).ready(function(){
          red.click(function(){
            $(".inbox-head").css("background-color", "red");
            $(".user-head").css("background-color", "red");
            $(".btn").css("background-color", "red");

          });
        });
        $(document).ready(function(){
          yellow.click(function(){
            $(".inbox-head").css("background-color", "yellow");
            $(".inbox-head").css("color", "black");
            $(".user-head").css("background-color", "yellow");
            $(".user-head").css("color", "black");
            $(".btn").css("background-color", "yellow");

          });
        });
        $(document).ready(function(){
          green.click(function(){
            $(".inbox-head").css("background-color", "greenyellow");
            $(".inbox-head").css("color", "black");
            $(".user-head").css("background-color", "greenyellow");
            $(".user-head").css("color", "black");
            $(".btn").css("background-color", "greenyellow");

          });
        });
        $(document).ready(function(){
          pink.click(function(){
            $(".inbox-head").css("background-color", "lightpink");
            $(".inbox-head").css("color", "black");
            $(".user-head").css("background-color", "lightpink");
            $(".user-head").css("color", "black");
            $(".btn").css("background-color", "lightpink");

          });
        });
        $(document).ready(function(){
          blue.click(function(){
            $(".inbox-head").css("background-color", "#3498db");
            $(".inbox-head").css("color", "black");
            $(".user-head").css("background-color", "#3498db");
            $(".user-head").css("color", "black");
            $(".btn").css("background-color", "#3498db");

          });
        });