import axios from "axios";

export default axios.create({
  baseURL: "https://api.unsplash.com",
  headers: {
    Authorization:
      "Client-ID bbc9829673a1d3cf58309a7a5ef41f476e81b3ffa0997d19e31fd803b63cd7c0"
  }
});
