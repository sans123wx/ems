  $("li.forchoice").click(function(){
      var customer_id = $(this).val()
      $(".active:not(.paginate_button,.gi)").removeClass('active')
      $(this).addClass('active')
      $(this).parent().parent().addClass('active')
      $.ajax({
        url:"/ajax_get_notes",
        data:{"customer_id":customer_id},
        success:function(data){
          $("tbody").html(data);
          var context = $("li.active span.forname").text();
          $("h1 small").text(context);
          $(".gi").text(context)
          var info_sh = $("li.active.forchoice").val();
          $("#id_sh").val(info_sh);
        }
      })
  }
    );
  function report_waring(){
    var info = confirm("是否确定报账?");
    var title_value = $("#id_title").val();
    var date_value = $("#id_date").val();
    if(title_value && date_value){
      return info;
    }
    else{
      alert('请填写时间和名称');
      return false;
    }
  };
    $(function () {
    $('#example1').DataTable({
      'paging'      : false,
      'lengthChange': false,
      'searching'   : false,
      'ordering'    : false,
      'info'        : false,
      'autoWidth'   : false,
    })
  });
  $(document).on("click",".show_detail",function(){
    note_id = $(this).val()
    $.ajax({
      url:"/ajax_get_notes_detail",
      data:{'note_id':note_id},
      success:function(data){
        $("div.modal-body").html(data)
      }
    })
  });
  var context = $("li.active span.forname").text()
  $("h1 small").text(context)
  $(".gi").text(context)
  var info_sh = $("li.active.forchoice").val()
  $("#id_sh").val(info_sh)
