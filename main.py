import webapp2
from pages import Page, ContentPage
from data import Pitcher, Fielder

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = Page()
        content = ContentPage()
        if self.request.GET:
            id = self.request.GET['id']
            type = self.request.GET['type']
            name = self.request.GET['name']

            if type == 'pitcher':
                pitcher_data = [['22', '2.41', '48', '24', '10'], ['16', '1.98', '61', '0', '30'], ['11', '5.18', '22', '16', '2']]
                do = Pitcher()
                do.id = id
                do.player_name = name
                do.position = 'Pitcher'
                do.ip = pitcher_data[int(id)][0]
                do.era = pitcher_data[int(id)][1]
                do.strikeouts = pitcher_data[int(id)][2]
                do.walks = pitcher_data[int(id)][3]
                do.saves = pitcher_data[int(id)][4]
                page.body = content.pitcher_profile(do)
            else:
                fielder_data = [
                    ['Catcher', 'Right', 'Right', '.238', '48', '20'],
                    ['Catcher', 'Left', 'Right', '.190', '61', '50'],
                    ['Third Base', 'Right', 'Right', '.345', '22', '33'],
                    ['Shortstop', 'Left', 'Right', '.209', '22', '68'],
                    ['Second Base', 'Right', 'Right', '.215', '22', '24'],
                    ['First Base', 'Left', 'Right', '.267', '22', '40'],
                    ['First Base', 'Right', 'Right', '', '22', '30'],
                    ['Second Base', 'Left', 'Right', '.409', '22', '100'],
                    ['Left Field', 'Right', 'Right', '.218', '22', '54'],
                    ['Center Field', 'Left', 'Right', '.240', '22', '27'],
                    ['Right Field', 'Right', 'Right', '.356', '22', '83'],
                    ['Right Field', 'Left', 'Right', '.406', '22', '64'],
                    ['Designated Hitter', 'Right', 'Right', '.367', '22', '120'],
                ]
                do = Fielder()
                do.id = id
                do.player_name = name
                do.position = fielder_data[int(id)][0]
                do.bats = fielder_data[int(id)][1]
                do.throws = fielder_data[int(id)][2]
                do.avg = fielder_data[int(id)][3]
                do.hr = fielder_data[int(id)][4]
                do.rbi = fielder_data[int(id)][5]
                page.body = content.fielder_profile(do)

        else:
            page.body = content.home()
        self.response.write(page.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
