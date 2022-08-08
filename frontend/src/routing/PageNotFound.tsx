import React from "react";
import { TbError404 } from "react-icons/tb";
import { Link } from "react-router-dom";

import Accent from "../components/utils/Accent";

const PageNotFound: React.FC = () => {
  return (
    <div className="flex flex-auto items-center justify-center">
      <div className="font-bold md:text-6xl inline-block">
        <Accent>Page Not Found!</Accent>
      </div>
      <Link to="/" className="inline-block text-5xl">
        <TbError404 className="h-16 w-16 ml-4" />
      </Link>
    </div>
  );
};

export default PageNotFound;
