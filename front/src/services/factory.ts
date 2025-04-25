import { formFields } from "./resources/form-fields";
import { Forms } from "./resources/forms";

const services = {
  formFields: new formFields(),
  forms: new Forms(),
};

type ServiceMap = {
  formFields: formFields;
  forms: Forms;
};

type ServiceName = keyof ServiceMap;

export default {
  resource: <T extends ServiceName>(name: T): ServiceMap[T] => services[name],
};
