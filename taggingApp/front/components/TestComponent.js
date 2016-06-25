/**
* @Author: valentin
* @Date:   2016-06-25T14:57:54+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-25T15:31:21+02:00
*/

import React, { Component, PropTypes } from 'react'

class TestComponent extends Component {
  constructor(props) {
    super(props)
  }

  render() {
    const { value, fetchUsers } = this.props
    return (
	  <p>
        <button onClick={fetchUsers}>
		  Load list
        </button>
		<br/>
		{value}
	  </p>
    )
  }
}

TestComponent.propTypes = {
  fetchUsers: PropTypes.func.isRequired
}

export default TestComponent
