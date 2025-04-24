import type { Field } from "./Field";

export interface Form {
  _id: string;
  name: string;
  fields: Field[];
}
