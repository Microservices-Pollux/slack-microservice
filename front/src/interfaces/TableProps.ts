import type { Snippet } from "svelte";

export interface TableProps {
  title: string;
  headers: Snippet;
  rows: Snippet;
}
