import webbrowser


if __name__ == "__main__":
    url = 'http://vk.com/feed'

    # Open URL in a new tab, if a browser window is already open.
    # webbrowser.open_new_tab(url)

    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)
