import type { Item } from "./Item";

export interface SelectProps {
  label: string;
  value: string;
  options: Item[];
}
