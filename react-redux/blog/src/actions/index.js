import jsonPlaceHolder from "../apis/jsonPlaceholder";

export const fetchPosts = () => {
  return async function (dispatch, getState) {
    const response = await jsonPlaceHolder.get("/posts");

    dispatch({ type: "FETCH_POSTS", payload: response })
  };
};

export const selectPost = () => {
  return {
    type: "SELECT_POST";
  };
};