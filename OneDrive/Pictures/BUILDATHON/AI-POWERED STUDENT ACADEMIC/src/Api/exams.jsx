import api from "./axios";

export const getExams = () => {
  return api.get("/exams");
};

export const getExam = (id) => {
  return api.get(`/exams/${id}`);
};

export const getExamMarks = (id) => {
  return api.get(`/exams/${id}/marks`);
};