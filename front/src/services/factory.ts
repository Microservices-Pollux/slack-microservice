import { formFields } from "./resources/form-fields";
import { Forms } from "./resources/forms";

const services = {
  formFields: new formFields(),
  forms: new Forms(),
};

type ServiceName = keyof typeof services;
type Service = (typeof services)[ServiceName];

export default {
  resource: (name: ServiceName): Service => services[name],
};
