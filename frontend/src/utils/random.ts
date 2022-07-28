export class JellyFactory {
  private _list = [
    ["amount", "unit", "의", "color", "jelly"],
    ["color", "jelly", "amount", "unit"],
    ["taste", "jelly"],
    ["color", "jelly"],
    ["taste", "color", "jelly", "amount", "unit"],
  ];
  private _amount = [
    "한",
    "두",
    "세",
    "네",
    "다섯",
    "여섯",
    "일곱",
    "여덟",
    "아홉",
  ];
  private _color = ["빨간색", "다홍색", "노란색", "파란색"];
  private _taste = ["시큼한", "달콤한", "씁쓸한", "맛있는"];
  private _unit = ["개", "자루", "봉지"];
  private _jelly = ["젤리", "곤약", "양갱"];

  public getJelly() {
    const ranList = this._list[Math.floor(Math.random() * this._list.length)];
    return ranList.map((e) => this.textConverter(e)).join(" ");
  }

  private textConverter(type: string) {
    switch (type) {
      case "amount":
        return this.getRandom(this._amount);
      case "unit":
        return this.getRandom(this._unit);
      case "color":
        return this.getRandom(this._color);
      case "taste":
        return this.getRandom(this._taste);
      case "jelly":
        return this.getRandom(this._jelly);
      default:
        return type;
    }
  }

  private getRandom(arr: Array<string>) {
    return arr[Math.floor(Math.random() * arr.length)];
  }
}
