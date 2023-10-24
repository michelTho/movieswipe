export const postVote = async ({movieId, isUpvote}) => {
  const requestConfig = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: {
      movie_id: movieId,
      is_upvote: isUpvote
    }
  }
  const response = await fetch(`/api/v1/votes/`, requestConfig)
  const validatedResponse = await response.json()
  return validatedResponse
}