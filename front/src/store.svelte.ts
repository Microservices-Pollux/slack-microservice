import factory from "./services/factory";
import type { Field } from "./interfaces/Field";

export const store = $state<{
  services: typeof factory;
  fields: Field[];
  isLoading: boolean;
}>({
  services: factory,
  fields: [],
  isLoading: true,
});
