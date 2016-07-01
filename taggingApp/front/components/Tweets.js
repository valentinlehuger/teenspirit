import React, { PropTypes, Component } from 'react'
import {Card, CardText} from 'material-ui/Card';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

export default class Tweets extends Component {
    getChildContext() {
    	return { muiTheme: getMuiTheme(Card, CardText) };
	}
	render() {
        console.log("In Tweets.render", this.props.tweets)
        if (this.props.tweets) {
            var tweets = this.props.tweets
        } else {
            var tweets = []
        }
		return (
            <div>
            {tweets.map((tweet, i) =>
                <Card>
                    <CardText>
		                  {tweet}
                    </CardText>
                </Card>
            )}
            </div>
	    )
	}
}

Tweets.propTypes = {
  tweets: PropTypes.array
}

Tweets.childContextTypes = {
    muiTheme: React.PropTypes.object.isRequired,
};
