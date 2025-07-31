const API_URL = 'http://localhost:8000/api';

export const fetchUser = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}`);
  if (!response.ok) {
    throw new Error('User not found');
  }
  return response.json();
};

export const fetchTransactions = async (userId: string) => {
  const response = await fetch(`${API_URL}/users/${userId}/transactions`);
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