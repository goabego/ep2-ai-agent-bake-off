import React from 'react';

interface Account {
  account_id: string;
  type: string;
  balance: number;
}

interface SidebarProps {
  accounts: Account[];
}

const Sidebar: React.FC<SidebarProps> = ({ accounts }) => {
  return (
    <div className="flex flex-col w-80">
      <h2 className="text-[#0e141b] text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Account</h2>
      {accounts.map((account) => (
        <div key={account.account_id} className="flex items-center gap-4 bg-slate-50 px-4 min-h-[72px] py-2 justify-between mb-2 rounded-lg">
          <div className="flex items-center gap-4">
            <div className="text-[#0e141b] flex items-center justify-center rounded-lg bg-[#e7edf3] shrink-0 size-12">
              {/* Bank SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M24,104H48v64H32a8,8,0,0,0,0,16H224a8,8,0,0,0,0-16H208V104h24a8,8,0,0,0,4.19-14.81l-104-64a8,8,0,0,0-8.38,0l-104,64A8,8,0,0,0,24,104Zm40,0H96v64H64Zm80,0v64H112V104Zm48,64H160V104h32ZM128,41.39,203.74,88H52.26ZM248,208a8,8,0,0,1-8,8H16a8,8,0,0,1,0-16H240A8,8,0,0,1,248,208Z"></path>
              </svg>
            </div>
            <div className="flex flex-col justify-center">
              <p className="text-[#0e141b] text-base font-medium leading-normal line-clamp-1">{account.type}</p>
              <p className="text-[#4e7397] text-sm font-normal leading-normal line-clamp-2">{account.type === 'Checking' ? 'Checking' : account.type === 'Savings' ? 'Savings' : 'Account'}</p>
            </div>
          </div>
          <div className="shrink-0"><p className="text-[#0e141b] text-base font-normal leading-normal">${account.balance.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</p></div>
        </div>
      ))}
      {/* Actions */}
      <h2 className="text-[#0e141b] text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Actions</h2>
      <div className="flex flex-col gap-2">
        {/* Transfer */}
        <div className="flex items-center gap-4 bg-slate-50 px-4 min-h-14 justify-between rounded-lg">
          <div className="flex items-center gap-4">
            <div className="text-[#0e141b] flex items-center justify-center rounded-lg bg-[#e7edf3] shrink-0 size-10">
              {/* ArrowsLeftRight SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M213.66,181.66l-32,32a8,8,0,0,1-11.32-11.32L188.69,184H48a8,8,0,0,1,0-16H188.69l-18.35-18.34a8,8,0,0,1,11.32-11.32l32,32A8,8,0,0,1,213.66,181.66Zm-139.32-64a8,8,0,0,0,11.32-11.32L67.31,88H208a8,8,0,0,0,0-16H67.31L85.66,53.66A8,8,0,0,0,74.34,42.34l-32,32a8,8,0,0,0,0,11.32Z"></path>
              </svg>
            </div>
            <p className="text-[#0e141b] text-base font-normal leading-normal flex-1 truncate">Transfer</p>
          </div>
          <div className="shrink-0">
            <div className="text-[#0e141b] flex size-7 items-center justify-center">
              {/* CaretRight SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path>
              </svg>
            </div>
          </div>
        </div>
        {/* Pay Bills */}
        <div className="flex items-center gap-4 bg-slate-50 px-4 min-h-14 justify-between rounded-lg">
          <div className="flex items-center gap-4">
            <div className="text-[#0e141b] flex items-center justify-center rounded-lg bg-[#e7edf3] shrink-0 size-10">
              {/* Receipt SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M72,104a8,8,0,0,1,8-8h96a8,8,0,0,1,0,16H80A8,8,0,0,1,72,104Zm8,40h96a8,8,0,0,0,0-16H80a8,8,0,0,0,0,16ZM232,56V208a8,8,0,0,1-11.58,7.15L192,200.94l-28.42,14.21a8,8,0,0,1-7.16,0L128,200.94,99.58,215.15a8,8,0,0,1-7.16,0L64,200.94,35.58,215.15A8,8,0,0,1,24,208V56A16,16,0,0,1,40,40H216A16,16,0,0,1,232,56Zm-16,0H40V195.06l20.42-10.22a8,8,0,0,1,7.16,0L96,199.06l28.42-14.22a8,8,0,0,1,7.16,0L160,199.06l28.42-14.22a8,8,0,0,1,7.16,0L216,195.06Z"></path>
              </svg>
            </div>
            <p className="text-[#0e141b] text-base font-normal leading-normal flex-1 truncate">Pay Bills</p>
          </div>
          <div className="shrink-0">
            <div className="text-[#0e141b] flex size-7 items-center justify-center">
              {/* CaretRight SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path>
              </svg>
            </div>
          </div>
        </div>
        {/* Deposit */}
        <div className="flex items-center gap-4 bg-slate-50 px-4 min-h-14 justify-between rounded-lg">
          <div className="flex items-center gap-4">
            <div className="text-[#0e141b] flex items-center justify-center rounded-lg bg-[#e7edf3] shrink-0 size-10">
              {/* PlusSquare SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M208,32H48A16,16,0,0,0,32,48V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V48A16,16,0,0,0,208,32Zm0,176H48V48H208V208Zm-32-80a8,8,0,0,1-8,8H136v32a8,8,0,0,1-16,0V136H88a8,8,0,0,1,0-16h32V88a8,8,0,0,1,16,0v32h32A8,8,0,0,1,176,128Z"></path>
              </svg>
            </div>
            <p className="text-[#0e141b] text-base font-normal leading-normal flex-1 truncate">Deposit</p>
          </div>
          <div className="shrink-0">
            <div className="text-[#0e141b] flex size-7 items-center justify-center">
              {/* CaretRight SVG */}
              <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                <path d="M181.66,133.66l-80,80a8,8,0,0,1-11.32-11.32L164.69,128,90.34,53.66a8,8,0,0,1,11.32-11.32l80,80A8,8,0,0,1,181.66,133.66Z"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
