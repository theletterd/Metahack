$(document).ready(function() {

    var refreshMessageArea = function() {
        if ($('.message-area').text() !== '') {
            $('.message-area').hide();
            $('.message-area').fadeIn(500).delay(1500).fadeOut(1000);
        }
    };
    refreshMessageArea();

    $('.another-suggestion button').click(function() {
        $.ajax({
            url: '/get_idea'
        }).done(function(data) {
            $('.hackathon-idea').text(data);
        });
    });

    $('.keep-forever button').click(function() {
        var idea = $('.hackathon-idea').text();
        $.ajax({
            url: '/bestof',
            method: 'POST',
            data: {'idea': idea}
        }).done(function() {
            $('.message-area').text('We\'ll cherish it.');
            refreshMessageArea();
        });
    });

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
