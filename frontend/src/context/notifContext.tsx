import React from "react";

import { NotifContextProps } from "../types";

export const NotifContext = React.createContext<NotifContextProps>(
  {} as NotifContextProps,
);

const NotificationProvider = ({ children }: { children: React.ReactNode }) => {
  function toggleNotificataion(opt: string) {
    localStorage.setItem("notif", opt);
  }

  return (
    <NotifContext.Provider
      value={{
        toggleNotificataion,
      }}
    >
      {children}
    </NotifContext.Provider>
  );
};

export default NotificationProvider;
