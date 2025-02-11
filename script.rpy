#Voici le script python de notre jeu !

# Celle-ci suit un ordre chronologique, se référer à la documentation et au scénario du google document.
# https://docs.google.com/document/d/1HDw3mW9NIu5vepDeZaQeyRIbAjHawILjSqCUIB48f1c/edit?usp=sharing

# Personnages du jeu :
define i = Character('Isidore', color="#1192fc")
define s = Character('Sao Mai', color="#f53528")
define al = Character('Mr Al Badre', color="#1c5e14")
define la = Character('La Classe', color="#24830f")
define l = Character('Mr Loyer', color="#794883")
define o = Character('Océane', color="#b02dfc")
define p = Character('Perrine', color="#ff54f1")
define e = Character('Evan', color="#1f13c2")
define ig = Character('Igor', color="#12da1c")
define si = Character('Isidore et Sao Mai', color="#eed70d")

# Le jeu commence ici
label start:
    #On initie les valeurs affectant tout le jeu : la police d'écriture et les boîtes de dialogue.

    #Intro
    scene black
    show text "Isidore et Sao Mai vous présente..." with dissolve
    $ renpy.pause(1.0)
    show text "Un jeu vidéo..." with dissolve
    $ renpy.pause(1.0)
    show text "...sur Ren'Py." with dissolve
    $ renpy.pause(1.0)
    hide text with dissolve

    #Le vrai jeu commence
    scene bg classroom
    s "Aïeuh !"
    show sao confus at left with easeinright
    show isi neutral at right with easeinleft
    show isi surpris
    i "Tu t’es fait mal en dormant ?"
    show sao embarras
    s "Ouais j’ai glissé… "
    show isi neutral
    al "Monsieur Isidore, Mademoiselle Sao Mai. Vous avez terminé vos exercices ?"
    show sao surpris
    s "(Merde j’ai rien fait)"

menu:
    "oui":
        jump yes

    "non":
        jump no

label yes:
    show sao fier
    show isi fier
    al "Ah oui ? Et les autres ?"
    la "Nan monsieur."
    al "Ahh et bah alors, qu’attendez-vous ?"
    show sao dout
    s "T’as vraiment fait les exo ?"
    show isi embarras
    i "Non j’ai pas compris."
    show sao confus
    s "J’ai même pas lu l’énoncé, on est à quelle question là ?"
    show isi neutral
    i "Faut faire la 1, la 2 et la 4, sur les probabilités."
    s "Et merde."
    show sao neutral
    s "Autant les faire à deux."
    scene black
    with dissolve
    jump numbers_game

label no:
    show sao embarras
    show isi embarras
    al "Ah oui ? Et les autres ?"
    la "Nan monsieur."
    al "Ahh et bah alors, qu’attendez-vous ?"
    show isi colere
    i "En même temps tu dormais donc-"
    show sao colere
    s "Ta gueule."
    show sao embarras
    i "Tu sais au moins où est-ce qu’on en est ?"
    jump chapitre

menu chapitre:
    "logarithme ":
        jump logarithme

    "exponentielle":
        jump exponentielle

label logarithme:
    show sao confus
    i " T’es en retard de deux chapitres."
    show isi fier
    i " Même moi je suis plus à jour sur One Piece."
    show sao colere
    s " Aucun rapport."
    show isi neutral
    i "Bref là on est sur les probabilités."
    show sao dout
    s "Ah c’est chiant ça…"
    show sao neutral
    s "Autant faire l’exo ensemble."
    scene black
    with dissolve
    jump numbers_game

label exponentielle:
    show sao confus
    i " T’es en retard de deux chapitres."
    show isi fier
    i " Même moi je suis plus à jour sur One Piece."
    show sao colere
    s " Aucun rapport."
    show isi neutral
    i "Bref là on est sur les probabilités."
    show sao dout
    s "Ah c’est chiant ça…"
    show sao neutral
    s "Autant faire l’exo ensemble."
    scene black
    with dissolve
    jump numbers_game

# ---------------------  Écran du jeu  --------------

transform roto_transform(roto_var):
    rotate roto_var
    rotate_pad False

screen numbers_scr:
    # on désactive les touches pour n'avoir que la souris

    key "K_LEFT" action Hide("nonexistent_screen")
    key "K_RIGHT" action Hide("nonexistent_screen")
    key "K_UP" action Hide("nonexistent_screen")
    key "K_DOWN" action Hide("nonexistent_screen")
    key "K_RETURN" action Hide("nonexistent_screen")
    key "K_KP_ENTER" action Hide("nonexistent_screen")

    # minuteur
    timer 1 action [

        Return("smth"),
        If(game_timer > 1,
            If(max(numbers_buttons.values(), key=lambda x: x["b_number"])["b_to_show"] == False,
                Return("win"),
                SetVariable("game_timer", game_timer - 1)
            ),
            Return("lose")
        )
    ] repeat True

    text "[game_timer]" size 25 xpos 10 ypos 10

    for each_b in sorted(numbers_buttons.values(), key=lambda x: x["b_number"], reverse=True):
        if each_b["b_to_show"]:
            $ text_var = each_b["b_value"]
            $ i = each_b["b_number"] - 1

            button:
                text '[text_var]{size=18}.{/size}' size 30 align (0.5, 0.55) color "#000"
                xminimum 100 xmaximum 100
                yminimum 100 ymaximum 100
                xpos each_b["b_x_pos"]
                ypos each_b["b_y_pos"]
                background Solid("#e6e1e1")  # Ajout d'un fond blanc pour la visibilité
                anchor (0.5, 0.5)
                action If(i < 0 or numbers_buttons.get(i, {}).get("b_to_show", False) == False,
                    SetDict(numbers_buttons[each_b["b_number"]], "b_to_show", False),
                    SetVariable("game_timer", game_timer - 1)
                )  # La mauvaise clic réduit le temps restant de 1 seconde
                at roto_transform(renpy.random.randint(0, 10) * 36)

    # affichage de l'ordre des boutons à cliquer
    side "c b":
        area (150, 05, 640, 70)  # Taille de la zone d'indice
        viewport id "vp":
            draggable True
            hbox:
                xalign 1.0
                for each_b in sorted(numbers_buttons.values(), key=lambda x: x["b_number"]):
                    $ text_var = each_b["b_value"]
                    button:
                        text '[text_var]{size=18}.{/size}' size 30 align (0.5, 0.55) color "#000"
                        xminimum 100 xmaximum 100
                        yminimum 100 ymaximum 100
                        background Solid("#ccc9c9")  # Ajout d'un fond blanc pour la visibilité
                        action If(each_b["b_to_show"], Hide("nonexistent_screen"), None)
                        at Transform(zoom=0.5)  # Taille
        bar value XScrollValue("vp")

label numbers_game:
    # Taille de l'écran de jeu
    $ screen_width = config.screen_width
    $ screen_height = config.screen_height
    # Génération des valeurs pour les boutons
    $ numbers_buttons = {i: {"b_number": i, "b_value": str(i), "b_x_pos": renpy.random.randint(200, screen_width - 200), "b_y_pos": renpy.random.randint(200, screen_height - 200), "b_to_show": True} for i in range(1, 21)}
    "Cliquez sur les boutons dans l'ordre croissant (commencez par \"1\")."
    "Attention, vous n'avez que 25 secondes ! Chaque mauvais clic vous retire une seconde."
    window hide

    # on met un timer de 25 secondes
    $ game_timer = 25
    # on montre les numéros (l'écran du jeu)
    show screen numbers_scr

    # une boucle pour que le jeu ne s'arrête pas
    label loop:
        $ result = ui.interact()
        if result == "smth":
            jump loop

    if result == "lose":
        hide screen numbers_scr
        "Oh non !"
        jump loi_bino

    if result == "win":
        hide screen numbers_scr
        "Gagné !"
        jump loi_bino

label loi_bino :
    scene bg classroom
    with dissolve
    show sao dout at left
    with dissolve
    show isi neutral at right
    with dissolve
    s "Tu te rends compte qu’on termine à 18h30, que c’est une option et que ça nous baisse la moyenne ?"
    show isi happy
    i "Oui."
    show sao embarras
    show isi neutral
    s "En plus j’ai rien compris à la loi Binominale."
    i "Binomiale."
    show sao surpris
    s "Binominale."
    show isi surpris
    i "Binomiale."
    show sao dout
    s "Binominale."
    show isi question
    i "Binomiale."

menu:
    "Binomiale":
        jump Binomiale

    "Binominale":
        jump Binominale

label Binomiale:
    show isi fier
    show sao neutral
    i "Voilà ! Binomiale !"
    show sao happy
    s "Bi"
    s "No  "
    s "Mi"
    s "Ale"
    show isi happy
    i "C’est ça !"
    show sao fier
    s "Binominale !"
    show isi colere
    i "Laisse tomber…"
    jump Oscaaar

label Binominale:
    show sao happy
    show isi confus
    s "Ah bah tu vois, toi même tu le dis"
    i "Merde."
    i"Tu m’as perdu !"
    show sao fier
    s "C’est un de mes talents."
    show sao neutral
    show isi question
    s "Au moins ça te fait un point commun avec Zoro."
    jump Oscaaar

label Oscaaar:
    show sao neutral
    show isi neutral
    al "Oscaaaar…"

    menu:
        "Tais toi !!!":
            show sao happy
            show isi happy
            la "Tais toi !!!"
            scene black
            with dissolve
            jump id_projet

        "...":
            al "Tais toi !"
            scene black
            with dissolve
            jump id_projet

#Nous inition des valeurs booléennes à chaque choix afin de les retirer une fois sélectionné 

init:
    $ Site_disponible = True
    $ Appli_disponible = True
    $ I_A_disponible = True
    $ Jeu_disponible = True 

label id_projet:
    scene illu findescours
    with dissolve
    i "Au fait, t’as réfléchi pour le projet de troisième trimestre ?"
    s "En NSI ? En vrai…"
    s "Comme on n’a aucune contrainte, on a trop de liberté…"
    i "Ouais c’est vrai, on peut faire tellement de truc."
    i "On peut faire un site, une application, une I.A., un jeu…"
    s "Attends t'as dit quoi là ?"
    i "Hein ?"
    s "Répètes c’que t’as dit ?"
    jump choice 

label choice:
    # Utilisation d'une boucle while pour afficher le menu tant que le choix "Jeu" n'a pas été sélectionné
    while Jeu_disponible:
        menu:
            "Site" if Site_disponible == True:
                    $ Site_disponible = False
                    s "Non pas ça !"

            "Appli" if Appli_disponible == True:
                    $ Appli_disponible = False
                    s "Non pas ça !"

            "I.A" if I_A_disponible == True :
                    $ I_A_disponible = False
                    s "Non pas ça !"
 
            "Jeu" if Jeu_disponible:
                    $ Jeu_disponible = False
                    jump jeu

label jeu:
    s "Oui !"
    s "C’est ça ! C’est super comme idée !"
    i "Une idée digne du grand Satoru Gojo."
    s "Arrête avec toutes tes références de manga !!"
    scene black
    with dissolve

    jump soirée

label soirée:

    scene illu maison
    "Et c’est ainsi qu’Isidore et Sao Mai se lancèrent sur la création d’un jeu-vidéo pour leur projet de NSI…"
    "Ou du moins le rêve d’un jeu vidéo."
    "La journée du lundi fût longue et épuisante et les deux ont bien mérité un peu de repos."
    "Si ce soir ils dorment sur leur deux oreilles, sans crainte de savoir dans quoi ils venaient de s’embarquer, ce ne sera plus le cas plus tard."
    "Leurs choix et actions peuvent être sans importance pour l’instant, mais la chose la plus anecdotique peut, par un effet boule de neige, devenir la chose déterminante dans l’histoire."
    "Laissons les profiter de leur temps libre tant qu’ils en ont encore."
    "Voyez avec quels activités chacun s’occupe. Préfériez-vous…"

    menu:
        "Regarder Youtube":
            jump Youtube
        "Lire un livre":
            jump lecture

