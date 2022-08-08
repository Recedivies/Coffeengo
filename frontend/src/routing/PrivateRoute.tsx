import React from "react";
import { Navigate, Outlet } from "react-router-dom";

const PrivateRoute: React.FC = () => {
  const isAuthenticated = localStorage.getItem("token");

  if (isAuthenticated) {
    return <Outlet />;
  }
  return <Navigate to="/login" />;
};

export default PrivateRoute;
