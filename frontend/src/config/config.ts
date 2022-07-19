// dev server 및 end point가 따로 존재하는 게 아니므로, 단독 env를 사용한다.
export const config = {
  serverUrl: import.meta.env.VITE_SERVER_URL,
};