label Youtube:
    "Ahh ! Quoi de mieux que de se poser dans son canapé et de regarder la télé ?"
    "Les heures défilent sans qu’on ne s’en rende compte au point où l’on peut oublier de manger !"
    scene illu youtube
    "Sao Mai oublie souvent de manger à cause de ça, en plus de s’éclater les yeux."
    "Une bonne distance permet une meilleure perception des couleurs d’un écran, alors restez à l’écart !"
    "Reposons-nous maintenant avant de dormir en cours de philosophie."
    scene black
    with dissolve
    jump Mardi

label lecture:
    "Un manga ça reste un livre, non ?"
    "Qui n’aime pas lire un, deux, cinq, sept, douze chapitres d’une histoire passionnante aux personnages charismatiques entièrement illustrée ?"
    scene illu livre
    "Isidore vous recommande de lire One Piece."
    "Il vous le recommande grandement."
    "Mais genre beaucoup."
    "Allons vite dormir avant qu’il ne commence à vous expliquer les arcs !"
    scene black
    with dissolve
    jump Mardi

### Mardi ----------------------------------------------------


init:
        $ Océane = True
        $ Evan = True
        $ Igor = True
        $ Perrine = True
        $ Jai_terminé = True

label Mardi:

    scene bg nsi
    with dissolve

    show testloyer neutre
    with dissolve
    l "Bonjour les terminales NSI."
    l "Aujourd’hui comme nous en avons discuté la semaine dernière,vous allez pouvoir commencer à travailler sur votre projet."
    l "Je vous laisse libre là-dessus, mais ayez de l’ambition !"
    l "Je vais faire mes petites visites habituelles histoire de voir un peu comment ça se passe dans chaque groupe alors…"
    hide testloyer neutre
    with dissolve

    show sao neutral at left with easeinright
    show isi neutral at right with easeinleft
    show isi happy
    i "Bon, faut qu’on se mette au travail !"
    show sao surpris
    s "Attend, faut déjà qu’on développe plus notre idée !"
    show isi question
    i "Comment ça ? On fait un jeu, non ?"
    show sao dout
    s "Mais quelle forme, genre de jeu, quels langages de programmation !"
    show sao fier
    s "Python, Pygame, Tkinter, HTML et CSS… Tant de possibilité mais un seul projet à rendre !"
    show isi embarras
    i "Je vois, c’est vrai que c’est vaste la NSI, même si on a déjà choisi de faire un jeu…"
    show sao embarras
    s "Le dernier projet d’Igor et Amel était incroyable par exemple, mais s’ils l’ont présenté en projet de second trimestre, on doit être capable de faire mieux que ça au troisième !"
    show sao happy
    show isi surpris
    s "Et si on allait voir les autres groupes pour voir ce qu’ils ont prévu de faire ? Ça nous évitera qu’on fasse doublon."
    show isi happy
    i " Excellente idée ! On commence par qui ?"
    show sao neutral
    show isi neutral

menu visites:
        "Océane" if Océane == True:
                    $ Océane = False
                    jump Océane

        "Evan" if Evan == True:
                    $ Evan = False
                    jump Evan

        "Igor" if Igor == True:
                    $ Igor = False
                    jump Igor

        "Perrine" if Perrine == True:
                    $ Perrine = False
                    jump Perrine

        "J'ai terminé" if Jai_terminé == True:
                    $ Jai_terminé = False
                    jump echanges

label Océane:
    hide isi neutral
    with easeinleft
    show oce lazy at right with easeinright
    show sao happy
    s "Coucou Océane ! Ça avance votre projet ?"
    show oce neutral
    o "Salut Sao ! Eh bah écoute il avance doucement, tranquille."
    show oce neutral
    o "Avec Telmo et Milo on a vu ce qui marchait bien dans les projets du deuxième trimestre. On a pioché un peu partout."
    show sao surpris
    s "Ah ouais ? C’est quoi ?"
    show sao dout
    show oce fier
    o "Ah non par contre c’est secret ! C’est notre dernier projet alors c’est mieux si vous avez la surprise…"
    s "T’abuses tu peux pas me laisser sur un tel trailer !"
    show oce happy
    o "Haha ! Arrête de dire n’importe quoi !"
    show oce lazy
    o "Bon de toute façon, t’es assise derrière moi. Je pourrais pas t’empêcher indéfiniment de regarder mon écran."
    show sao surpris
    show oce happy
    o "On compte faire un casino !"
    show sao happy
    show oce excited
    s "THE BLACK JACK !"
    o "THE BLACK JACK !!"
    s "THE BLACK JACK !!!"
    show oce happy
    o "Haha ! Mais oui en gros ça serait un casino avec un système de parie, comme des vrais jeux d’argent. On compte faire un site web."
    show sao neutral
    show oce neutral
    s "Mais ça a l’air incroyable ! Un projet bien stylé en tout cas."
    show oce fier
    o "Pas aussi stylé que votre pokédex."
    show sao fier
    s "Pas aussi stylé que ta personne."
    show oce happy
    o "Oh arrête tu vas me faire rougir !"
    s "Hahaha !"
    hide oce happy
    with easeinleft
    show isi neutral at right with easeinright
    show sao neutral
    s "Alors ? T’en as pensé quoi ?"
    show isi question
    i "Ça donne à réfléchir…"
    show sao dout
    s "Oui mais est-ce que ça t’aide à trouver de l’inspiration ?"
    i "Mmh…. Je pense que…."
    jump visites

label Perrine:
    hide sao neutral
    with easeinright
    show testper neutral at left with easeinright
    show isi happy
    i "Hey ! C’est quoi votre projet pour le dernier trimestre ?"
    p "Salut ! Alors nous on a prévu de construire une console portable du style GameBoy."
    i "C’est une trop bonne idée ! Votre projet est super original."
    i "Du coup vous allez faire comment pour assembler ?"
    p "Bah on va acheter tous les composants puis on va les souder entre eux afin de construire la console."
    i "OK. Donc votre projet est un peu orienté réseaux."
    p "Pas seulement. "
    p "En plus de la fabrication de la console on a prévu de créer un petit jeu et de l’importer, comme ça on pourra y jouer."
    i "Ah ouuuuaaaaiiis ! C’est incroyable !"
    i "En fait vous êtes vraiment dans le peau des constructeurs et ça va vous permettre de découvrir un tout autre aspect du milieu du jeu vidéo et des consoles."
    p "On a mis pas mal de temps à trouver une idée de projet."
    p "Mais maintenant que l’on a trouvé celle là on va se donner à fond sur le dernier projet que l’on va réaliser au lycée."
    hide testper neutral
    with easeinleft
    show sao neutral at left with easeinright
    show isi neutral
    s "Alors ? T’en as pensé quoi ?"
    show isi question
    i "Ça donne à réfléchir…"
    show sao dout
    s "Oui mais est-ce que ça t’aide à trouver de l’inspiration ?"
    i "Mmh…. Je pense que…."
    jump visites     


label Igor:
    hide sao neutral
    with easeinright
    show testper neutral at left with easeinright
    show isi happy
    i "Salut ! Alors vous avez prévu de faire quoi comme projet ?"
    ig "Salut, avec mon p’tit Amel on va faire un serveur Minecraft avec divers mini-jeux."
    i "C’est vraiment sympa, mais c’est pas trop compliqué à faire ?"
    ig "Non c’est assez simple à faire, le plus dur c’est d’héberger notre projet sur un VPS pour que vous ayez la possibilité de tester notre projet tous en même temps."
    i "C’est quoi un … VPS ?"
    ig "Un VPS c’est un serveur virtuel qui fonctionne avec son propre système d’exploitation et ses propres ressources, il va nous permettre d’héberger notre serveur Minecraft et  va donc avoir la même utilité qu’un serveur physique."
    i "OK, ça n’a pas l’air simple mais en même temps vous êtes tellement fort    en informatique que pour vous c’est du gâteau de faire ça."
    ig "Ouais c’est ça, après on s’est beaucoup documentés sur le sujet quand même afin de savoir ce que l’on faisait."
    i "Vous utilisez quoi comme langage de programmation du coup ? Car je suppose que c’est pas avec du Python que vous gérez le bon fonctionnement de votre serveur."
    ig "On utilise Python et Java pour le gros de la programmation, MySQL pour notre base de données et le Batch on l’utilise pour automatiser notre système et gérer les processus répétitifs."
    i "Ah bah oui.. Vous utilisez forcément Java pour un serveur Minecraft."
    i "Et donc c’est quel type de mini-jeux que vous avez fait ?"
    ig "On a fait un FFA donc un mini-jeu de combat où l’objectif est d’être le dernier survivant, un Pitchout, là l’objectif est de faire tomber les autres joueurs de la plateforme où vous vous trouvez et un dé à coudre."
    i "C’est trop cool le dé à coudre ! C’est le jeu où tu sautes dans une zone d’eau et à chaque tentative il y a des blocs qui apparaissent et il faut les éviter."
    ig "Tout à fait, en plus on a réussi à automatiser l'apparition des blocs doc les joueurs n’ont pas besoin de poser eux-même leur blocs après chaque essais."
    i "Votre projet il claque, j’ai trop hâte de voir le rendu final. "
    ig "Merci. Bon courage à vous aussi pour terminer votre projet."
    hide testper neutral
    with easeinleft
    show sao neutral at left with easeinright
    show isi neutral
    s "Alors ? T’en as pensé quoi ?"
    show isi question
    i "Ça donne à réfléchir…"
    show sao dout
    s "Oui mais est-ce que ça t’aide à trouver de l’inspiration ?"
    i "Mmh…. Je pense que…."
    jump visites  


label Evan:
    hide isi neutral
    with easeinleft
    show testper neutral at right with easeinright
    show sao happy
    s "Yo ! Alors ça avance votre projet ?"
    e "Oui ça avance comme on veut."
    s " Euh... C'est quoi déjà votre projet ?"   
    e " On fait une machine d'arcade avoir plusieurs jeux disponibles dessus."
    s "C'est sympa comme projet de fin de lycée."
    e " Ouais, avec Rose et Tiago on a voulu placer la barre haute pour ce dernier projet !"
    s " Vous la faites vous même la structure de la console ?"
    s "Parce que ça demande beaucoup de taff."
    e "On fait ça nous même, la structure de la borne on la fabrique avec une imprimante 3D et une fois que ce sera fait on montera le tout avec les boutons et les joysticks que l'on a achetés."
    s "Stylé !! Il en jette votre projet."
    s "Comment vous faites pour les jeux, vous en créer vous même ou c'est un peu chaud d'implémenter le tout ?"
    e "On utilise un Raspberry Pi qui permet l'émulation de jeu, créer nos propres jeux aurait demandé trop de temps."
    s "J'ai hâte de voir le rendu final, là tu me vends du rêve."
    hide testper neutral
    with easeinleft
    show isi neutral at right with easeinright
    show sao neutral
    s "Alors ? T’en as pensé quoi ?"
    show isi question
    i "Ça donne à réfléchir…"
    show sao dout
    s "Oui mais est-ce que ça t’aide à trouver de l’inspiration ?"
    i "Mmh…. Je pense que…."
    jump visites  
 

label echanges:

    show isi happy
    show sao happy
    s "Super on va enfin pouvoir commencer notre projet !!"
    i "Oui mettons nous au travail. Réaliser un projet…… "
    i "C’est follement excitant comme dirait Onizuka !!"
    show sao dout
    s "De GTO ?"
    show sao colere
    s "Quel est le rapport ?"
    show sao dout
    show isi embarras
    i "Ah oui pardon, comme dirait Senku de Dr Stone."
    show isi happy
    i "Je te donne un million de points pour cette bonne réponse !!"

    menu:
        "Frapper Isidore":
            show sao colere
            show isi confus
            "Aie !! Ça fait mal !"
            jump pensées

        "Ignorer Isidore":
            show sao dout
            show isi neutral
            jump pensées

