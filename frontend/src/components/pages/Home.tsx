import React from "react";
import { FiCoffee } from "react-icons/fi";
import { useNavigate } from "react-router-dom";

import { getUser } from "../../api/auth";
import clsxm from "../../lib/clsxm";
import Accent from "../utils/Accent";
import { toastSuccess } from "../utils/Toast";

const Home: React.FC = () => {
  const username = localStorage.getItem("username");
  const isAuthenticated = localStorage.getItem("token");
  const isNotificationActive = localStorage.getItem("notif");
  const navigate = useNavigate();

  React.useEffect(() => {
    const fetchUser = async (): Promise<void> => {
      const { data } = await getUser();
      const { username } = data;
      localStorage.setItem("username", username);
    };
    if (isAuthenticated) fetchUser();
  }, []);
  toastSuccess(isNotificationActive, username);

  return (
    <main
      className={clsxm("flex flex-grow flex-col items-center justify-center")}
    >
      <div className="spin-slow animate-logo-app">
        <FiCoffee
          className={clsxm(
            "fill-white h-16 w-16 mr-4 mb-6 inline-block",
            "text-gray-500 hover:text-primary-300 dark:text-gray-200 dark:hover:text-primary-300",
            "transition-colors",
          )}
        />
        <Accent className="font-bold md:text-5xl">Coffeengo</Accent>
      </div>

      <div className="m-4">
        {isAuthenticated ? (
          <div>
            {[
              ["Join Room", "/join"],
              ["Create Room", "/create"],
            ].map(([title, url]) => (
              <button
                key={title}
                className={clsxm(
                  "focus:outline-none focus-visible:ring focus-visible:ring-primary-500",
                  "shadow-sm",
                  "border border-primary-50",
                  "hover:bg-primary-500 hover:text-black",
                  "active:bg-primary-600",
                  "disabled:bg-primary-600 disabled:hover:bg-primary-600",
                  "scale-100 transform-gpu hover:scale-[1.03] active:scale-[0.97]",
                  "transition duration-300",
                  "font-bold py-2 px-6 rounded-full mx-3",
                )}
                onClick={() => navigate(url)}
              >
                {title}
              </button>
            ))}
          </div>
        ) : (
          <div>
            {[
              ["Login", "/login", "login-home"],
              ["Register", "/register", "register-home"],
            ].map(([title, url, id]) => (
              <button
                id={id}
                key={title}
                className={clsxm(
                  "focus:outline-none focus-visible:ring focus-visible:ring-primary-500",
                  "shadow-sm",
                  "border border-primary-50",
                  "hover:bg-primary-500 hover:text-black",
                  "active:bg-primary-400",
                  "disabled:bg-primary-600 disabled:hover:bg-primary-600",
                  "scale-100 transform-gpu hover:scale-[1.03] active:scale-[0.97]",
                  "transition duration-300",
                  "font-bold py-2 px-6 rounded-full mx-3",
                )}
                onClick={() => navigate(url)}
              >
                {title}
              </button>
            ))}
          </div>
        )}
      </div>
    </main>
  );
};

export default Home;
