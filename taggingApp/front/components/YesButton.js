import React, { PropTypes, Component } from 'react'
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

export default class YesButton extends Component {

	getChildContext() {
    	return { muiTheme: getMuiTheme(RaisedButton) };
	}

	render() {
		return (
			<RaisedButton label='YES' primary={true} />
		)
	}
}

YesButton.childContextTypes = {
    muiTheme: React.PropTypes.object.isRequired,
};