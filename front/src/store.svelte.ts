import factory from "./services/factory";
import type { Field } from "./interfaces/Field";
import type { Form } from "./interfaces/Form";

export const store = $state<{
  services: typeof factory;
  fields: Field[];
  forms: Form[];
  form: Form;
  isLoading: boolean;
}>({
  services: factory,
  fields: [],
  forms: [],
  form: { _id: "", name: "", fields: [] },
  isLoading: true,
});
