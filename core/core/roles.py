from rolepermissions.roles import AbstractUserRole


class Gerente(AbstractUserRole):
    available_permissions = {
        'add_product': True,
        'edit_product': True,
        'delete_product': True,
        'add_category': True,
    }
