import React, { PropTypes, Component } from 'react'
import RaisedButton from 'material-ui/RaisedButton';
import getMuiTheme from 'material-ui/styles/getMuiTheme';

export default class TagButton extends Component {

	getChildContext() {
    	return { muiTheme: getMuiTheme(RaisedButton) };
	}

	render() {
        const { label, handleClick } = this.props

		return (
			<RaisedButton label={label} onClick={handleClick} />
		)
	}
}

TagButton.propTypes = {
    handleClick: PropTypes.func.isRequired,
    label: PropTypes.string.isRequired,
}

TagButton.childContextTypes = {
    muiTheme: React.PropTypes.object.isRequired,
};
