# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# client_id = 'bd3961f49f8a4fc5b344e1c63b43c310'
# client_secret = '8303ce336e874e6597907a2c737cd790'
# redirect_uri = 'http://example.com'
# scope = 'playlist-modify-private'
#
# auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
# sp = spotipy.Spotify(auth_manager=auth_manager)
#
#
# # Create a private playlist for the user
# user_id = sp.current_user()['id']
# playlist = sp.user_playlist_create(user_id, "New Private Playlist", public=False)
# print("Created playlist:", playlist['name'])
#
# # Get the user's ID
# user_info = sp.current_user()
# user_id = user_info['id']
#
# print("Authenticated user's ID:", user_id)
