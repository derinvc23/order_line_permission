odoo.define('order_line_permission.hide_action_edit_buttons', function (require) {
    "use strict";
    let FormView = require('web.FormView');
    var core = require('web.core');

    FormView.include({
        load_record: function (record) {
            if (record && this.$buttons && this.get('actual_mode') === 'view' && this.model && this.model == 'sale.order' && !record.can_edit_so) {
//                this.$buttons.find('.o_form_button_edit').hide();
                var $button = this.$buttons.find(".o_form_button_edit");
                $button.prop("disabled", true);
            }
            return this._super(record);
        },
    });
});