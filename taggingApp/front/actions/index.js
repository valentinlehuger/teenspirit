import fetch from 'isomorphic-fetch'

export const REQUEST_USERS = 'REQUEST_USERS'
export const RECEIVE_USERS = 'RECEIVE_USERS'
export const INVALIDATE_USERS = 'INVALIDATE_USERS'
export const REQUEST_TWEETS = 'REQUEST_TWEETS'
export const RECEIVE_TWEETS = 'RECEIVE_TWEETS'

function requestUsers() {
  return {
    type: REQUEST_USERS
  }
}

function requestTweets() {
  return {
    type: REQUEST_TWEETS
  }
}

function receiveUsers(json) {
  console.log("in receiveUsers")
  return {
    type: RECEIVE_USERS,
    users: json.users
  }
}

function receiveTweets(json) {
  console.log("in receiveTweets")
  console.log("tweets: " + JSON.stringify(json.tweets, null, 2))
  return {
    type: RECEIVE_TWEETS,
    tweets: json.tweets
  }
}

export function invalidateUsers() {
  return {
    type: INVALIDATE_USERS
  }
}

function fetchUsers(n) {
  return dispatch => {
	console.log(n)
    dispatch(requestUsers())
    return fetch(`http://127.0.0.1:3033/fetch_users/${n}`)
      .then(response => response.json())
      .then(json => dispatch(receiveUsers(json)))
  }
}

export function fetchTweets(user) {
  console.log("in fetchTweets: " + user)
  return dispatch => {
    dispatch(requestTweets())
    return fetch(`http://127.0.0.1:3033/fetch_tweets/${user}`)
      .then(response => response.json())
      .then(json => dispatch(receiveTweets(json)))
  }
}

function shouldFetchUsers(state) {
  const users = state.users
  console.log("shouldFetchUsers", state, !users)
  if (!users) {
    return true
  }
  if (users.length < 10) {
	  return true
  }
  if (state.isFetchingUsers) {
    return false
  }
  return posts.didInvalidate
}

export function fetchUsersIfNeeded() {
  return (dispatch, getState) => {
	const state = getState()
    if (shouldFetchUsers(state)) {
		var n = 10
		if (state.users) {
			n = n - state.users.length
		}
		return dispatch(fetchUsers(n))
    }
  }
}
