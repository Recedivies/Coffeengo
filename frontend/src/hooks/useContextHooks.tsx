import { useContext } from "react";

import { NotifContext } from "../context/notifContext";
import { ThemeContext } from "../context/themeContext";

export function useThemeContext() {
  return useContext(ThemeContext);
}

export function useNotifContext() {
  return useContext(NotifContext);
}
