$(document).ready(function() {

    $('.another-suggestion button').click(function() {
        $.ajax({
            url: '/get_idea'
        }).done(function(data) {
            $('.hackathon-idea').text(data);
        });
    });

    $('.message-area').hide();
    $('.message-area').fadeIn(500).delay(1500).fadeOut(1000);

    var defaultValue = 'Enter your suggestion...';
    $('textarea.hackathon-idea').val(defaultValue);
    $('textarea.hackathon-idea').addClass('empty');

    $('textarea.hackathon-idea').focus(function() {
        $(this).removeClass('empty');
        if ($(this).val() === defaultValue) {
            $(this).val('');
        }
    });

    $('textarea.hackathon-idea').blur(function() {
        console.log($(this).val());
        if ($(this).val() === '') {
            $(this).val(defaultValue);
            $(this).addClass('empty');
        }
    });

});
