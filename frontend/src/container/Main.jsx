import React, { useState } from "react";

const Main = () => {
    const [youtubeLink, setYoutubeLink] = useState("");
    const iframeStyle = {
        width: "100%",
        height: "100vh"
    }
    const getVideo = (url) => {
        const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
        const match = url.match(regExp);

        return (match && match[2].length === 11)
            ? match[2]
            : null;
    }

    return (
        <div className="container">
            <div className="container youtube">
                <div className="container link">
                    <input onChange={(e) => setYoutubeLink(e.target.value)} type="text" className="form-control" placeholder="유튜브 영상 링크를 입력하세요." />
                </div>
                {getVideo(youtubeLink) ?
                    (<div className="container video rati">
                        <iframe style={iframeStyle} src={`https://www.youtube.com/embed/${getVideo(youtubeLink)}`} title="youtube-video" allowFullScreen></iframe>
                    </div>) : null}
                <div className="container face-result">
                    face result area
                </div>
            </div>
            <div className="container folder">
                <div className="container new-folder">
                    new folder
                </div>
                <div className="container folder-list">
                    folder list
                </div>
            </div>
        </div>
    );
}

export default Main