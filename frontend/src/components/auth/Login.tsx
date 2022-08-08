import axios, { AxiosError } from "axios";
import React from "react";
import { IoIosUnlock } from "react-icons/io";
import { Link, useNavigate } from "react-router-dom";
import { toast } from "react-toastify";

import { onLogin } from "../../api/auth";
import { useNotifContext } from "../../hooks/useContextHooks";
import clsxm from "../../lib/clsxm";
import Accent from "../utils/Accent";

const Login: React.FC = () => {
  const navigate = useNavigate();
  const { toggleNotificataion } = useNotifContext();

  const [username, setUsername] = React.useState<string>("");
  const [password, setPassword] = React.useState<string>("");

  const submitForm = async (e: React.FormEvent): Promise<void> => {
    e.preventDefault();
    try {
      const { data } = await onLogin({
        username: username,
        password: password,
      });
      localStorage.setItem("token", data.token);

      toggleNotificataion("login");
      setTimeout(() => navigate("/"), 500);
    } catch (error) {
      if (axios.isAxiosError(error)) {
        const serverError = error as AxiosError;
        if (serverError && serverError.response) {
          toast.error(
            JSON.stringify(serverError.response.data)
              .replace(/]|[[]/g, "")
              .replace(/[{}]/g, ""),
          );
        }
      }
    }
  };

  return (
    <main
      className={clsxm("flex flex-grow flex-col items-center justify-center")}
    >
      <div className="spin-slow flex flex-col items-center justify-center">
        <span>
          <IoIosUnlock
            className={clsxm("h-10 w-10 mb-2", "transition-colors")}
          />
        </span>
        <span className="font-bold md:text-2xl">
          <Accent>Sign in</Accent>
        </span>
      </div>

      <form onSubmit={submitForm}>
        <div className="mb-3">
          <label className="block mb-2 text-sm font-medium transition-colors">
            User Name
          </label>
          <input
            id="username"
            type="text"
            className="text-black shadow-sm text-lg rounded-lg block w-96 p-2.5"
            placeholder="John Doe"
            required
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="block mb-2 text-sm font-medium transition-colors">
            Password
          </label>
          <input
            id="password"
            type="password"
            className="text-black shadow-sm text-lg rounded-lg block w-96 p-2.5"
            placeholder="********"
            required
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <div className="my-4">
          <button
            className={clsxm(
              "shadow-sm text-sm rounded-lg w-full",
              "border border-primary-50",
              "hover:bg-primary-500 hover:text-black",
              "scale-100 transform-gpu hover:scale-[1.03] active:scale-[0.97]",
              "transition duration-300",
              "font-bold py-2 px-6",
              "active:bg-primary-400",
            )}
          >
            SIGN IN
          </button>
        </div>
        <div className="justify-items-end items-end flex flex-col text-sm">
          <Link className="text-primary-300 underline" to="/register">
            Don't have an account? Sign Up
          </Link>
        </div>
      </form>
    </main>
  );
};
export default Login;
