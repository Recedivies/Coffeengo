import React from "react";

import Accent from "../utils/Accent";

/**
 *
 * name, host->user, slots->x/total, Status->4 choices, Password->true/false
 */
const Lobby: React.FC = () => {
  return (
    <div className="flex flex-grow flex-col items-center justify-center">
      <Accent className="text-3xl font-bold">Lobby</Accent>
    </div>
  );
};
export default Lobby;
