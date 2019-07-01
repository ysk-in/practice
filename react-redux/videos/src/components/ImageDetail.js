import "./ImageDetail.css";
import React from "react";
import getDescription from "../utils/GetDescription";

const ImageDetail = ({ image }) => {
  if (!image) {
    return <div>Loading...</div>;
  }
  const tags = image.tags.map(tag => {
    return (
      <a
        key={tag.title}
        className="ui label"
        href={`https://unsplash.com/search/photos/${tag.title}`}
      >
        {tag.title}
      </a>
    );
  });
  return (
    <div>
      <div className="ui embed image-detail">
        <a href={image.links.html}>
          {/* I gave up using iframe. Because I could not find anything usable in Unsplash.
            <iframe title="image link" src="{image.links.html}" /> */}
          <img src={image.urls.regular} alt={image.alt_description} />
        </a>
      </div>
      <div className="ui segment">
        <h4 className="ui header">{getDescription(image.description, 500, "No description.")}</h4>
        <div className="ui tag labels">{tags}</div>
      </div>
    </div>
  );
};

export default ImageDetail;
