console.log('hwe')

$(document).ready(function() {
    var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    $("#createButton").click(function(){
        var serializedData = 
        $("#createTodoForm").serialize();
        
        $.ajax({
            url: $("#createTodoForm").data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $("#todoList").prepend(`
                <div class="card mb-1" data-id=${response.todo.id}>
                    <div class="card-body" style="background-color:${response.todo.background_color };">
                        <font color="${response.todo.text_color }">${response.todo.message}</font>
                            <button type="button" class="close float-right" data-id=${response.todo.id}>
                                <span aria-hidden="true">&times;</span>
                            </button>
                    </div>
                </div>`)
            }
        })
        
        $("#createTodoForm")[0].reset();
    })
    
    $("#todoList").on('click', 'button.close', function(event) { 
        var dataId = $(this).data('id');
        // $.post('/todo/' + dataId + '/delete/', 
            
        // )
        $.ajax({
            url: '/todo/' + dataId + '/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            type: 'post',
            dataType: 'json',
            success: function() {
                $('.card[data-id="' + dataId + '"]').remove()
            }
        })
});
}
)