label pensées:
    show sao neutral
    show isi neutral
    s "Bon. Revenons à nos moutons."
    i "Oui ! Les projets."
    show sao fier
    s "J'ai pas mal d'idées de jeux que l'on pourrait faire et toi ?"
    show isi fier
    show sao neutral
    i "Moi aussi j'en ai quelques unes."

   

label projet:
    show isi neutral
    show sao fier
    "Sao Mai et Isidore ont tout deux beaucoup d'idées de jeux, lesquelles veux tu voir ? "
    menu:
        "Voir les idées de Sao Mai":
            show sao happy
            s "Un RPG !"
            show isi question
            i "Un RPG ?"
            show sao fier
            s "Bien sûr ! Je n’joue qu’à ça !"
            show sao happy
            s "Si je fais un jeu, c’est forcément un RPG !"
            i "C’est quoi ça déjà, “Rôle Play Game” quelque chose comme ça ?"
            show isi neutral
            s "C’est ça ! Un RPG est un jeu où l’on incarne un personnage."
            show isi question
            i "Mais on joue forcément un personnage dans un jeu, donc tous les jeux seraient des RPG ?"
            show sao fier
            s "Nuh-uh !"
            show sao neutral
            s "Il y a une différence entre “contrôler” et “incarner”."
            show sao dout
            s "Tu “n’incarne pas” le serpent dans Snake ou le vaisseau dans Space Invaders… Tu le contrôles juste."
            show sao neutral
            s "En vérité le terme “RPG” réfère plus à des mécaniques de jeu, s’inspirantdes jeux de rôle sur table tel que Donjons & Dragons."
            i "Donjons & Dragons ?"
            show sao fier
            s "On va y retrouver des systèmes de statistique, d’inventaire, de combat et surtout !"
            show sao happy
            s "Une narration complexe et au coeur du jeu !"
            show sao neutral
            s "Il est très fortement liée à la littérature de l’imaginaire, ou en anglais “speculative fiction”, permettant au joueur de faire des choses ou de découvrir une histoire qu’il n’aurait jamais pu faire autrement que par la fiction !"
            show isi confus
            i "Attends, t’es en train de me perdre !"
            show sao happy
            s "Le genre du RPG est un genre vaste, si ce n’est le genre le plus vaste du jeu-vidéo !"
            show sao fier
            s "De Zelda à NEO Scavenger, du médiéval au futuriste… Son oeuvre la plus célèbre est le fameux “Final Fantasy 7” sortie en 1997 sur Playstation 1 et ordinateurs !"
            s "Final Fantasy 7 marque un tournant dans l’histoire du jeu-vidéo et dans son influence mondiale. Il est le pilier du genre bien qu’il ne soit pas le premier."
            s "Dans une perspective eschatologique, le jeu présente de l’exploration, des combats et des personnage dans une narration simplement sublime égalent les plus grands romans d’aventure et de tragédie, l’épopé d’un héros : le joueur."
            s "La narration évolue. Ses personnages grandissent et changent en fonction des choix, des actions et des événements présents dans le jeu."
            show sao happy
            s "Final Fantasy 7 est-"
            show isi colere
            i "Rhaaaa tais-toi !!"
            show sao embarras
            s "…"
            show isi embarras
            i "…"
            s "Ce que je veux dire avec les RPG-"
            show isi colere
            i "…"
            s "…C’est que j’adore les RPG."
            show sao dout
            i "Bon."
            show isi question
            i "Et quel genre de RPG ?"
            show sao happy
            s "Alors les différents sous-genre des RPG-"
            show isi colere
            i "Tais-toi !!"
            show sao dout
            s "Faisons simple : des pirates ou des chevaliers ?"

            menu:
                "Des pirates":
                    show sao happy
                    s "Des pirates ! Mon frère est fan de pirate !"
                    show isi question
                    i "Celui qui a un chapeau de pirate et des sculptures de requins dans sa chambre ?"
                    show sao dout
                    s "C’est sûr que c’est pas celui qui a figurine d’anime aux jupes un peu trop courtes."
                    show sao surpris
                    i "Quoi ?"
                    show sao surpris
                    s "Quoi ?"
                    show sao dout
                    show isi embarras
                    i "…"
                    show isi neutral
                    i "Bref ouais des pirates c’est pas mal ! On pourra faire des batailles navales, des équipages ! Chasse aux trésors, rivalité et amitié…"
                    show isi happy
                    show sao happy
                    i "The One Piece is Real !!"
                    s "The One Piece is Real !!"
                    show sao neutral
                    s "Le jeu le plus populaire avec des pirates, en ce moment et dans l’histoire du jeu-vidéo, je pense pouvoir aisément dire que c’est “Sea of Thieves”, de Rare, sortie en 2018."
                    show isi question
                    i "Rare ? C’est quel studio ça ?"
                    show isi neutral
                    s "Rare ou Rareware, peu importe le nom c’est le même studio ! Les mêmes que Banjo & Kazooie pardi !"
                    s "Donkey Kong Country, Star Fox ou Viva Piñata… Ils sont pionniers dans les jeux en 3D !"
                    show sao surpris
                    s "D’ailleurs, un des plus gros challenge des jeux de pirate en 3D c’est la modélisation d’un élément essentiel !"
                    show isi question
                    i "Les bateaux ?"
                    show sao fier
                    s "Eh non ! Tout con !"
                    show sao happy
                    show isi surpris
                    s "L’eau !"
                    show isi happy
                    i "Law ? Trafalgar Law ?"
                    show sao surpris
                    s "Non non ! L’eau, le liquide ! T’es vraiment matrixé toi."
                    show isi embarras
                    i "Oh…"
                    show sao neutral
                    show isi neutral
                    s "Enfin, plus que l’eau en elle-même, c’est ses reflets et surtout ses éclaboussures qui sont extrêmement difficiles à coder sans prendre toute la RAM du monde."
                    s "Assassin Creed : Black Pearl a passé près d’un tier de son développement uniquement sur ce problème !"
                    show isi neutral
                    i "J’imagine la difficulté du problème."
                    show isi question
                    i "Comment prévoir chaque goutte d’eau, l’écume et les reflets, la direction, les fluides et le son face à un évènement répété et hasardeux sans qu’il ne fasse office de “vieille texture moche réutilisée”."
                    show sao surpris
                    s "Le réalisme de l’eau est le plus gros frein du jeu-vidéo."
                    show sao dout
                    s "En vérité, un jeu de pirate sans eau serait… un peu nul. Imagine des pirates aquaphobics."
                    show isi colere
                    i "N’insulte pas One Piece."
                    show sao happy
                    s "Haha !"
                    show sao neutral
                    show isi neutral
                    s "Bref maintenant quel type de RPG ?"
                    show isi confus
                    i "Oh non c’est repartie pour un tour…"
                    show sao embarras
                    s "….Ok je vais faire simple."

                    menu:
                        "OpenWorld":
                            show isi question
                            i "Et pourquoi pas un open world ?"
                            show sao neutral
                            s "Ah, un jeu “à monde ouvert” ?"
                            show isi embarras
                            i "Ça sonne plus classe en anglais…"
                            show isi neutral
                            show sao happy
                            i "Mais oui, c’est ça, un “monde ouvert” !"
                            show isi happy
                            show sao neutral
                            i "C’est un genre de jeu, plus qu’un genre en réalité, c’est une mécanique. On peut très bien avoir des farming simulators open world, ou des jeux d’horreur open world, ou encore des FPS open world !"
                            show sao surpris
                            show isi neutral
                            s "Enfin je pense qu’il est important de rappeler qu’il provient tout d’abord des RPG !"
                            show sao fier
                            s "Popularisé avec “The Elder Scrolls : Arena” en 1994, le jeu sera un tel succès que toute la série des Elder Scrolls se fera dans des mondes ouverts, nous offrant son opus le plus célèbre."
                            show sao happy
                            s "The Elder Scrolls V : Skyrim !"
                            show sao neutral
                            show isi question
                            i "Ah ouais ? Alors Skyrim doit être l’open world le plus célèbre !"
                            show sao fier
                            s "J’en serais pas si sûre si j’étais toi."
                            s "Certes, Skyrim est l’un des jeux les plus connus de l’histoire du jeu vidéo, mais il y a une autre série de jeux tout aussi légendaire en open world… "
                            show isi surpris
                            i "The Legend of Zelda ?"
                            show sao dout
                            show isi confus
                            s "Euh non je pensais pas à cette licence."
                            s "Hormis les deux derniers gros opus, soit donc BoTW et ToTK, les jeux Zelda sont en réalité des semi-open world."
                            i "B.O.T.W. et T.O.T.K. ?? Des semi-open world ???"
                            s "“Breath of the Wild” et “Tears of the Kingdom”. C’est des abréviations. Y’en a pleins dans le monde du jeu vidéo…"
                            show sao neutral
                            s "Non, moi je pensais plus à WoW et à GTA."
                            show isi colere
                            i "Dit les noms entier par pitié !"
                            show sao dout
                            s "“World of Warcraft” et “Grand Theft Auto” si tu préfères…"
                            show sao neutral
                            show isi neutral
                            s "Ces deux très vieilles licences furent parmis les premières et bonne réalisation d’open world total, et non de semi-open world !"
                            show isi embarras
                            i "Mais j’ai toujours pas compris la différence entre un open world et un semi-open world… Est-ce que le monde est “à moitié ouvert” ? Il est “à moitié fermé” ?"
                            show isi neutral
                            s "Un open world est un jeu où l’entièreté de la carte est accessible sans transition. Tu es libre de te balader et de prendre le chemin que tu souhaites sans craindre d’un temps de chargement quelconque ou d’une voie forcée."
                            s "Un semi-open world est un jeu disposant de très grande zone, mais nécessitant tout de même des temps de chargement et des transitions entre ces dernières."
                            show sao surpris
                            s "Par exemple, reprenons ton exemple de Zelda."
                            show sao neutral
                            s "The Legend of Zelda : Ocarina of Time, est-ce un open world ou un semi open world ?"
                            show isi question
                            i "Un open world, non ?"
                            show isi happy
                            i "Les plaines d’Hyrules ! On peut les traverser entièrement sur le dos d’Épona sans soucis !"
                            show sao fier
                            s "Nuh-uh !"
                            s "Certes, les plaines d’Hyrules sont très grandes et on peut la traverser sans problème. Mais dès que tu rentres dans un village, eh bah alors ?"
                            show sao neutral
                            s "Dès que tu changes de zone, tu as un temps de chargement, une transition. On ne peut pas aller du domaine Zora au désert Gerudo sans ce changement de carte !"
                            show isi surpris
                            i "Mais dans Breath of the Wild on peut !"
                            show sao happy
                            show isi happy
                            s "Et dans ToTK aussi ! C’est pour ça que je t’ai dit “seuls les deux derniers” ! De l’autre côté, GTA et TES ont toujours fait des full open world !"
                            show isi confus
                            i "T.O.T.K., G.T.A. et T.E.S. ??"
                            show sao dout
                            s "“Tears of the Kingdom”, “Grand Theft Auto” et “The Elder Scrolls”..."

                            jump FinMardi
 

                        "MMORPG":
                            show sao happy
                            s "Moi je te propose un MMO !"
                            show isi question
                            i "C’est quoi cette abréviation ?"
                            show sao colere
                            show isi embarras
                            s "Rho t’abuses."
                            s "Un MMORPG désigne un jeu de rôle en ligne massivement multijoueur, en anglais ”Massively Multiplayer Online Role-Playing Game.”"
                            show sao dout
                            s "En français on appelle ça un JDRMM."
                            show isi confus
                            i "Ok là je comprends pourquoi y’a besoin d’une abréviation."
                            i "C’est terriblement long comme nom ce truc !"
                            show sao surpris
                            show isi question
                            s "Attention à bien dire chaque lettre séparément. C’est un M-M-O-R-P-G."
                            show sao embarras
                            show isi neutral
                            s "EN 2010, Nathanaël de Rincquesen, un journaliste français de France 2l’avait honteusement prononcé “Meuporg” lors d’une émission surl’addiction au jeu…"
                            show sao colere
                            s "Imagine parler d’un sujet sans même savoir comment il se prononce ! Lafraude ultime !"
                            show isi embarras
                            i "En même temps, des fois y a des abréviations tirées par les cheveux…"
                            show sao surpris
                            s "Par exemple les extensions de World of Warcraft ?"
                            show sao embarras
                            s "En vrai ça paaaaasse."
                            show sao fier
                            s "WoW:BC, WoW:WotLK, WoW:MoP, WoW:WoD, WoW:BfA, WoW:TWW,WoW:TLT…. Sans compter les classiques ! En même temps, le premier jeuest sorti en 2004 ! Ça fait 20 ans !"
                            show isi confus
                            i "Ils vont vraiment trop loin dans les noms de jeu !"
                            show sao dout
                            s "C’est la même chose avec les mangas."
                            s "Le vrai titre de Konosuba c’est “Kono subarashii sekai ni shukufuku o!”."
                            s "Ou le titre complet de DanMachi c’est “Dungeon ni deai o motomeru no wa machigatteiru darō ka”."
                            show isi colere
                            i "Non mais ça c’est des exceptions !"
                            show sao colere
                            show isi embarras
                            s "SNK."
                            show isi colere
                            i "Bon ok j’ai perdu."
                            show isi question
                            i "Mais comment un jeu peut survivre 20 ans ?"
                            show sao neutral
                            s "Aujourd’hui, je ne sais pas si ça serait possible, mais le jeu reste populairecar il garde la même ou pratiquement la même communauté depuis sesdébuts !"
                            show isi surpris
                            i "Hein ? Mais comment en 2004 tu pouvais avoir autant de monde ?"
                            show sao happy
                            s "Là est la révolution de WoW, qui lui a valu une communauté gantesque !Il a toujours sa place dans le Guiness Book pour “la plus grandepopularité pour un MMORPG” !"
                            s "Aujourd’hui, nous sommes environs à 10 millions de joueurs actif àtravers le monde, mais la barre des 12 millions de joueurs actifs au mêmemoment fût dépassée plus d’une fois ! Un événement mondiale !"
                            show isi neutral
                            s "L’univers n’est accessible que par un réseau et il n’est pas persistant :c’est-à-dire qu’il existe tout le temps, que le joueur y soit connecté ou non."
                            s "Tu te déconnectes une heure, et tu peux revenir dans un monde de feuet de cendre !"
                            show isi confus
                            i "Mais ça à l’air horrible ! Comment ça se fait ? Que se passe-t-il quand je me déconnecte ?"
                            show sao fier
                            show isi surpris
                            s "Rien."
                            show sao happy
                            show isi neutral
                            s "C’est juste que les autres joueurs peuvent faire les fous !"
                            show sao neutral
                            s "La différence entre un RPG et un MMORPG c’est qu’un grand nombre de joueurs peuvent interagir simultanément dans un monde virtuel. On y axe beaucoup de social."
                            show sao embarras
                            s  "Ceci accroît néanmoins le risque de dépendance ludique."
                            s "“Je ne peux pas quitter le jeu maintenant, et si telle ou telle chose se produisait en mon absence ?”"
                            s "“Je ne peux pas arrêter, la guilde m’attend, je ne peux pas les laissertomber.”"
                            show sao dout
                            s "La communauté peut devenir un poids, une pression sociale avec desdevoirs et des attentes envers les autres joueurs."
                            show isi fier
                            i "L’addiction aux jeux vidéos…."
                            show isi neutral
                            i "C’est vrai que c’est principalement, voir même exclusivement, dans les jeux multijoueurs."
                            show sao fier
                            s "C’est un risque, mais un beau sacrifice."
                            show sao neutral
                            s "Les MMORPG ont certes un risque d’addiction, de dépendance etd’isolement mais il a permis de beaux événements !"
                            s "Forgé des amitiés légendaires, faire rencontrer deux futurs mariés… C’estémouvant de voir deux personnes se rencontrer sur un jeu, se mettre encouple et ensuite se marier avec comme témoin les membres de laguilde."
                            s "Un peu plus triste, on a également eu des enterrements virtuels, pour des personnes vivant seuls ou isolés car étant à l’autre bout du monde…"
                            show isi happy
                            i "Tu m’étonnes que les MMORPG restent des très gros jeux ! Ces jeux viventpar leur communauté elle-même !"
                            i "Les MMO, c’est formidable !"

                            jump FinMardi
               

                "Des chevaliers":
                    show sao happy
                    show isi happy
                    s "Des chevalieeeeers !!!"
                    i "Des chevalieeeeeers !!!"
                    show sao colere
                    s "Tu mérites même pas de me côtoyer pour avoir posé cette question : à 1000%% je prends les chevaliers."
                    show sao happy
                    s "Des hommes en armures, en cuirasse et en cotte de maille… N’EST-CE PAS SÉDUISANT ?!"
                    show isi colere
                    i "Avec les famines, la pauvreté, le tier-état et la religion aussi… non ?"
                    show sao embarras
                    s "Rhoo mais ça on s’en fout."
                    show sao colere
                    s "Tu serais le genre de joueur à donner des pièces aux mendiants dans Baldur’s Gate 3 toi ?"
                    show isi embarras
                    i "Bah…"
                    s "Ça sert à rien. T’as même pas d’évent bonus ou autre. Le seul item qu’ils peuvent te passer, c'est des haillons. Sauf que ce truc donne même pas 1 de défense."
                    show sao happy
                    s "Moi je te parle des combats sanglants, où ça se tape vraiment !"
                    show sao fier
                    s "Les duels dans les codes et l’art de la chevalerie ! Les tensions entre noblesse, clergé et tier-état ! Un monde où le joueur prend les armes et s'impose par la FORCE !"
                    show isi colere
                    i "Dit juste que tu veux de la grosse bagarre…"
                    show sao colere
                    s "Alors de un."
                    show sao neutral
                    show isi neutral
                    s "Le monde médiéval, souvent rattaché au genre du Heroic Fantasy, est le cœur même des premiers jeux de rôles. Bien qu’aujourd’hui le genre s’est nettement développé, il est important de rappeler les origines."
                    s "Le choix et la popularité du genre, pourtant existant depuis belle et lurette peut s’expliquer par les raisons suivantes :"
                    s "L’influence du Moyen- ge : le Moyen- ge est une période fascinante qui a inspiré de nombreux artistes, écrivains et cinéastes. Les légendes, les mythes et les contes de fées de cette époque ont fourni un terreau fertile pour les créations fantastiques."
                    show isi embarras
                    i "Hein ?"
                    show sao fier
                    s "L’influence de la littérature classique : les écrivains du XIXe siècle, tels que Walter Scott et Alfred Tennyson, ont déjà exploré le Moyen ge dans leurs œuvres, créant ainsi un terrain préparé pour les créations fantastiques ultérieures."
                    show isi confus
                    i "Qui ça ??"
                    show sao surpris
                    s "De plus, des écrivains de fantasy modernes, tels que J.R.R. Tolkien et George R.R. Martin, ont également contribué à populariser le médiéval fantastique en créant des univers immenses et complexes."
                    i "Attend quoi ?"
                    show sao happy
                    s "Les créatures fantastiques, telles que les nains, les elfes et les dragons, sont des éléments clés du médiéval fantastique. Elles permettent de créer des histoires épiques et des aventures fantastiques par leur caractéristique extraordinaire."
                    show sao neutral
                    s "L’homme a toujours voulu voler, alors pourquoi ne pas imaginer des hommes vêtus d’ailes ? Pourquoi ne pas imaginer de terrible créature plus terrifiante que les animaux de notre réalité ?"
                    show sao happy
                    s "Les dragons, c’est super badass !"
                    show isi embarras
                    i "Je…"
                    show sao fier
                    s "Et de deux."
                    show isi surpris
                    i "Oh non c’est repartie….!"
                    show sao happy
                    s "J’adore les grosses bagarres !!"
                    show isi surpris
                    i "….!"
                    show isi colere
                    i "Bizarrement j’ai plus été convaincue par le premier argument que le second… "
                    show sao dout
                    s "Tu peux me dire si t’as juste skip."
                    show isi embarras
                    i "C’est pas que c’est un peu long mais…"
                    i "…."
                    s "…."
                    show isi neutral
                    i "Et tu comptes en faire quoi de tes chevaliers ?"
                    show sao happy
                    s "T’en fais pas j’ai tout prévu !"
                    show isi question
                    i "OK, donc que veux tu faire ?"

                    menu:
                        "Dungeon Crawler":
                            show sao happy
                            show isi confus
                            s "UN DUNGEON CRAWLEEEEEEEEEEEER !!"
                            i "POURQUOI TU CRIES ???"
                            s "PARCE QUE J’ADORE LES DUNGEON CRAWLEEEEEEEEEEER !!!"
                            i "WaaAAAaAAAA !!"
                            s "DUNGEOOOOON CRAAAAAAAWWWWWLEEEEEEEEEEER !!!"
                            l "Isidore ! Sao Mai ! Taisez vous enfin !"
                            show sao embarras
                            show isi colere
                            s "…"
                            i "…"
                            s "Mes excuses."
                            show sao neutral
                            s "Donc euh je proposais un-"
                            show sao colere
                            show isi confus
                            s "Pourquoi tu te bouches les oreilles."
                            show isi embarras
                            i "Parce que je tiens à mes oreilles…?"
                            s "…"
                            show isi neutral
                            show sao neutral
                            s "Bref, un dungeon crawler est simplement mon archétype de jeu préféré."
                            show isi question
                            i "C’est quoi, tu “crawle” un donjon ?"
                            show sao happy
                            s "Tout est dans le nom oui : tu rampes dans un donjon."
                            show isi colere
                            i "Un peu nul comme gameplay de serpent…"
                            show sao colere
                            show isi embarras
                            s "Ça c’est offensant."
                            show sao neutral
                            show isi neutral
                            s "Enfin on ne “rampe” pas littéralement. Ça signifie simplement l’exploration de donjon par le propre joueur."
                            s "Souvent labyrinthique, la carte se ne dévoile que petit à petit par les efforts du joueur, bravant les monstres et les pièges pour “gratter” le moindre avancement du donjon."
                            s "D’où le terme “ramper”, tu grattes chaque centimètre d’exploration à la sueur de ton front !"
                            show isi surpris
                            i "J’avais jamais entendu parler de ce genre de jeu !"
                            show isi neutral
                            show sao dout
                            s "Ouais c’est un genre plutôt niche et qui est malheureusement mourant…"
                            s "On lui fait le reproche d’être “trop répétitif”... Bah c’est de l’exploration de donjon avec beaucoup de farm. Moi j’aime énormément mais ça ne convient pas au grand public…"
                            show isi question
                            i "Je vois surtout pas comment tu peux innover dans ce genre de jeu."
                            show sao fier
                            s "Détrompe toi Isidore ! Le progrès et les nouveaux gameplay sont toujours possibles ! C’est ce qu’à prouver la licence la plus populaire du genre."
                            show sao happy
                            s "Etrian Odyssey ! Sortie en 2007 sur la Nintendo DS !"
                            show isi confus
                            i "2007 ! Elle a presque notre âge ! Innovation d'antan !"
                            show isi neutral
                            s "Ce jeu où l’on explore le labyrinth d’Yggdrasil est réputé pour être le meilleur Dungeon Crawler car il pallie les lacunes des mécaniques du genre."
                            s "Par exemple : c’est le joueur lui-même qui cartographie sa carte ! Et non le jeu qui prend automatiquement la case sur lequel est le joueur : il n’aura plus à marcher dans un piège pour le noter sur sa carte !"
                            s "On explore alors réellement selon notre point de vue et non plus sous une carte à débloquer !"
                            show isi question
                            i "Et si le joueur oublie de noter son chemin ?"
                            show sao fier
                            show isi surpris
                            s "S’il oublie ! Eh bien tant pis pour lui !"
                            show sao neutral
                            show isi neutral
                            s "Dans un labyrinthe, on ne connaît pas forcément le chemin qu’on a prit, là est tout le jeu !"
                            show isi confus
                            i "Bon je te laisse la conception de labyrinthe puisque c’est toi la fana d’Etrian Odyssey !"
                            s "Pourtant c’est pas mon jeu préféré."
                            show sao happy
                            s "Mon jeu préféré de tous les temps c’est “Labyrinth of Refrain : Coven of Dusk”, sortie en 2016 sur PC et console !"
                            show isi colere
                            show sao neutral
                            i "Laisse moi deviner…"
                            show isi question
                            i "Un Dungeon Crawler ?"
                            show sao happy
                            show isi neutral
                            s "EXACTEMENT !"
                            s "LoR c’est vraiment UN JEU INCROYABLE avec des labyrinthes et un lore, des easters eggs avec les jeux d’autres saga, des personnages profonds et complexes dans une narration époustouflante pleine de rebondissement !"
                            show isi confus
                            s "Les labyrinthes ont leur propre histoire, détachée de l’intrigue principale avec leur propre personnage. Et même les pantins du joueur peuvent créer des liens dans la brigade entre eux !"
                            s "Avec les musiques de Tenpei Sato, vraiment le boss de la musique vraiment BANGER ! Et Dronya est vraiment magnifique genre femme charismatique/20 je m’INCLINE."
                            s "Tu savais que j’avais cité ce jeu dans mon dossier Parcoursup tellement il est brillantissime ?"
                            i "Rhaaaa !!! TAIS TOI !"
                            show sao colere
                            s "JAMAAAAAAAAIS !!"
                            l "Isidore ! Sao Mai ! Taisez vous enfin !"
                            show sao embarras
                            show isi embarras
                            s "…"
                            i "…"
                            jump FinMardi

                        "SoulsLike":
                            show sao happy
                            show isi neutral
                            s "UN SOULSLIKE !"
                            show isi colere
                            i "Ton sourire ne dit rien qui vaille…"
                            show sao surpris
                            s "Oh mais c’est super les souslikes !"
                            show sao neutral
                            i "Vas-y, explique moi c’est quoi comme genre de jeu ? Gameplay chill avec des graphismes mignons ?"
                            show isi surpris
                            i "Oh moi j’aimerais bien un jeu de ferme ! "
                            show isi happy
                            i "Qu’est-ce que c’est relaxant, mignon et doux !"
                            show sao colere
                            s "NAAAAAN MOI JE VEUX DE LA GROSSE BAGARRE !!"
                            show isi confus
                            i "Nooooooooon !"
                            show sao neutral
                            show isi colere
                            s "Les Soulslikes sont des jeux avec pour volonté d’être nerveux, horriblement dur et technique, avec des combats violents et injustes."
                            show isi embarras
                            i "Oh non…"
                            show isi colere
                            show sao fier
                            s "Ce sous-genre tire son nom d’une license légendaire qui inventa le sous-genre. Suite à sa popularité, de nombreux jeux tentèrent de l’égaler en en faisant des “jeux comme”"
                            show sao happy
                            s "Des Souls’ like !"
                            i "Souls ?"
                            show sao embarras
                            s "Ah oui, c’est vrai que tu ne joues absolument pas à ce genre de jeu : ils ne sont pas du tout, mais alors pas du tout, tout public par leur atroce difficulté."
                            show sao happy
                            show isi neutral
                            s "Dark Souls !"
                            show isi surpris
                            show sao neutral
                            i "Ah oui c’est le truc de ta sonnerie de téléphone non ?"
                            show sao happy
                            s "Exactement !"
                            show sao fier
                            s "“Vordt of the Boreal Valley” est une musique qui inspire la crainte, la présence d’un danger imminent et que nul mortel ne saurait vaincre !"
                            s "La license des Souls, comprenant donc “Dark Souls” de 1 à 3, la saga des “Bloodborne” et la saga des “Demon’s Souls” ainsi que dernièrement l’excellentissime “Elden Ring” sont des monuments du jeux-vidéos."
                            show sao happy
                            show isi confus
                            s "C’est LES JEUX par EXCELLENCE de LA DIFFICULTÉ."
                            show sao fier
                            s "Univers sombre, morts multiples, ennemis à foisons, monde hostiles…"
                            s "C’est le genre de jeux qui te rappelle que l’univers est injuste."
                            show sao neutral
                            s "Un Souslike est un jeu présentant alors un niveau de difficulté extrême, à la mort répétée et demandant alors un acharnement sans nom."
                            show isi surpris
                            i "Le fameux “You died”."
                            show isi neutral
                            s "L’écran de mort des jeux Dark Souls est devenu iconique tellement il est fréquent en jeu. Une bande noire avec un texte en rouge, et surtout le son légendaire de souffle lent…"
                            show isi embarras
                            i "Faut être un peu masochiste non ?"
                            show sao surpris
                            s "C’est bien là la réputation des fans de ces jeux !"
                            show sao embarras
                            show isi neutral
                            s "Des masochistes fous, des tryhard qui apprennent par cœur des paternes d’attaque parfois longues de 30 minutes."
                            show sao fier
                            s "Les combats sont comparables à de véritables danses classiques tellement tout est précis et calculé."
                            show sao neutral
                            s "Le tout se déroule dans un univers de dark fantasy que le joueur devra explorer s’il veut devenir plus puissant."
                            s "L’évolution du personnage est alors au cœur du gameplay. Il pourra toujours mieux s’équiper, avoir de meilleur sort…"
                            s "Mais la réelle évolution est celle du joueur."
                            show sao surpris
                            show isi surpris
                            s "Une étude à démontrer que les joueurs aguerries de ses jeux présentaient un temps de réaction monstre et une mémoire à toute épreuve, pour apprendre les parternes d’attaques des ennemis."
                            s "Ils y apprennent également la patience et la détermination dans des jeux qui présentent également des histoires poignantes et travaillées."
                            show embarras
                            s "Qui n’a pas lâché de larme dans Elden Ring à la fin de-"
                            show isi colere
                            i "Pas de spoil !"
                            show sao conlus
                            s "Quelle tragédie !"
                            show isi neutral
                            i "Je vois le genre."
                            show isi colere
                            i "Des jeux de gros tryhard."
                            show sao embarras
                            s "On peut résumer la chose à ça oui…"

                            jump FinMardi

    
        "Voir les idées de Isidore":
            show isi happy
            show sao neutral
            i "Un RPG !!"
            s "Un RPG ?"
            show sao colere
            s "Tu veux faire un Rôle Play Game alors qu’il en existe déjà plein ?"
            show isi neutral
            i "Oui ! C’est l’un des meilleurs types de jeux !"
            show isi happy
            i "Regarde, quel est ton RPG préféré ?"
            show sao happy
            s "Labyrinth of Refrain : Coven of Dusk !"
            show isi neutral
            show sao neutral
            i "Et c'est quoi ton personnage préféré dans celui-ci ?"
            show sao happy
            s "Labyrinth of Refrain : Coven of Dusk !"
            show isi fier
            show sao neutral
            i "Tu vois, ce qui est incroyable avec ce genre de jeu c’est que le joueur qui est impliqué dans le jeu."
            show sao happy
            s "Labyrinth of Refrain : Coven of Dusk !"
            show isi colere
            show sao embarras
            i "Stop !!! Laisse-moi faire mon monologue !!"
            s "…"
            show isi neutral
            i "Donc je disais que les jeux de type RPG comme Monster Hunter World, qui est un jeu où tu ne joues pas un personnage déjà existant. Tu joues ton propre personnage !"
            s "…"
            show isi fier
            i "Cela permet donc une meilleure immersion du joueur, car tous les PNJ interagissent avec le joueur de différentes manières en fonction de ces choix."
            s "Euh…Je peux te poser une question ?"
            show isi colere
            i "Si tu me reparles de Labyrinth of the frame to host."
            show sao happy
            s "C’est Labyrinth of…"
            i "J’ai dis quoi ?!"
            show sao colere
            s "Respecte mon jeu préféré ou je te pète les genoux."
            show isi embarras
            i "…"
            show isi neutral
            i "Donc quelle est ta question ?"
            show sao embarras
            s "C’est quoi déjà un PNJ ?"
            show isi fier
            i "Un PNJ est un “Personnage Non Jouable” qui va donc interagir avec le joueur en fonction de ces dires et de ces actions. "
            show isi question
            i "On peut citer par exemple le personnage Zelda dans les jeux Breath of the wild et Tears of the Kingdom. Elle guide le joueur tout au long du jeu et amène de la profondeur à l’histoire."
            show isi neutral
            show sao dout
            s "Mouais je vois le genre… C’est que c’est une bonne idée de jeu."
            s "Mais pourquoi les jeux s’appellent The Legends of Zelda si on joue jamais Zelda…?"
            show isi question
            i "Je pense que c’est parce que Zelda est la princesse d’Hyrule et que Link est son chevalier et qu’il va l’aider à ce qu'elle se développe personnellement."
            show isi neutral
            s "Heureusement que tous les jeux n’appliquent pas cette logique…"
            s "Imagine si la série de jeu “Bayonetta” s’appelait “Enzo et Rodin”.Un peu moins classe d’un coup."
            show isi happy
            i "Après “La Légende de Link”, ça sonne moins bien aussi."
            show isi neutral
            show sao neutral
            i "Mais bref on n’est pas là pour juger les choix de Nintendo. Passons à la suite !"
            s "Tu penses qu’on devrait orienter notre RPG vers quoi ?"

            menu:
                "Multijoueur":
                    show sao happy
                    show isi surpris
                    s "Moi je pense qu’un RPG multijoueur serait formidable !"
                    show isi happy
                    i "C’est une idée géniale !"
                    show sao neutral
                    i "Les jeux multijoueur permettent de rassembler un grand nombre de joueurs dans le jeu en même temps et plus seulement autour du jeu."
                    s "Vas-y développe."
                    i "Le fait que plusieurs joueurs jouent tous ensemble dans une même partie, cela renforce l’expérience de jeu vécu par les utilisateurs."
                    show isi fier
                    show sao colere
                    i "Regarde par exemple dans Sword Art Online, Kirito et Asuna font équipe et ils vont créer des liens en dehors du jeu, et du coup…"
                    show isi neutral
                    s "Tu sais très bien ce que je pense de cet anime."
                    s "Une bonne idée et une terrible exécution. Pour parler du multijoueur dans les MMO, on peut plutôt parler de tuerie de masse et meurtre en bande organisée avec un harem pour le fan service."
                    s "Mauvais exemple Sword Art Online."
                    show isi fier
                    i "Pourquoi ? Parce que l’abréviation de cet animé c’est S.A.O. ?"
                    s "VIENS LÀ QUE JE T’ATTRAPE !!"
                    show isi confus
                    i "SAUVEZ MOI DE CETTE SORCIÈRE !!!"
                    l "Sao Mai, Isidore, parlez moins fort s’il vous plaît."
                    s "…"
                    s "Parle encore une fois de cet anime des enfers et je te jure que ta ligné s’arrêtera avec toi."
                    show isi colere
                    i "…"
                    show isi neutral
                    i "Bon… Donc je disais qu' on peut prendre comme exemple Overwatch développé par la compagnie Blizzard Entertainment."
                    show sao dout
                    s "Quel magnifique jeu. Dommage qu’il ait été gâché avec le 2. "
                    show isi surpris
                    i "C’est vrai. D'ailleurs, on n’y a jamais joué ensemble."
                    show isi neutral
                    show sao neutral
                    i "Ce jeu est la représentation même d’un bon jeu en multijoueur, où la cohésion d’équipe est primordiale pour gagner et où la victoire n’est que meilleure quand tout se passe sans accrocs."
                    show sao happy
                    s "Ça me donne envie d’aller voir s' il y a encore des matchs d’e-sport sur ce jeu."
                    show sao dout
                    s "Quoique, sa META est vraiment nulle."
                    show isi colere
                    i "On verra ça plus tard."
                    show isi neutral
                    i "Il y a aussi des jeux en multijoueur où c'est chacun  pour soi. Le premier jeu qui me vient à l’esprit est…"
                    show sao happy
                    s "Mario Kart !"
                    show sao neutral
                    show isi happy
                    i "C’est un très bon jeu de course en multijoueur, mais je pensais plutôt aux Mario Party. Ces jeux de plateau où tu te déplaces avec des dés et tu affrontes les autres dans une poignée de mini-jeux."
                    i "Mon préféré c’est Porte-à-porte de Mario Party 9."
                    s "Pas mal. Un jeu qui brise des amitiés."
                    show sao embarras
                    s "Mon frère me parle plus depuis que je lui ai envoyé une carapace bleue… Ça fait 3 ans… "
                    show isi embarras
                    i "Ah oui : les jeux vidéos, qu’ils soient en multijoueurs en coopération ou en versus, peuvent briser des amitiés !"
                    show sao dout
                    s "Plus les jeux co-op… Versus c’est normal qu’il y ait rivalité mais lorsqu’on est dans la même équipe… Combien de fois j’ai baissé de rang à cause de mon équipe ! Quel enfer !"
                    show isi colere
                    i "Y a que toi pour être une frustrée de la vie."
                    s "Mais alors, on ferait quel type de jeu multijoueur ?"

                    menu:
                        "Coopération":
                            show isi neutral
                            i "On pourrait faire un jeu en coopération, tu en penses quoi ?"
                            show sao happy
                            s "C’est super comme jeu."
                            show isi happy
                            show sao neutral
                            i "Moi j’adore."
                            show isi fier
                            i "Tu veux que je te réexplique ce que c’est ?"
                            show sao dout
                            s "Nan ça va aller, je ne suis pas complètement idiote."
                            i " Alors…"
                            show sao colere
                            s "Mais…"
                            show sao dout
                            show isi neutral
                            i "Un jeu en co-op, ou coopération, est un genre de jeu où deux joueurs vont collaborer afin de progresser dans le jeu et accomplir les objectifs qu’ils ont en commun."
                            show sao surpris
                            s "Ils ont des objectifs en commun, mais ils ne sont pas forcément dans la même équipe, non ?"
                            show sao neutral
                            show isi happy
                            i "Tout à fait, je ne l’avais pas précisé mais les deux joueurs forment un duo."
                            show sao dout
                            s "Mais c’est pas ce que j’ai dit-"
                            show isi fier
                            i "Ce genre de jeu regorge de mécaniques de tous types. On peut prendre par exemple le jeu “It Takes Two “qui est LE jeu de coopération par excellence !!"
                            i "On y incarne deux personnages minuscules dans notre monde qui vont donc le parcourir afin de retrouver leur taille normale, le plus de ce jeu c’est que l’on peut se reconnaître dans la narration qui est axée sur les relations humaines."
                            s "Et à part me parler de l’histoire du jeu que je connais déjà, parle moi des mécaniques présentes."
                            show isi embarras
                            i "Oui, pardon."
                            show isi neutral
                            i "Ce jeu met un point d’honneur sur une grande mécanique du jeu vidéo…. Les plateformes ! Étant donné que les héros sont miniatures, les interactions avec l’univers sont énormes, mais ce jeu laisse tout de même un aspect d’indépendance entre les deux joueurs."
                            i "Chaque joueur a son personnage, qu’il va pouvoir contrôler dans un environnement qui ne sera pas toujours partagé."
                            show isi happy
                            i" En étant dans deux milieux différents mais interagissant entre eux, on force les joueurs à évoluer “seul” mais avec la nécessité d’une aide extérieure."
                            show sao neutral
                            s "Oui je vois le genre."
                            show isi neutral
                            s "C’est comme les escapes games où l’on commence dans des salles séparées : on a chacun nos chemins et nos énigmes, mais les réponses se partagent d’une salle à l’autre !"
                            s "Le jeu d’énigme “The Past Within”, de la saga de jeux Rusty Lake est le premier Point and Click co-op par exemple, et il se base justement sur la notion d’énigme dont les réponses sont éparpillées entre deux salles et ainsi, deux joueurs."
                            show isi happy
                            i "Mais d’autres jeux co-op peuvent-être beaucoup plus simple et diablement efficace !"
                            show isi surpris
                            i "Une simple mécanique : les deux joueurs sont inséparables."
                            show isi happy
                            i "Un platformer où les deux joueurs sont collés, ça demande une véritable cohésion d’équipe, une synergie !"
                            i "Ou alors, les jeux où c’est LA combinaison des DEUX joueurs qui permettra la suite !"
                            show isi neutral
                            i "Le jeu Snipperclips illustre bien lui aussi les jeux de coopération, où la présence d’un autre joueur allié est ici primordiale et indispensable."
                            show sao dout
                            s "Pourquoi tu dis primordiale et indispensable alors qu’un seul de ces mots suffit ?"
                            show isi surpris
                            i "Parce que c’est primordiale…"
                            show isi neutral
                            s "…"
                            i "Dans ce jeu seul l’entraide permet d’avancer, de réussir les niveaux proposés dans ce jeu. En plus de ça, le style graphique du jeu se démarque de beaucoup de jeux avec un univers en papier et des objets du quotidien."
                            show sao colere
                            s "Je tiens tout de même à mettre un grain de sel."
                            show isi embarras
                            i "Hein ? Quoi ?"
                            i "T’aime pas les jeux en co-op ?"
                            show sao surpris
                            s "J’adore !"
                            show isi neutral
                            show sao colere
                            s "Mais tout n’est pas noir ou blanc."
                            show isi surpris
                            i "Y a un jeu co-op qui s’appelle Blanc."
                            show sao surpris
                            show isi happy
                            s "Oui et il est adorable mais c’est pas de ça dont je voulais parler…"
                            show sao colere
                            show isi colere
                            s "Dans les jeux compétitifs comme LOL ou Valorant, quand t’as ton jungler qui reste au centre pour farmer alors que l’équipe adverse est en train de prendre le boss."
                            s "Que le boss est proche du jungler et qui pourrait le voler ou même attaquer l’équipe adverse après que toute ton équipe ait attaqué avant et qu’ils n’ont plus de PV."
                            s "Que le jungler fait des attaques AoE et qu’il a 7 niveau de plus et que-"
                            i "Non mais la co-op dans les jeux compétitifs c’est toxique."
                            show sao dout
                            s "C’est pas la co-op qui est toxique."
                            show sao colere
                            s "C’est juste que les gens jouent COMME DES GROSSES M-"
                            i "Average joueuse de League Of Legends et de Valorant."

                            jump FinMardi

                        "Battle Royal":
                            show isi happy
                            show sao surpris
                            i "Un Battle Royal !!" 
                            i "Ça c’est un RPG en multi qui claque !"
                            show sao happy
                            s "Arriver sur une zone en même temps qu’une cinquantaine de joueurs, chercher du loot et tous les exterminer !!!"
                            show isi surpris
                            i "Doucement, on dirait que tu adores faire du mal aux autres avec cette phrase."
                            show sao embarras
                            s "C’est pas ce que tu crois."
                            show isi colere
                            i "…"
                            show isi neutral
                            show sao neutral
                            i "Bon, donc je me disais que faire un jeu où de nombreux joueurs doivent se battre entre eux pour leur survie pourrait être cool."
                            show sao happy
                            s "À la fin, il n’en restera qu’un !"
                            show sao neutral
                            show isi fier
                            i "Le premier “grand” Battle Royal qui a été créé c’est Bomber Man."
                            show isi neutral
                            i "Quatre joueurs dans une arène pose des bombes pour essayer de faire exploser leurs ennemis. C’était super original à l’époque."
                            show sao dout
                            s "C’est sûr. Mais peut-on le caractériser de battle royal avec seulement 4 joueurs qui s'affrontent ?"
                            show isi embarras
                            i "Forcément quand on le compare aux jeux d’aujourd’hui il fait pâle copie."
                            show isi fier
                            show sao neutral
                            i "En vérité, dès qu’il y a la notion de multijoueur et d’élimination des adversaire avec le dernier en vie gagnant : c’est un battle royal !"
                            show isi happy
                            i "Regarde par exemple PUBG."
                            show isi neutral
                            show sao happy
                            s "“Player Unknown's BattleGrounds”, vraiment un super jeu ! Connu à l’international !"
                            show isi surpris
                            s "Tu savais que même au Vietnam c’est un jeu tendance ? Là bas, un ordinateur coûte très cher donc ils jouent principalement à des jeux mobiles."
                            show sao neutral
                            show isi neutral
                            s "PUBG étant disponible gratuit, sur mobile et cross platform, il jouit d’une très grande popularité et un grand nombre de joueurs ! "
                            show isi fier
                            i "Avec 100 joueurs présent dans le même matchmaking, des graphismes réalistes, une carte immense avec des villes, comment ne pas créer une grosse communauté qui va jouer au jeu ?"
                            show sao fier
                            s "À sa sortie c’était devenu le meilleur Battle Royal existant, personne ne pouvait faire mieux. Un jeu fluide, nerveux, technique."
                            show sao neutral
                            i "C’est sans compter l'arrivée d’un nouveau challenger qui va rassembler toute la communauté des joueurs de battle royal derrière lui."
                            show isi happy
                            i "Avec une forte communauté, tout est possible !"
                            show isi neutral
                            i "Il y existe même un jeu si influent avec une si grosse communauté qu’il a pu organiser une coupe du monde dès sa deuxième année d'existence, je parle bien évidemment de…"
                            show sao happy
                            s "SpellBreak ! Sortie en 2020 ! C’est génial de pouvoir balancer des sorts de tous types à ses adversaires et de pouvoir faire des combos en les fusionnant."
                            show sao neutral
                            s "Un jeu qui allie le battle royal et la fantaisie à la perfection ! Il sort du lot par ce beau mélange, la plupart des battles royals étant avec des armes à feu."
                            show isi happy
                            i "C’est vrai qu’il était sympa."
                            show isi neutral
                            show sao dout
                            s "Comment ça “il était” ?"
                            show isi embarras
                            i "Malheureusement les serveurs ont fermé début 2023."
                            i "C’est vrai que le système de combat se démarque beaucoup des autres jeux, mais il a toujours eu du mal à se maintenir."
                            i "A chaque partie que je voulais faire je devais attendre 15 minutes pour que la partie se lance et il n’y avait jamais 50 joueurs présents dans un même lobby."
                            show isi fier
                            i "Nan je parlais bien évidemment de Fortnite !"
                            i "Honnêtement laisserais-tu ton enfant de 8 ans jouer à un jeu avec des graphismes réalistes où tu tires sur des gens ?"
                            show sao neutral
                            s "Honnêtement oui."
                            show isi surpris
                            i "Quoi ?"
                            show isi colere
                            show sao embarras
                            s "Quoi ?"
                            i "..."
                            show isi neutral
                            i "Et bien Fortnite c’est tout le contraire."
                            show isi happy
                            i "Un univers Cartoon, des armes factices et surtout un univers complètement modifiable grâce à la possibilité de construire et détruire des structures."
                            show sao dout
                            show isi neutral
                            s "Ouais, SpellBreak n’était juste pas à la hauteur de tous les autres."
                            show isi happy
                            i "Et puis qui ne rêverait pas de se battre en jouant son super-héros préféré ou bien même Dark Vador ou Naruto !"
                            show sao colere
                            s "Horrible ! J’en ai marre de voir des collabs de partout. Au début c’était fun mais maintenant…"
                            show isi colere
                            i "J’EN AI MARRE DES ENFANTS QUI ME DISENT QUE YUJI OU SON GOKU SONT LES MECS DE FORTNITE !!!!!"
                            show sao dout
                            s "…"
                            show isi embarras
                            i "…"
                            show sao neutral
                            show isi neutral
                            i "Sinon il y a d'autres jeux indépendants sympa comme Ninjala. Tous les jeux indépendants sont tellement plus originaux je trouve."
                            show isi surpris
                            i "Ça me fait penser qu’il existe aussi un jeu qui a tellement bien marché, qu’il a maintenant un animé à son effigie. C’est Danganronpa !!"
                            show isi neutral
                            show sao happy
                            s "Danganronpa est un bon exemple car il met au grand jour le principe de “kill party” !"
                            show sao neutral
                            s "Dans cette sombre dystopie, des lycéens sont enfermés dans un établissement macabre. Pour sortir ils ont une solution : tuer quelqu’un sans se faire prendre."
                            s "S’il réussit à tuer quelqu’un sans que les autres ne le découvrent, il peut s’échapper mais tous les autres lycéens ayant échoué à trouver le tueur meurent automatiquement."
                            s "Si c’est lui qui se fait prendre, c’est lui qui est exécuté !"
                            show sao fier
                            s "Un endroit clos, un meurtre et un nombre de personne définie : un super jeu d’enquête ou le plus fourbe gagnera !"
                            i "C’est le Cluedo quoi."
                            show sao dout
                            s "Ouais."

                            jump FinMardi

                "Crossover":
                    show isi question
                    i "Et si on faisait un Crossover ?"
                    show sao colere
                    s "Et voilà, après m’avoir parlé tout le temps de mangas, tu me parles maintenant de mouvements de basket."
                    show sao dout
                    show isi surpris
                    i "Mais nan je parle d’un jeu qui mélange plusieurs licences qui ressemble ou alors qui n’ont rien à voir afin de susciter l'intérêt de plusieurs communauté ou de faire des jeux vraiment originaux."
                    show isi neutral
                    s "Là je comprends mieux. Ce serait donc un jeu comme Mario et Sonic aux Jeux olympiques."
                    i "Pourquoi pas, c’est l’exemple type d’un crossover, surtout qu’avec celui-ci la guerre entre Sega et Nintendo a pris fin."
                    s "La fameuse guerre des consoles de 1990 avec la MegaDrive face à la Super Nintendo."
                    i "La possibilité de faire un cent mètres avec Mario et Blaze est vraiment une idée ingénieuse de la part des deux entreprises."
                    show sao embarras
                    s "Espérons qu’il y aura un Mario et Sonic aux Jeux Olympiques de Paris 2024."
                    show isi happy
                    i "Se serait trop cool !"
                    show isi question
                    show sao dout
                    i " Mais tu arrives à imaginer Mario nager dans la Seine ?"
                    s "C'est sur que c'est pas très vendeur ça."
                    show sao neutral
                    show isi neutral
                    s "Après le Crossover le plus emblématique c’est Poker Night at the Inventory, on incarne tout simplement un personnage qui fait des parties de poker avec des personnages des licences Sam & Max,  Team Fortress 2, Strong Bad ou bien même Borderlands."
                    show isi colere
                    i "C’est purement un rassemblement de plein de licences avec un jeu simple et efficace, on peut pas faire mieux."
                    show sao dout
                    s "Alors ne sois pas si sûr de toi, parce que de très bon jeux crossover de combat je peux t’en citer beaucoup."
                    show isi embarras
                    i "Je t'écoute."
                    show isi neutral
                    show sao neutral
                    s "Il y a Mortal Kombat qui est le jeu de combat en mode arcade le plus travailler de tous que ce soit les graphismes, les dommages physiques que subissent les personnages." 
                    s "Tout a été réalisé de manière à ce que l’on ai l’impression de regarder un film avec des acteurs et non de jouer à un jeu."
                    show sao happy
                    s "En plus d’implémenter des personnages de d’autres univers comme le Joker et Harley Quinn de DC."
                    show isi fier
                    i "J’ai rien à redire sur ce point tu as totalement raison."
                    show isi surpris
                    i "Mais sincèrement je préfère les jeux où tu résous des énigme, un peu prise de tête et où tu fais travailler ta matière grise."
                    show sao happy
                    s " Le meilleur de ce type c'est “Professeur Layton vs. Phoenix Wright: Ace Attorney“, ce jeu mélange la résolution d'énigme avec Layton et la résolution de jugement avec Phoenix Wright dans un monde médiéval."
                    show isi question
                    show sao fier
                    s "Le parti pris de ce jeu est énorme même si les deux milieux sont assez proches. Car les deux licences ne parlent pas des mêmes sujets et ont des gameplay complètement éloignés l'un de l'autre."
                    i " Intéressant. Je l'essayerais et je te donnerais mon avis."
                    show sao neutral
                    show isi neutral
                    s "Bon, on fait quoi comme type de crossover du coup ?"

                    menu:
                        "Hack'n'Slash":
                            show isi happy
                            i "Moi j’aime bien les Hack’n’Slash !"
                            show sao happy
                            s "Ouais pareil ! C’est tellement agréable de se défouler !"
                            s "Foncer dans le tas, taper tout ce qui bouge, balancer des gros ulti dans la foule et voir une horde de cadavres voltiger…"
                            show isi embarras
                            i "Ça fait terriblement glauque dit comme ça…"
                            show sao fier
                            s "Pourtant c’est bien là que réside tout le plaisir."
                            show isi neutral
                            i "En même temps y’a pas plus satisfaisant : ton personnage, au milieu d’une map, des ennemies en masse et tu les tabasses !"
                            show isi happy
                            i "Ce genre de jeu n’existe que pour faire voltiger des tonnes et des tonnes d'ennemis, puisqu’on en élimine à la pelle !"
                            show sao happy
                            s "D’où le nom !"
                            show sao neutral
                            show isi neutral
                            s "“Hack’n’Slash” ! Tailler et trancher ! On ne fait que de zigouiller des monstres !"
                            show isi question
                            i "Même si le principe du jeu est de tapper dans la masse, le fait qu’il y ait uncôté gestion avec l’amélioration de tes armes de tes personnages et de lieux qui vont te permettre d’être plus puissant est vraiment sympa. "
                            i "C’est comme une zone de calme où tu peux trouver un peu de repos."
                            s "Ça rajoute un côté humain."
                            show isi neutral
                            i "Un côté humain dans un monde un monde un peu gore."
                            show sao happy
                            s "Le principe des Hack’n’Slash quoi."
                            show sao neutral
                            show isi fier
                            i "Franchement Koei Tecmo et Omega Force ils sont vraiment forts, parce qu’ils ont été les précurseurs du genre, et honnêtement Samurai Warrior est le pilier des Hack’n’Slash !"
                            i "Le point positif de ce jeu est qu’il y a un large panel de personnage, et donc à un large panel de technique d’armes et d’attaque ultime bien badass qui détruisent des centaines d’ennemis en même temps."
                            show isi neutral
                            show sao dout
                            s "C’est vrai que pouvoir que pouvoir lâcher pleins de grosses attaques diverses ça rend le jeu moins monotone."
                            show isi surpris
                            show sao neutral
                            i "Ce qui a bien été amené par les développeurs lors de la création du jeu, c’est que l’on ne se bat pas sans aucune raison."
                            show isi neutral
                            i "Il y a une histoire tout au long du jeu, histoire qui va intégrer le joueur entièrement dans le jeu en plus d’ajouter de la profondeur à celui-ci."
                            show sao happy
                            show isi happy
                            s "Qui ne rêverait pas de se battre en étant dans la peau des plus grandsguerriers du Japon, avec des katanas, des lances et des pouvoirs…"
                            si "LES SAMOURAÏ !!!"
                            show isi neutral
                            show sao neutral
                            i "C’est après la sortie du 5ème opus de cette licence que Nintendo va sauter sur l’occasion afin de faire une collaboration avec ces deux entreprises afin de donner vie à leur meilleur Hack’n’Slash, Hyrule Warrior l’ère du fléau."
                            s "On peut plutôt parler d’un crossover vu que c’est littéralement les mécaniques de Samurai Warrior avec les armes, les personnages et l’histoire de Zelda Breath of the Wild."
                            i "C’est quand même trop cool de pouvoir exploser la face de milliers de Bokoblins avec Link ou bien même Impa et ces techniques de ninjutsu."
                             
                            jump FinMardi

                        "SandBox":
                                show isi question
                                i "Et si on faisait un jeu SandBox ?"
                                s "Un jeu où on peut faire ce que l’on veut , ça peut être une bonne idée de laisser libre court à l’imagination du joueur."
                                show isi neutral
                                i "Moi j’aime bien ce genre de jeux, généralement ils sont sans prise de tête."
                                show isi happy
                                i "T’es posé dans ton canap et tu kiff."
                                show sao dout
                                s "Moi je préfères les jeux un peu plus dynamique, qui demande de la réflexions."
                                show sao neutral
                                show isi surpris
                                i "Tous les SandBox ne sont pas forcément des jeux où tu peux mettre ton cerveau en off."
                                show isi neutral
                                i "Minecraft par exemple, c’est le plus grand SandBox de tous les temps et lejeu le plus vendu au monde. Même si au premier abord avec le style graphique et le principe du jeu selon lequel tu peux construire ce que tu veux avec des blocs."
                                i "Bien qu’il soit démuni d’une quelconque histoire, le jeu a un objectif bien précis: tu apparais dans l’OverWorld où tu vas chercher à te procurer les matériaux les plus importants. "
                                show isi fier
                                show sao surpris
                                i "Une fois cela fait, tu vas t'aventurer dans le Nether où tu vas de nouveau devoir te procurer les matériaux de cet environnement afin d’aller dans l’Ender et battre le boss ultime de ce jeu, l’Ender Dragon."
                                show sao confus
                                show isi neutral
                                s "C’est pas vraiment un jeu bac à sable alors, comme il y a un objectif précis à accomplir."
                                show isi question
                                i "Et bien si, car tu n'es pas obligé de suivre cette trame. Si tu désires vivre une vie paisible et construire un village c’est possible, tu peux aussi t’amuser un miner afin de trouver du diamant ou des émeraudes."
                                show sao happy
                                show isi neutral
                                s "Après avec le mode créatif c’est plus simple de faire de belle construction qu’en mode survie."
                                show isi happy
                                i "C’est sûr."
                                show isi neutral
                                show sao surpris
                                s "Il y a aussi une licence qui base ses jeux sur la création libre comme ça."
                                show sao neutral
                                show isi happy
                                i "Animal Crossing est l’exemple type lui aussi. Surtout avec la sortie du dernier opus sur Nintendo Switch."
                                show sao happy
                                show isi neutral
                                s "New Horizon ! Ce jeu où tu t’installes sur une île déserte que tu vas développer au fil du temps et que tu peux entièrement modifié comme bon te semble."
                                i "C’est un très bon jeu qui  reflète assez bien la réalité, avec son système de craft d’objet, le cycle jour/nuit qui suit le notre, la pêche de poisson et la chasse aux insectes."
                                s "En plus il y a aussi un système monétaire. On doit rembourser les prêts que l’on a fait pour construire notre maison."
                                show sao colere
                                show isi colere
                                si "Ah, Tom Nook le fameux tanuki capitaliste."
                                show isi neutral
                                show sao neutral
                                i "Le jeu est sorti pendant le COVID et il a permis à tellement de personne de se changer les idées pendant cette période compliquée."
                                show sao surpris
                                s "Il y a même des anniversaire et des mariages qui ont été célébrés sur ce jeu."
                                show sao neutral
                                show isi happy
                                i "Voilà une belle preuve qui montre que dans ce jeu tout est possible."

                                jump FinMardi


