var CUI = CUI ? CUI : {};


CUI.toggleInput = function() {
  var inputValue = "";

  $('.control_group.checkbox.inline .control input[type="checkbox"]').click(function(){
    var checkbox = $(this);
    var input = $('.control_group.checkbox.inline .input > input');
    var isDisabled = checkbox.prop('checked');

    input.attr('disabled', isDisabled);

    if(isDisabled) {
      inputValue = input.val();
      input.val('');
    } else {
      input.val(inputValue);
    }
  });
};

$(document).ready(function() {
  CUI.toggleInput();
});
