import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { fetchUsersIfNeeded, invalidateUsers } from '../actions'


class App extends Component {
	constructor(props) {
		console.log("App.constructor", props)
		super(props)
	}

	componentDidMount() {
	  const { dispatch } = this.props
	  dispatch(fetchUsersIfNeeded())
	}

	render() {
		const { users, isFetchingUsers } = this.props
		return (
			<p>
				users {users}<br/>
				isFetchingUsers {isFetchingUsers}
			</p>
		)
	}
}

// App.propTypes = {
// 	users: propTypes.array.isRequired,
// 	isFetchingUsers: PropTypes.bool.isRequired,
// 	dispatch: PropTypes.func.isRequired
// }

function mapStateToProps(state) {
	const { apiUsers } = state
	console.log("mapStateTopProps", state, isFetchingUsers, users)
	const {
		isFetchingUsers,
		users: users
	} = apiUsers || {
		isFetchingUsers: true,
		users: []
	}

	return {
		users,
		isFetchingUsers
	}
}

export default connect(mapStateToProps)(App)
