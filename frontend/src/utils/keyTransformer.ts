export const snakeToCamel = (str: string) =>
  //prettier-ignore
  str.replace(/(_\w)/g, (match) => {
    return match[1].toUpperCase();
  });

export function keyTransformer(object: Object) {
  const result = Object.entries(object).reduce((pre, [key, value]) => {
    // 이거 그대로 리턴하면 누산기에 value가 그대로 할당되어서 키 에러가 난다.
    // (pre가 {}가 아니라 value가 되어버림)
    pre[snakeToCamel(key)] = value;
    return pre;
  }, {} as Record<string, any>);

  return result;
}
