import axios from "axios";

const API_URL = "http://localhost:8000/api/auth/";

export const login = async (email, password) => {
    return axios.post(`${API_URL}login/`, { email, password });
};

export const register = async (email, password1, password2) => {
    return axios.post(`${API_URL}registration/`, { email, password1, password2 });
};