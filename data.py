#! /usr/bin/env python
# -*- coding: utf-8 -*-
payload = {
    'email': '+79996080340',
    'password': 'Discord10741!'
}

headers = ["name acc: OVALEXOLK adress: 6226 S Archer Ave (Chicago)",
"name acc: Retry_88 Adress: 100 Portales Real (Bakersfield)",
"name acc: Dashut Adress: 204 Skeet CT (Bakersfield)",
"name acc: Senko_ Adress: 6617 Hammond Way (Bakersfield)",
"name acc: Nimoryan"
]

old_types = [
'Elite',
'Key Player',
'Starter',
'Starter (cont.)',
'Contributor (cont.)',
'Contributor'
]

types = [
'memento',
'essential',
]

seasons = [
"2017",
"2018",
"2019",
"2020",
'2021',
'2022',
'2023',
'2024',
'2025',
'2026',
"2027",
"2028",
"2029",
"2030",
"2031",
"2032",
"2033",
"2034",
"2035",
"2036",
"2037",
"2038",
"2039",
"2040"
]

unistyle = """<style>

    h2 {
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
    }
    .redify{
        background-color: red;
    }
    table { 
        margin-left: auto;
        margin-right: auto;
    }
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    th, td {
        padding: 5px;
        text-align: center;
        font-family: Helvetica, Arial, sans-serif;
        font-size: 90%;
    }
    table tbody tr:hover {
        background-color: #dddddd;
    }
    .wide {
        width: 90%; 
    }

</style>"""

leggits = [
'Essential Cap',
'Essential Variant Cap',
'Essential Jersey',
'Essential Variant Jersey',
'Replica Cap',
'Replica Jersey',
'Replica Football',
'Memento Cap',
'Memento Ball',
'Memento Jersey',
'Memento Football',
'Essential Away Cap',
'Essential Away Variant Cap',
'Essential Away Jersey',
'Essential Away Variant Jersey',
'Replica Away Cap',
'Replica Away Jersey',
'Replica Away Football',
'Memento Away Cap',
'Memento Away Jersey',
'Memento Away Football'
]

teams = ['Arizona', 'Atlanta', 'Baltimore', 'Buffalo', 'Carolina', 'Chicago', 'Cincinnati', 'Cleveland', 'Dallas', 'Denver', 'Detroit', 'Green Bay', 'Houston', 'Indianapolis', 'Jacksonville', 'Kansas City', 'Las Vegas', 'Los Angeles #2', 'Los Angeles #1', 'Miami', 'Minnesota', 'New England', 'New Orleans', 'New York #1', 'New York #2', 'Philadelphia', 'Pittsburgh', 'San Francisco', 'Seattle', 'Tampa Bay', 'Tennessee', 'Washington', 'Los Angeles', 'New York']

