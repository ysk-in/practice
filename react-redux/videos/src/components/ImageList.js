import React from "react";
import ImageItem from "./ImageItem";

const ImageList = ({ images, onImageSelect }) => {
  const renderedList = images.map(image => {
    return (
      <ImageItem onImageSelect={onImageSelect} key={image.id} image={image} />
    );
  });
  return <div className="ui relaxed divided list">{renderedList}</div>;
};

export default ImageList;
