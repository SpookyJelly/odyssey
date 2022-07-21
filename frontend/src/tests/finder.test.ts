import { describe, expect, it } from "vitest";
import { VO } from "../models";
import { findProperJokefromResponse } from "../utils/finder";

const dummyResponseList: Array<VO.JokeResponse> = [
  {
    ENG: [
      {
        lang: "ENG",
        updatedAt: "2020-01-05T13:42:23",
        id: "MNV6pEQ9Q3CVG9G2EWbc_Q",
        url: "https://api.chucknorris.io/jokes/MNV6pEQ9Q3CVG9G2EWbc_Q",
        categories: [],
        createdAt: "2020-01-05T13:42:23",
        value: "Chuck Norris knows what you did last winter.",
        iconUrl: "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
      },
    ],
    KOR: [],
  },
  {
    ENG: [
      {
        lang: "ENG",
        categories: ["explicit"],
        createdAt: "2020-01-05 13:42:29.855523",
        iconUrl: "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        id: "NeQ_Tt0DT72dBZqgR7VD-Q",
        updatedAt: "2020-01-05 13:42:29.855523",
        url: "https://api.chucknorris.io/jokes/NeQ_Tt0DT72dBZqgR7VD-Q",
        value:
          "HI IM CHRIS AND MAUNDERS JIZZED ON MY NECK LOL, I GOT PWNED ON COD6 BY JOHNSON !!! I LIKE GAY SEX WITH CHUCK NORRIS,! FUCKIN HARDEST GUY IN ROCHDALE HERE 2K9",
      },
    ],
    KOR: [
      {
        lang: "KOR",
        id: 1,
        refId: "NeQ_Tt0DT72dBZqgR7VD-Q",
        value: "번역된 내용 1",
        score: 2,
      },
    ],
  },
];

describe("proper Joke finder test", () => {
  it("case : ENG JOKE only", () => {
    const result = findProperJokefromResponse(dummyResponseList[0]);
    expect(result).toBe(dummyResponseList[0]["ENG"][0]);
  });
  it("case : ENG JOKE and KOR JOKE mixed", () => {
    const result = findProperJokefromResponse(dummyResponseList[1]);
    expect(result).toBe(dummyResponseList[1]["KOR"][0]);
  });
});
