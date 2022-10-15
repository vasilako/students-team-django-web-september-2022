from django import forms

from web.models import Pet

# TODO ---------Only look this piece of code------------
class AddPersonForm(forms.Form):
    MAX_LENGTH = 20
    MIN_LENGTH = 3

    person_name = forms.CharField(
        label='Name',
        max_length=MAX_LENGTH,
        min_length=MIN_LENGTH,
        required=True,
        help_text='Feel your name',
        widget=forms.TextInput(attrs={
            'placeholder': "put hear your name",
            'class': 'form-control'
        })
    )

    MIN_AGE = 1
    MAX_AGE = 99
    person_age = forms.IntegerField(

        label='Age correct',
        max_value=MAX_AGE,
        min_value=MIN_AGE,
        required=True,
        help_text='Your age',
        widget=forms.NumberInput(attrs={
            'placeholder': 'put hear your age',
            'class': 'form-control'

        }),
    )

    # TODO ---------- This field doesn't work -----------
    person_pet = forms.ModelMultipleChoiceField(
        label="Person's pet",
        required=False,
        queryset= Pet.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )





# TODO --------- From hear to down es the Doncho code -----
class PersonForm(forms.Form):
    OCCUPANCIES = (
        (1, 'Child'),
        (2, 'High school student'),
        (3, 'Student'),
        (4, 'Adult'),
    )

    your_name = forms.CharField(
        max_length=30,
        label='Name',
        help_text='Enter your name',
        widget=forms.TextInput(
            # This corresponds to HTML attributes
            attrs={
                'placeholder': 'Enter name',
                'class': 'form-control',
            },
        )
    )
    age = forms.IntegerField(
        required=False,
        initial=0,
        help_text='Enter your age',
        # This is the default for `IntegerField`
        widget=forms.NumberInput(),
    )

    # email = forms.CharField(
    #     widget=forms.EmailInput(),
    # )
    #
    # url = forms.CharField(
    #     widget=forms.URLInput(),
    # )
    #
    # secret = forms.CharField(
    #     widget=forms.PasswordInput(),
    # )
    #
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    # )

    occupancy = forms.ChoiceField(
        choices=OCCUPANCIES,
        # This is the default for `ChoiceField`:
        widget=forms.Select,
    )

    # occupancy2 = forms.ChoiceField(
    #     choices=OCCUPANCIES,
    #     widget=forms.RadioSelect(),
    # )

    occupancy3 = forms.ChoiceField(
        choices=OCCUPANCIES,
        widget=forms.SelectMultiple(),
    )
