/**
* @Author: valentin
* @Date:   2016-06-25T15:15:43+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-25T15:20:10+02:00
*/

import { combineReducers } from 'redux'
import {
	REQUEST_USERS, RECEIVE_USERS, INVALIDATE_USERS
} from '../actions'

function users(state = {
	isFetching: false,
	didInvalidate: false,
	users: []
}, action) {
	console.log("Enter in users reducer")
	switch (action.type) {
		case INVALIDATE_USERS:
			return Object.assign({}, state, {
				didInvalidate: true
			})
		case REQUEST_USERS:
			return Object.assign({}, state, {
				isFetching: true,
				didInvalidate: false
			})
		case RECEIVE_USERS:
			console.log("In users.RECEIVE_USERS", action.users)
			return Object.assign({}, state, {
				isFetching: false,
				didInvalidate: false,
				users: action.users
			})
		default:
			return state
	}
}

function apiUsers(state = {}, action) {
	console.log("In apiUsers", state, action)
	switch (action.type) {
		case INVALIDATE_USERS:
		case RECEIVE_USERS:
		case REQUEST_USERS:
			return Object.assign({}, state,
				 users(state, action) // not sure
			)
		default:
			return state
	}
}

const rootReducer = combineReducers({
	apiUsers
})

export default rootReducer
