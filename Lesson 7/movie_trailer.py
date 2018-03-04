import fresh_tomatoes
import media

#Creating instances
toy_story = media.Movie("Toy Story", "About a boy and his toys which come into life.", "http://cdn.playbuzz.com/cdn/ef075a32-76b0-4209-8a6a-182e7b9d9a70/a80a0788-e513-4381-9ebd-f4cd85108a16_560_420.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "Some blue aliens", "http://www.movieposter.com/posters/archive/main/98/MPW-49246", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
blade_runner_2049 = media.Movie("Blade Runner 2049", "Set in future; retiring replicants.", "https://cdn.traileraddict.com/content/warner-bros-pictures/blade-runner-2049-poster-8.jpg", "https://youtu.be/gCcx85zbxz4")
justice_league = media.Movie("Justice League", "Heroes fight together.", "http://nerdist.com/wp-content/uploads/2017/07/justice-league-poster.jpg", "https://www.youtube.com/watch?v=r9-DM9uBtVI")

movies = [toy_story, avatar, blade_runner_2049, justice_league]
fresh_tomatoes.open_movies_page(movies)