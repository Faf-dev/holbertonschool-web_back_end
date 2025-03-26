export default class Building {
  constructor(sqft) {
    if (new.target !== Building) {
      if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
        throw new Error('Class extending Building must override evacuationWarningMessage');
      }
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft should be a number');
    }
    this._sqft = value;
  }

  evacuationWarningMessage() {
    throw new Error(`Evacuate ${this._sqft} sqft immediatly!`);
  }
}
