import "@testing-library/jest-dom/extend-expect";
import { render, screen } from "@testing-library/react";

import App from "../components/App";

test("renders App", () => {
  render(<App />);
  expect(screen.getAllByText(/Coffeengo/i)).toBeDefined();
});
