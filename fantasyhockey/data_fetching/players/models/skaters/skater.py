

class Skater:
    def __init__(self, id):
        self.id = id
        self.__skater_stats = []
        self.__youth_stats = []
        self.__advanced_stats_toi = []
        self.__advanced_stats_shootout = []
        self.__advanced_stats_scoring = []
        self.__advanced_stats_powerplay = []
        self.__advanced_stats_penalty_kill = []
        self.__advanced_stats_penalties = []
        self.__advanced_stats_misc = []
        self.__advanced_stats_goals = []
        self.__advanced_stats_faceoffs = []
        self.__advanced_stats_corsi_fenwick = []

    def get_id(self):
        return self.id

    def set_skater_stats(self, skater_stats):
        self.__skater_stats = skater_stats

    def get_skater_stats(self):
        return self.__skater_stats
    
    def set_youth_stats(self, youth_stats):
        self.__youth_stats = youth_stats

    def get_youth_stats(self):
        return self.__youth_stats
    
    def set_advanced_stats_toi(self, advanced_stats_toi):
        self.__advanced_stats_toi = advanced_stats_toi

    def get_advanced_stats_toi(self):
        return self.__advanced_stats_toi
    
    def set_advanced_stats_shootout(self, advanced_stats_shootout):
        self.__advanced_stats_shootout = advanced_stats_shootout

    def get_advanced_stats_shootout(self):
        return self.__advanced_stats_shootout
    
    def set_advanced_stats_scoring(self, advanced_stats_scoring):
        self.__advanced_stats_scoring = advanced_stats_scoring

    def get_advanced_stats_scoring(self):
        return self.__advanced_stats_scoring
    
    def set_advanced_stats_powerplay(self, advanced_stats_powerplay):
        self.__advanced_stats_powerplay = advanced_stats_powerplay

    def get_advanced_stats_powerplay(self):
        return self.__advanced_stats_powerplay
    
    def set_advanced_stats_penalty_kill(self, advanced_stats_penalty_kill):
        self.__advanced_stats_penalty_kill = advanced_stats_penalty_kill

    def get_advanced_stats_penalty_kill(self):
        return self.__advanced_stats_penalty_kill
    
    def set_advanced_stats_penalties(self, advanced_stats_penalties):
        self.__advanced_stats_penalties = advanced_stats_penalties

    def get_advanced_stats_penalties(self):
        return self.__advanced_stats_penalties
    
    def set_advanced_stats_misc(self, advanced_stats_misc):
        self.__advanced_stats_misc = advanced_stats_misc

    def get_advanced_stats_misc(self):
        return self.__advanced_stats_misc
    
    def set_advanced_stats_goals(self, advanced_stats_goals):
        self.__advanced_stats_goals = advanced_stats_goals

    def get_advanced_stats_goals(self):
        return self.__advanced_stats_goals
    
    def set_advanced_stats_faceoffs(self, advanced_stats_faceoffs):
        self.__advanced_stats_faceoffs = advanced_stats_faceoffs

    def get_advanced_stats_faceoffs(self):
        return self.__advanced_stats_faceoffs
    
    def set_advanced_stats_corsi_fenwick(self, advanced_stats_corsi_fenwick):
        self.__advanced_stats_corsi_fenwick = advanced_stats_corsi_fenwick

    def get_advanced_stats_corsi_fenwick(self):
        return self.__advanced_stats_corsi_fenwick

