import axios from "axios";

const backendUrl = process.env.REACT_APP_BACKEND_URL;

const AxiosClient = axios.create({
  baseURL:
    window.location.host === "localhost:8080"
      ? ""
      : window.location.host === "localhost:3000"
      ? "http://localhost:8000"
      : backendUrl,
  headers: { "Content-Type": "application/json" },
});

// before sending request attach auth token
AxiosClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  /* eslint-disable-next-line  @typescript-eslint/no-non-null-assertion*/
  config!.headers!.Authorization = token ? `Token ${token}` : "";
  return config;
});

export default AxiosClient;
