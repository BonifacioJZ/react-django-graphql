import React from 'react';
import {useQuery} from '@apollo/react-hooks';
import {gql} from 'apollo-boost';
import ActorsMovie from './ActorsMovie';
const MOVIES_DATA = gql`
{
    movies{
        id,
        title,
        actors{
            id,
            name
        }
        year
    }
}`;

function Movies(){
    const { loading, error, data } = useQuery(MOVIES_DATA);
  
    if (loading) return <p>Loading...</p>;
    if(error) return <p>Error :(</p>;
    
    const movies = data.movies
    return movies.map(({id,title,year,actors})=>(
        <div key={id}>
            <p>
                {title}:{year}  
            </p>
            <ActorsMovie actors={actors}/>
         
        </div>
    ))
} 

export default Movies