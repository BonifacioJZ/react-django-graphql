import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import ApolloClient from 'apollo-boost';
import {ApolloProvider} from '@apollo/react-hooks';
//import Movies from './Movies'
import Actors from './Actors'
import AddActor from './AddActor';
const client = new ApolloClient({
    uri:'http://127.0.0.1:8000/graphql/'
})

const App = () => (
    <ApolloProvider client={client}>
      <div>
        <h2>My first Apollo app</h2>
        <Actors/>
        <AddActor/>
      </div>
    </ApolloProvider>
  );


ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

