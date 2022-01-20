import { BsFillTrashFill } from "react-icons/bs";
import styled from "styled-components";

const Empty = () => {
  return (
    <EmojiContainer>
      <BsFillTrashFill size={48}></BsFillTrashFill>
    </EmojiContainer>
  );
};
const EmojiContainer = styled.div`
  width: 100%;
  height: 5rem;
  text-align: center;
  line-height: 5rem;
`;

export default Empty;
