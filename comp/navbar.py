import dash_bootstrap_components as dbc


def Navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Labs",
                children=[
                    dbc.DropdownMenuItem("Lab 1 - Recommender System",
                            href="/lab1"),
                    dbc.DropdownMenuItem("Lab 2 - blah",
                            href="/lab2"),
                    dbc.DropdownMenuItem("Lab 3 - blash",
                            href="/lab3"),
                ],
            ),
        ],
        brand="Home",
        brand_href="/home",
        sticky="top",
    )

    return navbar
