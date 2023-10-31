import axios from 'axios'

export const getMovie = async () => {
  const response = await axios.get(`/api/v1/movies/`)
  const validatedResponse = await response.data
  return validatedResponse
}