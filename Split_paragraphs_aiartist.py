import re

input_paragraph ="""The postmaster first took up his duties in the village of Ulapur. Though the village was a small one, there was an indigo factory near by, and the proprietor, an Englishman, had managed to get a post office established.

Our postmaster belonged to Calcutta. He felt like a fish out of water in this remote village. His office and living-room were in a dark thatched shed, not far from a green, slimy pond, surrounded on all sides by a dense growth.

The men employed in the indigo factory had no leisure; moreover, they were hardly desirable companions for decent folk. Nor is a Calcutta boy an adept in the art of associating with others. Among strangers he appears either proud or ill at ease. At any rate, the postmaster had but little company; nor had he much to do.

At times he tried his hand at writing a verse or two. That the movement of the leaves and the clouds of the sky were enough to fill life with joy—such were the sentiments to which he sought to give expression. But God knows that the poor fellow would have felt it as the gift of a new life, if some genie of the Arabian Nights had in one night swept away the trees, leaves and all, and replaced them with a macadamised road, hiding the clouds from view with rows of tall houses.

The postmaster's salary was small. He had to cook his own meals, which he used to share with Ratan, an orphan girl of the village, who did odd jobs for him.

When in the evening the smoke began to curl up from the village cowsheds, and the cicalas chirped in every bush; when the mendicants of the Baül sect sang their shrill songs in their daily meeting-place, when any poet, who had attempted to watch the movement of the leaves in the dense bamboo thickets, would have felt a ghostly shiver run down his back, the postmaster would light his little lamp, and call out "Ratan."

Ratan would sit outside waiting for this call, and, instead of coming in at once, would reply, "Did you call me, sir?"

"What are you doing?" the postmaster would ask.

"I must be going to light the kitchen fire," would be the answer.

And the postmaster would say: "Oh, let the kitchen fire be for awhile; light me my pipe first."

It seemed as though the showers of the season would never end. Canals, ditches, and hollows were all overflowing with water. Day and night the patter of rain was heard, and the croaking of frogs. The village roads became impassable, and marketing had to be done in punts.

One heavily clouded morning, the postmaster's little pupil had been long waiting outside the door for her call, but, not hearing it as usual, she took up her dog-eared book, and slowly entered the room. She found her master stretched out on his bed, and, thinking that he was resting, she was about to retire on tip-toe, when she suddenly heard her name—"Ratan!" She turned at once and asked: "Were you sleeping, Dada?" The postmaster in a plaintive voice said: "I am not well. Feel my head; is it very hot?"

In the loneliness of his exile, and in the gloom of the rains, his ailing body needed a little tender nursing. He longed to remember the touch on the forehead of soft hands with tinkling bracelets, to imagine the presence of loving womanhood, the nearness of mother and sister. And the exile was not disappointed. Ratan ceased to be a little girl. She at once stepped into the post of mother, called in the village doctor, gave the patient his pills at the proper intervals, sat up all night by his pillow, cooked his gruel for him, and every now and then asked: "Are you feeling a little better, Dada?"

It was some time before the postmaster, with weakened body, was able to leave his sick-bed. "No more of this," said he with decision. "I must get a transfer." He at once wrote off to Calcutta an application for a transfer, on the ground of the unhealthiness of the place.

Relieved from her duties as nurse, Ratan again took up her old place outside the door. But she no longer heard the same old call. She would sometimes peep inside furtively to find the postmaster sitting on his chair, or stretched on his bed, and staring absent-mindedly into the air. While Ratan was awaiting her call, the postmaster was awaiting a reply to his application. The girl read her old lessons over and over again,—her great fear was lest, when the call came, she might be found wanting in the double consonants. At last, after a week, the call did come one evening. With an overflowing heart Ratan rushed into the room with her—"Were you calling me, Dada?"

The postmaster said: "I am going away to-morrow, Ratan."

"Where are you going, Dada?"

"I am going home."



"When will you come back?"

"I am not coming back."

"""

finalList = []

output = re.split('\n',input_paragraph)


counter = 0
word_counter_para = ""
paragraph_limit = 400
for para in output:
    counter = counter + len(para.split())
    word_counter_para = word_counter_para+para
    if counter >=paragraph_limit:
        finalList.append([word_counter_para,counter])
        counter = 0
        word_counter_para=""


for each in finalList:
    print (each)