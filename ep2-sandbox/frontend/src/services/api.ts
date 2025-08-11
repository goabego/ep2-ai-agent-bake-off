const API_URL = import.meta.env.VITE_API_URL || 'https://backend-ep2-879168005744.us-west1.run.app/api';
const TOKEN_URL = import.meta.env.VITE_TOKEN_URL || 'https://backend-ep2-426194555180.us-west1.run.app/token';
// const API_URL = process.env.API_URL;
// const API_URL = 'http://backend:8081/api';

// Get authentication token from backend
export const fetchAuthToken = async () => {
  const response = await fetch(TOKEN_URL);
  if (!response.ok) {
    throw new Error('Failed to get authentication token');
  }
  const data = await response.json();
  if (data.status === 'success' && data.token) {
    return data.token;
  } else {
    throw new Error('Invalid token response from backend');
  }
};

export const fetchUser = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}`);
  if (!response.ok) {
    throw new Error('User not found');
  }
  return response.json();
};

export const fetchTransactions = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/transactions?history=365`);
  if (!response.ok) {
    throw new Error('Could not fetch transactions');
  }
  return response.json();
};

export const fetchAccounts = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/accounts`);
  if (!response.ok) {
    throw new Error('Could not fetch accounts');
  }
  return response.json();
};

export const fetchDebts = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/debts`);
  if (!response.ok) {
    throw new Error('Could not fetch debts');
  }
  return response.json();
};

export const fetchInvestments = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/investments`);
  if (!response.ok) {
    throw new Error('Could not fetch investments');
  }
  return response.json();
};

export const fetchNetWorth = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/networth`);
  if (!response.ok) {
    throw new Error('Could not fetch net worth');
  }
  return response.json();
};
