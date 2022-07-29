import { VO } from "../models";

export const findProperJokefromResponse = (data: VO.JokeResponse) => {
  const translatedJoke = data.KOR.find((elem) => elem);
  return translatedJoke || data.ENG[0];
};
