BASIC_SUBJECTS = 'לשון תנ"ך אזרחות ספרות היסטוריה מתמטיקה אנגלית'
BASIC_SUBJECTS_LIST = BASIC_SUBJECTS.split(' ')

SUBJECTS_HIGH = 'חינוך-גופני תקשורת מדעי-המוח רפואה דיפלומטיה רובוטיקה ביוטכנולוגיה קולנוע ערבית מנהל-עסקים גיאוגרפיה מדעי-המחשב פיזיקה כימיה אומנות ביולוגיה מוזיקה פסיכולוגיה'
HIGH_SCHOOL_SUBJECT_LIST = SUBJECTS_HIGH.split(' ') + BASIC_SUBJECTS_LIST

SUBJECTS_MIDDLE = 'פיזיקה כימיה מדעי-המחשב ביולוגיה'
MIDDLE_SCHOOL_SUBJECT_LIST = SUBJECTS_MIDDLE.split(' ') + BASIC_SUBJECTS_LIST

ELEMENTARY_SCHOOL_LIST = BASIC_SUBJECTS_LIST

EDUCATION = 'יסודי חטיבה תיכון'
EDUCATION_LEVEL = EDUCATION.split(' ')

GRADE = 'א ב ג ד ה ו ז ח ט י י"א י"ב'
GRADE_LIST = GRADE.split(' ')

SUB_SUBJECT = []

DESCRIPTION_LIST = []

NUM_STARS = 5

LAYOUT_SIZE ="500x300"
BACKGROUND_COLOR = "#809bce"