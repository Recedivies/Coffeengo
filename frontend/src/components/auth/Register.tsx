import axios, { AxiosError } from "axios";
import React from "react";
import { IoIosLock } from "react-icons/io";
import { Link } from "react-router-dom";
import { toast } from "react-toastify";

import { onRegister } from "../../api/auth";
import { useNotifContext } from "../../hooks/useContextHooks";
import clsxm from "../../lib/clsxm";
import Accent from "../utils/Accent";

const Register: React.FC = () => {
  const { toggleNotificataion } = useNotifContext();

  const [username, setUsername] = React.useState<string>("");
  const [email, setEmail] = React.useState<string>("");
  const [password1, setPassword1] = React.useState<string>("");
  const [password2, setPassword2] = React.useState<string>("");

  const submitForm = async (e: React.FormEvent): Promise<void> => {
    e.preventDefault();
    try {
      const { data } = await onRegister({
        username: username,
        email: email,
        password1: password1,
        password2: password2,
      });
      localStorage.setItem("token", data.token);

      toggleNotificataion("register");
      window.location.reload();
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

  const passwordMatch = () => password1 === password2;

  return (
    <main
      className={clsxm(
        "flex flex-grow flex-col items-center justify-center min-h-screen",
      )}
    >
      <div className="spin-slow flex flex-col items-center justify-center">
        <span>
          <IoIosLock className={clsxm("h-10 w-10 mb-2", "transition-colors")} />
        </span>
        <span className="font-bold md:text-2xl">
          <Accent>Sign up</Accent>
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
            Email
          </label>
          <input
            id="email"
            type="email"
            className="text-black shadow-sm text-lg rounded-lg block w-96 p-2.5"
            placeholder="JohnDoe@gmail.com"
            required
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="mb-3">
          <label className="block mb-2 text-sm font-medium transition-colors">
            Password
          </label>
          <input
            id="password1"
            type="password"
            className="text-black shadow-sm text-lg rounded-lg block w-96 p-2.5"
            placeholder="********"
            required
            onChange={(e) => setPassword1(e.target.value)}
          />
          {!passwordMatch() && (
            <p className="mt-2 text-sm text-red-600 dark:text-red-500">
              <span className="font-medium">Passwords don't match</span>
            </p>
          )}
        </div>
        <div className="mb-3">
          <label className="block mb-2 text-sm font-medium transition-colors">
            Confirm Password
          </label>
          <input
            id="password2"
            type="password"
            className="text-black shadow-sm text-lg rounded-lg block w-96 p-2.5"
            placeholder="********"
            required
            onChange={(e) => setPassword2(e.target.value)}
          />
          {!passwordMatch() && (
            <p className="mt-2 text-sm text-red-600 dark:text-red-500">
              <span className="font-medium">Passwords don't match</span>
            </p>
          )}
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
            )}
          >
            SIGN UP
          </button>
        </div>
        <div className="justify-items-end items-end flex flex-col text-sm">
          <Link className="text-primary-300 underline" to="/login">
            Already have an account? Sign in
          </Link>
        </div>
      </form>
    </main>
  );
};
export default Register;
