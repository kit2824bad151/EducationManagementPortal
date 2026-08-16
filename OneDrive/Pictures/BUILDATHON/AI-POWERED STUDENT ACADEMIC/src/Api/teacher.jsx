import api from "./axios";

export const getTeachers = () => {
  return api.get("/teachers");
};

export const getTeacher = (id) => {
  return api.get(`/teachers/${id}`);
};

export const updateTeacher = (id, data) => {
  return api.put(`/teachers/${id}`, data);
};