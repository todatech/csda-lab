import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        # dbc.NavItem(dbc.NavLink("Time-Series", href="/time-series")),
        dbc.NavItem(dbc.NavLink("Lab 1", href="/lab1")),
        dbc.NavItem(dbc.NavLink("Lab 2", href="/lab2")),
        dbc.NavItem(dbc.NavLink("Lab 3", href="/lab3")),
        # dbc.DropdownMenu(
        #     nav=True,
        #     in_navbar=True,
        #     label="Labs",
        #     children=[
        #         dbc.DropdownMenuItem("Lab 1 - Recommender System",
        #                 href="/lab1"),
        #         dbc.DropdownMenuItem("Lab 2 - blah",
        #                 href="/lab2"),
        #         dbc.DropdownMenuItem("Lab 3 - blash",
        #                 href="/lab3"),
        #     ],
        # ),
    ],
    brand="CSDA1040 Fall 2019 - Group 8",
    brand_href="/home",
    sticky="top",
)
