import React from "react";
import FolderItem from "./FolderItem";

const FolderList = (props) => {
  return (
    <div className="container border mt-1 pb-2">
      <FolderItem></FolderItem>
      <FolderItem></FolderItem>
      <FolderItem></FolderItem>
    </div>
  );
};

export default FolderList;
