import pygame
import sys
import os
import json

class Display:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.text = [
            "New game",
            "Score",
            "Exit",
            "Easy",
            "Normal",
            "Hard",
            "main menu"
        ]
        
        self.language ="en" #Default language English
        self.language_text = self.lang[self.language]["language"] # "language' display with the menu
        """"texts[language]["language"] extracts the value associated with the key "language".
This key is used to display a button that allows changing the language.
If language is "en", the obtained value is "FR" (to offer switching to French).
If language is "fr", the obtained value is "EN" (to offer switching to English)."""

        self.lang = {
            "en": {
                "new_game": "New Game",
                "score_history": "Score History",
                "exit": "Exit",
                "language": "FR",
                "you_win": "You Win",  
                "you_lose": "You Lose",
                "enter_name": "Enter your name:",
                "return_menu": "Return menu",
                "score_board": "SCORE BOARD",
                "missed" : "Missed"
            },
            "fr": {
                "new_game": "Nouvelle Partie",
                "score_history": "Historique des Scores",
                "exit": "Quitter",
                "language": "EN",
                "you_win": "Vous avez gagné", 
                "you_lose": "Vous avec perdu" ,
                "enter_name": "Entrez votre nom :", 
                "return_menu": "Retour menu",
                "score_board": "TABLEAU SCORES",
                "missed" : "Loupés"
            }
        }


        self.rect1 = pygame.Rect(400,300, 400, 50)
        self.rect2 = pygame.Rect(400, 400, 400, 50)
        self.rect3 = pygame.Rect(400, 500, 400, 50)
        self.rect4 = pygame.Rect(100,100, 1000, 400)
        self.rect5 = pygame.Rect(500,0, 200, 50)
        self.language_rect = pygame.Rect(10, 10, 150, 50)
        self.color = (253, 165,15)
        self.running = True
        self.state = "main menu"

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "main menu":

                    if self.rect1.collidepoint(event.pos):
                        self.state = "difficulty"
                    if self.rect2.collidepoint(event.pos):
                        self.state = "score"
                    if self.rect3.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

                elif self.state == "score":
                    if self.rect5.collidepoint(event.pos):
                        self.state = "main menu"
                elif self.language_rect.collidepoint(event.pos):  # Verify if the button is used 
                        language = "fr" if language == "en" else "en"  # If the button is used, the language is set

                
                


    def display_menu(self):
        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)

        
        text1 = self.font.render(self.text[0], True, (0, 0, 0))
        text2 = self.font.render(self.text[1], True, (0, 0, 0))
        text3 = self.font.render(self.text[2], True, (0, 0, 0))

        
        self.screen.blit(text1, text1.get_rect(center=self.rect1.center))
        self.screen.blit(text2, text2.get_rect(center=self.rect2.center))
        self.screen.blit(text3, text3.get_rect(center=self.rect3.center))

    def display_difficulty(self):

        pygame.draw.rect(self.screen, self.color, self.rect1)
        pygame.draw.rect(self.screen, self.color, self.rect2)
        pygame.draw.rect(self.screen, self.color, self.rect3)

        
        text1 = self.font.render(self.text[3], True, (0, 0, 0))
        text2 = self.font.render(self.text[4], True, (0, 0, 0))
        text3 = self.font.render(self.text[5], True, (0, 0, 0))

        
        self.screen.blit(text1, text1.get_rect(center=self.rect1.center))
        self.screen.blit(text2, text2.get_rect(center=self.rect2.center))
        self.screen.blit(text3, text3.get_rect(center=self.rect3.center))


    def display_score(self, score):
        vertical_pos =self.rect4.top + 20
        pygame.draw.rect(self.screen, self.color, self.rect4)
        pygame.draw.rect(self.screen, self.color, self.rect5)

        text1 = self.font.render(self.text[6], True, (0, 0, 0))


        for i, score_text in enumerate(score):
            text2 = font_score = self.font.render(score_text, True,(0, 0, 0))  
            font_rect = font_score.get_rect(midtop=(self.rect4.centerx, vertical_pos))  
            self.screen.blit(text2, font_rect)
            vertical_pos += 40
        
        
        self.screen.blit(text1, text1.get_rect(center=self.rect5.center))
       

    def scores_history():
        score_hist= []
        with open (os.path.join("score.json"), "r") as f:
                player_list= json.load(f)      
        for i, player in enumerate(player_list):
            score_hist.append(f'{i+1}. {player["name"]} => {player["score"]}')
        return score_hist
        
        
    def display(self):
        if self.state == "main menu":
            self.display_menu()
        elif self.state == "difficulty":
            self.display_difficulty()
        elif self.state == "score":
            score = Menu.scores_history()
            Menu.display_score(self, score)

    def display_languages(self):
        # Draw the button for languages
        pygame.draw.rect(screen, yellow, self.language_rect)
        font_dis_lang = font.render(self.language_text, 1, white) # diqplay font used
        font_rect_lang = font_dis_lang.get_rect(center=self.language_rect.center)
        screen.blit(font_dis_lang, font_rect_lang)


#Exemples d'utilisation du changement de langue dans le code:
prompt_text = font.render(texts[language]["enter_name"], True, (255, 255, 255))  # Blanc
screen.blit(prompt_text, ((SCREEN_WIDTH - prompt_text.get_width()) // 2, SCREEN_HEIGHT // 3))

lose_text = LARGE_FONT.render(self.lang[self.language]["you_lose"], True, RED)
screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))


        


