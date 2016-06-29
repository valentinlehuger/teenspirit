import React, { PropTypes, Component } from 'react'

export default class Tweets extends Component {
	render() {
		return (
			<ul>
            {this.props.tweets}
	        </ul>
		)
	}
}

Tweets.propTypes = {
  tweets: PropTypes.object.isRequired
}
