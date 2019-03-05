$(document).on('change','#id_sh',function(){
    var customer_id = $(this).val();
    $.ajax({
      url:"/ajax_get_unit_types",
      data:{'customer_id':customer_id},
      success:function(data){
        $('#id_lb').html(data)
      }
    })
  });
  $(document).on('change','#id_lb',function(){
    var unit_type_id = $(this).val();
    $.ajax({
      url:"/ajax_get_unit_models",
      data:{'unit_type_id':unit_type_id},
      success:function(data){
        $('#id_xh').html(data)
      }
    })
  });