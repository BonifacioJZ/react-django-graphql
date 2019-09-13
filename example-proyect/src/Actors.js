import React from 'react';
import {useQuery} from '@apollo/react-hooks';
import {gql} from 'apollo-boost';

const ACTORS_DATA= gql`
{
    actors{
        id,
        name
    }
}`

function Actors(){
    const { loading, error, data } = useQuery(ACTORS_DATA);
    if (loading) return <p>Loading...</p>;
    if(error) return <p>Error :(</p>;
    const actors = data.actors
    return actors.map(({id,name})=>(
        <div key={id}>
            <p>{name}</p>
        </div>
    )); 
}
export default Actors;