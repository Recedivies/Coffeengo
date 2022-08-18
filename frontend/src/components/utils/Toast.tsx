import { ToastContent, toast } from "react-toastify";

import { WebResponse } from "../../types";

export const toastError = (data: WebResponse): ToastContent<unknown> => {
  const ret = JSON.stringify(data.message)
    .replace("password1", "Password")
    .replace(/]|[[]/g, "")
    .replace(/[{}]/g, "")
    .replace(",", "")
    .replaceAll('"', "");
  return toast.error(ret);
};

export const toastSuccess = (
  isNotificationActive: string | null,
  username: string | null,
): void => {
  if (isNotificationActive && username) {
    if (
      isNotificationActive === "login" ||
      isNotificationActive === "register"
    ) {
      toast.success(`Welcome, ${username}.`);
    }
    if (isNotificationActive === "logout") {
      toast.success(
        `Goodbye, ${username}. Looking forward to seeing you at Coffeengo.`,
      );
    }
    localStorage.removeItem("username");
    localStorage.removeItem("notif");
  }
};
