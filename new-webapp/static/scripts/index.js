/**
* @Author: valentin
* @Date:   2016-06-22T20:41:21+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-22T21:50:00+02:00
*/

import 'babel-polyfill'

import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { createStore, applyMiddleware } from 'redux'
import tweetsApp from './reducers'
import App from './components/App'


let store = createStore(
	tweetsApp,
	initialState,
    applyMiddleware(
      thunkMiddleware,
      loggerMiddleware
    )

)

render(
    <Provider store={store}>
        <App />,
    </Provider>
    document.getElementById('content')
);
