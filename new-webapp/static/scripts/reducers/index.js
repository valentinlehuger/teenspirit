/**
* @Author: valentin
* @Date:   2016-06-22T20:41:21+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-22T21:27:38+02:00
*/


import { combineReducers } from 'redux'


function users(state = {
	isFetchingUser: false,
	users: []
}, action) {
	switch (action.type) {
		case REQUEST_USERS:
			return Object.assign({}, state, {
			        isFetching: true
			      })
		case RECEIVE_USERS:
			return Object.assign({}, state, {
		        isFetching: false,
		        items: action.posts
      		})
		default:
			return state
	}
}

const tweetsApp = combineReducers({
	users
})

export default tweetsApp
