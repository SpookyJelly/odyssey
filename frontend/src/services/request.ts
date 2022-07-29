import axios, { AxiosResponse } from "axios";
import config from "../config";
import { VO } from "../models";
import { keyTransformer } from "../utils/keyTransformer";

const serverUrl = config.serverUrl;

export const getRandomJoke = async () => {
  const response: AxiosResponse<VO.JokeResponse> = await axios.get(
    `${serverUrl}/api/random`
  );
  const { ENG, KOR } = response.data;

  return {
    ENG: ENG.map((elem) => ({ lang: "ENG", ...keyTransformer(elem) })),
    KOR: KOR.map((elem) => ({ lang: "KOR", ...keyTransformer(elem) })),
  } as VO.JokeResponse;
};

export const translateJoke = async (refId: string, data: FormData) => {
  console.log("ref id", refId);

  const response = await axios.post(
    `${serverUrl}/api/translate/${refId}`,
    data
  );
};
