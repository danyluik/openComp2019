from window_state import WindowState, MainMenuState, GameState

    
class WindowManager:
    def __init__(self, window):
        self.window = window
        
        # Register the window states
        WindowState.main_menu = WindowState('main_menu', MainMenuState(self.window))
        WindowState.settings = WindowState('settings', None)
        WindowState.game = WindowState('game', GameState(self.window))

        # Start on the main_menu state
        self.current_state = WindowState.main_menu
        print("Current State: {}".format(self.current_state))

    def run(self, events):
        # Run the current state then move to the next state
        self.current_state.state.run()
        self.current_state = self.current_state.state.next(events)
                            
