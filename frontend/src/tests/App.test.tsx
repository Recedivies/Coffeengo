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
  let container: HTMLElement;

  beforeEach(() => {
    container = render(<App />).container;
  });

  test("clicking Login Button on Home Page", async () => {
    const user = userEvent.setup();
    const button = getById<HTMLInputElement>(container, "login-home");
    const mockHandler = jest.fn();

    await user.click(button);

    // expect(mockHandler.mock.calls).toHaveLength(1);

    expect(screen.getByText("Sign in")).toBeInTheDocument();
  });
});
