import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.models import Task
from django.utils import timezone


class Command(BaseCommand):
    help = "Generate dummy tasks for a specified user"

    def add_arguments(self, parser):
        parser.add_argument(
            "username", type=str, help="Username of the user to create tasks for"
        )
        parser.add_argument("num_tasks", type=int, help="Number of tasks to create")

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        num_tasks = kwargs["num_tasks"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User "{username}" does not exist'))
            return

        titles = [
            "Complete project report",
            "Prepare presentation slides",
            "Update website content",
            "Organize team meeting",
            "Review codebase",
            "Write unit tests",
            "Fix bugs in application",
            "Design new feature",
            "Conduct user testing",
            "Deploy application",
        ]
        descriptions = [
            "Finish the project report and submit it to the manager.",
            "Create and finalize the presentation slides for the upcoming meeting.",
            "Update the website content with the latest information.",
            "Organize and schedule a team meeting to discuss project progress.",
            "Review the codebase and suggest improvements.",
            "Write unit tests for the new features added to the application.",
            "Fix the reported bugs in the application and test the fixes.",
            "Design a new feature based on the user requirements.",
            "Conduct user testing to gather feedback on the new feature.",
            "Deploy the application to the production environment.",
        ]
        statuses = ["P", "IP", "C"]
        priorities = ["L", "M", "H"]
        categories = ["W", "P", "H"]

        for _ in range(num_tasks):
            title = random.choice(titles)
            description = random.choice(descriptions)
            status = random.choice(statuses)
            priority = random.choice(priorities)
            category = random.choice(categories)
            due_date = timezone.now() + timezone.timedelta(days=random.randint(1, 30))

            Task.objects.create(
                user=user,
                title=title,
                description=description,
                status=status,
                priority=priority,
                category=category,
                due_date=due_date,
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {num_tasks} tasks for user "{username}"'
            )
        )