init python:
    # must be persistent to be able to record the scores
    # after adding new songs, please remember to delete the persistent data

    rhythm_game_songs = [
    Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt'),
    Song('Positivity', 'audio/Positivity.mp3', 'audio/Positivity.beatmap.txt'),
    Song('Pearlescent', 'audio/Pearlescent.mp3', 'audio/Pearlescent.beatmap.txt'),
    Song('Pearlescent - trimmed', 'audio/Pearlescent - trimmed.mp3', 'audio/Pearlescent - trimmed.beatmap.txt'), # 22 sec, easy to test 
    Song('Thoughts', 'audio/Thoughts.mp3', 'audio/Thoughts.beatmap.txt')
    ]

    # # init
    # if persistent.rhythm_game_high_scores:
    #     for song in songs:
    #         if not song in persistent.rhythm_game_high_scores:
    #             persistent.rhythm_game_high_scores[song] = (0, 0)

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
default selected_song = None
label FinMardi:

    scene black
    with dissolve

    "Après cette journée remplie de réflexions, nos deux amis vont avoir besoin de méditer sur leurs idées de projet à tête reposée."
    "Il en va de soit que le squelette de leur jeu doit être sélectionné avec rigueur. "
    "Mais pour le moment, il me semble qu'il serait mieux de laisser vaquer à leur occupation tant qu'ils le peuvent."
    "D'ailleurs c'est aujourd'hui qu'ils ont tous deux une activité extrascolaire, que voulez-vous faire ?"

    menu: 
        "Faire du théâtre avec Sao Mai.":
            jump music

        "Faire du basket avec Isidore.":
            jump basket

