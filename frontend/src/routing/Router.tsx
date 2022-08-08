import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";

import Login from "../components/auth/Login";
import Register from "../components/auth/Register";
import Layout from "../components/layout/Layout";
import CreateRoom from "../components/pages/CreateRoom";
import Home from "../components/pages/Home";
import JoinRoom from "../components/pages/JoinRoom";
import Lobby from "../components/pages/Lobby";
import Profile from "../components/pages/Profile";
import Room from "../components/pages/Room";
import AuthRoute from "./AuthRoute";
import PageNotFound from "./PageNotFound";
import PrivateRoute from "./PrivateRoute";

const Router: React.FC = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>
          <Route index element={<Home />} />

          <Route path="/" element={<PrivateRoute />}>
            <Route path="lobby" element={<Lobby />} />
            <Route path="profile" element={<Profile />} />
            <Route path="join" element={<JoinRoom />} />
            <Route path="create" element={<CreateRoom />} />
            <Route path="room/:code" element={<Room />} />
          </Route>

          <Route path="/" element={<AuthRoute />}>
            <Route path="login" element={<Login />} />
            <Route path="register" element={<Register />} />
          </Route>

          <Route path="*" element={<PageNotFound />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
};

export default Router;
