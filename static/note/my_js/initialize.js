  $(function () {
    $('#example1').DataTable({
      'paging'      : true,
      'lengthChange': false,
      'searching'   : true,
      'ordering'    : true,
      'info'        : false,
      'autoWidth'   : true,
    })
  });
  $("button.show_detail").click(function(){
    note_id = $(this).val()
    $.ajax({
      url:"/ajax_get_notes_detail",
      data:{'note_id':note_id},
      success:function(data){
        $("div.modal-content").html(data)
      }
    })
  })
