export interface JokeResponse {
  ENG: Array<EngJoke>;
  KOR: Array<KorJoke>;
}

export interface EngJoke {
  lang: string;
  id: string;
  value: string;
  categories: Array<string>;
  iconUrl: string;
  updatedAt: string;
  createdAt: string;
  url: string;
}

// turn snake case to camel Case
export interface KorJoke {
  lang: string;
  id: number;
  value: string;
  refId: string;
  score: number;
}
