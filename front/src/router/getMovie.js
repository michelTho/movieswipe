// export type MovieResponse = {
//   id: number
//   title: string
//   description: string
//   image_url: string
// }

export const getMovie = async () => {
  const response = await fetch(`http://localhost:8000/api/v1/movies/`)
  const validatedResponse = await response.json()
  return validatedResponse
}