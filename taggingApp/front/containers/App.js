import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { fetchUsersIfNeeded, invalidateUsers,
		fetchTweetsIfNeeded,
		validateUser, unvalidateUser } from '../actions'
import Tweets from '../components/Tweets'

class App extends Component {
    constructor(props) {
        console.log("App.constructor", props)
        super(props)
		this.handleValidate = this.handleValidate.bind(this)
		this.handleUnvalidate = this.handleUnvalidate.bind(this)
    }

    componentDidMount() {
        const { dispatch } = this.props
        dispatch(fetchUsersIfNeeded())
    }

	handleValidate() {
		const { dispatch, current_user } = this.props
		console.log("In handleValidate", current_user)
		if (current_user) {
			var xmlhttp = new XMLHttpRequest();
			xmlhttp.open("POST", "http://localhost:3033/tag_user");
			xmlhttp.setRequestHeader("Content-Type", "application/json");
			xmlhttp.send(JSON.stringify({user_id:current_user, tag_name: "depressed", tag_value: true}));
			dispatch(validateUser(current_user, dispatch))
		}
	}

	handleUnvalidate() {
		const { dispatch, current_user } = this.props
		console.log("In handleUnvalidate", current_user)
		if (current_user) {
			var xmlhttp = new XMLHttpRequest();
			xmlhttp.open("POST", "http://localhost:3033/tag_user");
			xmlhttp.setRequestHeader("Content-Type", "application/json");
			xmlhttp.send(JSON.stringify({user_id:current_user, tag_name: "depressed", tag_value: false}));
			dispatch(unvalidateUser(current_user, dispatch))
		}
	}

    render() {
        const { tweets, users, isFetchingUsers, dispatch } = this.props
        return (
            <div>
                users {users}<br/>
                isFetchingUsers {isFetchingUsers}<br/>
				<Tweets tweets={tweets} />
				<a href="#" onClick={this.handleValidate}>
	             	Validate
				 </a>
				 <a href="#" onClick={this.handleUnvalidate}>
 	             	Unvalidate
 				 </a>
            </div>
        )
    }
}

App.propTypes = {
    users: PropTypes.array.isRequired,
    tweets: PropTypes.array.isRequired,
	current_user: PropTypes.string,
    isFetchingUsers: PropTypes.bool.isRequired,
    dispatch: PropTypes.func.isRequired
}

function mapStateToProps(state) {
    const { apiUsers } = state
    const { apiTweets } = state
    console.log("mapStateTopProps", apiUsers)
    const {
        isFetchingUsers,
        users,
		current_user
    } = apiUsers || {
        isFetchingUsers: true,
        users: [],
		current_user: ''
    }
    const {
        tweets
    } = apiTweets || {
        tweets: []
    }

    return {
        users,
        isFetchingUsers,
        tweets,
		current_user
    }
}

export default connect(mapStateToProps)(App)
