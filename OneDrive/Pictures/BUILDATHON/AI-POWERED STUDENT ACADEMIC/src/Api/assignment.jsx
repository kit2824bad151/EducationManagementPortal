import api from "./axios";

export const getAssignments = () => {
  return api.get("/assignments");
};

export const getAssignment = (id) => {
  return api.get(`/assignments/${id}`);
};

export const submitAssignment = (id, data) => {
  return api.post(`/assignments/${id}/submit`, data);
};