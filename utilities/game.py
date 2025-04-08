import time
import os

from utilities.file_handler import Json_Handler
from gui.interactions import update_stats_table, delete_all_entries, add_list_to_textbox, gui_initialize, gui_input, add_list_to_textbox_slow, add_text_to_textbox, add_text_to_textbox_slow, add_dict_to_textbox, add_dict_to_textbox_slow, add_choice_button, delete_choice_buttons

class Game():

    json_file_path = "./modules/story_text.json"
    sleep_time = 0.05
    main_character = ""
    separator_length = 120
    MainWindowInstance = None
    gui_mode = True
    color_scheme = "Default"

    def __init__(self) -> None:
        pass

    @staticmethod
    def start():
        """## Starts the game loop"""
        if not Game.gui_mode:
            Story.story_loop(Game.main_character)
        else:
            gui_initialize()
            Game.wait_for_main_window()

    @staticmethod
    def wait_for_main_window():
        """## Waits for the main window to be open"""
        from gui.interactions import root
        if Game.MainWindowInstance:
            Story.story_loop(Game.main_character)
        else:
            if hasattr(Game.MainWindowInstance, "after"):
                Game.MainWindowInstance.after(100, Game.wait_for_main_window)
            else:
                if root:
                    root.after(100, Game.wait_for_main_window)

    @staticmethod
    def clear_terminal():
        """## Clears the terminal"""
        if not Game.gui_mode:
            os.system("cls")
        else:
            delete_all_entries(Game.MainWindowInstance)

    @staticmethod
    def dict_print(in_dict: dict, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False):
        """## Prints a dictionary
        Can also print seperator lines and newlines above and below the dict.
        
        Args:
            in_dict (dict): The dictionary to print
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")
            for key, value in in_dict.items():
                print(f'{key}: {value}')
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator()
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            add_dict_to_textbox(Game.MainWindowInstance, in_dict)
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance,"")
            if separator_bottom:
                Game.separator()

    @staticmethod
    def slow_dict_print(in_dict: dict, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False):
        """## Prints a dictionary using the slow print method
        Can also print seperator lines and newlines above and below the dict.
        
        Args:
            in_dict (dict): The dictionary to print
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")
            for key, value in in_dict.items():
                Game.slow_print(f'{key}: {value}')
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator()
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            add_dict_to_textbox_slow(Game.MainWindowInstance, in_dict, Game.sleep_time)
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance, "")
            if separator_bottom:
                Game.separator()
        
    @staticmethod
    def slow_print(in_str: str, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False):
        """## Prints a string slowly
        Can also print seperator lines and newlines above and below the dict.

        Args:
            in_str (str): The string to print
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")
            for char in in_str + "\n":
                print(char, end = "", flush = True)
                time.sleep(Game.sleep_time)
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator()
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            add_text_to_textbox_slow(Game.MainWindowInstance, in_str, Game.sleep_time)
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance, "")
            if separator_bottom:
                Game.separator()
    
    @staticmethod
    def slow_input(in_str: str, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False, callback=None):
        """## Input with slow print prompt
        Calls the input method with the slow print as the prompt

        Args:
            in_str (str): The string to print in the input
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.

        Returns:
            value (str): User input
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")      
            for char in in_str:
                print(char, end = "", flush = True)
                time.sleep(Game.sleep_time)
            value = input()
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator()
            return value
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            gui_input(Game.MainWindowInstance, lambda _, value: callback(value) if callback else None, in_str)
            if Game.MainWindowInstance.input_callback_value is not None:
                Game.MainWindowInstance.input_callback_value = None
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance, "")
            if separator_bottom:
                Game.separator()
            return Game.MainWindowInstance.input_callback_value

    @staticmethod
    def enter(separator_top: bool = False, new_line_top=False, callback=None):
        """## Checks if enter is pressed
        Returns true if the user presses enter
        
        Args:
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.

        Returns:
            True (bool): when pressed 
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")
            pressed = input("Drücke die Eingabe-Taste>\n")
            if pressed:
                return True
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            gui_input(Game.MainWindowInstance, lambda _, __: callback() if callback else None, "V Drücke die Eingabe-Taste V")
            if Game.MainWindowInstance.input_callback_value is not None:
                Game.MainWindowInstance.input_callback_value = None
                return True

    @staticmethod
    def separator():
        """## Prints a separator line
            Prints a line of dashes to the console
        """
        separator = ""
        for _ in range(Game.separator_length):
            separator += "-"
        if not Game.gui_mode:
            print(separator)
        else:
            add_text_to_textbox(Game.MainWindowInstance, separator)

    def reset_attribute(self, class_name, attributes: list):
        """## Resets attributes of a class
        Resets the attributes of a class to their default values as saved in initial_values

        Args:
            class_name (str): The name of the class to reset
            attributes (list): A list of the attributes to reset
        """
        for attribute in attributes:
            if hasattr(class_name, attribute):
                setattr(class_name, attribute, self.initial_values[attribute])

class Entity(Game):
    """## Entity class
    A class representing an entity in the game

    Attributes:
        name (str): The name of the entity
        inventory (dict): Dict containing the inventory
        attributes (dict): Dict containing the attributes like health, strength, etc.
    """
    def __init__(self, name: str, inventory: dict, attributes: dict):
        self.name = name
        self.inventory = inventory
        self.attributes = attributes

    @staticmethod
    def in_inventory(check_items: dict):
        """## Checks if items are in inventory
        Accesses the text_not_inv in the json if the items are not in the inventory

        Args:
            check_items (dict): A dictionary containing the items to check
        """
        for key, value in check_items.items():
            if key in Game.main_character.inventory:
                if Game.main_character.inventory[key] >= value:
                    return True
                else:
                    Story.story_loop(Game.main_character, "text_not_in_inv")
            else:
                Story.story_loop(Game.main_character, "text_not_in_inv")

    def add_inventory(self, additive: dict):
        """## Adds items to inventory
        Adds item in additive to the inventory

        Args:
            additive (dict): A dictionary containing the items to add
        """
        for key, value in additive.items():
            if key == "Münzen":
                self.attributes["Münzen"] += value
            else:
                if key in self.inventory:
                    self.inventory[key] += value
                else:
                    self.inventory[key] = value

    def add_inventory_room(self, items: dict):
        """## Adds items to inventory from room
        Only adds items to inventory if they are also in the room inventory

        Args:
            items (dict): A dictionary containing the items to check and add
        """
        current_room_name = Game.main_character.current_location
        current_room = eval(current_room_name)
        for item, quantity in items.items():
            if item in current_room.inventory and current_room.inventory[item] >= quantity:
                if item == "Münzen":
                    self.attributes["Münzen"] += quantity
                else:
                    if item in self.inventory:
                        self.inventory[item] += quantity
                    else:
                        self.inventory[item] = quantity
                    current_room.inventory[item] -= quantity

    def sub_inventory(self, subtract: dict): 
        """## Subtracts items from inventory
        Subtracts item in subtract from the inventory

        Args:
            subtract (dict): A dictionary containing the items to subtract
        """
        for key, value in subtract.items():
            if key == "Münzen":
                initial_value = self.attributes["Münzen"]
                new_value = initial_value - value
                self.attributes["Münzen"] = new_value
            else:
                initial_value = self.inventory[key] = value
                new_value = initial_value - value
                self.inventory[key] = new_value

    def display_inventory(self):
        """## Displays the inventory of the player
        Prints the current inventory of the player using slow print
        """
        Game.clear_terminal()
        Game.slow_print(f'{self.name} hat folgendes in seinem Inventar:', separator_top = True, new_line_top = True)
        if len(self.inventory) > 0:
            Game.dict_print(self.inventory, separator_bottom = True, new_line_bottom = True)
        else:
            Game.slow_print("Dein Inventar ist leer!", separator_bottom = True, new_line_bottom = True)
        Game.enter()   
        Story.story_loop(Game.main_character, sub_chapter_index = 1)

    def display_status(self):
        """## Displays the status of the player
        Prints the current status of the player using slow print
        """
        Game.clear_terminal()
        Game.slow_print(f'{self.name} hat folgenden Status:', separator_top = True, new_line_top = True)
        Game.slow_dict_print(Game.main_character.attributes, separator_bottom = True, new_line_bottom = True)
        Game.enter()
        Story.story_loop(Game.main_character, sub_chapter_index = 1)

class Room(Game):
    """## Room class
    A class used to represent a room in the game

    Attributes:
        name (str): The name of the room
        choices (list): Choices in the room
        next_rooms (list): Rooms corresponding to the choices
        inventory (dict): Items in the room
    """
    def __init__(self, name: str, choices: list, next_rooms: list, inventory: dict) -> None:
        self.__name = name
        self.choices = choices
        self.next_rooms = next_rooms
        self.__inventory = inventory

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        if "_" in value:
            self.__name = value
        else:
            raise ValueError("Name of Room instance must include at least one underline")

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, value: dict):
        if isinstance(value, dict):
            self.__inventory = value
        else:
            raise TypeError("Inventory must be a dictionary")

class Player(Entity):
    """## Player class
    Class representing a Player in the game

    Attributes:
        inventory (dict): Items in the player's inventory
        attributes (dict): Attributes of the player like health, strength, etc.
        current_location (str): The current location of the player
    """
    initial_values = {
        "xp_points": 10
    }

    def __init__(self, inventory: dict, attributes: dict, current_location: str) -> None:
        self.__inventory = inventory
        self.__attributes = attributes
        self.current_location = current_location
        self.name: str = "Player"
        self.xp_points: int = 10

    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, value: dict):
        if isinstance(value, dict):
            self.__inventory = value
        else:
            raise TypeError("Inventory must be a dictionary")
        
    @property
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value: dict):
        if isinstance(value, dict):
            self.__attributes = value
        else:
            raise TypeError("Attributes must be a dictionary")

    def satisfied(self, func_name: str, callback=None):
        """## Checks if the player is satisfied
        Checks if the player is satisfied with their input

        Args:
            func_name (str): function to be evaled if player is not satisfied
        """
        if not Game.gui_mode:
            flag = True 
            while flag: 
                value = str(Game.slow_input("Zufrieden? (y/n)>\n", separator_bottom = True, new_line_top = True))
                if value.lstrip().strip().lower() in ["yes", "y", "ja"]:
                    flag = False
                if value.lstrip().strip().lower() in ["no", "n", "nein"]:
                    eval(f'self.{func_name}()')
                    flag = False
                else:
                    Game.slow_print("Bitte gib y oder n ein!")
        else:
            def ask_satisfaction():
                Game.slow_input("Zufrieden? (y/n)>", new_line_top=True, callback=process_response)
            def process_response(value):
                value = value.strip().lower()
                if value in ["yes", "y", "ja"]:
                    if callback:
                        callback()
                elif value in ["no", "n", "nein"]:
                    eval(f'self.{func_name}(callback=ask_satisfaction)')
                else:
                    Game.slow_print("Bitte gib y oder n ein!")
                    ask_satisfaction()
            ask_satisfaction()

    def set_name(self):
        """## Sets the player's name
        Sets the player's name and makes sure it cant be longer than 15 characters or empty
        """
        if not Game.gui_mode:
            Game.clear_terminal()
            flag = True
            while flag:
                value = str(Game.slow_input("Wie soll dein Charakter heißen?>\n", separator_top = True, new_line_top = True, new_line_bottom = True).lstrip().strip())
                if len(value) <= 15 and len(value)> 0:
                    self.name = value
                    Game.slow_print(f'Der Name deines Charakters lautet {self.name}!', separator_top = True, separator_bottom = True, new_line_top = True, new_line_bottom = True)
                    self.satisfied("set_name")
                    flag = False
                else:
                    Game.slow_print("Der Name darf nicht 0 Zeichen oder länger als 15 Zeichen sein!")
        else:
            self.name = Game.MainWindowInstance.player_name

    def set_points(self, callback=None):
        """## Lets the player set their xp points
        Lets the player assign xp points to each attribute
        """
        if not Game.gui_mode:
            Game.clear_terminal()
            self.reset_attribute(Game.main_character, ["xp_points"])
            attribute_str = ""
            for key in self.attributes:
                attribute_str += key
                if key == list(self.attributes)[-2]:
                    attribute_str += " oder "
                elif key != list(self.attributes)[-1]:
                    attribute_str += ", "
            Game.slow_print(f'Du hast {self.xp_points} Punkte zur Verfügung.\nDu kannst sie auf {attribute_str} verteilen!', separator_top = True, separator_bottom = True, new_line_top = True, new_line_bottom = True)
            for key in self.attributes:
                flag = True
                while flag:
                    try:
                        value = int(Game.slow_input(f'{key}> ').lstrip().strip())
                        if value < 0:
                            Game.slow_print("Bitte gib eine positive ganze Zahl ein!")
                        elif value > self.xp_points:
                            Game.slow_print("Du hast nicht genug Punkte!")
                        else:
                            self.attributes[key] = value
                            self.xp_points -= value
                            if key != list(self.attributes)[-1]:
                                Game.slow_print(f'Verfügbare Punkte: {self.xp_points}')
                            flag = False
                    except ValueError:
                        Game.slow_print("Bitte gib eine positive ganze Zahl ein!")
            Game.clear_terminal()
            self.slow_print(f'Deine Verteilung sieht wie folgt aus:', separator_top = True, new_line_top = True)
            self.slow_dict_print(self.attributes, separator_bottom = True, new_line_bottom = True)
            self.satisfied("set_points")
        else:
            Game.clear_terminal()
            self.reset_attribute(Game.main_character, ["xp_points"])
            attribute_str = ", ".join(list(self.attributes.keys())[:-1]) + " oder " + list(self.attributes.keys())[-1]
            Game.slow_print(f'Du hast {self.xp_points} Punkte zur Verfügung.\nDu kannst sie auf {attribute_str} verteilen!', separator_top=True, new_line_top=True, new_line_bottom=True)
            attributes = list(self.attributes.keys())
            index = 0
            def assign_points():
                nonlocal index
                if index < len(attributes):
                    key = attributes[index]
                    Game.slow_print(f'Verfügbare Punkte: {self.xp_points}', separator_top=True, new_line_top=True)
                    Game.slow_print(f'Bitte gib Punkte für {key} ein:', new_line_top=True)
                    gui_input(Game.MainWindowInstance, gui_input_callback=lambda _, value: process_input(key, value), label_text=f"{key} V")
                else:
                    Game.clear_terminal()
                    Game.slow_print(f'Deine Verteilung sieht wie folgt aus:', separator_top=True, new_line_top=True)
                    Game.slow_dict_print(self.attributes, new_line_bottom=True)
                    self.satisfied("set_points", callback=callback)
            def process_input(key, value):
                nonlocal index
                try:
                    value = int(value.strip())
                    if value < 0:
                        Game.slow_print("Bitte gib eine positive ganze Zahl ein!")
                        assign_points()
                    elif value > self.xp_points:
                        Game.slow_print("Du hast nicht genug Punkte!")
                        assign_points()
                    else:
                        self.attributes[key] = value
                        self.xp_points -= value
                        index += 1
                        assign_points()
                except ValueError:
                    Game.slow_print("Bitte gib eine positive ganze Zahl ein!")
                    assign_points()
            assign_points()

class Enemy(Entity):
    """## Represents an enemy in the game
    """
    def __init__(self) -> None:
        ...

class Shop(Entity):
    """## Represents a shop in the game

    Attributes:
        inventory (dict): A dictionary of items to be sold
        prices (dict): A dictionary of prices for each item
    """
    def __init__(self, inventory: dict, prices: dict) -> None:
        self.inventory = inventory
        self.prices = prices
    
    @staticmethod
    def shop():
        """## Opens the shop menu
        Lets the user purchase items from the shops inventory
        """
        if not Game.gui_mode:
            shop_name = Game.main_character.current_location.split("_")[2] + "_" + Game.main_character.current_location.split("_")[3]
            shop = eval(shop_name)
            while True:
                Game.clear_terminal()
                Game.slow_print("Willkommen im Shop!\nHier sind die verfügbaren Items:\n", separator_top=True, new_line_top=True)
                for index, (item, quantity) in enumerate(shop.inventory.items(), start = 1):
                    price = shop.prices[item]
                    Game.slow_print(f"[{index}]: {item} (Preis: {price} Münzen) - Verfügbar: {quantity}")
                Game.slow_print("[e]: Exit", new_line_bottom = True)
                choice = Game.slow_input("Wähle ein Item oder 'e' zum Verlassen>\n", separator_bottom=True).strip()
                if choice.lower() in ["e", "exit"]:
                    break
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(shop.inventory):
                        item = list(shop.inventory.keys())[choice_index]
                        price = shop.prices[item]
                        quantity_choice = int(Game.slow_input(f"Wie viele {item} möchtest du kaufen? (Verfügbar: {shop.inventory[item]})> "))
                        if quantity_choice <= 0:
                            Game.slow_print("Bitte gib eine positive Zahl ein!")
                            continue
                        if quantity_choice <= shop.inventory[item] and Game.main_character.attributes["Münzen"] >= price * quantity_choice:
                            Game.main_character.add_inventory({item: quantity_choice})
                            Game.main_character.sub_inventory({'Münzen': price * quantity_choice})
                            shop.inventory[item] -= quantity_choice
                            Game.slow_print(f"Du hast {quantity_choice} {item} für {price * quantity_choice} Münzen gekauft!")
                        else:
                            Game.slow_print("Nicht genug Münzen oder nicht genügend Artikel verfügbar!")
                    else:
                        Game.slow_print("Ungültige Auswahl!")
                except ValueError:
                    Game.slow_print("Bitte gib eine ganze Zahl ein!")
            Story.story_loop(Game.main_character, sub_chapter_index = 1)
        else:
            def display_shop():
                Game.clear_terminal()
                Game.slow_print("Willkommen im Shop!\nHier sind die verfügbaren Items:\n", separator_top=True, new_line_top=True)
                for index, (item, quantity) in enumerate(shop.inventory.items(), start=1):
                    price = shop.prices[item]
                    Game.slow_print(f"[{index}]: {item} (Preis: {price} Münzen) - Verfügbar: {quantity}")
                Game.slow_print("[e]: Exit", new_line_bottom=True)
                Game.slow_input("Wähle ein Item oder 'e' zum Verlassen>\n", separator_bottom=True, callback=process_choice)
            def process_choice(choice):
                choice = choice.strip()
                if choice.lower() in ["e", "exit"]:
                    Story.story_loop(Game.main_character, sub_chapter_index=1)
                    return
                try:
                    choice_index = int(choice) - 1
                    if 0 <= choice_index < len(shop.inventory):
                        item = list(shop.inventory.keys())[choice_index]
                        price = shop.prices[item]
                        if Game.main_character.attributes["Münzen"] >= price:
                            Game.main_character.sub_inventory({"Münzen": price})
                            Game.main_character.add_inventory({item: 1})
                            shop.inventory[item] -= 1
                            Game.slow_print(f"Du hast {item} gekauft!", separator_bottom=True, new_line_bottom=True)
                            if shop.inventory[item] == 0:
                                del shop.inventory[item]
                            display_shop()
                        else:
                            Game.slow_print("Du hast nicht genug Münzen!", separator_bottom=True, new_line_bottom=True)
                            display_shop()
                    else:
                        Game.slow_print("Ungültige Auswahl!", separator_bottom=True, new_line_bottom=True)
                        display_shop()
                except ValueError:
                    Game.slow_print("Bitte gib eine ganze Zahl ein!", separator_bottom=True, new_line_bottom=True)
                    display_shop()
            display_shop()

class Story(Game):
    """## Story class
    Handles the story progression and sub-chapters
    """

    started: bool = False

    def __init__(self) -> None:
        pass

    @staticmethod
    def story_print(list_to_print: list, chapter_functions: dict, sub_chapter_index: int = 0, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False, callback=None):
        """## Prints the story
        Prints the text for each element in list and evals any functions in chapter_functions

        Args:
            list_to_print (list): The list to be printed
            chapter_functions (dict): The functions to be evaluated
            sub_chapter_index (int): Whether to skip the first function. Defaults to 0.
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")
            for index, element in enumerate(list_to_print):
                if str(index + sub_chapter_index) in chapter_functions:
                    eval(chapter_functions[str(index)])
                print(element)
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator() 
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            for index, element in enumerate(list_to_print):
                if str(index + sub_chapter_index) in chapter_functions:
                    eval(chapter_functions[str(index)])
            add_list_to_textbox(Game.MainWindowInstance, list_to_print, callback=callback)
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance, "")
            if separator_bottom:
                Game.separator()

    @staticmethod
    def story_slow_print(list_to_print: list, chapter_functions: dict, sub_chapter_index: int = 0, separator_top: bool = False, separator_bottom: bool = False, new_line_top = False, new_line_bottom = False):
        """## Prints the story using slow print
        Prints the text for each element in list slowly and evals any functions in chapter_functions

        Args:
            list_to_print (list): The list to be printed
            chapter_functions (dict): The functions to be evaluated
            sub_chapter_index (int): Whether to skip the first function. Defaults to 0.
            separator_top (bool): Whether to print a separator line above the dict. Defaults to False.
            separator_bottom (bool): Whether to print a separator line below the dict. Defaults to False.
            new_line_top (bool): Whether to print a newline above the dict. Defaults to False.
            new_line_bottom (bool): Whether to print a newline below the dict. Defaults to False.
        """
        if not Game.gui_mode:
            if separator_top:
                Game.separator()
            if new_line_top:
                print("")  
            for index, element in enumerate(list_to_print):
                if str(index + sub_chapter_index) in chapter_functions:
                    eval(chapter_functions[str(index)])
                Game.slow_print(element)
            if new_line_bottom:
                print("")
            if separator_bottom:
                Game.separator()
        else:
            if separator_top:
                Game.separator()
            if new_line_top:
                add_text_to_textbox(Game.MainWindowInstance, "")
            for index, element in enumerate(list_to_print):
                if str(index + sub_chapter_index) in chapter_functions:
                    eval(chapter_functions[str(index)])
            add_list_to_textbox_slow(Game.MainWindowInstance, list_to_print, Game.sleep_time)
            if new_line_bottom:
                add_text_to_textbox(Game.MainWindowInstance, "")
            if separator_bottom:
                Game.separator()
        
    @staticmethod
    def death():
        """## Prints the death message
        Prints the death message to the console
        """
        json_handler = Json_Handler(Game.json_file_path)
        if not Game.gui_mode:
            Game.enter(new_line_top=True)
            Game.clear_terminal()
            Story.story_print(json_handler.load_json_chapter_text("start", "death_screen"), "")
            quit()
        else:
            Game.clear_terminal()
            def show_death_message():
                Story.story_print(json_handler.load_json_chapter_text("start", "death_screen"), "", callback=lambda: Game.MainWindowInstance.after(5000, quit))
            Game.MainWindowInstance.after(100, show_death_message)

    @staticmethod
    def start_game():
        """## Prints the start message
        Prints the start message to the console/GUI
        """
        if not Game.gui_mode:
            json_handler = Json_Handler(Game.json_file_path)
            Game.clear_terminal()
            Game.separator()
            for element in ["logo", "title", "(c)"]:
                Story.story_print(json_handler.load_json_chapter_text("start", element), "")
            Game.enter()
        else:
            json_handler = Json_Handler(Game.json_file_path)
            Game.clear_terminal()
            Game.separator()
            def show_logo():
                Story.story_print(json_handler.load_json_chapter_text("start", "logo"), "", callback=show_title)
            def show_title():
                Story.story_print(json_handler.load_json_chapter_text("start", "title"), "", callback=show_copyright)
            def show_copyright():
                Story.story_print(json_handler.load_json_chapter_text("start", "(c)"), "", callback=wait_for_enter)
            def wait_for_enter():
                Game.enter(new_line_top=True, callback=proceed_to_name)
            def proceed_to_name():
                Game.clear_terminal()
                Game.main_character.set_name()
                Game.main_character.set_points(callback=lambda: Story.story_loop(Game.main_character))
            show_logo()

    @staticmethod
    def story_loop(player: Player, sub_chapter_name: str = "text", sub_chapter_index: int = 0):
        """## Main story loop
        Prints the text for each chapter and progresses to the next after getting user input

        Args:
            player (Player): Instanc of Player class as main character
            sub_chapter_name (str, optional): The name of the sub-chapter. Defaults to "text".
            sub_chapter_index (int, optional): The index of the chapter_functions. Defaults to 0
        """
        json_handler = Json_Handler(Game.json_file_path)
        current_room = player.current_location # starting location
        if not Game.gui_mode:
            checked_sub_chapter_index = False
            if current_room == "start" and not Story.started:
                Story.started = True
                Story.start_game()
                player.set_name()
                player.set_points()
            while current_room:
                if not checked_sub_chapter_index:
                    checked_sub_chapter_index = True
                else:
                    sub_chapter_index = 0
                current_room = player.current_location # update location
                chapter_text = json_handler.load_json_chapter_text(current_room, sub_chapter_name)
                chapter_functions = json_handler.load_json_chapter_functions(current_room, sub_chapter_name)
                Game.clear_terminal()
                Story.story_slow_print(chapter_text, chapter_functions, sub_chapter_index, separator_top = True, separator_bottom = True, new_line_top = True)
                Game.slow_print("Wähle eine Option> ")
                for index, choice in enumerate(eval(f'{current_room}.choices')):
                    Game.slow_print(f'[{index + 1}]: {choice}')
                Game.slow_print("[i]: Inventory")
                Game.slow_print("[s]: Status")
                flag = True
                while flag:
                    choice = Game.slow_input("", separator_bottom = True)
                    if choice.lower().strip() in ["i", "s", "status", "inventory"]:
                        if choice.lower().strip() in ["i", "inventory"]:
                            player.display_inventory()
                        else:
                            player.display_status()
                    else: 
                        try:
                            choice_index = int(choice) - 1
                            if 0 <= choice_index < len(eval(f'{current_room}.choices')):
                                player.current_location = eval(f'{current_room}.next_rooms[{choice_index}]') # set new location
                                flag = False
                            else:
                                Game.slow_print("Bitte gib eine ganze Zahl, i oder s ein!")
                        except ValueError:
                            Game.slow_print("Bitte gib eine ganze Zahl, i oder s ein!")
        else:
            if current_room == "start" and not Story.started:
                Story.started = True
                Story.start_game()
                return
            def process_choice(choice):
                delete_choice_buttons(Game.MainWindowInstance)
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(eval(f'{current_room}.choices')):
                    player.current_location = eval(f'{current_room}.next_rooms[{choice_index}]')
                    Story.story_loop(player)
            def display_choices():
                room_choices = eval(f'{current_room}.choices')
                for index, choice_text in enumerate(room_choices, start=1):
                    add_choice_button(Game.MainWindowInstance, text=f"{index}: {choice_text}", callback=lambda choice=index: process_choice(str(choice)))
            update_stats_table(Game.MainWindowInstance, Game.main_character.attributes)
            chapter_text = json_handler.load_json_chapter_text(current_room, sub_chapter_name)
            chapter_functions = json_handler.load_json_chapter_functions(current_room, sub_chapter_name)
            Story.story_slow_print(chapter_text, chapter_functions, sub_chapter_index, separator_top=True, new_line_top=True)
            display_choices()

    @staticmethod
    def repair(cost: dict):
        """## Repair Function
        Repair the player's equipment with the given cost.

        Args:
            cost (dict): The cost of the repair.
        """
        choice = Game.slow_input("Willst du dein Schiff reparieren?\n[j]: Ja\n[n]: Nein\n")
        if choice.lower().strip() in ["ja", "j"]:
            for key, value in cost.items():
                if cost[key] in Game.main_character.inventory:
                    if Game.main_character.inventory[key] >= cost[key]:
                        Game.main_character.inventory[key] -= value
                    else:
                        Game.slow_print(f'Du hast nicht genügend {cost}!')
                        Story.story_loop(Game.main_character, Game.main_character.current_location, "text_not_repaired")
                else:
                    Game.slow_print(f'Du hast nicht genügend {cost}!')
                    Story.story_loop(Game.main_character, Game.main_character.current_location, "text_not_repaired")

