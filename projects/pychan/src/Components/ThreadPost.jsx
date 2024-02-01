import "../styles/ThreadPost.css"
import {useState} from "react"
import {IconDownload} from "@tabler/icons-react"
import Info from "./utils/Info";

export default function ThreadPost(){
    const [fullImage, setFullImage] = useState(false);


    function handleImageClick(){
        setFullImage(!fullImage)
    }
    
    return(
        <div>
        <div>
            <div style={{display: "flex"}}>
                <div style={{display: "flex", alignItems: "center"}}>
                    <span className="fileinfo">File: <a href="/Duke.png" target="_blank" className="link">Duke.png</a> (100KB, 500x500) </span>
                    <a download className="link__download" href="/Duke.png"><IconDownload size={"18px"} style={{marginLeft: "8px", cursor: "pointer"}}/></a>

                </div>

            </div>
            {fullImage ? (
            <>
                <img src="Duke.png" className="fullimage" onClick={handleImageClick} />
            </>) : (
            <>
                <img src="Duke.png" className="image__small" onClick={handleImageClick}/>
            </>
            )}
            
            <div className="op__post" id="10000">
                <Info />
                <div className="post__description">
                    <span>What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.

                        I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words.

                        You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands.

                        Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue.

                        But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it..</span>
                </div>
            </div>
        </div>
        </div>
    )
}