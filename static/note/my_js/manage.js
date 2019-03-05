 function delete_waring(){
   var info = confirm("是否确定删除?");
   return info
  };
 $("button.edit").click(function(){
 	var note_id = $(this).val()
 	$.ajax({
 		url:"/edit_note",
 		data:{'note_id':note_id},
 		success:function(data){
 			$("div.modal-content").html(data)
 		}
 	})
 });
 $("button.edit_sh").click(function(){
 	var sh_id = $(this).val()
 	$.ajax({
 		url:"/edit_sh",
 		data:{'sh_id':sh_id},
 		success:function(data){
 			$("div.modal-content").html(data)
 		}
 	})
 });
 $("button.edit_lx").click(function(){
 	var lx_id = $(this).val()
 	$.ajax({
 		url:"/edit_lx",
 		data:{'lx_id':lx_id},
 		success:function(data){
 			$("div.modal-content").html(data)
 		}
 	})
 });
 $("button.edit_xh").click(function(){
 	var xh_id = $(this).val()
 	$.ajax({
 		url:"/edit_xh",
 		data:{'xh_id':xh_id},
 		success:function(data){
 			$("div.modal-content").html(data)
 		}
 	})
 });
