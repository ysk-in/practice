const DEFAULT_TITLE_LEN = 50;

function getDescription(title, len = DEFAULT_TITLE_LEN) {
  if (title === null || title === undefined) return "No description.";
  return title.length <= len ? title : title.substr(0, len) + "...";
}

export default getDescription;
