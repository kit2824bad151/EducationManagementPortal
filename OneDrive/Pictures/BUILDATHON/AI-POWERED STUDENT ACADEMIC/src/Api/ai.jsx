import api from "./axios";

export const getAIInsights = (studentId) => {
  return api.get(`/ai/insights/${studentId}`);
};

export const getAIRecommendations = (studentId) => {
  return api.get(`/ai/recommendations/${studentId}`);
};