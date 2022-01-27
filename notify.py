class Notifier:
    condition = {
        "company": {"check_list": [
            "is_deleted",
            "is_blacklisted",
            "crawling_status"
        ], },
        "event": {"check_list": [
            "is_deleted",
            "is_blacklisted",
            "crawling_status"
        ], },
        "webinar": {"check_list": [
            "is_deleted",
            "is_blacklisted",
            "crawling_status"
        ], },
        "contentitem": {"check_list": [
            "is_deleted",
            "is_blacklisted",
            "crawling_status"
        ], },
        "companyforevent": {"check_list": [
            "is_deleted",
            "is_blacklisted",
            "crawling_status"
        ], },
        "companyforwebinar": {"check_list": [
            "is_deleted",
            "is_blacklisted"
        ], },
        "companycompetitor": {"check_list": [
            "is_deleted"
        ], },
    }

    def __setattr__(self, name, value):
        old_value = getattr(self, name, None)
        class_name = self.__class__.__name__.lower()
        check_list = self.condition.get(class_name).get("check_list", [])

        if name in check_list and old_value is not None and value != old_value:
            if name != "crawling_status" or value in ["TEXT_ANALYZED", "TEXT_UPLOADED"]:
                self.notify(self.__class__.__name__, 'changed', self.__class__.__name__)
        super().__setattr__(name, value)

    def __del__(self):
        self.notify(self.__class__.__name__, 'deleted', self.__class__.__name__)

    def __new__(cls, *args, **kwargs):
        cls.notify(cls.__name__, 'created', cls.__name__)
        return super().__new__(cls)

    @staticmethod
    def notify(name, action, notify_on):
        print(f"Notification: The {name} has been {action}.")
