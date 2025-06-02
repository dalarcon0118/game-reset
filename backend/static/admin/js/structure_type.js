django.jQuery(function($) {
    var $nodeType = $('#id_node_type');
    var $customType = $('.field-custom_type');

    function toggleCustomType() {
        if ($nodeType.val() === 'other') {
            $customType.show();
        } else {
            $customType.hide();
        }
    }

    $nodeType.on('change', toggleCustomType);
    toggleCustomType(); // Initial state
});