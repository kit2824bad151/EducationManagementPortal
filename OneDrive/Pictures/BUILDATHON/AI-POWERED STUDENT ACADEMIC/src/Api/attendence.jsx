import api from "./axios";

export const getAttendance = (studentId) => {
  return api.get(`/attendance/${studentId}`);
};

export const markAttendance = (data) => {
  return api.post("/attendance", data);
};