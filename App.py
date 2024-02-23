from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

class QuizScreen(Screen):
    def __init__(self, questions, **kwargs):
        super().__init__(**kwargs)
        self.questions = questions
        self.score = 0
        self.current_question_index = 0
        self.layout = BoxLayout(orientation='vertical')
        self.question_label = Label(text=self.questions[self.current_question_index].prompt)
        self.options_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.options_layout.bind(minimum_height=self.options_layout.setter('height'))
        for idx, option in enumerate(self.questions[self.current_question_index].options):
            button = Button(text=option, size_hint_y=None, height=40)
            button.bind(on_press=self.answer_selected)
            self.options_layout.add_widget(button)
        self.layout.add_widget(self.question_label)
        self.scroll_view = ScrollView(size_hint=(1, None), size=(1, 300))
        self.scroll_view.add_widget(self.options_layout)
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)

    def answer_selected(self, instance):
        user_answer = instance.text
        correct_answer_index = self.questions[self.current_question_index].correct_answer
        if user_answer == self.questions[self.current_question_index].options[correct_answer_index]:
            self.score += 1
            message = "Correct ! You Are Hero !"
        else:
            message = "Incorrect. Try Again Yash..! !"
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.question_label.text = self.questions[self.current_question_index].prompt
            self.question_label.color = (1, 1, 1, 1)  # Set text color to white
            self.question_label.bold = True  # Set text to bold
            self.options_layout.clear_widgets()
            for option in self.questions[self.current_question_index].options:
                button = Button(text=option, size_hint_y=None, height=40)
                button.bind(on_press=self.answer_selected)
                self.options_layout.add_widget(button)
        else:
            message += f"\nQuiz ended! Your score: {self.score}/{len(self.questions)}"
        popup = Popup(title='Result', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

class QuizApp(App):
    def build(self):
        # Define your questions here
        questions = [
            Question(
                "Which international organization initiates a program to reduce the average temperature of the Earth?",
                ["World Wildlife Day", "Friends of Marine Life", "International Climate Change Initiative",
                 "World Wildlife Day for all living beings on Earth"], 2),
            Question("Why did Japan's tourism suffer temporarily?",
                     ["Fresh flight ban", "Joint states emergency accusation", "COVID-19", "Lack of migrant workers"],
                     2),
            Question("Which organization is not a member of the Palestinian democracy organization?",
                     ["European Union", "United States", "United Nations", "Arab Union"], 0),
            Question("How is the H-1B explosion spreading?", ["In Indonesia", "In Kenya", "In Yemen", "In Syria"], 1),
            Question("What is another name for the Bali Sea or the Bali Sea?",
                     ["Nayga River", "New Guinea", "Indian Ocean", "Caribbean Sea"], 1),
            Question("What is another name for the Bay of Bengal or the Bay of Bengal?",
                     ["Pacific Ocean", "Indian Ocean", "Arctic Ocean", "Nile"], 0),
            Question("Who is considered the 'King of the Indian Independence Movement' in Indian history?",
                     ["Mahatma Gandhi", "Chhatrapati Shivaji Maharaj", "Rani Lakshmibai",
                      "Netaji Subhash Chandra Bose"], 0),
            Question("On which date did the early days of the Indian Independence Movement begin?",
                     ["15 August 1857", "10 May 1857", "1 June 1857", "26 January 1857"], 3),
            Question("From which newspaper in Varanasi did the Indian Independence Movement message come from?",
                     ["Kesari", "Yugantar", "Marathi", "Rashtramat"], 1),
            Question("Which side was controversial in all major campaigns of the Indian Independence Movement?",
                     ["Satyashodhak", "Swarajya", "Rebellion", "Independence"], 0),
            Question("Who was India's first President?",
                     ["Rajendra Prasad", "Sardar Patel", "Jawaharlal Nehru", "Dr. Bhimrao Ambedkar"], 0),
            Question(
                "Which country helped for the independence of India in all major campaigns of the Indian Independence Movement?",
                ["France", "America", "Russia", "Britain"], 0),
            Question(
                "Which Maharashtrian king participated in the initial phase of the Indian Independence Movement of the Indian States?",
                ["Bajirao Peshwa", "Chhatrapati Shivaji Maharaj", "Chhatrapati Sambhaji Maharaj", "Nanasaheb Peshwa"],
                0),
            Question("Who narrated the battle of Kurukshetra in the Mahabharata?",
                     ["Yudhishthira", "Bhimsen", "Arjuna", "Karna"], 2),
            Question("How did the war begin in the Mahabharata epic?",
                     ["After the end of the residence of the Kauravas", "After the end of the Pandavas' exercise",
                      "At the end of the Dvapara Yuga", "After the end of the Kauravas' exercise"], 0),
            Question("How did Shivaji Maharaj conduct the coronation?", ["Raigad", "Rajgad", "Pratapgad", "Rameshwar"],
                     1),
            Question("How many forts did Shivaji Maharaj win?", ["100", "125", "250", "300"], 1),
            Question("How did Shivaji Maharaj give a gift to Tanaji Malusare in which fort?",
                     ["Raigad", "Sinhagad", "Pratapgad", "Rajgad"], 1),
            Question("Where was the residence of Chhatrapati Shivaji Maharaj?",
                     ["Raigad", "Pratapgad", "Sinhagad", "Rajgad"], 0),
            Question("How many years did King Shivaji Maharaj rule?", ["35 years", "25 years", "45 years", "55 years"],
                     0),
            Question("Which assurance document of King Shivaji Maharaj was found in the enemy's pillow?",
                     ["Samvad", "Gadala", "Haak", "Garuda"], 1),
            Question("Where was King Shivaji Maharaj born?", ["Shivneri", "Sinhagad", "Raigad", "Pratapgad"], 0),
            Question("Who was the first wife of King Shivaji Maharaj?", ["Saibai", "Soibai", "Sakavare", "Saibai"], 0)
        ]
        Question("WHO BECAME THE WIFE OF KING SHIVAJI MAHARAJ?", ["RAJMATTA JIJABAI", "SOYABAI", "SAIBAI", "SAKAVARE"],
                 1),
        Question("DOES KING SHIVAJI MAHARAJ HAVE ANOTHER NAME?", ["SHIVNERI", "SHIVTARA", "SHIVSENA", "SHIVAJI"], 2),
        Question("WHAT WERE THE NAMES OF THE TWO SONS OF KING SHIVAJI MAHARAJ?",
                 ["SAMBHAJI AND RAJARAM", "SAMBHAJI AND RAMARAM", "SAMBHAJI AND RAMCHANDRA", "SAMBHAJI AND VITHALRAM"],
                 0),
        Question("WHO WAS THE FOUNDER OF THE MARATHA EMPIRE?",
                 ["SAMBHAJI MAHARAJ", "RAJARAM", "BAJIRAO PESHWA", "SHIVAJI MAHARAJ"], 3),
        Question("WHERE IS THE SAMADHI OF KING SHIVAJI MAHARAJ?", ["SINHAGAD", "RAIGAD", "PRATAPGAD", "RAJGAD"], 2),
        Question("WHO WERE THE TWO SONS AND HEIRS OF KING SHIVAJI MAHARAJ?",
                 ["SAMBHAJI, RAJARAM", "SAMBHAJI, RAMCHANDRA", "SAMBHAJI, RAMARAM", "SAMBHAJI, VITHALRAM"], 0),
        Question("HOW MANY FORTS DID CHHATRAPATI SHIVAJI MAHARAJ HAVE?", ["300", "400", "500", "600"], 1),
        Question("WHAT IS THE HIGHEST PEAK IN INDIA?", ["KANCHENJUNGA", "HIMALAYA", "DHAULAGIRI", "EVEREST"], 3),
        Question("WHICH SEA IS ON THE WESTERN SIDE OF INDIA?",
                 ["ARABIAN SEA", "INDIAN OCEAN", "BAY OF BENGAL", "INDIAN OCEAN"], 0),
        Question("WHERE IS INDIA'S FIRST INTERNATIONAL AIRPORT LOCATED?", ["MUMBAI", "DELHI", "BENGALURU", "CHENNAI"],
                 1),
        Question("WHERE IS INDIA'S LARGEST GANDHI FLAG HOISTED?", ["WAGAH", "BAY OF BENGAL", "TIRANGA", "KANCHENJUNGA"],
                 0),
        Question("WHERE IS THE WESTERN SHORE OF INDIA?",
                 ["ARABIAN SEA", "INDIAN OCEAN", "BAY OF BENGAL", "INDIAN OCEAN"], 0),
        Question("IN WHICH CITY OF INDIA ARE THE MOST NORTHERN FORTS LOCATED?",
                 ["JAMMU", "AMRITSAR", "SRINAGAR", "CHANDIGARH"], 2),
        Question("WHERE IS THE LARGEST PORT IN INDIA LOCATED?", ["KOCHI", "MUMBAI", "CHENNAI", "KOLKATA"], 3),
        Question("WHERE IS THE LOWEST POINT IN INDIA?", ["KUTCH", "ANDAMAN AND NICOBAR", "CHANDIGARH", "GOA"], 1),
        Question("WHICH IS THE LARGEST ANIMAL-HUSBANDRY AREA IN INDIA?",
                 ["GANGA PRADESH", "MALWA", "MARATHWADA", "MAGDALA"], 0),
        Question("WHERE IS THE LARGEST DAM IN INDIA?", ["BHAKRA", "HIRAKUD", "NAGA", "GOVIND SAGAR"], 0),
        Question("WHICH STATE HAS THE LARGEST AGRICULTURAL AREA IN INDIA?",
                 ["JHARKHAND", "UTTAR PRADESH", "MADHYA PRADESH", "BIHAR"], 0),
        Question("WHERE IS THE LARGEST MUSEUM IN INDIA LOCATED?", ["KOLKATA", "NEW DELHI", "PUNE", "MUMBAI"], 1),
        Question("WHERE IS THE LARGEST STADIUM IN INDIA LOCATED?", ["KOLKATA", "MUMBAI", "CHENNAI", "DELHI"], 0),
        Question("WHERE IS THE LARGEST NATURAL LAKE IN INDIA LOCATED?", ["CHILKA", "WULAR", "PULICAT", "WEMBAD"], 0),
        Question("WHERE IS THE LARGEST RAILWAY NETWORK IN INDIA?", ["MUMBAI", "KOLKATA", "DELHI", "CHENNAI"], 2),
        Question("WHAT IS THE LARGEST HERITAGE SITE IN INDIA?", ["TAJ MAHAL", "VANI VILAS", "HAMPI", "KONKANI GAD"], 0),
        Question("WHO IS THE PRIME MINISTER OF INDIA IN 2024?",
                 ["NARENDRA MODI", "RAHUL GANDHI", "AMIT SHAH", "SONIA GANDHI"], 0),
        Question("IN WHICH INDIAN STATE IS THE 'ONE NATION, ONE RATION CARD' SCHEME NOW IMPLEMENTED?",
                 ["MAHARASHTRA", "KERALA", "BIHAR", "GUJARAT"], 2),
        Question("IN WHICH INDIAN CITY WAS THE FINAL OF THE INDIAN PREMIER LEAGUE (IPL) HELD IN 2024?",
                 ["MUMBAI", "DELHI", "CHENNAI", "BENGALURU"], 3),
        Question("WHICH INDIAN ACTOR WON AN OSCAR IN 2023?",
                 ["AMITABH BACHCHAN", "SHAHRUKH KHAN", "RANVEER SINGH", "PRIYANKA CHOPRA"], 3),
        Question("WHICH INDIAN ACTRESS WON AN OSCAR IN 2023?",
                 ["AMITABH BACHCHAN", "SHAHRUKH KHAN", "RANVEER SINGH", "PRIYANKA CHOPRA"], 3)
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 0),
        Question("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome", "Chloroplast"], 0),
        Question("WHO IS THE PRIME MINISTER OF INDIA IN 2024?",
                 ["NARENDRA MODI", "RAHUL GANDHI", "AMIT SHAH", "SONIA GANDHI"], 0),
        Question("WHO WAS THE PRESIDENT OF INDIA IN 2023?",
                 ["RAM NATH KOVIND", "PRANAB MUKHERJEE", "RAHUL GANDHI", "NARENDRA MODI"], 0),
        Question("IN 2023, IN WHICH INDIAN STATE DID THE 'COVID-19' TESTING BEGIN?",
                 ["MAHARASHTRA", "KERALA", "GUJARAT", "BIHAR"], 1),
        Question("IN 2023, IN WHICH INDIAN STATE WAS THE 'JALNIRAY' PROJECT INITIATED?",
                 ["GUJARAT", "MAHARASHTRA", "KERALA", "TAMIL NADU"], 0),
        Question("IN 2023, IN WHICH INDIAN CITY WAS THE FINAL OF THE INDIAN PREMIER LEAGUE (IPL) HELD?",
                 ["MUMBAI", "CHENNAI", "KOLKATA", "BENGALURU"], 2),
        Question("IN 2023, WHICH INDIAN MUSICIAN WAS AWARDED THE 'GRAMMY MUSIC ACADEMY AWARD'?",
                 ["A.R. RAHMAN", "LATA MANGESHKAR", "SHANKAR MAHADEVAN", "GULZAR"], 3),
        Question("IN 2023, WHICH INDIAN SPORTSPERSON WAS AWARDED THE 'ALL INDIA SPORTS ASSOCIATION' AWARD?",
                 ["PV SINDHU", "MIRABAI CHANU", "HARMANPREET SINGH"], 0),
        Question("IN 2023, WHICH INDIAN ACTRESS WON AN OSCAR?",
                 ["AMITABH BACHCHAN", "SHAHRUKH KHAN", "RANVEER SINGH", "PRIYANKA CHOPRA"], 3),
        Question("WHERE IS THE CAPITAL OF MAHARASHTRA?", ["NAGPUR", "PUNE", "MUMBAI", "NASHIK"], 2),
        Question("WHO IS THE PRESIDENT OF INDIA?", ["RAM NATH KOVIND", "NARENDRA MODI", "RAHUL GANDHI", "AMIT SHAH"],
                 0),
        Question("WHO WAS THE FIRST PRESIDENT OF INDIA?",
                 ["DR. RAJENDRA PRASAD", "BHIMRAO AMBEDKAR", "JAWAHARLAL NEHRU", "SARDAR PATEL"], 0),
        Question("WHERE IS THE FIRST DISTRICT AND DEVELOPMENT AREA OF MAHARASHTRA?",
                 ["PUNE", "NASHIK", "RATNAGIRI", "MUMBAI"], 3),
        Question("WHICH IS THE LARGEST DISTRICT IN MAHARASHTRA?", ["PUNE", "THANE", "NASHIK", "NAGPUR"], 1),
        Question("WHO WAS THE FIRST FEMALE PRIME MINISTER OF INDIA?",
                 ["INDIRA GANDHI", "SONIA GANDHI", "SUSHMA SWARAJ", "MEERA KUMARI"], 0),
        Question("WHO WAS THE FIRST FEMALE CHIEF MINISTER OF MAHARASHTRA?",
                 ["SUSHMA SWARAJ", "INDIRA GANDHI", "VASUNDHARA RAJE", "SONIA GANDHI"], 2),
        Question("WHO WAS THE FIRST FEMALE GOVERNOR OF MAHARASHTRA?",
                 ["PRATIBHA PATIL", "SONIA GANDHI", "SUSHMA SWARAJ", "INDIRA GANDHI"], 0),
        Question("WHO WAS THE FIRST FEMALE SPEAKER OF MAHARASHTRA?",
                 ["MEENAKSHI LEKI", "SUSHMA SWARAJ", "INDIRA GANDHI", "SONIA GANDHI"], 0),
        Question("WHO WAS THE FIRST FEMALE CHIEF JUSTICE OF MAHARASHTRA?",
                 ["SONIA GANDHI", "SUSHMA SWARAJ", "INDIRA GANDHI", "BHANUTAI WANG"], 3),
        Question("WHO WAS THE FIRST FEMALE WARRIOR IN MAHARASHTRA?",
                 ["TATYA TOPE", "BHIKIBAI LAXMIKANT NYAGANBAVKAR", "VASUDEV BALWANT PHADKE", "SABAJI BOMBALI"], 3),
        Question("WHERE IS THE FIRST RAILWAY STATION IN MAHARASHTRA?", ["PUNE", "NASHIK", "MUMBAI", "NAGPUR"], 2),
        Question("WHERE IS THE FIRST AIRPORT IN MAHARASHTRA?", ["PUNE", "NASHIK", "MUMBAI", "NAGPUR"], 2),
        Question("WHERE IS THE FIRST MUNICIPALITY IN MAHARASHTRA?", ["PUNE", "NASHIK", "MUMBAI", "NAGPUR"], 2),
        Question("WHO IS THE FIRST FEMALE PRIME MINISTER OF NEPAL?",
                 ["SUSHILA KARMANDU", "KIRTI AZAD", "SANTIA GANDHI", "VIDYADEVI BHANDARI"], 0),
        Question("WHICH OCEAN IS NEAR THE UNITED STATES?",
                 ["HIND MAHARAJA", "ATLANTIC OCEAN", "PACIFIC OCEAN", "ARCTIC OCEAN"], 1),
        Question("WHO WAS THE FOUNDER OF THE MUGHAL EMPIRE?", ["BABUR", "HUMAYUN", "AKBAR", "JAHANGIR"], 0),
        Question("WHERE IS THE MUGHAL EMPIRE'S FOUNDER BABUR'S FAMILY IN WHICH COUNTRY?",
                 ["TURKMENISTAN", "UZBEKISTAN", "AFGHANISTAN", "PAKISTAN"], 1),
        Question("WHAT WAS THE FULL NAME OF THE FOUNDER OF THE MUGHAL EMPIRE BABUR?",
                 ["JALALUDDIN MOHAMMAD AKBAR", "NASIRUDDIN MAHMOOD", "AHMAD SHAH ABDALI", "JALALUDDIN MOHAMMAD BABUR"],
                 3),
        Question("WHO WAS THE KHILJI RULER OF THE MUGHAL EMPIRE?", ["AKBAR", "JAHANGIR", "BABUR", "HUMAYUN"], 2),
        Question("WHICH RELIGION DID AKBAR MARRY?", ["BUDDHIST", "JAIN", "HINDU", "MUSLIM"], 2),
        Question("DURING AKBAR'S REIGN, WHERE WAS THE CENTRAL GOVERNANCE OF THE MUGHAL EMPIRE?",
                 ["DELHI", "LAHORE", "AGRA", "AJMER"], 3),
        Question("TO WHOM DID JAHANGIR GIVE CONGRATULATIONS AS 'NAZAR'?", ["SALEEM", "AKBAR", "BABUR", "HUMAYUN"], 0)
        Question("Which famous building was constructed by Shah Jahan?",
                 ["Taj Mahal", "Gol Gumbaz", "Film Palace", "Hawa Mahal"], 0),
        Question("On which place did Adil Shah build the fort of Bijapur?", ["Pune", "Nashik", "Satara", "Aurangabad"],
                 3),
        Question("Which fort did Shivaji Maharaj master throughout his life?",
                 ["Raigad", "Pratapgad", "Sinhagad", "Pratapgad"], 2),
        Question("Which religion did Akbar expect to have a relationship with?",
                 ["Buddhist", "Jain", "Hindu", "Muslim"], 0),
        Question("Which ruler in the Mughal Empire made a simple structure for resolving the conflicts of kings?",
                 ["Bairam Khan", "Nanavati", "Second", "Fourth"], 2),
        Question("Who was the son of Shivaji Bhosale who made a structure on the fort?",
                 ["Shivaji", "Shahaji", "Sambhaji", "Chhatrapati Shivaji Maharaj"], 0),
        Question("What was the name of the fort built by Babar's leadership in the Mughal Empire?",
                 ["Ajmer", "Chitrapat", "Golconda", "Div"], 2),
        Question("Which city did Kutub-ud-din Aibak establish in the Mughal Empire?",
                 ["Delhi", "Agra", "Lahore", "Ajmer"], 0),
        Question("Which king in the Mughal Empire was the owner of which city?",
                 ["Humayun - Delhi", "Jahangir - Agra", "Akbar - Fatehpur Sikri", "Shah Jahan - Agra"], 2),
        Question("What was the name of the city established by Akbar in the Mughal Empire?",
                 ["Allahabad", "Lahore", "Fatehpur Sikri", "Ajmer"], 2),
        Question("What was the name of the fort whose name Babar changed in the Mughal Empire?",
                 ["Purana Qila", "Golconda", "Chitrapat", "Div"], 0),
        Question("Which king in the Mughal Empire established the Parsi in which city?",
                 ["Farrukhabad", "Agra", "Shahjahanpur", "Fatehpur Sikri"], 3),
        Question("What is the age limit for eligible candidates for railway recruitment?",
                 ["18 to 25 years", "20 to 30 years", "22 to 35 years", "25 to 40 years"], 2),
        Question("What is the necessary educational qualification for railway recruitment?",
                 ["10th", "12th", "Graduate", "MBA"], 1),
        Question("Which exam is conducted for railway recruitment?",
                 ["Primary", "Main", "Physical Fitness", "Interview"], 1),
        Question("How much is the required fee for the thumb impression for railway recruitment?",
                 ["₹500", "₹1000", "₹1500", "₹2000"], 0),
        Question("What is the syllabus for the primary exam for railway recruitment?",
                 ["Marathi, English, Social Science, Mathematics", "Social Science, Physics, Chemistry, Mathematics",
                  "Social Science, Physics, Chemistry, Mathematics", "Marathi, English, Physics, Chemistry"], 0),
        Question("What are the subjects in the syllabus of the main exam for railway recruitment?",
                 ["Social Science, Physics, Chemistry, Mathematics", "Marathi, English, Physics, Chemistry",
                  "Social Science, Physics, Chemistry, Mathematics",
                  "Social Science, Mathematics, Chemistry, Mathematics"], 2),
        Question("What documents are required for eligible candidates to apply for railway recruitment?",
                 ["Caste Certificate, Education Certificate", "Education Certificate, Aadhar Card",
                  "Aadhar Card, Application Number", "Application Number, Caste Certificate"], 0),
        Question("What is the cancellation of physical examination for eligible candidates for railway recruitment?",
                 ["1600 meters", "1000 meters", "800 meters", "1200 meters"], 2),
        Question("What is the last date for applying for railway recruitment?",
                 ["30 January", "30 April", "30 May", "30 June"], 1),
        Question("When was the result of the railway recruitment exam announced?",
                 ["15 May", "15 June", "15 July", "15 August"], 0),
        Question("What fee is charged for eligible candidates for railway recruitment?",
                 ["Caste Certificate", "Aadhar Card", "Education Certificate", "Application Number"], 3),
        Question("Which city in Maharashtra is known as the financial capital of India?",
                     ["Pune", "Nagpur", "Mumbai", "Nashik"], 2),

        Question("Which district in Maharashtra is famous for its oranges?",
                     ["Satara", "Sangli", "Nagpur", "Solapur"], 2),

        Question("What is the traditional Maharashtrian headgear called?", ["Topi", "Pagadi", "Pheta", "Turban"], 2),

        Question(
                "Which festival, known for its colorful processions, is celebrated with great enthusiasm in Maharashtra?",
                 ["Diwali", "Holi", "Ganesh Chaturthi", "Navratri"], 2),

        Question("Which hill station in Maharashtra is often referred to as the 'Queen of the Sahyadri'?",
                     ["Matheran", "Lonavala", "Mahabaleshwar", "Panchgani"], 2),

        Question("Which river is the longest river flowing entirely within the state of Maharashtra?",
                     ["Krishna", "Godavari", "Tapi", "Bhima"], 1),

        Question("Which fort in Maharashtra is famous for its triangular shape and is known as the 'Lion Fort'?",
                     ["Raigad Fort", "Sinhagad Fort", "Pratapgad Fort", "Torna Fort"], 1),

        Question(
                "What is the traditional Maharashtrian sweet dish made during festivals, especially Ganesh Chaturthi?",
                ["Modak", "Puran Poli", "Shrikhand", "Gulab Jamun"], 0),

        Question("Which wildlife sanctuary in Maharashtra is known for its population of Bengal tigers?",
                     ["Tadoba Andhari Tiger Reserve", "Melghat Tiger Reserve", "Sanjay Gandhi National Park",
                      "Navegaon National Park"], 0),

        Question(
                "Which traditional dance form of Maharashtra is characterized by rhythmic footwork and vibrant costumes?",
                ["Bharatanatyam", "Kuchipudi", "Kathak", "Lavani"], 3),

        Question(
                "Which city in Maharashtra is famous for its caves, including the UNESCO World Heritage Site known as the Ellora Caves?",
                ["Pune", "Nashik", "Aurangabad", "Nagpur"], 2),

        Question("Which river flows through the city of Pune in Maharashtra?",
                     ["Krishna", "Tapi", "Mula", "Godavari"], 2),

        Question(
                "Which festival marks the beginning of the new agricultural year and is celebrated with the worship of cattle in Maharashtra?",
                ["Pola", "Gudi Padwa", "Makar Sankranti", "Baisakhi"], 0),

        Question("Which Marathi saint-poet is known for his devotional compositions called 'Abhang'?",
                     ["Namdev", "Tukaram", "Eknath", "Dnyaneshwar"], 1),

        Question("Which ancient Buddhist cave complex is located near Aurangabad in Maharashtra?",
                     ["Karla Caves", "Pandavleni Caves", "Kanheri Caves", "Ajanta Caves"], 3),

        Question(
                "Which traditional Maharashtrian dish is a spicy preparation of sprouted moth beans often served with pav?",
                ["Misal Pav", "Vada Pav", "Pav Bhaji", "Sabudana Khichdi"], 0),

        Question("Which famous Indian cricketer hailing from Maharashtra is known as the 'Master Blaster'?",
                     ["Kapil Dev", "Rahul Dravid", "Sachin Tendulkar", "Virat Kohli"], 2),

        Question(
                "Which festival celebrated in Maharashtra involves the worship of the 'Kalash' symbolizing prosperity and is observed during Navratri?",
                ["Ganesh Chaturthi", "Diwali", "Gudi Padwa", "Navratri"], 2),

        Question(
                "Which Marathi film, directed by Nagraj Manjule, won the National Film Award for Best Feature Film in 2016?",
                ["Sairat", "Natsamrat", "Court", "Fandry"], 0),

        Question("Which is the largest district by area in Maharashtra?",
                     ["Thane", "Nagpur", "Ahmednagar", "Palghar"], 1),
        Question("Who won the 2024 Indian Premier League (IPL) cricket tournament?",
                 ["Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bangalore", "Kolkata Knight Riders"], 1),
        Question("Which Indian state implemented a new policy to promote electric vehicle adoption in 2024?",
                 ["Maharashtra", "Gujarat", "Karnataka", "Tamil Nadu"], 3),
        Question("Which Indian city was declared as the cleanest city in the Swachh Survekshan 2024 rankings?",
                 ["Indore", "Surat", "Chandrapur", "Mysuru"], 0),
        Question("Who won the gold medal for India in the men's individual event at the 2024 Paris Olympics?",
                 ["Neeraj Chopra", "Bajrang Punia", "Abhinav Shaw", "Manika Batra"], 2),
        Question(
            "Which Indian state became the first to achieve 100% COVID-19 vaccination coverage of its eligible population in 2024?",
            ["Kerala", "Goa", "Himachal Pradesh", "Sikkim"], 1),
        Question("Who was appointed as the new Chief Justice of India in 2024?",
                 ["N. V. Ramana", "Uday Lalit", "Rohinton Nariman", "Indu Malhotra"], 0),
        Question("Which Indian company became the first to achieve a market capitalization of $1 trillion in 2024?",
                 ["Tata Group", "Reliance Industries", "Infosys", "Wipro"], 1),
        Question(
            "Which Indian state launched the 'One Family, One Job' scheme in 2024 to provide government jobs to every family?",
            ["Rajasthan", "Uttar Pradesh", "Madhya Pradesh", "Bihar"], 2),
        Question("Who won the 2024 Nobel Prize in Literature from India?",
                 ["Arundhati Roy", "Jhumpa Lahiri", "Salman Rushdie", "Vikram Seth"], 3),
        Question("Which Indian startup became the first to achieve a valuation of $100 billion in 2024?",
                 ["Zomato", "Swiggy", "Byju's", "Ola"], 2),
        Question(
            "Which Indian state government announced the implementation of a universal basic income scheme in 2024?",
            ["Telangana", "Andhra Pradesh", "Kerala", "Punjab"], 0),
        Question("Who was appointed as the new Chief Minister of Uttar Pradesh after the 2024 assembly elections?",
                 ["Yogi Adityanath", "Mayawati", "Akhilesh Yadav", "Priyanka Gandhi Vadra"], 2),
        Question("Which Indian film won the Best Foreign Language Film award at the 2024 Oscars?",
                 ["The Disciple", "Gully Boy", "Ludo", "Dhamaka"], 0),
        Question("Which Indian state became the first to achieve 100% literacy rate in 2024?",
                 ["Kerala", "Tamil Nadu", "Andhra Pradesh", "Manipur"], 1),
        Question("Who was named as the ICC Men's Cricketer of the Year for 2024 from India?",
                 ["Virat Kohli", "Rohit Sharma", "Jasprit Bumrah", "Rishabh Pant"], 3),
        Question("Which Indian scientist won the Nobel Prize in Physics in 2024?",
                 ["C. N. R. Rao", "S. Chandrasekhar", "Venkatraman Ramakrishnan", "Abhijit Banerjee"], 2),
        Question("Which Indian state banned the sale and usage of single-use plastic from January 1, 2024?",
                 ["Karnataka", "Tamil Nadu", "Maharashtra", "Himachal Pradesh"], 0),
        Question("Who won the 2024 Booker Prize for Fiction from India?",
                 ["Arundhati Roy", "Salman Rushdie", "Aravind Adiga", "Kiran Desai"], 2),
        Question("Which Indian city hosted the G20 Summit in 2024?", ["New Delhi", "Mumbai", "Hyderabad", "Bangalore"],
                 0),
        Question("Who was named as the 2024 ICC Women's Cricketer of the Year from India?",
                 ["Smriti Mandhana", "Harmanpreet Kaur", "Mithali Raj", "Jhulan Goswami"], 0),
            # Add more questions here
        # Create the root layout
        root = BoxLayout(orientation='vertical')
        screen_manager = ScreenManager()
        background = Image(source=r"C:\Users\91967\Pictures\live wallpaper\yashwolf.jpg", allow_stretch=True, keep_ratio=False)

        root.add_widget(background)
        quiz_screen = QuizScreen(questions, name='quiz')
        screen_manager.add_widget(quiz_screen)
        return screen_manager

if __name__ == "__main__":
    QuizApp().run()
