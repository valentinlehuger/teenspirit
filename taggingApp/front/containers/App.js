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
		const { users, isFetching } = this.props
		return (
			<p>
				users {users}<br/>
				isFetching {isFetching}
			</p>
		)
	}
}

// App.propTypes = {
// 	users: propTypes.array.isRequired,
// 	isFetching: PropTypes.bool.isRequired,
// 	dispatch: PropTypes.func.isRequired
// }

function mapStateToProps(state) {
	const { apiUsers } = state
	console.log("mapStateTopProps", state, isFetching, users)
	const {
		isFetching,
		users: users
	} = apiUsers || {
		isFetching: true,
		users: []
	}

	return {
		users,
		isFetching
	}
}

export default connect(mapStateToProps)(App)
