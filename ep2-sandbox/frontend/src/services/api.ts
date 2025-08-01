const API_URL = 'https://backend-426194555180.us-west1.run.app/api';

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
