# tests/test_models.py
from django.test import TestCase
from EMS.models import Employee, Task
from django.urls import reverse
from EMS.forms import EmployeeForm, TaskForm


class TestEmployeeModel(TestCase):
    def test_employee_creation(self):
        employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            department='HR'
        )
        self.assertEqual(employee.first_name, 'John')
        self.assertEqual(employee.last_name, 'Doe')
        self.assertEqual(employee.email, 'johndoe@example.com')
        self.assertEqual(employee.department, 'HR')

    def test_employee_str_representation(self):
        employee = Employee(first_name='John', last_name='Doe')
        self.assertEqual(str(employee), 'John Doe')

class TestTaskModel(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            assigned_to=Employee.objects.create(first_name='John', last_name='Doe')
        )
        self.assertEqual(task.title, 'Test Task')
        self.assertEqual(task.description, 'This is a test task')
        self.assertEqual(task.assigned_to.first_name, 'John')
        self.assertEqual(task.assigned_to.last_name, 'Doe')

    def test_task_str_representation(self):
        task = Task(title='Test Task')
        self.assertEqual(str(task), 'Test Task')

class TestEmployeeViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            department='HR'
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee_list.html')
        self.assertContains(response, self.employee.first_name)

    def test_employee_detail_view(self):
        response = self.client.get(reverse('employee_detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employee_detail.html')
        self.assertContains(response, self.employee.first_name)

class TestTaskViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task',
            assigned_to=Employee.objects.create(first_name='John', last_name='Doe')
        )

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_list.html')
        self.assertContains(response, self.task.title)

    def test_task_detail_view(self):
        response = self.client.get(reverse('task_detail', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'task_detail.html')
        self.assertContains(response, self.task.title)

        class TestEmployeeForm(TestCase):
            def test_valid_form(self):
                form_data = {
                    'first_name': 'John',
                    'last_name': 'Doe',
                    'email': 'johndoe@example.com',
                    'department': 'HR'
                }
                form = EmployeeForm(data=form_data)
                self.assertTrue(form.is_valid())

            def test_invalid_form(self):
                form_data = {
                    'first_name': '',
                    'last_name': '',
                    'email': '',
                    'department': ''
                }
                form = EmployeeForm(data=form_data)
                self.assertFalse(form.is_valid())

        class TestTaskForm(TestCase):
            def test_valid_form(self):
                form_data = {
                    'title': 'Test Task',
                    'description': 'This is a test task',
                    'assigned_to': Employee.objects.create(first_name='John', last_name='Doe').id
                }
                form = TaskForm(data=form_data)
                self.assertTrue(form.is_valid())

            def test_invalid_form(self):
                form_data = {
                    'title': '',
                    'description': '',
                    'assigned_to': ''
                }
                form = TaskForm(data=form_data)
                self.assertFalse(form.is_valid())