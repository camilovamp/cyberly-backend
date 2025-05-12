BASIC = 'basic'
INTERMEDIATE = 'intermediate'
ADVANCED = 'advanced'
FLUENT = 'fluent'
NATIVE = 'native'

GENDER_MALE = 'M'
GENDER_FEMALE = 'F'
GENDER_NONBINARY = 'NB'
GENDER_OTHER = 'O'
GENDER_UNDISCLOSED = 'U'

PROFICIENCY_CHOICES = [
    (BASIC, 'Basic'),
    (INTERMEDIATE, 'Intermediate'),
    (ADVANCED, 'Advanced'),
    (FLUENT, 'Fluent'),
    (NATIVE, 'Native'),
]

GENDER_CHOICES = [
    (GENDER_MALE, 'Male'),
    (GENDER_FEMALE, 'Female'),
    (GENDER_NONBINARY, 'Non-binary'),
    (GENDER_OTHER, 'Other'),
    (GENDER_UNDISCLOSED, 'Prefer not to say'),
]

AVAILABILITY_TYPE_CHOICES = [
    ('d', 'One-day or Daily'),
    ('w', 'Weekly'),
]

WEEKDAY_CHOICES = [
    ('1', 'Monday'),
    ('2', 'Tuesday'),
    ('3', 'Wednesday'),
    ('4', 'Thursday'),
    ('5', 'Friday'),
    ('6', 'Saturday'),
    ('7', 'Sunday'),
]

RESOURCE_TYPE_CHOICES = [
    ('profile_photo', 'Profile Photo', ),
    ('company_logo', 'Company Logo', ),
    ('conversation_video', 'Video Conversation', ),
    ('certification_photo', 'License/Certification', ),
    ('education_photo', 'Education', ),
    ('letter_of_recommendation_photo', 'Letter Of Recommendation', ),
    ('career_photo', 'Career Photo', ),
]

YEARS_OF_EXPERIENCE_CHOICES = [
    (0, 'Less than 1 year of experience'),
    (1, "1 year of experience", ),
    (2, "2 years of experience", ),
    (3, "3 years of experience", ),
    (4, "4 years of experience", ),
    (5, "5 years of experience", ),
    (6, "6 years of experience", ),
    (7, "7 years of experience", ),
    (8, "8 years of experience", ),
    (9, "9 years of experience", ),
    (10, "10 years of experience", ),
    (11, "11 years of experience", ),
    (12, "12 years of experience", ),
    (13, "13 years of experience", ),
    (14, "14 years of experience", ),
    (15, "15 years of experience", ),
    (16, "16 years of experience", ),
    (17, "17 years of experience", ),
    (18, "18 years of experience", ),
    (19, "19 years of experience", ),
    (20, "20 years of experience", ),
    (99, "More than 20 years of experience", ),

]
