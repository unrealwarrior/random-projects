import { useState } from "react";
import { Tooltip } from "react-tooltip";

export default function Info(props){
    const displayTitle = props.title;
    const [dropmenu, setDropmenu] = useState(false);

    function handlePostReply(e){
        const id = e.target.text;
        console.log(`Trying to reply to post >${id}`)
    }

    const placeholders = ["10637834", "10637835", "10637836", "10637837", "10637838"]
    return(
        <>
            <input type="checkbox" id="select" />
            {displayTitle && (<span className="title">First Post!!!</span>)}
            <span className="name">Anonymous</span>
            <span className="date" id="date">01/19/2024(Fri)22:33:07 </span>
            <span className="thread__no"><a href='#10000' className="link">No.</a><a href="#" className="link" onClick={(e) => {handlePostReply(e)}}>?????????</a></span>
            <div style={{position: "relative"}} className={`op__dropmenu ${dropmenu && "dropmenu__clicked"}`} onClick={() => {setDropmenu(!dropmenu)}}>
                <span>▶</span>
                {/* dropdown menu here */}
            </div>
            {placeholders.map((p, i) => (
                <span><a key={i} href={`#${p}`} id={p} className="reply__link">{`>>${p}`}</a></span>
            ))}
            <Tooltip style={{padding: "4px 8px", backgroundColor: "#000", borderRadius: "0px", transition: "none"}} place="top" anchorSelect="#date">
                <span>x time ago</span>
            </Tooltip>
        </>
    )
}