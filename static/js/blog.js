$(function(){
  $("#likes").click(function(){
    alert("like is clicked");
    var artid = $(this).attr("data-artid");
    $.get('/blog/like', {article_id: artid}, function(data){
      $("#likes_count").html(data);
      $("#likes").hide();
    });
  });
});
