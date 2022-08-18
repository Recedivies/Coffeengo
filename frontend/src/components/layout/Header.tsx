import React from "react";
import { FiCoffee } from "react-icons/fi";
import { Link, useNavigate } from "react-router-dom";

import { onLogout } from "../../api/auth";
import { useNotifContext } from "../../hooks/useContextHooks";
import clsxm from "../../lib/clsxm";
import { Links } from "../../types";
import Accent from "../utils/Accent";
import ColorModeToggle from "../utils/ColorModeToggle";

const mainLinks: Links = [
  { href: "/", label: "Home" },
  { href: "/lobby", label: "Lobby" },
];

const authLinks: Links = [
  { href: "/login", label: "Login" },
  { href: "/register", label: "Register" },
];

const Header: React.FC = () => {
  const navigate = useNavigate();
  const { toggleNotificataion } = useNotifContext();

  const logout = async (): Promise<void> => {
    try {
      await onLogout();
      localStorage.removeItem("token");
      toggleNotificataion("logout");
      setTimeout(() => navigate("/"), 500);
    } catch (error) {
      // remove token and reload either way;
      // even though user might still be logged on the backend with old creds
      localStorage.removeItem("token");
      window.location.reload();
    }
  };
  const isAuthenticated = localStorage.getItem("token");
  return (
    <header className={clsxm("top-0 z-50 transition-shadow", "shadow-lg")}>
      <nav className={clsxm("flex items-center justify-between flex-wrap")}>
        <div className="flexitems-center flex-shrink-0 text-white mr-6 ml-8">
          <Link to="/" className="inline-block mt-3">
            <FiCoffee
              className={clsxm(
                "fill-white h-12 w-14 mr-2 mb-3 inline-block",
                "text-gray-500 hover:text-primary-300 dark:text-gray-200 dark:hover:text-primary-300",
                "transition-colors",
              )}
            />
            <Accent className="font-semibold text-3xl tracking-tight">
              Coffeengo
            </Accent>
          </Link>
        </div>

        <div className="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
          {mainLinks.map(({ href, label }) => (
            <Link key={`${href}${label}`} to={href}>
              <span
                className={clsxm(
                  "transition",
                  "duration-300 hover:bg-gradient-to-r group-hover:opacity-100",
                  "hover:text-primary-50",
                  "block mt-4 lg:inline-block lg:mt-0 mr-5",
                )}
              >
                {label}
              </span>
            </Link>
          ))}
        </div>

        <div className={clsxm("flex items-center")}>
          {isAuthenticated ? (
            <div>
              <Link to="/profile">
                <span
                  className={clsxm(
                    "transition",
                    "duration-300 hover:bg-gradient-to-r group-hover:opacity-100",
                    "hover:text-primary-50",
                    "block mt-4 lg:inline-block lg:mt-0 mr-5",
                  )}
                >
                  Profile
                </span>
              </Link>
              <button onClick={logout}>
                <span
                  className={clsxm(
                    "transition",
                    "duration-300 hover:bg-gradient-to-r group-hover:opacity-100",
                    "hover:text-primary-50",
                    "block mt-4 lg:inline-block lg:mt-0 mr-5",
                  )}
                >
                  Logout
                </span>
              </button>
            </div>
          ) : (
            <div>
              {authLinks.map(({ href, label }) => (
                <Link key={`${href}${label}`} to={href}>
                  <span
                    className={clsxm(
                      "transition",
                      "duration-300 hover:bg-gradient-to-r group-hover:opacity-100",
                      "hover:text-primary-50",
                      "block mt-4 lg:inline-block lg:mt-0 mr-5",
                    )}
                  >
                    {label}
                  </span>
                </Link>
              ))}
            </div>
          )}
          <ColorModeToggle />
          <div className="block lg:hidden">
            <button className="flex items-center px-4 py-3 border rounded text-teal-500 border-teal-500 focus:outline-none">
              <svg
                className="fill-current h-3 w-3"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <title>Menu</title>
                <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
              </svg>
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
