import React from "react";
import SearchBar from "./SearchBar";
import unsplash from "../apis/unsplash";
import ImageList from "./ImageList";
import ImageDetail from "./ImageDetail";

class App extends React.Component {
  state = { images: [], selectedImage: null };

  componentDidMount() {
    this.onTermSubmit("kyoto");
  }

  onTermSubmit = async term => {
    // I can not use the Google API.
    // Because our company network can not connect to Google servicelogin.
    // Therefore, I use Unsplash API in this project as well as pics.
    const response = await unsplash.get("/search/photos", {
      params: {
        query: term,
        per_page: 5,
        orientation: "landscape"
      }
    });
    this.setState({
      images: response.data.results,
      selectedImage: response.data.results[0]
    });
  };

  onImageSelect = image => {
    this.setState({ selectedImage: image });
  };

  render() {
    return (
      <div className="ui container">
        <SearchBar onFormSubmit={this.onTermSubmit} />
        <div className="ui grid">
          <div className="ui row">
            <div className="eleven wide column">
              <ImageDetail image={this.state.selectedImage} />
            </div>
            <div className="five wide column">
              <ImageList
                onImageSelect={this.onImageSelect}
                images={this.state.images}
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
