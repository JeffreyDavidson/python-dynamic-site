class Page(object):
    def __init__(self):
        self.title = ""
        self.css = "css/styles.css"
        self.head = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/normalize/3.0.3/normalize.css" rel="stylesheet">
        <link href="{self.css}" rel="stylesheet">
    </head>
    <body>
    """

        self.header = """
        <header><h1>New York Yankees</h1></header>
    """

        self.container_open = """
        <div id="page-wrap">
            <nav>
                <ul>
                    <li><a href="#">Schedule</a></li>
                    <li><a href="#">Yankee Stadium</a></li>
                    <li><a href="#">Tickets</a></li>
                    <li><a href="#">Store</a></li>
                </ul>
            </nav>
            """

        self.section_open = """
            <section id="main-content">
        """

        self.body = ""

        self.section_close = """
            </section>
        """

        self.sidebar = """
            <aside>
                <h2>Roster</h2>
                <h3>Pitchers</h3>
                <ul>
                    <li><a href="?id=0&type=pitcher&name=Dellin+Betances">Dellin Betances</a></li>
                    <li><a href="?id=1&type=pitcher&name=Nathan+Eovaldi">Nathan Eovaldi</a></li>
                    <li><a href="?id=2&type=pitcher&name=Nick+Goody">Nick Goody</a></li>
                </ul>
                <h3>Catchers</h3>
                <ul>
                    <li><a href="?id=0&type=fielder&name=Brian+McCann">Brian McCann</a></li>
                    <li><a href="?id=1&type=fielder&name=John+Ryan+Murphy">John Ryan Murphy</a></li>
                </ul>
                <h3>Infielders</h3>
                <ul>
                    <li><a href="?id=2&type=fielder&name=Case+Headley">Chase Hedley</a></li>
                    <li><a href="?id=3&type=fielder&name=Didi+Gregorius">Didi Gregorius</a></li>
                    <li><a href="?id=4&type=fielder&name=Stephen+Drew">Stephen Drew</a></li>
                    <li><a href="?id=5&type=fielder&name=Mark+Teixeira">Mark Teixeira</a></li>
                    <li><a href="?id=6&type=fielder&name=Greg+Bird">Greg Bird</a></li>
                    <li><a href="?id=7&type=fielder&name=Brendan+Ryan">Brendan Ryan</a></li>
                </ul>
                <h3>Outfielders</h3>
                <ul>
                    <li><a href="?id=8&type=fielder&name=Brett+Gardner">Brett Gardner</a></li>
                    <li><a href="?id=9&type=fielder&name=Jacoby+Ellsbury">Jacoby Ellsbury</a></li>
                    <li><a href="?id=10&type=fielder&name=Carlos+Beltran">Carlos Beltran</a></li>
                    <li><a href="?id=11&type=fielder&name=Chris+Young">Chris Young</a></li>
                </ul>
                <h3>Designated Hitter</h3>
                <ul>
                    <li><a href="?id=12&type=fielder&name=Alex+Rodriquez">Alex Rodriguez</a></li>
                </ul>
            </aside>
        """
        self.container_close = """
        </div>
        """

        self.footer = """
            <footer>
                <p>&copy; 2015 Jeffrey Davidson
            </footer>
        """

        self.close = """
    </body>
</html>
"""
    def print_out(self):
        all = self.head + self.header + self.container_open + self.sidebar + self.section_open + self.body + self.section_close + self.container_close + self.footer + self.close
        all = all.format(**locals())
        return all


class ContentPage(object):
    def __init__(self):
        pass

    def pitcher_profile(self, do):

        all = """<h2>{do.player_name}</h2>
        <h3>{do.position}</h3>
        <ul>
            <li>Innings Pitched: {do.ip}</li>
            <li>ERA: {do.era}</li>
            <li>Strikeouts: {do.strikeouts}</li>
            <li>Walks: {do.walks}</li>
            <li>Saves: {do.saves}</li>
        </ul>
        """
        all = all.format(**locals())
        return all

    def fielder_profile(self, do):

        all = """<h2>{do.player_name}</h2>
        <h3>{do.position}</h3>
        <ul>
            <li>Bats: {do.bats}</li>
            <li>Throws: {do.throws}</li>
            <li>Batting Average: {do.avg}</li>
            <li>Home Runs: {do.hr}</li>
            <li>RBI: {do.rbi}</li>
        </ul>
        """
        all = all.format(**locals())
        return all

    def home(self):
        return """
            <h2>Yankees Win</h2>
            <p>The Yankees win tonight against Houston...<a href="">see more</a></p>
            """

