import React from "react";
import SearchBar from "./SearchBar";
import unsplash from "../apis/unsplash";
import ImageList from "./ImageList";
import ImageDetail from "./ImageDetail";

class App extends React.Component {
  state = { images: [], selectedImage: null };

  onTermSubmit = async term => {
    // I can not use the Google API.
    // Because our company network can not connect to Google servicelogin.
    // Therefore, I use Unsplash API in this project as well as pics.
    const response = await unsplash.get("/search/photos", {
      params: {
        query: term
      }
    });
    this.setState({ images: response.data.results });
  };

  onImageSelect = image => {
    this.setState({ selectedImage: image });
  };

  render() {
    return (
      <div className="ui container">
        <SearchBar onFormSubmit={this.onTermSubmit} />
        <ImageDetail image={this.state.selectedImage} />
        <ImageList
          onImageSelect={this.onImageSelect}
          images={this.state.images}
        />
      </div>
    );
  }
}

export default App;
