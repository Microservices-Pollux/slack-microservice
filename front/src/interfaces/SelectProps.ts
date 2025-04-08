import type { Item } from "./Item";

export interface SelectProps {
  label: string;
  name: string;
  value: string;
  onClick: (item: Item) => void;
}
