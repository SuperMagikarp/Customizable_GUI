# README

This is a proof of concept for a GUI based, TTRPG dice-roller that uses Discord Webhooks to
deliver the result of rolls into a channel on a Discord server.

## Requirements

You'll need the following :

- `Pip` (*To install dependencies*)
- `Discord` Server (*To generate a webhook*)
- `Python` (*To run the script*)

## Setup

1. Install Dependencies:

    *It is recommended you set up a virtual environment to work in.*

    Install `discordwebhook` & `kivy` via pip package management tool.

        pip install discordwebhook kivy

2. Create a Webhook to use with the script.

    *If you are not the server owner or admin, you may need additional permissions to follow the next steps.*

    Select a channel in the server you'd like the messages to appear in.

        Under Settings > Integrations > Webhooks > Create Webhook

    - Create a new Webhook.
    - Select the Webhook.
    - Copy the URL of this Webhook and save it in a text file in an accessible location, e.g. `config/web_hook_url.txt`.

    ---  

    **Do not upload or share this text file.**

    *Anyone with access to the URL of your Webhook can send content through your Webhook, via that URL. So keep it safe and hidden.*

    ---

3. (Optional) Set up the script

    *If you saved the file in a different folder, or under a different file name, you'll need to edit the script and pass the path to the file into the function `get_webhook()` in the main script within `basic_grid_dice_roller`.*

4. Run the Script

        python basic_grid_dice_roller.py
