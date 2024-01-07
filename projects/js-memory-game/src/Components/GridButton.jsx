import "../styles/GridButton.css"
import { useState, useEffect } from "react"
function GridButton(props){
    const isActive = props.data.isActive
    const value = props.data.value
    const id = props.data.index
    return(
        <>
            <div onClick={() => {props.showValue(id)}} className={"grid__block"}>
                <p>{isActive ? value : ""}</p>
            </div>
            
        </>
    )
}

export default GridButton