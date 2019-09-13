import React from 'react';
import {useMutation} from '@apollo/react-hooks';
import {gql} from 'apollo-boost';
const ADD_ACTOR = gql`
    mutation CreateActors($input:ActorInput!){
        createActor(input:$input){
            ok,
            actor{
                name
            }
        }

    }
`

function AddActor(){
    let input;
    const [createActor,{mutationError}]= useMutation(ADD_ACTOR)
    
    return (
        <div>
            <form
                onSubmit={e=>{
                    
                    e.preventDefault();
                    let inputActor = {
                        name:input.value
                    }
                    createActor({variables:{input:inputActor}});
                    input.value='';
                    console.log(mutationError)
                }}>
                <input
                    ref={node=>{
                        input = node;
                    }}
                />
                <button type="submit">Add Actor</button>
            </form>
        </div>
    )
}
export default AddActor;