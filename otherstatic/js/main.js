jQuery(function ($) {

    'use strict';

    // -------------------------------------------------------------
    // News Slider
    // -------------------------------------------------------------

    $(function (){

        var ticker = $('#ticker'),
            container = ticker.find('ul'),
            tickWidth = 1,
            speed = 0.1, // Control pace
            distance,
            timing;

            container.find("li").each(function(i) {
            tickWidth += $(this, i).outerWidth(true);
            });

            distance = tickWidth + (ticker.outerWidth() - $('#gameLabel').outerWidth());
            timing = distance / speed;

            function scrollIt(dist, dur) {
            container.animate({
              left: '-=' + dist
            }, dur, 'linear', function() {
              container.css({
                'left': ticker.outerWidth()
              });
              scrollIt(distance, timing);
            });
            }

            scrollIt(distance, timing);

            ticker.hover(function() {
            container.stop();
            }, function() {
            var offset = container.offset(),
              newPosition = offset.left + tickWidth,
              newTime = newPosition / speed;
            scrollIt(newPosition, newTime);
        });
        
    }); 

    /*==============================================================*/
    // Aside menu
    /*==============================================================*/

    (function(){
        var mbMenu = $('.tr-hamburger');

        mbMenu.magnificPopup({
            mainClass: 'asd-menu mfp-slide-left',
            type:'inline',
            midClick: true,
            closeMarkup: '<span class="aside-menu-close-ic mfp-close"></span>',
            removalDelay: 300
        });
    })();     
   

    /*==============================================================*/
    // Search Slide
    /*==============================================================*/
           
   (function() {

        $('.search-icon').on('click', function() {
            $('.searchNlogin').toggleClass("expanded");
        });
    }());


    /*==============================================================*/
    // TheiaStickySidebar
    /*==============================================================*/
           
   (function() {

        $('.tr-sticky')
            .theiaStickySidebar({
                additionalMarginTop: 0
            });
    }());


    /*==============================================================*/
    // carouFredSel
    /*==============================================================*/
           
   (function() {

        $('.breaking-news-slider').carouFredSel({
            width: '100%',
            direction   : "bottom",
            scroll : 400,
            items: {
                visible: '+3'
            },
            auto: {
                items: 1,
                timeoutDuration : 4000
            },
            prev: {
                button: '.prev',
                items: 1
            },    
            next: {
                button: '.next',
                items: 1
            }
        });

    }());


    // -------------------------------------------------------------
    //  Slick Slider
    // -------------------------------------------------------------  

    (function() {

       $(".entertainment-slider").slick({
        infinite: true,
        slidesToShow: 5,
        autoplay:true,
        autoplaySpeed:10000,
        slidesToScroll: 2,
        responsive: [
        {
          breakpoint: 1025,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
          }
        }
        ]       
      });        

       $(".result-slider").slick({
        infinite: true,
        slidesToShow: 5,
        autoplay:true,
        autoplaySpeed:10000,
        slidesToScroll: 1,
        responsive: [
        {
          breakpoint: 1299,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 1025,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 769,
          settings: {
            slidesToShow: 1,
          }
        },
        {
          breakpoint: 481,
          settings: {
            slidesToShow: 1,
          }
        }
        ]        
      }); 

       $(".quotes-slider").slick({
        infinite: true,
        slidesToShow: 7,
        autoplay:true,
        autoplaySpeed:10000,
        slidesToScroll: 1,
        responsive: [
        {
          breakpoint: 1025,
          settings: {
            slidesToShow: 3,
          }
        },
        {
          breakpoint: 769,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 481,
          settings: {
            slidesToShow: 1,
          }
        }
        ]        
      }); 

    }());

    /*==============================================================*/
    // JPlayerPlaylist
    /*==============================================================*/
           
   (function() {

        new jPlayerPlaylist({
            jPlayer: "#tr-player",
            cssSelectorAncestor: "#tr-player-wrapper"
        }, [
            {
                artist: "Gibson", // the artist name
                title:"Angelina yet again",
                mp3:"http://www.jplayer.org/audio/mp3/TSP-01-Cro_magnon_man.mp3",
                oga:"http://www.jplayer.org/audio/ogg/TSP-01-Cro_magnon_man.ogg"
            },
            {
                title:"Stirring of a Fool",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-08-Stirring-of-a-fool.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-08-Stirring-of-a-fool.ogg"
            },
            {
                title:"Your Face",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/TSP-05-Your_face.mp3",
                oga:"http://www.jplayer.org/audio/ogg/TSP-05-Your_face.ogg"
            },
            {
                title:"Cyber Sonnet",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/TSP-07-Cybersonnet.mp3",
                oga:"http://www.jplayer.org/audio/ogg/TSP-07-Cybersonnet.ogg"
            },
            {
                title:"Tempered Song",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-01-Tempered-song.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-01-Tempered-song.ogg"
            },
            {
                title:"Hidden",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-02-Hidden.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-02-Hidden.ogg"
            },
            {
                title:"Lentement",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-03-Lentement.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-03-Lentement.ogg"
            },
            {
                title:"Lismore",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-04-Lismore.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-04-Lismore.ogg"
            },
            {
                title:"The Separation",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-05-The-separation.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-05-The-separation.ogg"
            },
            {
                title:"Beside Me",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-06-Beside-me.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-06-Beside-me.ogg"
            },
            {
                title:"Bubble",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-07-Bubble.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-07-Bubble.ogg"
            },
            
            {
                title:"Partir",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-09-Partir.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-09-Partir.ogg"
            },
            {
                title:"Thin Ice",
                artist: "Gibson", // the artist name
                mp3:"http://www.jplayer.org/audio/mp3/Miaow-10-Thin-ice.mp3",
                oga:"http://www.jplayer.org/audio/ogg/Miaow-10-Thin-ice.ogg"
            }
        ], {
            swfPath: "js/jquery.jplayer.swf",
            supplied: "oga, mp3",
            wmode: "window",
            useStateClassSkin: true,
            autoBlur: false,
            smoothPlayBar: true,
            keyEnabled: true,
            remainingDuration: true,
        });
        
    }());



	/*==============================================================*/
	// Animationend
	/*==============================================================*/


    (function( $ ) {

        //Function to animate slider captions 
        function doAnimations( elems ) {
            //Cache the animationend event in a variable
            var animEndEv = 'webkitAnimationEnd animationend';
            
            elems.each(function () {
                var $this = $(this),
                    $animationType = $this.data('animation');
                $this.addClass($animationType).one(animEndEv, function () {
                    $this.removeClass($animationType);
                });
            });
        }
        
        //Variables on page load 
        var $myCarousel = $('#home-carousel'),
            $firstAnimatingElems = $myCarousel.find('.item:first').find("[data-animation ^= 'animated']");
            
        //Initialize carousel 
        $myCarousel.carousel();
        
        //Animate captions in first slide on page load 
        doAnimations($firstAnimatingElems);
        
        //Pause carousel  
        $myCarousel.carousel('pause');
        
        //Other slides to be animated on carousel slide event 
        $myCarousel.on('slide.bs.carousel', function (e) {
            var $animatingElems = $(e.relatedTarget).find("[data-animation ^= 'animated']");
            doAnimations($animatingElems);
        });  
        
    })(jQuery);


   
// script end
});

