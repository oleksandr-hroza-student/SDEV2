# SDEV2
This is our SDEV group project

******************************************************************************************************************************************************************
Group 

Project Overview and target area: Global Art Gallery — a digital platform to explore, view, and submit artworks across cultures. Users: artists, enthusiasts, collectors, and cultural professionals.

Cultural Scope: English / Mandarin / Japanese. Ireland (high IDV, low PD), China (low IDV, high PD), Japan (moderate IDV, moderate PD). Dimensions: Hofstede’s Individualism vs Collectivism and Power Distance.

Design Rationale: Three PoV statements (Zhang Ming — formal/prestige; Brian — open submission; Kenji — restrained credibility). Three hypotheses: artist bios improve engagement; tiered navigation raises task completion; labelled mediums boost artist confidence.

Architecture and Structure Overview: Flask app on Render. Shared base.html with block inheritance. Routes: /, /gallery, /painting/<slug>, /artist/<slug>, /events, /submit, /contact. Language switching via /set_language/<locale>, persisted in session.

Internationalisation and Localisation Strategy: Flask-Babel; translation files for en_IE, zh_CN, ja_JP. All user-facing strings wrapped in translation functions. Language switcher in nav bar (base.html), selection stored in session.

Cultural Adaptation Mechanisms: Language — full UI translation across all pages. Tone — formal throughout; no casual or promotional copy. Layout — whitespace-heavy with artist bios prominent on the home page (depth for collectivist users, clarity for Irish). Navigation — curated pathways + open browsing to serve both structured and autonomous expectations. Artwork pages — medium, dimensions, year, description, and artist link on every entry. Colour — neutral whites/blacks/muted tones; red and white-dominant schemes deliberately avoided due to cultural connotations in China and Japan.

<hr>

Individual contributions:
Oleksandr Hroza, C24737185
Subsections:
1.	Home page (Html, CSS, Fully working translations & changing UI based on the language)
Cultural dimensions: Collectivism vs individualism, Low vs High power distance.
Hypothesis implemented: Implementing the artist biography/statement that connect individual stories to the broader cultural context for all users will result in stronger engagement across the three markets.

A personal statement from one of the artists appears on the home page, between featured works and overview of events. 

<hr>

Contributions made by Roshan Kadhiwala [D24125279]

### Pages / Features Implemented

I implemented two main user-facing pages: the Contact page and the Submit Artwork page, with a focus on usability, localization, and culturally aware design.
Contact Page
•	Localized form using translation wrappers for all labels, placeholders, and buttons 
•	Contact-purpose dropdown including an “Other” option with additional input field 
•	Clear contact information panel (hours, response time, phone, email) 
•	Social media section with locale-based visibility logic (hidden for China as these platforms are banned in that region) 
•	Helpful resources panel linking to FAQs, submission guide, and exhibitions 
•	Clean and simple form structure with required inputs 
Submit Page
•	Multi-section artwork submission form: 
o	Artist Information 
o	Portfolio / CV upload 
o	Artwork Details 
•	Required and optional fields clearly defined 
•	File upload controls with: 
o	Accepted formats 
o	File size guidance 
•	Localized success message using Flask flash system 
•	Consent checkbox before submission 
•	Structured layout using headings and separators for clarity 
•	
Routing / Backend Flow
•	GET/POST /contact with form submission handling 
•	GET/POST /submit with flash message + redirect flow 
•	Smooth user interaction with feedback after submission 

Cultural Dimensions Addressed
This implementation was guided by differences between high individualism and low power distance cultures like Ireland and , more collectivist / higher power distance cultures like China and Japan.
1. Individualism (IDV)
•	Users in Ireland typically prefer independence and minimal friction, so: 
o	Forms are straightforward and easy to complete without guidance 
o	Inputs are flexible (e.g., optional fields, “Other” category) 
•	Users in China and Japan often expect more structure and guidance, so: 
o	The submit form is divided into clear sections 
o	Helper text explains what to enter (e.g., artist statement, uploads) 
o	File upload instructions reduce uncertainty 
2. Power Distance (PD)
•	In higher PD cultures (China, Japan), users expect clear authority, structure, and instructions: 
o	Explicit labels, required fields, and step-by-step sections 
o	Consent checkbox reinforces formal process and accountability 
o	Clear submission confirmation builds trust 
•	In lower PD cultures like Ireland: 
o	Tone remains friendly and accessible, not overly formal 
o	Simple layout avoids unnecessary complexity 
Hypotheses Implemented
•	Using localized text helps users feel more confident
o	All labels, placeholders, and messages are translated using _(), so users can interact with the forms in a language they understand, making the experience smoother and more comfortable. 
•	Being transparent helps reduce users leaving the form midway
o	On the Contact page, response times and contact details are clearly shown, so users know what to expect.
o	On the Submit page, a clear success message reassures users that their submission has been received. 
•	 Clear structure and guidance reduce mistakes in complex forms
o	The Submit page is divided into sections with helpful instructions, making it easier to follow.
o	File upload requirements (formats and sizes) are clearly explained, helping users avoid errors before submitting. 
________________________________________
Where These Appear in the UI
Contact Page
•	Header with localized title and description 
•	Input fields: name, email, purpose, message 
•	“Other purpose” conditional input 
•	Contact information card (hours, response time, contact details) 
•	Social media panel (locale-dependent visibility) 
•	Helpful resources section 
Submit Page
•	Header with instructions 
•	Artist Information section 
•	Portfolio / CV upload controls with guidance 
•	Artwork Details section 
•	Artwork upload with constraints 
•	Consent checkbox 
•	Success alert message after submission 
•	Reset and submit buttons 

