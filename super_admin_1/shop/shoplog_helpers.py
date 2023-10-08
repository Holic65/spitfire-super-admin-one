from super_admin_1.models.shop_logs import ShopsLogs


# see sample usage in delete shop route
class ShopLogs:
    """
    Shop Logs

    :param admin_id: uuid of admin
    :param admin_username: username of admin
    :param shop_id: uuid of shop
    :param shop_name: name of shop
    """

    def __init__(self, admin_id, admin_username, shop_id, shop_name):
        self.admin_id = admin_id
        self.admin_name = admin_username
        self.shop_id = shop_id
        self.shop_name = shop_name

    def log_shop_created(self):
        """
        logs new shop created
        """

        shop = ShopsLogs(
            shop_id=self.shop_id,
            shop_name=self.shop_name,
            admin_id=self.admin_id,
            admin_name=self.admin_name,
            action="created",
        )
        shop.insert()

    def log_shop_deleted(self, delete_type="temporary"):
        """
        logs shop deleted

        :param delete_type: type of delete action (active or temporary)
        """

        if delete_type not in ["active", "temporary"]:
            raise ValueError("invalid delete type only (active or temporary)")

        shop = ShopsLogs(
            shop_id=self.shop_id,
            shop_name=self.shop_name,
            admin_id=self.admin_id,
            admin_name=self.admin_name,
            action=f"{delete_type} deleted ",
        )
        shop.insert()

    def log_shop_reviewed(self):
        """
        logs a shop passed review
        """

        shop = ShopsLogs(
            shop_id=self.shop_id,
            shop_name=self.shop_name,
            admin_id=self.admin_id,
            admin_name=self.admin_name,
            action="reviewed",
        )
        shop.insert()

    def log_shop_restricted(self, restrict_type="temporary"):
        """
        logs shop restricted

        :param restrict_type: type of restriction action ('no', 'temporary', 'permanent')
        """

        if restrict_type not in ["no", "temporary", "permanent"]:
            raise ValueError(
                "invalid restrict type only ('no', 'temporary', 'permanent')"
            )

        shop = ShopsLogs(
            shop_id=self.shop_id,
            shop_name=self.shop_name,
            admin_id=self.admin_id,
            admin_name=self.admin_name,
            action=f"{restrict_type} restricted on",
        )
        shop.insert()

    def log_shop_admin_status(self, status_type="pending"):
        """
        logs admin status of shop

        :param status_type: type of status action ('pending', 'review', 'approved', 'blacklist')
        """

        if status_type not in ["no", "temporary", "permanent"]:
            raise ValueError(
                "invalid status type only ('pending', 'review', 'approved', 'blacklist')"
            )

        shop = ShopsLogs(
            shop_id=self.shop_id,
            shop_name=self.shop_name,
            admin_id=self.admin_id,
            admin_name=self.admin_name,
            action=f"marked {status_type} admin status on",
        )
        shop.insert()