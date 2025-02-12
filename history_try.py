def scores_history(BASE_DIR):
    score_hist= []
    with open (os.path.join(BASE_DIR,"score.json"), "r") as f:
            player_list= json.load(f)      
    for i, player in enumerate(player_list):
       score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
    return score_hist        


def Score(screen, image, rect, ubuntu_font, WHITE, YELLOW, BASE_DIR, language):
    score = scores_history(BASE_DIR)
    vertical_pos = rect.top + 0
    pygame.Surface.blit(screen, image, (0, 0))

    # Display the title "SCORE BOARD"
    title_text = LARGE_FONT.render(texts[language]["score_board"], True, WHITE)
    title_rect = title_text.get_rect(center=(rect.centerx, rect.top + 0))
    screen.blit(title_text, title_rect)
    vertical_pos += 60
    
    # Display the scores
    for i, score_text in enumerate(score):
        font_score = ubuntu_font.render(score_text, True, WHITE)
        font_rect = font_score.get_rect(midtop=(rect.centerx, vertical_pos))
        screen.blit(font_score, font_rect)
        vertical_pos += 40

    # Create the "Back to Menu" button
    button_width = 200
    button_height = 50
    back_button_rect = pygame.Rect(10, screen.get_height() - button_height - 10, button_width, button_height)
    pygame.draw.rect(screen, YELLOW, back_button_rect)
    
    # Button text
    back_button_text  = ubuntu_font.render(texts[language]["return_menu"], True, (255, 255, 255))  # Blanc

    back_button_text_rect = back_button_text.get_rect(center=back_button_rect.center)
    screen.blit(back_button_text, back_button_text_rect)

    pygame.display.update()

    # Handle mouse click events
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button_rect.collidepoint(event.pos):
                back_ground_sound.stop()
                sword_1.play()
                main()


def add_points(score_container, player_name, points):
    for element in score_container:
        if element["name"] == player_name:
            element["score"] += points
            return score_container

def record_history(score, player_name):
    # Chemin du fichier score.json
    score_file = os.path.join(BASE_DIR, "score.json")
    
    # Lire les scores existants
    try:
        with open(score_file, "r") as f:
            score_container = json.load(f)
    except FileNotFoundError:
        # Si le fichier n'existe pas, initialiser une liste vide
        score_container = []
    except json.JSONDecodeError:
        # Si le fichier est mal formaté, initialiser une liste vide
        score_container = []
    
    # Mettre à jour le score du joueur existant ou ajouter un nouveau joueur
    player_found = False
    for player in score_container:
        if player["name"] == player_name:
            player["score"] += score
            player_found = True
            break
    
    if not player_found:
        score_container.append({"name": player_name, "score": score})
    
    # Trier les scores par ordre décroissant
    score_container = sorted(score_container, key=lambda x: x["score"], reverse=True)
    
    # Enregistrer les scores dans le fichier
    with open(score_file, "w") as f:
        json.dump(score_container, f, indent=4)  # indent=4 pour un formatage lisible