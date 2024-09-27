import axios from 'axios';

const API_URL = process.env.REACT_APP_BACKEND_URL;

export const login = () => {
 window.location.href = `${API_URL}/login`;
};

export const fetchData = async (url) => {
 return await axios.post(`${API_URL}/fetch-data/`, { url });
};
