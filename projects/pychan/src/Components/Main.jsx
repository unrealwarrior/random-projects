import Banner from "./banner"
import "../styles/main.css"
import CreateThread from "./CreateThread"
import ThreadPost from "./ThreadPost"
import Reply from "./Reply"
import {useState} from "react"

const dummyBoards = ["a", "b", "c", "vr", "v"]
function Main(){
    const [enableCounter, setEnableCounter] = useState(false);
    const [counter, setCounter] = useState(10)

    
    function handleCountdown(){
        setInterval(() => {
            setCounter(prev => prev - 1);
        }, 1000);
    }
    function handleCounter(e){
        if(e.target.checked){
            setEnableCounter(true)
        }else{
            setEnableCounter(false)
        }

    }
    return(
        <>
            <div className="boards">
                <span className="boards-list">
                    [
                        {dummyBoards.map((board, index) => (
                            <>
                                <a href={`/${board}`}> {board} </a>
                                {index < (dummyBoards.length - 1) && "/"}
                            </>
                            
                        ))}
                    ]
                </span>   
            </div>
            <div>
                <div className="main">
                    <div className="banner">
                        <Banner />
                    </div>
                    <h1 className="board__name">/b/ - random</h1>
                    <hr className="line sm" />
                    <CreateThread />

                </div>
                <hr className="line" />
                <span><a href="/b/">[Return]</a></span>
                <span><a href="/b/catalog">[Catalog]</a></span>
                <span><a href="/b/#bottom">[Bottom]</a></span>
                <span><a href="/b/#refresh">[Refresh]</a></span>
                <span>
                    <input type="checkbox" onChange={(e) => {handleCounter(e)}} />
                    <span>[Auto]</span>
                </span>
                {enableCounter && <span>{counter}</span>}


                <ThreadPost />
                <Reply />
                <br/>
                <Reply />
                <br/>
                <Reply />
                <br/>
                <Reply />
            </div>

        </>
    )
}

export default Main