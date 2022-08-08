import { Response } from "../types";
import axiosClient from "./axiosClient";

const baseUrl: string = "/api/auth/";

interface LoginData {
  username: string;
  password: string;
}

interface RegisterData {
  username: string;
  email: string;
  password1: string;
  password2: string;
}

interface PasswordChangeData {
  current_password: string;
  new_password: string;
}

export const onLogin = async (
  request_body: LoginData,
): Promise<Response<any>> => {
  return await axiosClient.post(baseUrl + "login", request_body);
};

export const onRegister = async (
  request_body: RegisterData,
): Promise<Response<any>> => {
  return await axiosClient.post(baseUrl + "register", request_body);
};

export const onLogout = async (): Promise<Response<any>> => {
  return await axiosClient.post(baseUrl + "logout", {});
};

export const getUser = async (): Promise<Response<any>> => {
  return await axiosClient.get(baseUrl + "me");
};

export const changePassword = async (
  request_body: PasswordChangeData,
): Promise<Response<any>> => {
  return await axiosClient.post(baseUrl + "password", request_body);
};