Justified Deviations from Group Guidelines
•	Locale-based social media visibility
Instead of showing all platforms equally, social links are conditionally displayed based on language/region to improve relevance and avoid clutter. 

<hr>

### Samuel Goldstein (d24125322) Contributions

Implemented the [art.html, artists.html, events.html, base.html, gallery.html, and, painting.html] as well as the correspondent CSS for said pages. Also worked on tweaking the other pages to match the overall aesthetic of the site. Implemented slight UI changed with the language change.



 **Chinese UI Changes:**
Font was changed to one that supports Chinese characters and has the formal, structured stroke style of traditional Chinese print. (Power Distance: formal, authoritative typography reflects China's high power distance culture, where hierarchy and formality are visually communicated.)
Switched to a Red accent (from gold) red symbolizes luck and prosperity in Chinese culture, making it the most culturally appropriate accent color. (Uncertainty Avoidance: using culturally familiar symbols like red reduces ambiguity and creates immediate cultural recognition for the user.)
Heavier font weight that mirrors the bold, confident visual weight of Chinese characters and formal Chinese signage. (Power Distance: bold, commanding visuals reinforce the formal and hierarchical tone expected in professional Chinese contexts.)
Wider letter-spacing that reflects how formal Chinese typography spaces characters generously to convey authority. (Power Distance:  generous spacing signals formality and seriousness, aligning with high power distance expectations.)
Double-line borders like most Chinese decorative framing traditions. 
Added a box-shadow because it appeared in a few Chinese galleries (and I honestly thought it looked nice), after investigating it was found that this is done to mimic Chinese woodblock printing, so it was decided to keep it as a part only for Chinese translation. 

**Japanese UI Changes:**
Font was changed to one that supports Japanese characters and has a noticeably lighter, more elegant stroke than the Chinese variant. (Indulgence vs. Restraint:  the lighter stroke reflects Japan's restrained, understated design culture.)
More line weight + more line-height, reflects ma, the Japanese concept of meaningful empty space and airiness in composition, while our design already somewhat applied this principle as we decided to go for a more minimalist design we found it was still possible to apply "ma". (in essence making our design more minimalistic than it already is). (Individualism vs. Collectivism:  ma as a design principle reflects a collective cultural understanding that silence and space carry meaning, not just content.)
Radius decreased to 0px, the sharp corners are a consistent feature of Japanese design across architecture, print and product design. (Uncertainty Avoidance:  precise, defined edges reflect Japan's high uncertainty avoidance, favoring clarity and exactness over ambiguity.)
Thinned out the borders, the new thinner borders reflect the Japanese value of restraint and understatement (wabi-sabi). (Indulgence vs. Restraint:  thinner borders embody wabi-sabi, the acceptance of impermanence and simplicity over decoration.)
Changed it to a blue accent (from gold) the blue accent is similar to the blue-grey tone of sumi ink used in Japanese calligraphy and ink wash painting.


### Hypotheses implemented:

**Hypothesis 1:**
Artist biography pages were implemented across all three versions of the site. Each artwork page includes an artist card with a photo and a short biography, aswell as a dedicated artist page that expands this into a full story with a portrait of them (currently a tree) and a grid of their works (also currently trees). This supports collectivist audiences in China and Japan who value understanding someone's place within a broader context, as well as the Irish preference for personal connection with the people behind the work.

**Hypothesis 3:**
Every artwork card and painting page across all three versions clearly displays the medium and material beneath the title, with the full painting page also showing the dimensions. This helps prospective artists immediately see their medium represented, removing any uncertainty about whether their work would be welcomed. It also satisfies the preference in Chinese and Japanese cultures for structured, clearly organized information.

<hr>

Additional Sections
Setup Instructions
1.	Install dependencies (e.g., Flask, Flask-Babel) 
2.	Run the Flask application 
3.	Open the app in a browser using the URL provided (typically http://127.0.0.1:5000) 
4.	Navigate to /contact or /submit 

Limitations
•	Form submissions are currently not stored in a database 
•	File uploads are only validated at the UI level 
•	Some translations may require refinement 
•	Social media localization logic is basic and can be expanded 

Future Work
•	Add backend persistence for contact messages and submissions 
•	Implement stronger server-side validation (file size, type, security checks) 
•	Improve translation quality with native speaker review 
•	Enhance locale-based personalization beyond social media 

****************************************************************************************************************************************************************