# initialize rooms
start = Room("start", ["Abenteuer starten!"], ["chapter_1"], inventory = {})
chapter_1 = Room("chapter_1", ["Flüchten", "Kämpfen"], ["chapter_1_fleeing", "chapter_2"], inventory = {})
chapter_1_fleeing = Room("chapter_1_fleeing", [], [], inventory = {})
chapter_2 = Room("chapter_2", ["Geschichte fortsetzen!"], ["chapter_3"], inventory = {"Münzen": 125, "Holzbretter": 3})
chapter_3 = Room("chapter_3", ["Taverne", "Waffenschmied", "Hafen"], ["chapter_3_taverne", "chapter_3_waffenschmied", "chapter_3_hafen"], inventory = {})
chapter_3_taverne = Room("chapter_3_taverne", ["Waffenschmied", "Hafen"], ["chapter_3_waffenschmied", "chapter_3_hafen"], inventory = {})
chapter_3_waffenschmied = Room("chapter_3_waffenschmied", ["Taverne", "Hafen"], ["chapter_3_taverne", "chapter_3_hafen"], inventory = {"Karte von Shipwreck-Beach": 1})
chapter_3_hafen = Room("chapter_3_hafen", ["Weiterfahren", "Einkaufen", "Taverne", "Waffenschmied"], ["chapter_4", "chapter_3_hafen_shop", "chapter_3_taverne", "chapter_3_waffenschmied"], inventory = {})
chapter_3_hafen_shop = Room("chapter_3_hafen_shop", ["Geschichte fortsetzen!"], ["chapter_3_hafen"], inventory = {})
chapter_4 = Room("chapter_4", ["Links vorbei", "Durch die Mitte", "Rechts vorbei"], ["chapter_4_links", "chapter_4_mitte", "chapter_4_rechts"], inventory = {})
chapter_4_links = Room("chapter_4_links", [], [], inventory = {})
chapter_4_mitte = Room("chapter_4_mitte", ["Geschichte fortsetzen!"], ["chapter_5"], inventory = {})
chapter_4_rechts = Room("chapter_4_rechts", ["Geschichte fortsetzen!"], ["chapter_5"], inventory = {})
chapter_5 = Room("chapter_5", ["Sachen nehmen", "Sachen liegenlassen"], ["chapter_5_fight", "chapter_5_sub"], inventory = {"altes Buch": 1})
chapter_5_fight = Room("chapter_5_fight", ["Geschichte fortsetzen!"], ["chapter_6"], inventory = {"Eisenrüstung": 1, "Eisenschwert": 1, "verfluchte Kanonenkugel": 10})
chapter_5_sub = Room("chapter_5_sub", ["Geschichte fortsetzen!"], ["chapter_6"], inventory = {})
chapter_6 = Room("chapter_6", ["Geschichte fortsetzen!"], ["chapter_7"], inventory = {})
chapter_7 = Room("chapter_7", ["Geschichte fortsetzen!"], ["chapter_8"], inventory = {"Logbuch": 1})
chapter_8 = Room("chapter_8", ["Norden", "Osten","Westen"], ["chapter_8_norden", "chapter_8_osten", "chapter_8_westen"], inventory = {})
chapter_8_norden = Room("chapter_8_norden", ["Geschichte fortsetzen!"], ["chapter_8"], inventory = {})
chapter_8_osten = Room("chapter_8_osten", ["Geschichte fortsetzen!"], ["chapter_8"], inventory = {"Münzen": 3})
chapter_8_westen = Room("chapter_8_westen", ["Geschichte fortsetzen!"], ["chapter_9"], inventory = {})
chapter_9 = Room("chapter_9", ["Geschichte beenden!"], ["credits"], inventory = {})
credits = Room("credits", [], [], inventory = {})

# initialize shop
hafen_shop = Shop({"Holzbretter": 10, "Flasche Alkohol": 1, "Hammer": 1, "Feder mit Tinte": 3}, {"Holzbretter": 10, "Flasche Alkohol": 15, "Hammer": 2, "Feder mit Tinte": 5})
