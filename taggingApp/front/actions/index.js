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

function fetchUsers(n) {
  return dispatch => {
	console.log(n)
    dispatch(requestUsers())
    return fetch(`http://127.0.0.1:3033/fetch_users/${n}`)
      .then(response => response.json())
      .then(json => dispatch(receiveUsers(json)))
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
  if (state.isFetching) {
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
