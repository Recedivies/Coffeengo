import clsxm from "../../lib/clsxm";

const Footer = () => {
  return (
    <footer className={clsxm("mt-auto p-5")}>
      <main className="layout flex flex-col items-center border-t pt-6 dark:border-gray-800">
        <div className="mt-2 text-sm transition-colors">
          © {new Date().getFullYear()} Recedivies - All Rights Reserved
        </div>
      </main>
    </footer>
  );
};

export default Footer;
