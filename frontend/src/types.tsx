import { AxiosResponse } from "axios";

export type ButtonToggleProps = {
  buttonClassName?: string;
  className?: string;
  iconClassName?: string;
  value?: string;
  onChange: (v: string) => void;
};

export type ThemeContextProps = {
  theme: string;
  toggleTheme: () => void;
};

export type NotifContextProps = {
  toggleNotificataion: (opt: string) => void;
};

export type Response<T> = AxiosResponse<T>;

export type User = {
  username: string;
  email: string;
};

export type AuthContextProps = {
  user: User;
  login: () => Promise<Response<any>>;
  logout: () => void;
};
