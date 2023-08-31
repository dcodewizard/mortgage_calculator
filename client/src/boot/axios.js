import axios from "axios"
const { VUE_APP_API_BASEURL } = process.env

const api = axios.create({
  baseURL: VUE_APP_API_BASEURL,
  headers: {
    "Content-Type": "application/json",
  },
})

export { axios, api }
