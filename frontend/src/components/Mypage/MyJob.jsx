import axios from "axios";
import useAsync from "../common/useAsync";
import Empty from "../common/Empty";
import { ListGroup, Spinner } from "react-bootstrap";

const getJobs = async () => {
  const res = await axios.get("face-image/jobs/");
  return res;
};

const MyJob = () => {
  const [state] = useAsync(getJobs, [], false, true);
  const { loading, data: jobs } = state;
  return (
    <div className="container row">
      {loading ? (
        <Spinner animation="border" />
      ) : (
        <>
          <div className="container col border working-jobs">
            {/* <ListGroup>
              {jobs
                .filter((job) => !job.finished)
                .map((job) => (
                  <ListGroup.Item>{job.id + job.link}</ListGroup.Item>
                ))}
            </ListGroup> */}
            <Empty></Empty>
          </div>
          <div className="container col border finished-jobs">
            <ListGroup>
              {jobs
                .filter((job) => job.finished)
                .map((job) => (
                  <ListGroup.Item>{job.id + job.link}</ListGroup.Item>
                ))}
            </ListGroup>
          </div>
        </>
      )}
    </div>
  );
};

export default MyJob;
