import axios from "axios";
import useAsync from "../common/useAsync";

const getJobs = async () => {
  const res = await axios.get("face-image/folders/");
  return res;
};

const MyJob = () => {
  const [state, reGetFolder] = useAsync(getJobs, [], false);
  const { loading, data: folders, error } = state;
  console.log(folders);

  return (
    <div className="container row">
      <div className="container col">finished JOB</div>
      <div className="container col">finished JOB</div>
    </div>
  );
};

export default MyJob;
