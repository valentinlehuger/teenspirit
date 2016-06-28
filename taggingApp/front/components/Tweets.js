import React, { PropTypes, Component } from 'react'

export default class Tweets extends Component {
	render() {
		return (
			<ul>
	          {this.props.tweets.map((tweet, i) =>
	            <li key={i}>{tweet}</li>
	          )}
	        </ul>
		)
	}
}

Tweets.propTypes = {
  tweets: PropTypes.array.isRequired
}
