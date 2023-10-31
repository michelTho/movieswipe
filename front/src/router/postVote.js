import axios from 'axios'

export const postVote = async ({movieId, isUpvote}) => {
  const headers = {
    'Content-Type': 'application/json'
  };
  const body = {
    movie_id: movieId,
    is_upvote: isUpvote
  };
  const response = await axios.post(`/api/v1/votes/`, body, headers)
  const validatedResponse = await response.data
  return validatedResponse
}