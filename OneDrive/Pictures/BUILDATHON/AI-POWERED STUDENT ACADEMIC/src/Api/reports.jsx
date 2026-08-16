import api from "./axios";

export const getAcademicReport = (studentId) => {
  return api.get(`/reports/student/${studentId}`);
};

export const getReports = () => {
  return api.get("/reports");
};