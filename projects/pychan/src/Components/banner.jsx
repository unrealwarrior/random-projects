import "../styles/banner.css"

export default function Banner(props){
    return(
        <>
        {props.photo ? (<>
            <img src={props.photo} width={"300px"} height={"100px"} />
        </>) : (<>
            <div className="banner__placeholder">
                <p>Banner placeholder</p>
                <p>Change the banner component with yours</p>
                <p className="brand">PyChan 0.1</p>
            </div>
        </>)}
        </>
    )
}