export const getMovie = async () => {
  const response = await fetch(`/api/v1/movies/`)
  const validatedResponse = await response.json()
  return validatedResponse
}