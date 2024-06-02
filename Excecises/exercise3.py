import random

# Kaun banega crorepati.
questions = [
            "with reference to genetics, which of these would best describe DNA and RNA?",
            "Current Railway Minister of India is", 
            "Which god is also known as ‘Gauri Nandan’?",
            
            "What does not grow on tree according to a popular Hindi saying?", 
            "Which city is known as Pink City in India?", 
            "Who wrote India's National Anthem?", 
            
            "How many major religions are there in India?", 
            "When is the National Hindi Diwas celebrated?", 
            "How many states are there in India?", 
            "Where in India Gate located?", 
            "Who wrote Vande Mataram?", 
            "Which one of the following places is famous for the Great Vishnu Temple?",
            "The largest Buddhist Monastery in India is located at",
            "Which Indian monument was originally built as a victory tower to commemorate the defeat of the Khan of Khambhat?", 
            "Who among the following was killed during 'Operation Bluestar' of 1984?", 
            "Which former Indian President died as a result of a road accident?",
            "which state or UT of india is divided into four districts - all named after the four cardinal directories?",
            "Kaiser-e-hind, found mostly in Nepal and the north-eastern part of india, is a rare species of which type of organism?"
             ]

options = [
        ["Base","Acid", "Salt", "Metal"],
        ["Mamta Banarjee","Ram Vilash","Ashwini Vaishnaw","Piyush Goyal"],
        ["Agni","Indra","Hanuman","Ganesha"],
        ["Money","Leaves","Flowers","Fruits"],
        ["Banglore","Maysore","Jaipur","Kochi"],
        ["Rabindranath Tagore","Lal Bahadur Shastri","Chetan Bhagat","RK Narayan"],
        
        ["6","7","8","9"],
        
        ["13 September","14 September","14 July","15 August"],
        
        ["28","29","30","31"],
        ["Agra","Punjab","Mumbai","New Delhi"],
        
        ["Sarat Chandra Chattopadhyay","Rabindranath Tagore","Bankim Chandra Chatterjee","Ishwar Chandra Vidyasagar"],
        
        ["Bordubar, Indonesia","Bamiyan, Afghanistan","Panja Sahib, Pakistan","Ankorvat, Cambodia"],
        ["Sarnath, Uttar Pradesh","Dharmashala, Himachal Pradesh","Gangtok, Sikkim","Tawang, Arunachal Pradesh"],
        ["Qutub Minar","India Gate","Charminar","Vijay Stambh"],
        ["Baba Santa Singh","Haji Mastan","Jarnail Singh Bhindrawale","Homi Jehangir Bhabha"],
        ["Rajendra Prasad","Faqruddin Ali Ahmed","Giani Zail Singh","R.Venkatraman"],
        ["Sikkim","Goa","Manipur","Chandigarh"],
        ["Fish","Butterfly","Bee","Lizard"],
    ]


answers = [2,3,4,1,3,1,1,2,1,4,3,4,4,4,3,3,1,2]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,500000,7500000,10000000,75000000]

# Get the user name
name = input("Welcome to Kaun Banega Crorepati.\nEnter Your Name :- ")

money = 0
askedQuestions = []

for i in range(len(levels)):
    
    # Find the random question
    randIdx = random.randint(0, 17)
    while(randIdx in askedQuestions):
        randIdx = random.randint(0, 17)
    
    askedQuestions.append(randIdx)
    print(f"\n\nYour question for Rs. {levels[i]} is: ")
    print(questions[randIdx])
    idx = 1
    for option in options[randIdx]:
        print(str(idx) + " " + option)
        idx+=1
    selectedAns = int(input("\nEnter option no. for selecting ans or 0 for quit from game :- "))
    if (selectedAns == 0):
        break
    money=levels[i]
    if selectedAns != answers[randIdx]:
        if (i <= 4):
            money = 0
        break
        
print("Hey ", name , " Your total amount won is ", money)
    
