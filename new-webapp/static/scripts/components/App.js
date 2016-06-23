/**
* @Author: valentin
* @Date:   2016-06-22T20:41:21+02:00
* @Last modified by:   valentin
* @Last modified time: 2016-06-22T21:52:49+02:00
*/

/**
 *  Structure:
 *      - UserBox
 *          - TweetList
 *              - Tweet
 *          - ChoiceBox
 *              - Choice
 */

 import React, { Component, PropTypes } from 'react'
 import { connect } from 'react-redux'
import { fetchUsers } from '../actions'

// var Tweet = React.createClass({
//     rawMarkup: function() {
//         var md = new Remarkable();
//         var rawMarkup = md.render(this.props.children.toString());
//         return { __html: rawMarkup };
//     },
//
//     render: function() {
//         var md = new Remarkable();
//         return (
//             <div className="tweet">
//                 <span dangerouslySetInnerHTML={this.rawMarkup()} />
//             </div>
//         );
//     }
// });
//
// var UserBox = React.createClass({
//     getInitialState: function() {
//         return {data: []};
//     },
//     componentDidMount: function() {
//         console.log(this.props.url)
//         $.ajax({
//             url: this.props.url,
//             dataType: 'json',
//             cache: false,
//             success: function(data) {
//                 this.setState({data: data});
//             }.bind(this),
//             error: function(xhr, status, err) {
//                 console.error(this.props.url, status, err.toString());
//             }.bind(this)
//         });
//     },
//     render: function() {
//         return (
//             <div className="userBox">
//             <h1>User</h1>
//             <TweetList data={this.state.data} />
//             <ChoiceBox />
//             </div>
//      );
//    }
//  });
//
// var TweetList = React.createClass({
//     render: function() {
//         var tweetNodes = this.props.data.map(function(tweet) {
//             return (
//                 <Tweet key={tweet.id}>
//                     {tweet.text}
//                 </Tweet>
//             );
//         });
//         return (
//             <div className="tweetList">
//                 {tweetNodes}
//             </div>
//         );
//     }
// });
//
//  var ChoiceBox = React.createClass({
//    render: function() {
//      return (
//        <div className="choiceBox">
//          Hello, world! I am a ChoiceBox.
//        </div>
//      );
//    }
//  });


const App = () => (
    <div>
        // <UserBox url="/api/tweets" />
    </div>
)

export default App
