import fetch from 'isomorphic-fetch'

export const REQUEST_USERS = 'REQUEST_USERS'
export const RECEIVE_USERS = 'RECEIVE_USERS'
export const INVALIDATE_USERS = 'INVALIDATE_USERS'

function requestUsers() {
  return {
    type: REQUEST_USERS
  }
}

function receiveUsers(json) {
  return {
    type: RECEIVE_USERS,
    users: json.users
  }
}

export function invalidateUsers() {
  return {
    type: INVALIDATE_USERS
  }
}

function fetchUsers() {
  return dispatch => {
    dispatch(requestUsers())
    return fetch(`http://127.0.0.1:3033/fetch_users`)
      .then(response => response.json())
      .then(json => dispatch(receiveUsers(json)))
  }
}

function shouldFetchUsers(state) {
	console.log("shouldFetchUsers", state)
  const posts = state.users
  if (!posts) {
    return true
  }
  if (posts.isFetching) {
    return false
  }
  return posts.didInvalidate
}

export function fetchUsersIfNeeded() {
  return (dispatch, getState) => {
    if (shouldFetchUsers(getState())) {
      return dispatch(fetchUsers())
    }
  }
}
