/**
* @Author: valentin
* @Date:   2016-06-25T15:15:43+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-25T15:20:10+02:00
*/

export default function testReducer(state = [], action) {
	switch (action.type) {
		case 'FETCH_USERS':
			return [1, 2, 3]
		default:
			return state
	}
}
