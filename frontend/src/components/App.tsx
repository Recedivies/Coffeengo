import NotificationProvider from "../context/notifContext";
import ThemeProvider from "../context/themeContext";
import Router from "../routing/Router";

function App() {
  return (
    <ThemeProvider>
      <NotificationProvider>
        <Router />
      </NotificationProvider>
    </ThemeProvider>
  );
}

export default App;
