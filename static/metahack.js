$(document).ready(function() {

    $('.another-suggestion button').click(function() {
        $.ajax({
            url: '/get_idea'
        }).done(function(data) {
            $('.hackathon-idea').text(data);
        });

    });
});