import { writable, type Writable} from "svelte/store";
import { type ISchoolInfo } from "./interfaces";

export const schoolList = writable([] as ISchoolInfo[]);
