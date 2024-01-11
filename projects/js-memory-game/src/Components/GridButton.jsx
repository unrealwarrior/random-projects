import "../styles/GridButton.css"
function GridButton(props){
    const isActive = props.data.isActive
    const value = props.data.value
    const id = props.data.index
    const status = props.data.status
    let c = ""
    if (status == "error"){
        c = "grid__error"
    }else if(status == "success"){
        c = "grid__success"
    }
    console.log(c)
    return(
        <>
            <div onClick={() => {props.showValue(id)}} className={`grid__block ${isActive && "grid__active"} ${c}`}>
                <div className="grid__value">
                    <p>{isActive ? value : ""}</p>
                </div>
            </div>
            
        </>
    )
}

export default GridButton