init:   
    image bg training-room = "assets/minigame_fish_catcher/training-room.png"
    
    python:
        import random
        import pygame
                
        class Basket():
            def __init__( self ):
                self.image = Image( "assets/minigame_fish_catcher/basket.png" )
                self.active = False
                self.dimensions = [ 100, 150 ]
                self.position = [ 0, 0 ]
                self.speed = [ 0, 10 ]
                self.maxY = 275
            # __init__
            
            def createNew( self ):
                self.position[0] = random.randrange( 0, 8 ) * 100
                self.position[1] = 0 - self.dimensions[1]                  # Start off-screen
                self.speed[1] = random.randrange( 2, 10 )
                self.active = True
            # createNew
            
            def update( self, deltaTime ):
                if ( self.active ):
                    self.position[1] += self.speed[1]
                
                if ( self.position[1] > self.maxY ):
                    self.active = False
            # update
            
            def isCaught( self, SakuragiPosition, SakuragiDimensions ):
                if ( SakuragiPosition[0] < self.position[0] + self.dimensions[0] and
                        SakuragiPosition[0] + SakuragiDimensions[0] > self.position[0] and
                        SakuragiPosition[1] < self.position[1] + self.dimensions[1] and
                        SakuragiPosition[1] + SakuragiDimensions[1] > self.position[1] ):
                    self.active = False
                    return True
                
                return False
            # isCaught
            
            def render( self, renderer, shownTimebase, animationTimebase ):
                if ( self.active ):
                    r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                    renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render 
        # Fish
    
        class Player():
            def __init__( self ):
                self.image = Image( "assets/minigame_fish_catcher/Sakuragi.png" )
                self.dimensions = [ 100, 150 ]
                self.position = [ 600, 600 ]
                self.speed = [ 100, 20 ]
                self.grabCounter = 0
                self.grabCounterMax = 20
                self.action = "NONE"
                self.score = 0
            # __init__
            
            def handleInput( self, action ):
                if ( self.grabCounter <= 0 ):
                    self.action = action
            # handleInput
            
            def update( self, deltaTime ):
                if ( self.grabCounter > 0 ):
                    if ( self.grabCounter > self.grabCounterMax/2 ):
                        self.position[1] -= self.speed[1] * deltaTime
                    else:
                        self.position[1] += self.speed[1] * deltaTime
                        
                    self.grabCounter -= 1
                    if ( self.grabCounter == 0 ):
                        self.position[1] = 450
                        
                else:
                    if ( self.action == "LEFT" and self.grabCounter <= 0 ):
                        self.position[0] -= self.speed[0] * deltaTime
                    
                    elif ( self.action == "RIGHT" and self.grabCounter <= 0 ):
                        self.position[0] += self.speed[0] * deltaTime
                    
                    elif ( self.action == "GRAB" and self.grabCounter <= 0 ):
                        self.grabCounter = self.grabCounterMax
                    
                    # Adjust position - can't go off screen!
                    if ( self.position[0] < 0 ):
                        self.position[0] = 0
                    elif ( self.position[0] > 800 - self.dimensions[0] ):
                        self.position[0] = 800 - self.dimensions[0] 
                
                self.action = "NONE"
            # update
            
            def render( self, renderer, shownTimebase, animationTimebase ):
                r = renpy.render( self.image, 800, 600, shownTimebase, animationTimebase )
                renderer.blit( r, ( self.position[0], self.position[1] ) )
            # render
        # Player
    
        class FishCatcherGame( renpy.Displayable ):
        
            def __init__( self ):
                renpy.Displayable.__init__( self )
                
                # Maybe I'll write a sub-class for this stuff
                self.player = Player()
                
                self.debug = []
                self.counter = 0
                
                self.basket = []
                self.basketCaught = 0
                
                self.lastStart = None   
                self.frameRate = 60
                
                self.clock = pygame.time.Clock()
                self.countdown = 30
                self.milliseconds = 0
                
                self.gameover = False
            # __init__
            
            def event( self, event, x, y, shownTimebase ):
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.handleInput( "GRAB" )
                    # Up Key
                    
                    if event.key == pygame.K_LEFT:
                        self.player.handleInput( "LEFT" )
                    # Left Key
                    
                    if event.key == pygame.K_RIGHT:
                        self.player.handleInput( "RIGHT" )
                    # Right Key
                # KEYDOWN
                         
            # event
            def update( self, shownTimebase, animationTimebase ):
                delta = self.getDelta( shownTimebase )
                rate = 1000 / self.frameRate
                speedAdjust = delta * rate
                
                if ( self.gameover == False ):
                
                    chance = random.randrange( 0, 20 )
                    if ( chance == 0 and len( self.basket ) < 5 ):
                        basket = Basket()
                        basket.createNew()
                        self.basket.append( basket )
                    
                    removalList = []
                    # TODO: There is probably a more Python-idiomatic way to do this
                    for basket in self.basket:
                        basket.update( 1 )
                        
                        if ( basket.isCaught( self.player.position, self.player.dimensions ) ):
                            self.player.score += 1
                        
                        if ( basket.active == False ):
                            removalList.append( basket )
                    
                    for basket in removalList:
                        self.basket.remove( basket )
                        
                    self.player.update( 1 )
                    
                    if ( self.milliseconds > 1000 ):
                        self.countdown -= 1
                        self.milliseconds = 0
                    
                    self.milliseconds += self.clock.tick_busy_loop( 60 )
                    if ( self.countdown <= 0 ):
                        self.gameover = True
                    
                    # TODO: Remove
                    del self.debug[:]
                    self.debug.append( "Déboguer" )
                    self.debug.append( "Aléatoire:  " + str( chance ) )
                    self.debug.append( "Position de Sakuragi : " + str( self.player.position[0] ) + ", " + str( self.player.position[1] ) )
                    for basket in self.basket:
                        self.debug.append( "Position du panier: " + str( basket.position[0] ) + ", " + str( basket.position[1] ) + ", Active: " + str( basket.active ) )
                    self.debug.append( "Delta : " + str( delta ) )
                    
                # Run while game is not over
            # update
            
            def render( self, width, height, shownTimebase, animationTimebase ):
                self.update( shownTimebase, animationTimebase )
                renderer = renpy.Render( width, height )
                
                if ( self.gameover == False ):
                    for basket in self.basket:
                        basket.render( renderer, shownTimebase, animationTimebase )
                    
                    self.player.render( renderer, shownTimebase, animationTimebase )

                    counter = 0
                    for debug in self.debug:
                        txt = Text( _( debug ), size= 10 )
                        textRender = renpy.render( txt, 800, 600, shownTimebase, animationTimebase )
                        renderer.blit( textRender, ( 0, 10 * counter ) )
                        counter += 1
                
                if (self.gameover == True): #Gameover
                    # Temporary
                    txt = Text( _( "Fin de l'entrainement" ), size= 40 )
                    renderer.blit( renpy.render( txt, 800, 600, shownTimebase, animationTimebase ), ( 725, 400 ) )
                       
                txtScore = Text( _( "Time : " + str( self.countdown ) ), size= 30 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 1700, 0 ) )
                txtScore = Text( _( "Points " + str( self.player.score ) ), size=30 )
                renderer.blit( renpy.render( txtScore, 800, 600, shownTimebase, animationTimebase ), ( 1700, 40 ) )
                renpy.redraw( self, 0 )
                
                return renderer     
            # render
            
            def per_interact( self ):
                renpy.timeout( 0 )
                renpy.redraw( self, 0 )
            # per_interact
            
            def getDelta( self, shownTimebase ):
                if self.lastStart is None:
                    self.lastStart = shownTimebase
                        
                delta = shownTimebase - self.lastStart
                self.lastStart = shownTimebase
                
                return delta

