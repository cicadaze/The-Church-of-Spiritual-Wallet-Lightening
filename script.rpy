define m = Character("MC")
define e = Character("Eli")
define v = Character("Vivian")
define i = Character("Indy")


transform zoom:
    zoom 1.5


# Opening scene
label start:
    scene cult room
    with fade
    
    "A dimly lit room with deep purple walls and ornate pentagram tapestries. Towering bookshelves line the walls while candles flicker throughout, casting dancing shadows."
    
    "You pace nervously in your clearance robe, checking your phone."
    
    m "(thinking) This community center room looks very promising. The whole mystical aesthetic is definitely going to bring in people. The pentagrams might have been the perfect touch after all."
    
    "You straighten up as footsteps approach."
    
    m "Welcome, seekers! Today begins your journey to enlightenment... and perhaps some strategic wallet lightening for your spiritual benefit."
    
    # Character introductions
    show eli open at center, zoom
    e "Still practicing that mystical voice - very convincing, though you might want to stop checking your phone during sacred moments."
    
    show vivi open at right, zoom
    v "Sorry I'm late! Parking was a nightmare - apparently this neighborhood doesn't have valet service, can you believe that?"
    
    show indy open at left, zoom
    i "The energy here is fascinating - chaotic but with genuine potential underneath all the theatrical elements."
    
    # Group sacrifice ritual
    hide eli
    hide vivi
    hide indy
    
    m "Let's begin with our first ritual - everyone place a sacrifice on the altar and we'll share our spiritual journeys."
    
    "Vivian dramatically drops her diamond ring on the makeshift altar"
    "Indy sits cross-legged in front of the altar in meditation"
    "Eli just leans against the wall, arms crossed"
    
    # Choice menu
    "Who do you talk to first?"
    
    menu:
        "Talk to Eli":
            jump eli_route
        
        "Talk to Vivian":
            jump vivian_route
        
        "Talk to Indy":
            jump indy_route

# Eli's route
label eli_route:
    show eli open at zoom, center
    
    e "(approaching you first) So... how's it feel being a spiritual leader? You look like you're about to throw up."
    
    m "I'm fine! Totally in control of this whole... enlightenment situation."
    
    e "(smirking) Right. Well, for what it's worth, they seem genuinely interested in whatever you're selling."
    
    m "What did you sacrifice for the ritual?"
    
    e "My better judgment, mostly. And maybe my reputation when people find out I helped you start a cult."
    
    m "How did you even know about this... spiritual endeavor?"
    
    e "(dryly) Are you seriously asking me how I knew about the cult I helped you plan?"

    e "I made the flyers, remember? Posted them all over social media? Spent three weeks listening to you practice your 'mystical leader' voice?"
    
    menu:
        "Right... thanks for believing in me when I didn't believe in myself.":
            jump ending
        
        "I couldn't have done this without you.":
            jump ending

# Vivian's route
label vivian_route:
    show vivi open at zoom, center
    
    v "(bouncing over excitedly) Oh my god, this is so much more authentic than my meditation retreat in Bali! You have like, real candles and everything! Though we should definitely talk about upgrading the interior design."
    
    m "I'm glad you're... enjoying the ambiance."
    
    v "The aesthetic is very 'mysterious cult chic' - I love it! But okay, business talk - what's your donation structure like? Because I'm thinking of making this a regular thing and I want to budget appropriately."
    
    m "(suddenly very interested) Donation... structure?"
    
    v "Well yeah! I mean, my life coach charges $800 an hour, my spiritual advisor in Monaco was $2000 per session, and don't even get me started on what I paid for that ayahuasca retreat in Peru. So what's your rate for enlightenment?"
    
    m "What did you sacrifice in our ritual?"
    
    v "My family ring! It's worth like, $50,000 - honestly it clashed with most of my outfits anyway. Plus I can always get daddy to buy me a new one if I want. But don't worry, I brought my checkbook for the real donations!"
    
    m "(heart racing) And how did you hear about our spiritual community?"
    
    v "Your flyer at the coffee shop! Well, technically my driver saw it, but whatever."

    v "It said 'Wallet Lightening' and I thought finally, someone who understands that money is just energy that needs to flow!" 

    v "Plus I was SO bored - I'd already redecorated my penthouse twice this month and bought everything worth buying from the new Chanel collection."
    
    m "(thinking) Holy shit. She's treating this like her latest expensive hobby, but she's talking about throwing serious money around." 

    m "This could be the easiest scam of my life... but why do I suddenly feel weird about taking advantage of someone who's just bored?"
    
    menu:
        "We're always open to... generous spiritual investments.":
            jump ending
        
        "So this is expensive entertainment for you..?":
            jump ending

# Indy's route
label indy_route:
    show indy open at zoom, center
    
    i "(speaking calmly as you approach) You're more nervous than you're letting on."

    i "That's refreshing - most spiritual leaders I've met are either totally confident or totally fake."
    
    m "Just... processing the energy of our new spiritual family."
    
    i "Mmm. The energy is definitely complex. You're all very different people with very different motivations."
    
    m "What did you sacrifice today?"
    
    i "My preconceptions. I'm trying to let go of what I think this should be and just experience what it actually is."

    i "Also my need to be the wisest person in the room - that's an old habit."
    
    m "How did you find out about us?"
    
    i "Your flyer was at Sacred Grounds where I work as a barista."

    i "I've been to six different spiritual communities in the past few years - most felt performative. But something about 'Church of Spiritual Wallet Lightening' made me think you either had an incredible sense of humor or were refreshingly honest about the business side of spirituality."
    
    menu:
        "Which do you think it is?":
            jump ending
        
        "You've been to six other places? What made them different?":
            jump ending
        
        "You work at a coffee shop but seek enlightenment?":
            jump ending

# Ending scene (all routes converge here)
label ending:
    show eli open at left, zoom
    show vivi open at zoom, center
    show indy closed at right, zoom
    
    m "(addressing the group) Thank you all for sharing your sacrifices and your journeys here. This is just the beginning of our spiritual exploration together."
    
    show vivi smug at zoom
    v "So we're definitely doing this again tomorrow, right? I have so many more things I could sacrifice! Most of my stuff from last month is soooooo out of fashion anyway."
    
    show indy open at zoom
    i "I'd like to continue exploring what we're building here."
    
    show eli open at zoom
    e "(quietly) Same time tomorrow then... oh mystical one."
    
    hide eli
    hide vivi
    hide indy
    with dissolve
    
    "As they prepare to leave, you're left alone with your thoughts and a pile of expensive sacrifices on your makeshift altar."
    
    m "(thinking) What did I just get myself into? They're not just throwing money at me - they're throwing pieces of themselves. Eli's loyalty, Vivian's boredom-driven generosity, Indy's genuine spiritual seeking..."
    
    "You look around the candlelit room that somehow felt sacred for a moment."
    
    m "(thinking) Tomorrow's going to be interesting."
    
    # End of Act 1 - Coming Soon message
    scene black
    with fade
    
    centered "{size=+20}{color=#d4af37}END OF ACT 1{/color}{/size}"
    
    centered "{size=+10}{color=#b8860b}🔮 COMING SOON: ACT 2 🔮{/color}{/size}"
    
    centered "THE INDIVIDUAL ROUTES"
    centered "- ELI'S ROUTE: Childhood secrets and hidden feelings revealed"
    centered "- VIVIAN'S ROUTE: Learning what money can't buy"
    centered "- INDY'S ROUTE: Discovering authentic spirituality together"
    
    centered "{color=#d4af37}Your choices will determine the fate of the Church of Spiritual Wallet Lightening{/color}"
    
    return