players = ['Tom Brady', 'Tristan Wirfs', 'Devin White', 'Chris Godwin', 'Ryan Jensen', 'Carlton Davis III', 'Shaquil Barrett', 'Scotty Miller', 'Mike Evans', 'Lavonte David', 'Antoine Winfield Jr', 'Jason Pierre-Paul', 'Ronald Jones II', 'Rob Gronkowski', 'Leonard Fournette', 'Sean Murphy-Bunting', 'Antonio Brown', 'Ndamukong Suh', 'Jordan Whitehead', 'Ali Marpet', 'Ryan Succop', 'Jamel Dean', 'Vita Vea', 'Anthony Nelson', 'Bradley Pinion', 'Mike Edwards', 'Alex Cappa', 'William Gholston', 'Cameron Brate', 'Donovan Smith', 'Joey Bosa', 'Justin Herbert', 'Keenan Allen', 'Michael Badgley', 'Austin Ekeler', 'Nick Vigil', 'Ty Long', 'Rayshawn Jenkins', 'Joshua Kelley', 'Kenneth Murray Jr', 'Denzel Perryman', 'Michael Davis', 'Uchenna Nwosu', 'Jalen Guyton', 'Mike Williams', 'Kyzir White', 'Linval Joseph', 'Hunter Henry', 'Nasir Adderley', 'Casey Hayward Jr', 'Trey Pipkins III', 'Forrest Lamp', 'Sam Tevi', 'Justin Jackson', 'Dan Feeney', 'Justin Jones', 'Chris Harris Jr', 'Tyron Johnson', 'Scott Quessenberry', 'Jerry Tillery', 'Brandon Scherff', 'Terry McLaurin', 'Chase Young', 'Chase Roullier', 'Tress Way', 'Logan Thomas', 'Cole Holcomb', 'Antonio Gibson', 'Kamren Curl', 'Landon Collins', 'Fabian Moreau', 'Montez Sweat', 'Cornelius Lucas', 'Dwayne Haskins Jr', 'Wes Schweitzer', 'Kendall Fuller', 'Jon Bostic', 'Daron Payne', 'Jonathan Allen', 'Cam Sims', 'Dustin Hopkins', 'Kyle Allen', 'Isaiah Wright', 'Steven Sims Jr', 'Jeremy Reaves', 'Morgan Moses', 'Ryan Kerrigan', 'JD McKissic', 'Deshazor Everett', 'Kevin Pierre-Louis', 'Bradley Chubb', 'Justin Simmons', 'Garett Bolles', "Dre'Mont Jones", 'Phillip Lindsay', 'Noah Fant', 'Dalton Risner', 'Drew Lock', 'Graham Glasgow', 'Jerry Jeudy', 'Michael Ojemudia', 'Royce Freeman', 'Alexander Johnson', 'Josey Jewell', 'Kareem Jackson', 'DeShawn Williams', 'Melvin Gordon III', 'Tim Patrick', 'Malik Reed', 'Bryce Callahan', 'DeMarcus Walker', 'KJ Hamler', 'Shelby Harris', 'Lloyd Cushenberry III', 'Sam Martin', 'Jeremiah Attaochu', 'Brandon McManus', 'Elijah Wilkinson', 'A.J. Bouye', 'Albert Okwuegbunam', 'Xavien Howard', 'Kyle Van Noy', 'Emmanuel Ogbah', 'Jerome Baker', 'Tua Tagovailoa', 'Bobby McCain', 'Eric Rowe', 'Elandon Roberts', 'Jakeem Grant Sr', 'Ryan Fitzpatrick', 'Brandon Jones', 'Austin Jackson', 'Andrew Van Ginkel', 'Myles Gaskin', 'Ted Karras', 'DeVante Parker', 'Nik Needham', 'Mike Gesicki', 'Christian Wilkins', 'Zach Sieler', 'Preston Williams', 'Raekwon Davis', 'Robert Hunt', 'Matt Haack', 'Shaq Lawson', 'Salvon Ahmed', 'Ereck Flowers', 'Jason Sanders', 'Jesse Davis', 'Matt Breida', 'Fred Warner', 'Nick Bosa', 'George Kittle', 'Daniel Brunskill', 'Mike McGlinchey', 'Dre Greenlaw', 'Colton McKivitz', 'Jeff Wilson Jr', 'Jason Verrett', 'Jimmy Garoppolo', 'Azeez Al-Shaair', 'Brandon Aiyuk', 'Raheem Mostert', 'Nick Mullens', 'D.J. Jones', 'Tarvarius Moore', 'Arik Armstead', 'Jimmie Ward', 'Trent Williams', 'Kendrick Bourne', 'Laken Tomlinson', 'Mitch Wishnowsky', 'Kyle Juszczyk', 'Robbie Gould', 'Kerry Hyder Jr', 'Richard Sherman', 'Jerick McKinnon', 'Dion Jordan', 'Emmanuel Moseley', 'Jamar Taylor', 'Fletcher Cox', 'Jason Kelce', 'Brandon Graham', 'Derek Barnett', 'Greg Ward', 'Carson Wentz', 'Alex Singleton', 'Zach Ertz', 'Marcus Epps', 'Duke Riley', 'Josh Sweat', 'Jalen Mills', 'Travis Fulgham', 'Miles Sanders', 'T.J. Edwards', 'Jason Peters', 'Nathan Gerry', 'Dallas Goedert', 'Rodney McLeod', 'Darius Slay', 'Jalen Reagor', "K'Von Wallace", 'Matt Pryor', 'Boston Scott', 'Jalen Hurts', 'Javon Hargrave', 'Jake Elliott', 'Nate Herbig', 'Cameron Johnston', 'Jordan Mailata', 'Lamar Jackson', 'Calais Campbell', 'Marlon Humphrey', 'Derek Wolfe', 'J.K. Dobbins', 'Willie Snead IV', 'Marcus Peters', 'Matt Judon', 'DeShon Elliott', 'Chuck Clark', 'Justin Tucker', 'Orlando Brown Jr', 'L.J. Fort', 'Mark Andrews', 'Matt Skura', 'Malik Harrison', 'Gus Edwards', 'Ben Powers', 'Patrick Queen', 'Marquise Brown', 'Patrick Mekari', 'Chris Board', 'Pernell McPhee', 'Miles Boykin', 'Bradley Bozeman', 'Brandon Williams', 'Sam Koch', 'Tyus Bowser', 'Dez Bryant', 'Devin Duvernay', 'Darius Leonard', 'DeForest Buckner', 'Quenton Nelson', 'Kenny Moore II', 'T.Y. Hilton', 'Braden Smith', 'Jonathan Taylor', '#Н/Д', 'Grover Stewart', 'Xavier Rhodes', 'Mark Glowinski', 'Rock Ya-Sin', 'Denico Autry', 'Khari Willis', 'Michael Pittman Jr', 'Zach Pascal', 'Julian Blackmon', 'Bobby Okereke', 'Justin Houston', 'Ryan Kelly', 'Tyquan Lewis', 'Rigoberto Sanchez', 'Jack Doyle', 'T.J. Carrie', 'Nyheim Hines', 'Jacoby Brissett', 'Rodrigo Blankenship', 'Al-Quadin Muhammad', 'Jordan Wilkins', 'Marcus Johnson', 'Dalvin Cook', 'Eric Kendricks', 'Justin Jefferson', 'Kirk Cousins', 'Jeff Gladney', 'Adam Thielen', "Brian O'Neill", 'Ifeadi Odenigbo', 'Kyle Rudolph', 'Jaleel Johnson', 'Anthony Harris', 'D.J. Wonnum', 'Cameron Dantzler', 'Harrison Smith', 'Riley Reiff', 'Eric Wilson', 'Alexander Mattison', 'Irv Smith Jr', 'Britton Colquitt', 'Yannick Ngakoue', 'Chad Beebe', 'Hardy Nickerson Jr', 'Garrett Bradbury', "Hercules Mata'afa", 'Harrison Hand', 'Dakota Dozier', 'Ezra Cleveland', 'Shamar Stephen', 'Bisi Johnson', 'Dan Bailey', 'Khalil Mack', 'Allen Robinson II', 'Roquan Smith', 'Akiem Hicks', 'Darnell Mooney', 'Tashaun Gipson', 'Buster Skrine', 'Eddie Jackson', 'Danny Trevathan', 'Jimmy Graham', 'Cody Whitehair', 'Mario Edwards Jr', 'Mitchell Trubisky', 'Germain Ifedi', 'Cordarrelle Patterson', 'Sam Mustipher', 'David Montgomery', 'Kyle Fuller', 'Bilal Nichols', 'Anthony Miller', 'Cairo Santos', "Pat O'Donnell", 'Brent Urban', 'Alex Bars', 'Cole Kmet', 'Charles Leno Jr', 'DeAndre Houston-Carson', 'Jaylon Johnson', 'Barkevious Mingo', 'Nick Foles', 'Patrick Mahomes II', 'Travis Kelce', 'Tyreek Hill', 'Charvarius Ward', 'Clyde Edwards-Helaire', 'Demarcus Robinson', 'Tyrann Mathieu', 'Austin Reiter', 'Anthony Hitchens', "L'Jarius Sneed", 'Chris Jones', 'Derrick Nnadi', 'Daniel Sorensen', 'Damien Wilson', 'Eric Fisher', 'Darrel Williams', 'Alex Okafor', 'Mike Remmers', 'Mecole Hardman', 'Frank Clark', "Le'Veon Bell", 'Juan Thornhill', 'Nick Allegretti', 'Sammy Watkins', 'Bashaud Breeland', 'Andrew Wylie', 'Tommy Townsend', 'Ben Niemann', 'Harrison Butker', 'Willie Gay', 'Stephon Gilmore', 'Jake Bailey', 'J.C. Jackson', 'David Andrews', 'Chase Winovich', 'Adrian Phillips', 'Devin McCourty', 'Damien Harris', 'Jason McCourty', 'Nick Folk', 'Deatrich Wise Jr', 'Jakob Johnson', 'Isaiah Wynn', 'John Simon', 'Joe Thuney', 'Adam Butler', 'Mike Onwenu', 'Sony Michel', 'Cam Newton', "Ja'Whaun Bentley", "N'Keal Harry", 'Jonathan Jones', 'Terez Hall', 'Rex Burkhead', 'Jarrett Stidham', 'Lawrence Guy', 'Shaq Mason', 'Ryan Izzo', 'Kyle Dugger', 'James White', 'Marcus Maye', 'Mekhi Becton', 'Neville Hewitt', 'John Franklin-Myers', 'Braxton Berrios', 'Sam Darnold', 'Connor McGovern', 'Quinnen Williams', 'Chris Herndon IV', 'Jordan Jenkins', 'Harvey Langi', 'Jamison Crowder', 'Avery Williamson', 'Frank Gore', 'Breshad Perriman', 'Pierre Desir', 'Tarell Basham', 'Brian Poole', 'Folorunso Fatukasi', 'Blessuan Austin', 'Chuma Edoga', 'Sam Ficken', 'Braden Mann', 'Henry Anderson', 'George Fant', 'Nathan Shepherd', 'Greg Van Roten', 'Denzel Mims', 'Ty Johnson', 'Joe Flacco', 'Derrick Henry', 'Jeffery Simmons', 'AJ Brown', 'Chris Jackson', 'Kenny Vaccaro', 'Kevin Byard', 'Jack Crawford', 'Anthony Firkser', 'David Long', 'Corey Davis', 'Ben Jones', 'Jayon Brown', 'Nate Davis', 'Amani Hooker', 'DaQuan Jones', 'Ryan Tannehill', 'Jonnu Smith', 'Harold Landry III', 'Rodger Saffold III', 'Rashaan Evans', 'Jadeveon Clowney', 'Dennis Kelly', 'Desmond King', 'Jeremy McNichols', 'Brett Kern', 'Tye Smith', 'Stephen Gostkowski', 'Adam Humphries', 'David Quessenberry', 'Kalif Raymond', 'Alvin Kamara', 'Michael Thomas', 'Marshon Lattimore', 'Cameron Jordan', 'Demario Davis', "Tre'Quan Smith", 'C.J. Gardner-Johnson', 'Jameis Winston', 'Emmanuel Sanders', 'Terron Armstead', 'Taysom Hill', 'Latavius Murray', 'Janoris Jenkins', 'Trey Hendrickson', 'Jared Cook', 'Ryan Ramczyk', 'Malcolm Jenkins', 'David Onyemata', 'Erik McCoy', 'Marcus Williams', 'Wil Lutz', 'Andrus Peat', 'Kwon Alexander', 'Marquez Callaway', 'Alex Anzalone', 'P.J. Williams', 'Carl Granderson', 'Cesar Ruiz', 'Malcom Brown', 'Thomas Morstead', 'Josh Allen', "Tre'Davious White", 'Stefon Diggs', 'Daryl Williams', 'Taron Johnson', 'Devin Singletary', 'Tremaine Edmunds', 'Jerry Hughes', 'Ed Oliver', 'Mario Addison', 'Vernon Butler', 'Isaiah McKenzie', 'Gabriel Davis', 'Jordan Poyer', 'Dion Dawkins', 'Cole Beasley', 'Zack Moss', 'A.J. Klein', 'Micah Hyde', 'Jon Feliciano', 'Tyler Matakevich', 'Levi Wallace', 'Dawson Knox', 'Mitch Morse', 'Matt Milano', 'Tyrel Dodson', 'Corey Bojorquez', 'Matt Barkley', 'Cody Ford', 'Tyler Bass', 'Aaron Donald', 'Jalen Ramsey', 'Andrew Whitworth', 'Robert Woods', 'Troy Hill', 'Micah Kiser', 'Darrell Henderson Jr', 'Michael Brockers', 'Cooper Kupp', 'Tyler Higbee', 'John Johnson III', 'Rob Havenstein', 'Darious Williams', 'Jared Goff', 'Austin Blythe', 'Leonard Floyd', 'Austin Corbett', 'Jordan Fuller', 'Cam Akers', 'Troy Reeder', 'Sebastian Joseph-Day', 'Matt Gay', 'Gerald Everett', 'Josh Reynolds', 'Kenny Young', 'Taylor Rapp', 'Malcolm Brown', 'Morgan Fox', 'Johnny Hekker', 'David Edwards', 'Myles Garrett', 'Joel Bitonio', 'Nick Chubb', 'Jedrick Wills Jr', 'Olivier Vernon', 'Denzel Ward', 'Jarvis Landry', 'Karl Joseph', 'Sione Takitaki', 'Malcolm Smith', 'Rashard Higgins', 'Wyatt Teller', 'Kareem Hunt', 'Austin Hooper', 'B.J. Goodson', 'Odell Beckham Jr', 'Baker Mayfield', 'Andrew Sendejo', 'Jack Conklin', 'Terrance Mitchell', 'Larry Ogunjobi', 'Cody Parkey', 'Adrian Clayborn', 'Mack Wilson', 'M.J. Stewart', 'JC Tretter', 'Sheldon Richardson', 'Jamie Gillan', 'David Njoku', 'Case Keenum', 'Laremy Tunsil', 'Brandin Cooks', 'Deshaun Watson', 'J.J. Watt', 'Randall Cobb', 'Keion Crossen', 'Charles Omenihu', 'Zach Cunningham', 'David Johnson', 'Jordan Akins', 'Vernon Hargreaves III', 'Justin Reid', 'Darren Fells', 'Lonnie Johnson Jr', 'Eric Murray', 'Bradley Roby', 'Tyrell Adams', 'Whitney Mercilus', 'Keke Coutee', 'Will Fuller V', 'Nick Martin', 'Tytus Howard', 'Bryan Anger', 'A.J. Moore Jr', 'Benardrick McKinney', 'Duke Johnson', 'Max Scharping', 'Carlos Watkins', 'Pharaoh Brown', "Ka'imi Fairbairn", 'Josh Jacobs', 'Johnathan Abram', 'Darren Waller', 'Maxx Crosby', 'Cory Littleton', 'Henry Ruggs III', 'Nevin Lawson', 'Nicholas Morrow', 'Nelson Agholor', 'Carl Nassib', 'Rodney Hudson', 'Lamarcus Joyner', 'Hunter Renfrow', 'Kolton Miller', 'Derek Carr', 'Nick Kwiatkoski', 'Erik Harris', 'Gabe Jackson', 'Trayvon Mullen', 'Devontae Booker', 'Kendal Vickers', 'Clelin Ferrell', 'AJ Cole III', 'Foster Moreau', 'Daniel Carlson', 'Richie Incognito', 'Jeff Heath', 'Denzelle Good', 'Johnathan Hankins', 'Marcus Mariota', 'DeAndre Hopkins', 'Budda Baker', 'Kyler Murray', 'Christian Kirk', 'Larry Fitzgerald', 'Chandler Jones', 'Byron Murphy Jr', 'Corey Peters', 'Maxx Williams', 'Jalen Thompson', 'Justin Murray', 'J.R. Sweezy', 'Jordan Hicks', 'Dennis Gardeck', 'Justin Pugh', 'Isaiah Simmons', 'Chase Edmonds', 'Kenyan Drake', 'Markus Golden', 'D.J. Humphries', 'Andy Lee', 'Andy Isabella', 'Mason Cole', 'Deionte Thompson', 'Rashard Lawrence', 'Leki Fotu', 'Jordan Phillips', 'Devon Kennard', 'Zane Gonzalez', 'Lamont Gaillard', 'Aaron Rodgers', 'Davante Adams', 'David Bakhtiari', 'Aaron Jones', 'Krys Barnes', 'Rashan Gary', 'Jamaal Williams', 'Billy Turner', 'Preston Smith', "Za'Darius Smith", 'Corey Linsley', 'Darnell Savage Jr', 'Allen Lazard', 'Robert Tonyan', 'Adrian Amos', 'Elgton Jenkins', 'Kevin King', 'Dean Lowry', 'Marquez Valdes-Scantling', 'Jaire Alexander', 'Kingsley Keke', 'Chandon Sullivan', 'AJ Dillon', 'Will Redmond', 'Mason Crosby', 'Kenny Clark', 'JK Scott', 'Ty Summers', 'Marcedes Lewis', 'Lucas Patrick', 'James Bradberry', 'Leonard Williams', 'Blake Martinez', 'Saquon Barkley', 'Jabrill Peppers', 'Evan Engram', 'Graham Gano', 'Alfred Morris', 'Dalvin Tomlinson', 'Nick Gates', 'Sterling Shepard', 'Julian Love', 'Tae Crowder', 'Daniel Jones', 'Dexter Lawrence', 'Wayne Gallman II', 'Kyler Fackrell', 'Logan Ryan', 'Darius Slayton', 'Golden Tate III', 'Will Hernandez', 'Devonta Freeman', 'Isaac Yiadom', 'Cameron Fleming', 'Riley Dixon', 'Darnay Holmes', 'Devante Downs', 'B.J. Hill', 'Andrew Thomas', 'Kevin Zeitler', 'Joe Schobert', 'Myles Jack', 'James Robinson', 'Adam Gotsis', 'Andrew Norwell', 'D.J. Chark Jr', 'Tyler Shatley', 'Tyler Eifert', 'Andrew Wingard', 'Josh Jones', 'Sidney Jones IV', 'Tre Herndon', 'Jarrod Wilson', 'Dawuane Smoot', 'Gardner Minshew II', 'A.J. Cann', 'Taven Bryan', 'Keelan Cole', 'Josh Allen', 'Laviska Shenault Jr', 'Joe Giles-Harris', 'Cam Robinson', "James O'Shaughnessy", 'Chris Conley', 'Chris Claybrooks', 'Doug Costin', 'Dare Ogunbowale', 'Logan Cooke', 'Jawaan Taylor', 'Aldrick Rosas', 'Russell Wilson', 'Jamal Adams', 'Bobby Wagner', 'Quandre Diggs', 'D.J. Reed', 'Jarran Reed', 'Freddie Swain', 'Benson Mayowa', 'Chris Carson', 'DK Metcalf', 'Alton Robinson', 'K.J. Wright', 'David Moore', 'Shaquem Griffin', 'Tyler Lockett', 'Shaquill Griffin', 'Carlos Dunlap', 'Ethan Pocic', 'Duane Brown', 'Damien Lewis', 'Will Dissly', 'Carlos Hyde', 'Jordyn Brooks', 'Ryan Neal', 'Jordan Simmons', 'Brandon Shell', 'Jacob Hollister', 'Jason Myers', 'Michael Dickson', 'Poona Ford', 'Christian McCaffrey', 'Taylor Moton', 'Shaq Thompson', 'Tahir Whitehead', 'Curtis Samuel', 'Matt Paradis', 'Robby Anderson', 'Marquis Haynes', 'Myles Hartsfield', 'DJ Moore', 'DontÃ© Jackson', 'Brian Burns', 'Tre Boston', 'Teddy Bridgewater', 'Jeremy Chinn', 'Colin Thompson', 'Mike Davis', 'Rasul Douglas', 'Trenton Cannon', 'Stephen Weatherly', 'Ian Thomas', 'Chris Reed', 'Sam Franklin', 'Yetur Gross-Matos', 'John Miller', 'Bravvion Roy', 'Trent Scott', 'Derrick Brown', 'Joey Slye', 'Joseph Charlton', 'Joe Burrow', 'Jessie Bates III', 'A.J. Green', 'Jonah Williams', 'Drew Sample', 'LeShaun Sims', 'Jordan Evans', 'Tee Higgins', 'Josh Bynes', 'Kevin Huber', 'Mackensie Alexander', 'Sam Hubbard', 'Carl Lawson', 'Darius Phillips', 'Tyler Boyd', 'Joe Mixon', 'Brandon Allen', 'Giovani Bernard', 'Vonn Bell', 'William Jackson III', 'Mike Daniels', 'Logan Wilson', 'Randy Bullock', 'Samaje Perine', 'Bobby Hart', 'Khalid Kareem', 'Xavier Williams', 'Alex Redmond', "Xavier Su'a-Filo", 'Trey Hopkins', 'Jack Fox', 'Frank Ragnow', 'T.J. Hockenson', 'Tyrell Crosby', 'Tracy Walker III', 'Jamie Collins Sr', 'Jarrad Davis', 'Amani Oruwariye', 'Taylor Decker', 'Duron Harmon', 'Adrian Peterson', 'Danny Amendola', 'Reggie Ragland', 'Jahlani Tavai', 'Matthew Stafford', 'Romeo Okwara', 'Trey Flowers', "D'Andre Swift", 'Jeff Okudah', 'Jonah Jackson', 'Matt Prater', 'Christian Jones', 'Quintez Cephus', 'Jesse James', 'Darryl Roberts', 'Jason Cabinda', 'Oday Aboushi', 'Jayron Kearse', 'Everson Griffen', 'Mohamed Sanu', 'Zack Martin', 'Amari Cooper', 'Ezekiel Elliott', 'Xavier Woods', 'Jourdan Lewis', 'Dalton Schultz', 'Joe Looney', 'Anthony Brown', 'Dak Prescott', 'Donovan Wilson', 'Demarcus Lawrence', 'Leighton Vander Esch', 'Dorance Armstrong Jr', 'Jaylon Smith', 'CeeDee Lamb', 'Connor Williams', 'Tony Pollard', 'Andy Dalton', 'Michael Gallup', 'Trevon Diggs', 'Joe Thomas', 'Greg Zuerlein', 'Noah Brown', 'Neville Gallimore', 'Terence Steele', 'Hunter Niswander', 'Aldon Smith', 'Chidobe Awuzie', 'Darian Thompson', 'Brandon Knight', 'Calvin Ridley', 'Younghoe Koo', 'Grady Jarrett', 'Russell Gage', 'Chris Lindstrom', 'Hayden Hurst', 'Alex Mack', 'Todd Gurley II', 'Jake Matthews', 'Keanu Neal', 'Steven Means', 'A.J. Terrell', 'Matt Ryan', 'Brian Hill', 'Julio Jones', 'Foyesade Oluokun', 'Isaiah Oliver', 'Ricardo Allen', 'Kendall Sheffield', 'Deion Jones', 'Keith Smith', 'Ito Smith', 'Tyeler Davison', 'John Cominsky', 'Kaleb McGary', 'Josh Harris', 'Dante Fowler Jr', 'Mykal Walker', 'Matt Hennessy', 'Jacob Tuioti-Mariner', 'T.J. Watt', 'Minkah Fitzpatrick', 'Cameron Heyward', 'Joe Haden', 'Bud Dupree', 'Mike Hilton', 'Stephon Tuitt', 'JuJu Smith-Schuster', 'Steven Nelson', 'James Conner', 'Alejandro Villanueva', 'Benny Snell Jr', 'Eric Ebron', 'Chase Claypool', 'David DeCastro', 'Tyson Alualu', 'Diontae Johnson', 'Ben Roethlisberger', 'Terrell Edmunds', 'Cameron Sutton', 'Mason Rudolph', 'Marcus Allen', 'Kevin Dotson', 'Robert Spillane', 'Alex Highsmith', 'Chukwuma Okorafor', 'Matt Feiler', 'Jordan Berry', 'Chris Boswell', 'James Washington']