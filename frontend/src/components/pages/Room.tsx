import React from "react";

import Accent from "../utils/Accent";

const Room: React.FC = () => {
  return (
    <div className="flex flex-grow flex-col items-center justify-center">
      <Accent className="text-3xl font-bold">Room</Accent>
    </div>
  );
};

export default Room;
