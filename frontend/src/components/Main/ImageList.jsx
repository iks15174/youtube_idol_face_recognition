import React from "react";
import image1 from "../../img/2.jpg";

const ImageList = (props) => {
  const imageWidth = "10%";
  return (
    <div className="container face-result mt-2 border bg-light text-center">
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
      <img src={image1} className="rounded m-1" width={imageWidth} alt=""></img>
    </div>
  );
};

export default ImageList;
