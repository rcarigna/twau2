# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite with the corresponding [filename].png.
    # For example, this is images/temp_bigby_wolf.png

    show temp_bigby_wolf

    # These display lines of dialogue.

    bigby "You've created a new Ren'Py game."

    bigby "Once you add a story, pictures, and music, you can release it to the world!"

    jump chapter1
