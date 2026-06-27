/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { onWillStart } from "@odoo/owl";
import { FormController } from "@web/views/form/form_controller";
import { ListController } from "@web/views/list/list_controller";

async function loadHiddenDeleteFlag(controller) {
    const modelName = controller.props.resModel;
    if (!modelName || !controller.orm) {
        controller.smHideDeleteAction = false;
        return;
    }
    controller.smHideDeleteAction = await controller.orm.call(
        "sm.hide.delete.rule",
        "sm_is_delete_hidden",
        [modelName]
    );
}

function filterDeleteAction(items, hidden) {
    if (!hidden || !items.delete) {
        return items;
    }
    const nextItems = { ...items };
    delete nextItems.delete;
    return nextItems;
}

patch(ListController.prototype, {
    setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
        this.smHideDeleteAction = false;
        onWillStart(async () => {
            await loadHiddenDeleteFlag(this);
        });
    },

    getStaticActionMenuItems() {
        return filterDeleteAction(super.getStaticActionMenuItems(), this.smHideDeleteAction);
    },
});

patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
        this.smHideDeleteAction = false;
        onWillStart(async () => {
            await loadHiddenDeleteFlag(this);
        });
    },

    getStaticActionMenuItems() {
        return filterDeleteAction(super.getStaticActionMenuItems(), this.smHideDeleteAction);
    },
});
