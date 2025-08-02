import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { fetchInvestments, fetchDebts, fetchUser } from '@/services/api';
import { Card, CardContent } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";

interface Account {
  account_id: string;
  category: string;
  type: string;
  sub_type: string;
  description: string;
  balance: number;
  institution?: string;
}

interface User {
  name: string;
  profile_picture: string;
  age?: number;
  risk_tolerance?: string;
  address?: string;
  credit_score?: number;
  net_worth?: number;
  member_since?: number;
  financial_blurb?: string;
  goals?: string[];
}

const Sidebar: React.FC = () => {
  const [investments, setInvestments] = useState<Account[]>([]);
  const [debts, setDebts] = useState<Account[]>([]);
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [searchParams] = useSearchParams();
  const userId = searchParams.get('userId');

  useEffect(() => {
    if (userId) {
      const loadData = async () => {
        try {
          const [investmentsData, debtsData, userData] = await Promise.all([
            fetchInvestments(userId),
            fetchDebts(userId),
            fetchUser(userId),
          ]);
          setInvestments(investmentsData);
          setDebts(debtsData);
          setUser(userData);
        } catch (err) {
          setError('Failed to load sidebar data.');
        } finally {
          setLoading(false);
        }
      };
      loadData();
    }
  }, [userId]);

  if (loading) {
    return <div className="w-80 p-4">Loading...</div>;
  }

  if (error) {
    return <div className="w-80 p-4">{error}</div>;
  }

  return (
    <div className="flex flex-col w-80">
      {/* User Details */}
      {user && (
        <div className="py-4">
          <Card className="overflow-hidden border-border bg-card shadow-none">
            <CardContent>
              {/* Header with Avatar and Name */}
              <div className="flex items-center space-x-4 mb-4">
                <Avatar className="h-12 w-12 border-2 border-border">
                  <AvatarImage 
                    src={`/users/${user.profile_picture}`} 
                    alt={user.name}
                    className="object-cover object-top"
                    style={{ objectPosition: 'center top' }}
                  />
                  <AvatarFallback className="text-sm font-semibold text-card-foreground">
                    {user.name.split(' ').map((n: string) => n[0]).join('')}
                  </AvatarFallback>
                </Avatar>
                
                <div className="flex-1 min-w-0">
                  <h2 className="text-lg font-semibold text-card-foreground mb-1">
                    Welcome, <span className="text-primary">{user.name}</span>
                  </h2>
                  <p className="text-muted-foreground text-sm">
                    {user.address}
                  </p>
                </div>
              </div>
              
              {/* Metrics Grid */}
              <div className="grid grid-cols-3 gap-3">
                {user.member_since && (
                  <div className="text-center">
                    <p className="text-xl font-bold text-card-foreground">{user.member_since}</p>
                    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide">Member Since</p>
                  </div>
                )}
                {user.risk_tolerance && (
                  <div className="text-center">
                    <p className="text-xl font-bold text-card-foreground capitalize">{user.age}</p>
                    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide">Current Age</p>
                  </div>
                )}
                {user.credit_score && (
                  <div className="text-center">
                    <p className="text-xl font-bold text-card-foreground">{user.credit_score}</p>
                    <p className="text-xs font-medium text-muted-foreground uppercase tracking-wide">Credit Score</p>
                  </div>
                )}
              </div>
              
              {/* Financial Status Indicator */}
              {user && (
              <div className="mt-4 pt-4 border-t border-border">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-medium text-muted-foreground uppercase tracking-wide">Financial Status</span>
                  <div className="flex items-center space-x-1">
                    <div className="w-2 h-2 bg-primary rounded-full"></div>
                    <span className="text-xs font-medium text-card-foreground">Active</span>
                  </div>
                </div>
                <div className="flex items-center justify-between mt-2">
                  <span className="text-xs font-medium text-muted-foreground uppercase tracking-wide">Risk Preference</span>
                  <div className="flex items-center space-x-1">
                    <div className="w-2 h-2 bg-primary rounded-full"></div>
                    <span className="text-xs font-medium text-card-foreground capitalize">
                       {user?.risk_tolerance?.replace('-', ' ') || 'N/A'}
                     </span>
                  </div>
                </div>
              </div>
              )}
            </CardContent>
          </Card>
        </div>
      )}
      {/* Investments Section */}
      <h2 className="text-foreground text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Assets</h2>
      {investments.slice(0, 5).map((account) => (
        <div key={account.account_id} className="flex items-center gap-4 bg-card px-4 min-h-[72px] py-2 justify-between mb-2 rounded-lg border border-border">
          <div className="flex items-center gap-4">
            <div className="text-muted-foreground flex items-center justify-center rounded-lg bg-accent shrink-0 size-12">
              {/* Placeholder Icon */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm40-88a8,8,0,0,1-8,8H136v24a8,8,0,0,1-16,0V136H96a8,8,0,0,1,0-16h24V96a8,8,0,0,1,16,0v24h24A8,8,0,0,1,168,128Z"></path></svg>
            </div>
            <div className="flex flex-col justify-center">
              <p className="text-card-foreground text-base font-medium leading-normal line-clamp-1">{account.description}</p>
              <p className="text-muted-foreground text-sm font-normal leading-normal line-clamp-2">{account.institution}</p>
            </div>
          </div>
          <div className="shrink-0"><p className="text-card-foreground text-sm font-normal leading-normal">${account.balance.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</p></div>
        </div>
      ))}
      {investments.length > 5 && (
        <button className="text-primary hover:text-primary/80 transition-colors mt-2 px-4">View More</button>
      )}

      {/* Commitments Section */}
      <h2 className="text-foreground text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Liabilities</h2>
      {debts.slice(0, 5).map((account) => (
        <div key={account.account_id} className="flex items-center gap-4 bg-card px-4 min-h-[72px] py-2 justify-between mb-2 rounded-lg border border-border">
          <div className="flex items-center gap-4">
            <div className="text-muted-foreground flex items-center justify-center rounded-lg bg-accent shrink-0 size-12">
              {/* Placeholder Icon */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M224,88H160V48a16,16,0,0,0-16-16H48A16,16,0,0,0,32,48V160H72a16,16,0,0,1,16,16v48a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V104A16,16,0,0,0,224,88ZM88,176a8,8,0,0,1-8,8H48V48H144V88a8,8,0,0,0,8,8h40v72H104A16,16,0,0,0,88,176Zm128,32H104v-8h88a8,8,0,0,0,0-16H104v-8h88a8,8,0,0,0,0-16H104v-8h88a8,8,0,0,0,0-16H104v-8h88a8,8,0,0,0,8-8V104h24Z"></path></svg>
            </div>
            <div className="flex flex-col justify-center">
              <p className="text-card-foreground text-base font-medium leading-normal line-clamp-1">{account.description}</p>
              <p className="text-muted-foreground text-sm font-normal leading-normal line-clamp-2">{account.institution}</p>
            </div>
          </div>
          <div className="shrink-0"><p className="text-destructive text-sm font-normal leading-normal">${Math.abs(account.balance).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</p></div>
        </div>
      ))}
      {debts.length > 5 && (
        <button className="text-primary hover:text-primary/80 transition-colors mt-2 px-4">View More</button>
      )}

      {/* Actions Section */}
      <h2 className="text-foreground text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Actions</h2>
      <div className="flex flex-col gap-2">
        {/* Transfer */}
        <div className="flex items-center gap-4 bg-card px-4 min-h-14 justify-between rounded-lg border border-border hover:bg-accent/50 transition-colors">
          <div className="flex items-center gap-4">
            <div className="text-muted-foreground flex items-center justify-center rounded-lg bg-accent shrink-0 size-10">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M213.66,181.66l-32,32a8,8,0,0,1-11.32-11.32L188.69,184H48a8,8,0,0,1,0-16H188.69l-18.35-18.34a8,8,0,0,1,11.32-11.32l32,32A8,8,0,0,1,213.66,181.66Zm-139.32-64a8,8,0,0,0,11.32-11.32L67.31,88H208a8,8,0,0,0,0-16H67.31L85.66,53.66A8,8,0,0,0,74.34,42.34l-32,32a8,8,0,0,0,0,11.32Z"></path></svg>
            </div>
            <p className="text-card-foreground text-base font-normal leading-normal flex-1 truncate">Transfer</p>
          </div>
          <div className="shrink-0">
            <div className="text-muted-foreground flex size-7 items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
            </div>
          </div>
        </div>
        {/* Pay Bills */}
        <div className="flex items-center gap-4 bg-card px-4 min-h-14 justify-between rounded-lg border border-border hover:bg-accent/50 transition-colors">
          <div className="flex items-center gap-4">
            <div className="text-muted-foreground flex items-center justify-center rounded-lg bg-accent shrink-0 size-10">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M72,104a8,8,0,0,1,8-8h96a8,8,0,0,1,0,16H80A8,8,0,0,1,72,104Zm8,40h96a8,8,0,0,0,0-16H80a8,8,0,0,0,0,16ZM232,56V208a8,8,0,0,1-11.58,7.15L192,200.94l-28.42,14.21a8,8,0,0,1-7.16,0L128,200.94,99.58,215.15a8,8,0,0,1-7.16,0L64,200.94,35.58,215.15A8,8,0,0,1,24,208V56A16,16,0,0,1,40,40H216A16,16,0,0,1,232,56Zm-16,0H40V195.06l20.42-10.22a8,8,0,0,1,7.16,0L96,199.06l28.42-14.22a8,8,0,0,1,7.16,0L160,199.06l28.42-14.22a8,8,0,0,1,7.16,0L216,195.06Z"></path></svg>
            </div>
            <p className="text-card-foreground text-base font-normal leading-normal flex-1 truncate">Pay Bills</p>
          </div>
          <div className="shrink-0">
            <div className="text-muted-foreground flex size-7 items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
            </div>
          </div>
        </div>
        {/* Deposit */}
        <div className="flex items-center gap-4 bg-card px-4 min-h-14 justify-between rounded-lg border border-border hover:bg-accent/50 transition-colors">
          <div className="flex items-center gap-4">
            <div className="text-muted-foreground flex items-center justify-center rounded-lg bg-accent shrink-0 size-10">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M208,32H48A16,16,0,0,0,32,48V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V48A16,16,0,0,0,208,32Zm0,176H48V48H208V208Zm-32-80a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32A8,8,0,0,1,176,128Z"></path></svg>
            </div>
            <p className="text-card-foreground text-base font-normal leading-normal flex-1 truncate">Deposit</p>
          </div>
          <div className="shrink-0">
            <div className="text-muted-foreground flex size-7 items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256"><path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path></svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