label basket:
    scene black
    with dissolve
    "Bienvenue dans le mini-jeu Basket Training !"
    "Dans ce mini-jeu ton objectif est de faire en sorte que Sakuragi marque un maximmum de panier !"
    "Pour cela tu vas pouvoir l'aider à se déplacer grâce aux flèches gauche et droite de ton clavier."
    "De plus tu peux aller chercher les paniers à l'aide de la flèche du haut."
    menu:
        "On commence l'entrainement !!":
            play music "audio/SlamDunk.mp3" volume 0.5 noloop
            jump fish_catcher

label fish_catcher:    
    window hide None
    scene bg training-room
    with fade
    python:
        ui.add( FishCatcherGame() )
        ui.interact( suppress_overlay=True, suppress_underlay=True )
    jump Mercredi


label music:
    scene bg room

    "Bienvenue dans le jeu de rythme Ren’Py ! Choisissez la chanson que vous souhaitez jouer."

    window hide
    call rhythm_game_entry_label

    "Bravo ! Vous devriez être musicien !"
    "Sao Mai a redoublé 2 fois son diplôme de musique avant de se faire renvoyé du conservatoire durant le covid."
    "Mais vous êtes meilleurs !"

    jump Mercredi

# a simpler way to launch the minigame 
label test:
    "Bienvenue au jeu de rythme Ren’Py! Prêt pour un défi ?"
    window hide
    $ quick_menu = False

    # avoid rolling back and losing chess game state
    $ renpy.block_rollback()

    $ song = Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt', beatmap_stride=2)
    $ rhythm_game_displayable = RhythmGameDisplayable(song)
    call screen rhythm_game(rhythm_game_displayable)

    # avoid rolling back and entering the chess game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

