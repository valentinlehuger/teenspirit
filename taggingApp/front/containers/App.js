import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { fetchUsersIfNeeded, invalidateUsers,
		fetchTweetsIfNeeded,
		validateUser, unvalidateUser } from '../actions'
import Tweets from '../components/Tweets'
import TagButton from '../components/TagButton'


class App extends Component {

    constructor(props) {
        console.log("App.constructor", props)
        super(props)
		this.handleValidate = this.handleValidate.bind(this)
		this.handleUnvalidate = this.handleUnvalidate.bind(this)
		this.intervalFunction = this.intervalFunction.bind(this)
    }

	intervalFunction() {
		const { dispatch } = this.props
		dispatch(fetchTweetsIfNeeded())
	}

    componentDidMount() {
        const { dispatch } = this.props
        dispatch(fetchUsersIfNeeded())
		setInterval(this.intervalFunction, 3000)
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
        const { tweets, users, current_user, dispatch } = this.props
		console.log("In app render", tweets, current_user, tweets[current_user])
        return (
            <div>
				<Tweets tweets={tweets[current_user]} />
                <TagButton label="Depressed" handleClick={this.handleValidate} />
                <TagButton label="Not depressed" handleClick={this.handleUnvalidate} />
            </div>
        )
    }
}

App.propTypes = {
    users: PropTypes.array.isRequired,
    tweets: PropTypes.object.isRequired,
	current_user: PropTypes.number,
    dispatch: PropTypes.func.isRequired
}

function mapStateToProps(state) {
    const { apiTweets } = state
    console.log("mapStateTopProps", apiTweets)
    const {
        users,
		current_user,
        tweets
    } = apiTweets || {
        users: [],
		current_user: '',
        tweets: {}
    }

    return {
        users,
        tweets,
		current_user
    }
}

export default connect(mapStateToProps)(App)
