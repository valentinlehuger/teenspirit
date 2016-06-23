/**
* @Author: valentin
* @Date:   2016-06-22T20:41:21+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-22T21:40:54+02:00
*/

import fetch from 'isomorphic-fetch'

export function requestUsers() {
    return {
        type: 'REQUEST_USERS'
    }
}

export function receiveUsers(json) {
    return {
        type: 'RECEIVE_USERS',
		posts: json.data.children.map(child => child.data)
    }
}

export function fetchUsers() {
	return function(dispatch) {
		dispatch(requestUsers())
		return fetch("http://127.0.0.1:3000/fetchUsers")
			.then(response => response.json())
			.then(json => dispatch(receiveUsers(json)))
	}
}
