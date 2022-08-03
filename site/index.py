#!/usr/bin/python3

import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Content-Type: text/html; charset=utf-8\n")

site_header = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">

  <link rel="icon" type="image/png" sizes="16x16" href="favicon.png">
  <title>Admin</title>

  <script src="index.js"></script>

</head>
<body>
<header>
  <div id="title" onclick="offToggAll()">
    <img src="favicon.png" alt="favicon" id="favicon" onclick="console.log('test')">
    <h1>Heurepika Panel</h1>
  </div>

  <div class="top-line"></div>

  <nav id="menu">

    <input type='checkbox' id='responsive-menu' onclick='updatemenu()'><label></label>
    
    <ul>
"""

print(site_header)

for folder in data["folder"]:
    if folder["name"] == "main":
        for site in folder["content"]:
            if site["iframe"]:
                menu_entry = f"""
      <li class='li-entry' onClick='multiTogg("{site["name"]}", "site", true)'>
        <div class="menu-entry">
          <img src="page.png" alt="" class="page">
          <a id="{site["name"]}Menu" class="menu-button-text">{site["name"]}</a>
        </div>
      </li>
"""
            else:
                menu_entry = f"""
      <li class='li-entry'>
        <div class="menu-entry">
          <img src="page.png" alt="" class="page">
          <a class="menu-button-text" href='{site["url"]}' target="_blank">{site["name"]}</a>
        </div>
      </li>
"""

            print(menu_entry)
    else:
        menu_start_folder = f"""
      <li class='li-menu'>
        <div class="menu-entry">
          <img src="folder.png" alt="" class="folder">
          <a class='dropdown-arrow' class="menu-button-text">{folder["name"]}</a>
        </div>
        <ul class='sub-menus'>
"""
        print(menu_start_folder)
        for site in folder["content"]:
            if site["iframe"]:
                menu_content_folder = f"""
          <li class='sub-menus-content' onClick='multiTogg("{site["name"]}", "site", true)'>
            <a id="{site["name"]}Menu" class="menu-button-text">{site["name"]}</a>
          </li>
"""
            else:
                menu_content_folder = f"""
          <li class='sub-menus-content'>
            <a class="menu-button-text" href='{site["url"]}' target="_blank">{site["name"]}</a>
          </li>
                """

            print(menu_content_folder)

        menu_end_folder = """
        </ul>
      </li>
"""
        print(menu_end_folder)

site_middle = """
  </nav>
  <img src="settings.png" alt="settings icon" id="settings" onClick='multiTogg("Settings", "site", true)'>

</header>

<div id="search_bar">
    <div class="widget_google">
        <form method="GET" action="https://www.google.com/search">
            <div class="row">
                <div class="twelve_cell_form">
                    <input type="text" class="twelve cell" name="q" size="31" maxlength="255" i18n-placeholder="search" value="" autofocus /> <input type="hidden" name="l" value="fr" />
                    <button><i class="search"><img src="logo-google.svg" alt="google" style="width: 75px"></i></button>
                </div>
            </div>
        </form>
    </div>
    <div id="DesktopListContent">     
        <ul>
"""
print(site_middle)

for desktop in data["desktops"]:
    site_content = f"""
            <li>
                <a href="{desktop["link"]}">
                    <img src="{desktop["icon"]}" alt="Nextcloud Icon">
                    <p>{desktop["name"]}</p>
                </a>
            </li>
"""
    print(site_content)

desktop_end = """
        </ul>
    </div>
</div>

<section id="page">
  <div id="site" class="showBoxClass iframeListe">
"""
print(desktop_end)

for folder in data["folder"]:
    for site in folder["content"]:
        if site["iframe"]:
            if site["dark"]:
                iframe_content = f"""
    <div id="{site["name"]}" class="showClass">
      <div class='iframe_bg'></div>
      <iframe src="{site["url"]}" class="dark"></iframe>
    </div>
"""
            else:
                iframe_content = f"""
    <div id="{site["name"]}" class="showClass">
      <img src="iframe_bg.png" alt="iframe background">
      <iframe src="{site["url"]}""></iframe>
    </div>
"""
            print(iframe_content)

start_form = """
    <div id="Settings" class="showClass">
        <h2>Settings</h2>
        <form action="/index.py">
            <div>
                <label for="folder">Choose a folder</label>
                <select name="folder" id="select_folder">
                    <option value="folder">Choose a folder</option>
"""

end_form = """
                </select>
            </div>
        </form>
    </div>
"""

site_end = """
  </div>
</body>
</html>
"""

print(site_end)
