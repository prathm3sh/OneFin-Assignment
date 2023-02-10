from movie.serializers import MovieSerializer
import requests


def get_movies():
  response = requests.get("https://demo.credy.in/api/v1/maya/movies/")
  parsed_response = response.json()
  return {
    "count": parsed_response["count"],
    "next": parsed_response["next"],
    "previous": parsed_response["previous"],
    "results": MovieSerializer(parsed_response["results"], many=True).data,
  }