import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { fetchUsersIfNeeded, invalidateUsers, fetchTweetsIfNeeded } from '../actions'
import Tweets from '../components/Tweets'
import YesButton from '../components/YesButton'
import NoButton from '../components/NoButton'

class App extends Component {

    constructor(props) {
        console.log("App.constructor", props)
        super(props)
    }

    componentDidMount() {
        const { dispatch } = this.props
        dispatch(fetchUsersIfNeeded())
        dispatch(fetchTweetsIfNeeded())
    }

    render() {
        const { tweets, users, isFetchingUsers, dispatch } = this.props
        return (
            <p>
                users {users}<br/>
                isFetchingUsers {isFetchingUsers}<br/>
				<Tweets tweets={tweets} />
                <YesButton /> <NoButton />
            </p>
        )
    }
}

App.propTypes = {
    users: PropTypes.array.isRequired,
    tweets: PropTypes.array.isRequired,
    isFetchingUsers: PropTypes.bool.isRequired,
    dispatch: PropTypes.func.isRequired
}

function mapStateToProps(state) {
    const { apiUsers } = state
    const { apiTweets } = state
    console.log("mapStateTopProps", apiUsers)
    const {
        isFetchingUsers,
        users
    } = apiUsers || {
        isFetchingUsers: true,
        users: []
    }
    const {
        tweets
    } = apiTweets || {
        tweets: []
    }

    return {
        users,
        isFetchingUsers,
        tweets
    }
}

export default connect(mapStateToProps)(App)
