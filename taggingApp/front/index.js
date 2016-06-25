import React from 'react'
import ReactDOM from 'react-dom'
import { createStore } from 'redux'
import TestComponent from './components/TestComponent'
import testReducer from './reducers'

const store = createStore(testReducer)
const rootEl = document.getElementById('root')

function render() {
  ReactDOM.render(
    <TestComponent
      value={store.getState()}
      fetchUsers={() => store.dispatch({type: 'FETCH_USERS'})}
    />,
    rootEl
  )
}

render()
store.subscribe(render)
