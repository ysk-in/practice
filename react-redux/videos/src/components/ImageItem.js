import "./ImageItem.css";
import React from "react";
import getDescription from "../utils/GetDescription";

const ImageItem = ({ image, onImageSelect }) => {
  return (
    <div onClick={() => onImageSelect(image)} className="image-item item">
      <img
        className="ui image"
        src={image.urls.small}
        alt={image.alt_description}
      />
      <div className="content">
        <div className="header">{getDescription(image.description)}</div>
      </div>
    </div>
  );
};

export default ImageItem;
