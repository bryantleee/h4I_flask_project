$(document).ready(function() {


    //**Change contrast of background**//
      function changeContrast(backgroundColor, textColor){
        $('body').css('background-color', backgroundColor);
        $('.text').css('color', textColor);
      }
      
       $('.dark_mode').click(function() {
         changeContrast('black', 'white');
       });
      
       $('.light_mode').click(function() {
         changeContrast('white', '#383838');
       });
      
       $('.sepia_mode').click(function() {
         changeContrast('#F4ECD8', '#685444');
       });


        //**Change font-style**//
        $('.sansseriffButton').click(function() {
            $('.text').css('font-family', 'sans-serif');
        });
        $('.seriffButton').click(function() {
            $('.text').css('font-family', 'serif');
        });

      
});
