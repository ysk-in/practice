import React from "react";
import getTitle from "../utils/GetTitle";

const ImageDetail = ({ image }) => {
  if (!image) {
    return <div>Loading...</div>;
  }

  console.log(image);
  return (
    <div>
      <div className="ui embed">
        <iframe src={image.links.html} />
      </div>
      <div className="ui segment">
        <h4 className="ui header">{getTitle(image.description)}</h4>
        <p>Tags: {image.tags.map(tag => `${tag.title} `)}</p>
      </div>
    </div>
  );
};

export default ImageDetail;
