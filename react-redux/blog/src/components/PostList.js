import React from "react";
import { connect } from "react-redux";
import { fetchPosts } from "../actions";

class PostList extends React.Component {
  componentDidMount() {
    this.props.fetchPosts();
  }

  render() {
    return (
      <div>
        Post List
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  return { blogs: state.fetchBlogs }
};

export default connect(mapStateToProps, { fetchPosts })(PostList);
