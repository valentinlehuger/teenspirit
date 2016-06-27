/**
* @Author: valentin
* @Date:   2016-06-25T15:15:43+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-25T15:20:10+02:00
*/

import { combineReducers } from 'redux'
import {
	REQUEST_USERS, RECEIVE_USERS, INVALIDATE_USERS, REQUEST_TWEETS, RECEIVE_TWEETS
} from '../actions'

function apiUsers(state = {
	isFetchingUsers: false,
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
				isFetchingUsers: true,
				didInvalidate: false
			})
		case RECEIVE_USERS:
			console.log("In users.RECEIVE_USERS", action.users)
			return Object.assign({}, state, {
				isFetchingUsers: false,
				didInvalidate: false,
				users: action.users
			})
		default:
			return state
	}
}

function apiTweets(state = {
	tweets: []
}, action) {
	console.log("Enter in tweets reducer", action.type)
	switch (action.type) {
		case REQUEST_TWEETS:
			console.log("In tweets.REQUEST_TWEETS", action.tweets)
			return Object.assign({}, state, {})
		case RECEIVE_TWEETS:
			console.log("In tweets.RECEIVE_TWEETS", action.tweets)
			return Object.assign({}, state, {
				tweets: action.tweets
			})
		default:
			return state
	}
}

// function apiUsers(state = {
// 	isFetchingUsers: false,
// 	didInvalidate: false,
// 	users: []
// }, action) {
// 	console.log("In apiUsers", state, action)
// 	switch (action.type) {
// 		case INVALIDATE_USERS:
// 		case RECEIVE_USERS:
// 		case REQUEST_USERS:
// 			return Object.assign({}, state, users(state, action))
// 		default:
// 			return state
// 	}
// }

const rootReducer = combineReducers({
	apiUsers,
	apiTweets
})

export default rootReducer
