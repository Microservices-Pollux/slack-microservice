import { Fields } from "./resources/fields";

const services = {
  fields: new Fields(),
};

type ServiceName = keyof typeof services;
type Service = (typeof services)[ServiceName];

export default {
  resource: (name: ServiceName): Service => services[name],
};
