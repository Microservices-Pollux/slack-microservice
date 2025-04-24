import { Base } from "../base";

export class formFields extends Base {
  constructor() {
    super("forms/$0/fields");
  }

  setFormId(formId: string): this {
    this.parents = [];
    this.parents.push(formId);
    return this;
  }
}
