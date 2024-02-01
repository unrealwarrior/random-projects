import {useRef, useState, useEffect, useCallback, useMemo} from "react";
import {useDropzone} from "react-dropzone";
import "../styles/CreateThread.css";
import {IconCamera} from "@tabler/icons-react"
export default function CreateThread(){
    const photo = useRef(null);
    const [hoverMode, setHover] = useState(false);
    const [image, setImage] = useState(null);
    const [fullDisplay, setFullDisplay] = useState(false);
    const [editMode, setEditMode] = useState(false);

    useEffect(() => {
        console.log(image)
    }, [image])

    const onDrop = useCallback((files) => {
        setImage(URL.createObjectURL(files[0]))
    }, [])
    const {getRootProps, getInputProps, isDragActive} = useDropzone({onDrop});

    function handleFileUpload(e){
        e.preventDefault()
        photo.current.click()
    }

    function handleImageClick(){
        setFullDisplay(!fullDisplay)
    }

    function handleInputClick(e){
        photo.current.click();
    }

    function selectFile(e){
        const files = e.target.files;
        setImage(URL.createObjectURL(files[0]))
    }
    const getFullDate = useMemo(() => {
        const weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]  // weeks starts with mondays ;)
        const weekday = weekdays[new Date().getDay()];
        const d = new Date().toLocaleString().split(" ")
        const date = `${d[0]} (${weekday}) ${d[1]}`
        return date
    }, [image])

    return(
        <>
            {editMode ? (
                <form className="form">
                    <div className="thread">
                            <div {...getRootProps()} className="thread__photo" onMouseEnter={() => {setHover(true)}} onMouseLeave={() => {setHover(false)}}>
                                {
                                    (isDragActive || hoverMode) &&
                                    <div className="photo__overlay" onClick={(e) => {handleInputClick(e)}}>
                                        <IconCamera color="#fff" size={"48px"} />
                                        <span>Click or Drop your photo here</span>
                                    </div>
                                }
                                    <input {...getInputProps()} ref={photo} type="file" id="ThreadPhoto" onChange={(e) => {selectFile(e)}} style={{display: "none"}}/>
                                    <div className="photo__upload">
                                        <img src={image || "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"} onClick={handleImageClick} />

                                    </div>
                            </div>
                        <div className="post__info">
                            <table>
                                <tbody>
                                    <tr>
                                        <th><span className="name">Anonymous </span></th>
                                        <td>
                                            <div style={{textAlign: "right"}}>
                                                <time className="date">{getFullDate} </time>
                                                <span className="post_no">No.?????????</span>
                                            </div>
                                        </td>
                                    </tr>
                                    <tr>
                                        <th><p>Title:</p></th>
                                        <td><input type="text" id="title"/></td>
                                    </tr>
                                    <tr>
                                        <th><p>Comment:</p></th>
                                        <td><textarea/></td>
                                    </tr>
                                    <tr>
                                        <th><p>Options:</p></th>
                                        <td><input type="text" id="options" /></td>
                                    </tr>
                                    <tr>
                                        <th><p>Password:</p></th>
                                        <td>
                                            <input type="text" id="password" />
                                            <span className="notice">• Please read the <a className="link" href="">Rules</a> and <a className="link" href="">FAQ</a> before posting.</span>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    <div className="verification">
                        <div className="verification__placeholder">
                            <span>CAPTCHA verification system goes here.</span>
                        </div>
                        <div className="submit">
                            <button>Preview</button>
                            <button className="mr-2">Create Post</button>
                        </div>
                    </div>
                    </div>

                    {/* <button onClick={(e) => {handleFileUpload(e)}} >upload file</button> */}
                </form>
            ) : (
                <div className="newthread__wrapper">
                    <h2>[<a href="#" className="new__thread" onClick={() => {setEditMode(true)}}>Create a New Thread</a>]</h2>
                </div>
            )}
        </>
    )
}