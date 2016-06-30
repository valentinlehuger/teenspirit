import fetch from 'isomorphic-fetch'

export const REQUEST_USERS = 'REQUEST_USERS'
export const RECEIVE_USERS = 'RECEIVE_USERS'
export const INVALIDATE_USERS = 'INVALIDATE_USERS'
export const REQUEST_TWEETS = 'REQUEST_TWEETS'
export const RECEIVE_TWEETS = 'RECEIVE_TWEETS'
export const VALIDATE_USER = 'VALIDATE_USER'
export const UNVALIDATE_USER = 'UNVALIDATE_USER'

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

function receiveUsers(dispatch, json) {
  console.log("in receiveUsers")
  return {
    type: RECEIVE_USERS,
    users: json.users
  }
}

function receiveTweets(json, user) {
  console.log("in receiveTweets")
  console.log("tweets: " + JSON.stringify(json.tweets, null, 2))
  return {
    type: RECEIVE_TWEETS,
    tweets: json.tweets,
    user: user
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
      .then(json => dispatch(receiveUsers(dispatch, json)))
  }
}

export function fetchTweets(user) {
  console.log("in fetchTweets: " + user)
  return dispatch => {
    dispatch(requestTweets())
    return fetch(`http://127.0.0.1:3033/fetch_tweets/${user}`)
      .then(response => response.json())
      .then(json => dispatch(receiveTweets(json, user)))
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

export function fetchTweetsIfNeeded() {
    return (dispatch, getState) => {
        const state = getState()
        console.log("In fetchTweetsIfNeeded", state, state.apiTweets.users.length, state.apiTweets.tweets.length)
        if (state.apiTweets.users.length > 0 && (!state.apiTweets.tweets.length || state.apiTweets.tweets.length < 10))
            return dispatch(fetchTweets(state.apiTweets.users[0]))
    }
}

export function validateUser(userId, dispatch) {
	dispatch(fetchUsersIfNeeded())
	return {
		type: VALIDATE_USER,
		userId: userId
	}
}

export function unvalidateUser(userId, dispatch) {
	dispatch(fetchUsersIfNeeded())
	return {
		type: UNVALIDATE_USER,
		userId: userId
	}
}
