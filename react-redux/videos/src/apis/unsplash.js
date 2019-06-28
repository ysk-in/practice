import axios from "axios";

export default axios.create({
  baseURL: "https://api.unsplash.com",
  headers: {
    Authorization:
      "Client-ID 05b843009a0ada92bb5e660a34bdf0c8c48538a66aabd78f580486fe5c4990a1"
  }
});
