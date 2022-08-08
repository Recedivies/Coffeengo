import "@testing-library/jest-dom/extend-expect";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import assert from "assert";

import App from "../components/App";

function getById<T extends Element>(container: HTMLElement, id: string): T {
  const element = container.querySelector<T>(`#${id}`);
  assert(element !== null, `Unable to find an element with ID #${id}.`);
  return element;
}

test("renders App", () => {
  render(<App />);
  expect(screen.getAllByText(/Coffeengo/i)).toBeDefined();
});

describe("<App />", () => {
  test("clicking Login Button on Home Page", async () => {
    const { container } = render(<App />);

    const user = userEvent.setup();
    const button = getById<HTMLInputElement>(container, "login-home");

    await user.click(button);

    expect(screen.getByText("Sign in")).toBeInTheDocument();
  });
});
