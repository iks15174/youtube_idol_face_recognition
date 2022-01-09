import React, { useState } from "react";
import ImageList from "../components/Main/ImageList";
import FolderList from "../components/Main/FolderList";

const Main = () => {
  const [youtubeLink, setYoutubeLink] = useState("");
  const iframeStyle = {
    width: "100%",
    height: "100vh",
  };
  const getVideo = (url) => {
    const regExp =
      /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);

    return match && match[2].length === 11 ? match[2] : null;
  };

  return (
    <div className="container">
      <div className="container youtube">
        <div className="container link p-0">
          <input
            onChange={(e) => setYoutubeLink(e.target.value)}
            type="text"
            className="form-control"
            placeholder="유튜브 영상 링크를 입력하세요."
          />
        </div>
        {getVideo(youtubeLink) ? (
          <div className="container video">
            <iframe
              style={iframeStyle}
              src={`https://www.youtube.com/embed/${getVideo(youtubeLink)}`}
              title="youtube-video"
              allowFullScreen
            ></iframe>
          </div>
        ) : null}
        <ImageList></ImageList>
      </div>
      <div className="container folder mt-5">
        <div className="input-group new-folder">
          <button className="btn btn-outline-primary" type="button">
            추가
          </button>
          <input
            onChange={(e) => setYoutubeLink(e.target.value)}
            type="text"
            className="form-control"
            placeholder="폴더이름을 입력하세요."
          />
        </div>
        <FolderList></FolderList>
      </div>
    </div>
  );
};

export default Main;
