
class Australia:
    def __init__(self):
        self.states = ('WA', 'NT', 'SA', 'QLD', 'NSW', 'ACT', 'VIC', 'TAS')
        self.colours = ('R', 'G', 'B')
        self.values = {state:'' for state in self.states}
        
        self.constraints = {'WA': ('NT', 'SA'),
                            'NT': ('WA', 'SA', 'QLD'),
                            'SA' : ('WA', 'NT', 'QLD', 'NSW', 'VIC'),
                            'QLD': ('NT', 'SA', 'NSW'),
                            'NSW': ('SA', 'QLD', 'ACT', 'VIC'),
                            'ACT': ('NSW'),
                            'VIC': ('SA', 'NSW'),
                            'TAS': ()}
    
    def get_init_state(self):
        return AustraliaEnvState(self, self.values.copy())
    
    def is_solved(self, env_state):
        for colour in env_state.values():
            if colour not in self.colours:
                return False 
        if not self.check_all_constraints(env_state):
            return False
        return True
    
    def check_all_constraints(self, env_state):
        for state in self.states:
            if not self.check_constraints(env_state, state):
                return False
        return True
            
    def check_constraints(self, env_state, state):
        state_colour = env_state[state]

        # TODO MAKE DYNAMIC
        if state == 'ACT':
            if state_colour == env_state[self.constraints[state]]:
                return False
            
        else:
            for neighbour in self.constraints[state]:
                if state_colour == env_state[neighbour]:
                    return False
        return True
    
class AustraliaEnvState:
    def __init__ (self, env, colouring: dict, parent=None):
        self.env = env
        self.state = colouring
        self.parent = parent
        
    def get_successors(self):
        next_state = None
        
        for state, colour in self.state.items():
            if not colour:
                next_state = state
                break
        
        if next_state is None:
            return [self] 
        
        successors = []
        for colour in self.env.colours:
            new_colouring = self.state.copy()
            new_colouring[next_state] = colour
            new_state = AustraliaEnvState(self.env, new_colouring, self)
            successors.append(new_state)
            
        return successors
            
    def get_representation(self):   
        return ''.join([value for value in self.state.values()])
        
    def __repr__(self):
        return str(self.state)
        
    def __str__(self):
        return str(self.state)