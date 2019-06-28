const DEFAULT_TITLE_LEN = 50;

function getTitle(title, len = DEFAULT_TITLE_LEN) {
  if (title === null || title === undefined) return "No title";
  return title.length <= len ? title : title.substr(0, len) + "...";
}

export default getTitle;
