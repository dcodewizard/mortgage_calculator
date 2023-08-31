import { api } from "@/boot/axios";

const config = (method, endpoint, data) => {
  return {
    method,
    url: endpoint,
    data: data || {}
  }
};

export const request = async (method, endpoint, data) => {
  try {
    const response = await api(config(method, endpoint, data))

    return {
      ...response.data
    }
  } catch (error) {
    return {
      message: error?.message
    }
  }
}
