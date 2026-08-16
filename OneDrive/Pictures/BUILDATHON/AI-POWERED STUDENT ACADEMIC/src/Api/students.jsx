import api from "./axios";

export const getStudents = () => {
  return api.get("/students");
};

export const getStudent = (id) => {
  return api.get(`/students/${id}`);
};


export const updateStudent = (id, data) => {
  return api.put(`/students/${id}`, data);
};

