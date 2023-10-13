export type MovieResponse = {
  id: number
  title: string
  description: string
  image_url: string
}

export const getMovie = async (): Promise<MovieResponse> => {
  const response = await fetch(`http://localhost:8000/api/movies/`)
  const validatedResponse: MovieResponse = await response.json()
  return validatedResponse
}