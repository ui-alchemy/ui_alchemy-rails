var CUI = CUI ? CUI : {};

CUI.closeFlashMessage = function() {
  $('.flash_hud .control').click(function(){
    $(this).closest($('.flash_hud')).slideUp(100).fadeOut(100);
  });
};

$(document).ready(function() {
  CUI.closeFlashMessage();
});

