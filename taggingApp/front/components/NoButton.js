import React, { PropTypes, Component } from 'react'
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

export default class NoButton extends Component {

	getChildContext() {
    	return { muiTheme: getMuiTheme(RaisedButton) };
	}

	render() {
		return (
			<RaisedButton label='Unvalidate' secondary={true} />
		)
	}
}

NoButton.childContextTypes = {
    muiTheme: React.PropTypes.object.isRequired,
};