import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { fetchTransactions, fetchAccounts } from '@/services/api';
import Sidebar from '@/components/Sidebar';
import Chatbot from '@/components/Chatbot';

interface Account {
  account_id: string;
  type: string;
  balance: number;
  description: string;
}

interface Transaction {
  transaction_id: string;
  account_id: string;
  date: string;
  description: string;
  amount: number;
  category: string;
}



const DashboardPage: React.FC = () => {
  const [accounts, setAccounts] = useState<Account[]>([]);
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchParams] = useSearchParams();
  const userId = searchParams.get('userId');
  
  // Pagination state
  const [currentPage, setCurrentPage] = useState(1);
  const transactionsPerPage = 15;

  // Calculate pagination values
  const indexOfLastTransaction = currentPage * transactionsPerPage;
  const indexOfFirstTransaction = indexOfLastTransaction - transactionsPerPage;
  const sortedTransactions = [...transactions].sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
  const currentTransactions = sortedTransactions.slice(indexOfFirstTransaction, indexOfLastTransaction);
  const totalPages = Math.ceil(transactions.length / transactionsPerPage);

  // Pagination handlers
  const goToPage = (pageNumber: number) => {
    setCurrentPage(pageNumber);
  };

  const goToPreviousPage = () => {
    setCurrentPage(prev => Math.max(prev - 1, 1));
  };

  const goToNextPage = () => {
    setCurrentPage(prev => Math.min(prev + 1, totalPages));
  };

  useEffect(() => {
    if (userId) {
      const loadData = async () => {
        try {
          const [accountsData, transactionsData] = await Promise.all([
            fetchAccounts(userId),
            fetchTransactions(userId),
          ]);
          setAccounts(accountsData);
          setTransactions(transactionsData); // Only show 5 most recent
        } catch (err) {
          setError('Failed to load data.');
        } finally {
          setLoading(false);
        }
      };
      loadData();
    }
  }, [userId]);

  if (loading) {
    return <div className="container mx-auto py-10 px-10">Loading...</div>;
  }

  if (error) {
    return <div className="container mx-auto py-10 px-10">{error}</div>;
  }

  return (
    <div className="relative flex min-h-auto flex-col bg-red overflow-x-hidden" style={{ fontFamily: 'Public Sans, Noto Sans, sans-serif' }}>
      
  
      <div className="flex h-full grow flex-col">
        {/* Chatbot */}
        <Chatbot />
        {/* Main Content Area */}
        <div className="gap-4 px-6 flex flex-1 justify-center py-6">
     
          {/* Sidebar */}
          <Sidebar />
          {/* Main Content */}
          <div className="flex flex-col max-w-[960px] flex-1">
            {/* <div className="grid gap-4 md:grid-cols-2 md:gap-8 lg:grid-cols-3">
              <Card>
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium">
                    Net Worth
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">
                    ${user?.net_worth?.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                  </div>
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                  <CardTitle className="text-sm font-medium">
                    Member Since
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">
                    {user?.member_since}
                  </div>
                </CardContent>
              </Card>
            </div> */}
            <div className="flex flex-wrap justify-between gap-3 p-4">
              <p className="text-foreground tracking-light text-[32px] font-bold leading-tight min-w-72">Recent Transactions</p>
            </div>
            <div className="px-4 py-3">
              <div className="flex overflow-hidden rounded-lg border border-border bg-background">
                <table className="flex-1">
                  <thead>
                    <tr className="bg-background">
                      <th className="px-4 py-3 text-left text-foreground w-[200px] text-sm font-medium leading-normal">Date</th>
                      <th className="px-4 py-3 text-left text-foreground w-[350px] text-sm font-medium leading-normal">Description</th>
                      <th className="px-4 py-3 text-left text-foreground w-[150px] text-sm font-medium leading-normal">Category</th>
                      <th className="px-4 py-3 text-left text-foreground w-[150px] text-sm font-medium leading-normal">Amount</th>
                    </tr>
                  </thead>
                  <tbody>
                    {currentTransactions.map((transaction) => {
                      const account = accounts.find(acc => acc.account_id === transaction.account_id);
                      return (
                        <tr key={transaction.transaction_id} className="border-t border-t-border">
                          <td className="h-[72px] px-4 py-2 w-[200px] text-muted-foreground text-sm font-normal leading-normal">
                            {new Date(transaction.date).toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' })}
                          </td>
                          <td className="h-[72px] px-4 py-2 w-[350px] text-muted-foreground text-sm font-normal leading-normal">
                            <div>{transaction.description}</div>
                            <div className="text-xs text-muted-foreground/80">{account?.description}</div>
                          </td>
                          <td className="h-[72px] px-4 py-2 w-[150px] text-muted-foreground text-sm font-normal leading-normal">
                            {transaction.category}
                          </td>
                          <td className={`h-[72px] px-4 py-2 w-[150px] text-sm font-normal leading-normal ${transaction.amount < 0 ? 'text-destructive' : 'text-primary'}`}>{transaction.amount < 0 ? '-' : '+'}${Math.abs(transaction.amount).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</td>
                        </tr>
                      )
                    })}
                  </tbody>
                </table>
              </div>
              
              {/* Pagination Controls */}
              {totalPages > 1 && (
                <div className="flex items-center justify-between px-4 py-3 border-t border-border">
                  <div className="flex items-center gap-2">
                    <button
                      onClick={goToPreviousPage}
                      disabled={currentPage === 1}
                      className="flex items-center justify-center w-8 h-8 rounded-lg border border-border text-muted-foreground hover:bg-accent disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 256 256">
                        <path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path>
                      </svg>
                    </button>
                    
                    <div className="flex items-center gap-1">
                      {Array.from({ length: totalPages }, (_, index) => {
                        const pageNumber = index + 1;
                        return (
                          <button
                            key={pageNumber}
                            onClick={() => goToPage(pageNumber)}
                            className={`w-8 h-8 rounded-lg text-sm font-medium ${
                              currentPage === pageNumber
                                ? 'bg-accent text-accent-foreground'
                                : 'text-muted-foreground hover:bg-accent'
                            }`}
                          >
                            {pageNumber}
                          </button>
                        );
                      })}
                    </div>
                    
                    <button
                      onClick={goToNextPage}
                      disabled={currentPage === totalPages}
                      className="flex items-center justify-center w-8 h-8 rounded-lg border border-border text-muted-foreground hover:bg-accent disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 256 256">
                        <path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path>
                      </svg>
                    </button>
                  </div>
                  
                  <div className="text-sm text-muted-foreground">
                    Showing {indexOfFirstTransaction + 1}-{Math.min(indexOfLastTransaction, transactions.length)} of {transactions.length} transactions
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashboardPage;