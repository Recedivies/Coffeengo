import { useThemeContext } from "../../hooks/useContextHooks";
import clsxm from "../../lib/clsxm";
import Footer from "./Footer";
import Header from "./Header";

const Layout = ({ children }: { children: React.ReactNode }) => {
  const { theme } = useThemeContext();
  return (
    <div
      className={clsxm(
        "bg-light transition-colors dark:bg-dark dark:text-light flex min-h-screen flex-col justify-between",
        theme,
      )}
    >
      <Header />
      {children}
      <Footer />
    </div>
  );
};

export default Layout;
