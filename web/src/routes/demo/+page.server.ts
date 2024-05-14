import { type ISchoolInfo } from "$lib/interfaces";

// NOTE: 서버사이드에서는 env 활용 가능
const API_HOST = process.env.VITE_PLAYGROUND_SERVER_SIDE_API_URL || "http://localhost:17001"

// 학교 목록 불러오는 기능
const fetchSchoolList = async (): Promise<ISchoolInfo[]> => {
  const response = await fetch(`${API_HOST}/서울/초등학교`);
  if (!response.ok) {
    throw new Error("Failed to fetch school list");
  }
  const { status, school_list } = await response.json();
  if (status !== true) {
    throw new Error("Failed to fetch school list");
  }
  return school_list;
}

// 서버사이드에서 데이터 로드한 뒤, props로 넘겨주는 함수
export async function load( { params, setHeaders }) {
  try {
    const schoolListFromAPI = await fetchSchoolList();
    return {
      status: true,
      props: {
        schoolList: schoolListFromAPI
      }
    }
  } catch (e) {
    console.error(e);
    return {
      status: false,
      props: {
        schoolList: []
      },
      error: new Error('Failed to fetch school list')
    }
  }
}
