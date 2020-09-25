from django.apps import AppConfig


class CollegeConfig(AppConfig):
    name = 'college'
    def ready(self):
        print("="*100)
        import college.mysignlas