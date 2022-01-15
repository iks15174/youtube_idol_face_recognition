import React, { useState } from "react";
import axios from "axios";
import useAsync from "../components/common/useAsync";

const getFolders = async () => {
  const res = await axios.get("face-image/folders/");
  return res;
};

const Mypage = () => {
  const [state, reGetFolder] = useAsync(getFolders, [], false);
  const { loading, data: folders, error } = state;
  console.log(folders);

  return (
    <div className="container">
      <div className="container row">
        <div className="container col">on working JOB</div>
        <div className="container col">finished JOB</div>
      </div>
      <div className="container">folder area</div>
    </div>
  );
};

export default Mypage;
