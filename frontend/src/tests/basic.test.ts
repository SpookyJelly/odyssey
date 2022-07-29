import { assert, expect, test } from "vitest";
import { VO } from "../models";
import { keyTransformer, snakeToCamel } from "../utils/keyTransformer";

const dummyEngJoke = {
  lang: "ENG",
  id: "1",
  categories: [],
  value: "value",
  icon_url: "iconUrl",
  updated_at: "updatedAt",
  created_at: "createdAt",
  url: "url",
};

test("vitest init", () => {
  expect(Math.sqrt(4)).toBe(2);
  expect(Math.round(Math.random() * 100)).lessThan(1000);
});

test("snake_case to camelCase", () => {
  expect(snakeToCamel("i_am_ready")).toBe("iAmReady");
  expect(snakeToCamel("alreadyCamel")).toBe("alreadyCamel");
  expect(snakeToCamel("broken_arrow")).toBe("brokenArrow");
});

test("key converter", () => {
  const convertedEng: VO.EngJoke = {
    lang: "ENG",
    id: "1",
    value: "value",
    categories: [],
    iconUrl: "iconUrl",
    updatedAt: "updatedAt",
    createdAt: "createdAt",
    url: "url",
  };
  expect(keyTransformer(dummyEngJoke)).toStrictEqual(convertedEng);
});