label Mercredi:
    scene bg nsi
    show sao neutral at left with easeinright
    show isi neutral at right with easeinleft
    show sao happy
    s "Salut, alors tu sais ce que tu veux que l'on fasse comme jeux ?"
    show isi question
    i "Je pensais à un visual novel."
    show sao dout
    show isi neutral
    s "Un visual Novel ? Tu veux faire une histoire ?"
    show isi happy
    show sao neutral
    i "Oui ça peut être sympa. En plus comme ça on design l'entièreter du jeu. "
    s "C'est une bonne idée, mais moi je vois pas se que l'on pourrait raconter."
    show isi question
    show sao surpris
    i " Et si notre jeu racontais notre aventure sur la recherche et la création de notre jeu ?"
    show sao happy
    s " C'est super original ! On l'appelerai comment ?"
    show isi question
    show sao neutral
    i "Mmmh..."
    show isi happy
    show sao happy
    i "Le jeu !"    

    jump crédits


label crédits:

    #Outro
    scene black
    with dissolve

    show text "Merci d'avoir jouer à notre jeu !" with dissolve
    $ renpy.pause(1.0)
    show text "Créé par Saoi Mai et Isidore" with dissolve
    $ renpy.pause(1.0)
    show text "Sprites réalisé par Sao Mai" with dissolve
    $ renpy.pause(1.0)
    show text "Réalisation du code par Sao Mai et Isidore" with dissolve
    $ renpy.pause(1.0)
    show text "Scénario Sao Mai et Isidore" with dissolve
    $ renpy.pause(1.0)
    hide text with dissolve