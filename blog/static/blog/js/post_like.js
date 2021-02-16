$(".like").click(function () { // .like 버튼을 클릭 감지
    var pk = $(this).attr('name')
    $.ajax({ // ajax로 서버와 통신
        type: "POST", // 데이터를 전송하는 방법 
        url: "{% url 'blog:post_like' %}", // 통신할 url을 지정
        data: { 
            'pk': pk, 
            'csrfmiddlewaretoken': '{{ csrf_token }}' 
        }, // 서버로 데이터 전송시 옵션, pk를 넘겨야 어떤 post인지 알 수 있음
        dataType: "json",
        success: function (response) { // 성공
            $("#count-" + pk).html(response.likes_count+response.message); // 좋아요 개수 변경
            if(response.message == '좋아요 취소'){
                $(".like-btn").html("<i class='far fa-heart'></i>");
            }
            else{
                $(".like-btn").html("<i class='fas fa-heart' style='color:#F58A8A'></i>");
            }

        },
        error: function (request, status, error) { // 실패
            alert("로그인이 필요합니다.");
            window.location.replace("{% url 'accounts:login' %}") // 로그인 페이지로 넘어가기
        },
    });
})
