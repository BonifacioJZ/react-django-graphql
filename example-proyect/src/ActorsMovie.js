import React from 'react'

function ActorsMovies(props){
    return props.actors.map(({id,name})=>(
        <div key={id}>
           
            {name}
        </div>
    ))
}
export default ActorsMovies