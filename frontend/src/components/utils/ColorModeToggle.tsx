import React from "react";
import { FiMoon, FiSun } from "react-icons/fi";

import { useThemeContext } from "../../hooks/useContextHooks";
import clsxm from "../../lib/clsxm";

const ColorModeToggle = (): JSX.Element => {
  const { theme, toggleTheme } = useThemeContext();
  const [mounted, setMounted] = React.useState<boolean>(false);

  React.useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <div className={clsxm("h-8 w-8 mr-8")}>
      <button
        aria-label="Color mode toggle"
        className={clsxm(
          "flex h-full w-full items-center justify-center rounded-full transition-colors hover:bg-gray-400 focus:ring dark:hover:bg-gray-500",
        )}
        type="button"
        onClick={() => toggleTheme()}
      >
        {mounted && (
          <>
            <FiSun
              className={clsxm(theme !== "light-theme" && "hidden", "text-2xl")}
            />
            <FiMoon
              className={clsxm(theme !== "dark-theme" && "hidden", "text-2xl")}
            />
          </>
        )}
      </button>
    </div>
  );
};

export default ColorModeToggle;
