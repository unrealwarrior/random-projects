import "../styles/Reply.css"
import Info from "./utils/Info"
export default function Reply(){
    return(
        <>
            <span className="reply__chevron">{">>"}</span>
            <div className="post__reply">
                <div className="op__post">
                    <Info title={false} />
                    <div className="files">
                    </div>
                    <div className="body">
                        <a href="#" className="reply__highlight">{">>1"}</a>
                        <span className="reply">bump.</span>
                    </div>
                </div>
            </div>
        </>
    )
}