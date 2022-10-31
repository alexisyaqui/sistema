$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {'data': "id"},
            {"data": "pnombre_med"},
            {"data": "snombre_med"},
            {"data": "papellido_med"},
            {"data": "sapellido_med"},
            {"data": "dpi_med"},
            {"data": "fecha_nac_med"},
            {"data": "direccion_med"},
            {"data": "email_med"},
            {"data": "titulo_medico"},
            {"data": "colegiado_act"},
            {"data": "telefono_med"},
            {"data": "sexo_med"},
            {"data": "religion_med"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/medico/editar/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/medico/eliminar/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});