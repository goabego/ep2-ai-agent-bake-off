import React from 'react';

const Navbar: React.FC<{ userName?: string, profilePicture?: string }> = ({ profilePicture }) => {
  return (
    <header className="flex items-center justify-between border-b border-solid border-b-border px-10 py-3 mx-auto w-full max-w-7xl">
      <div className="flex items-center gap-4 text-foreground">
        <div className="size-4">
          {/* Logo SVG */}
          <svg viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clipPath="url(#clip0_6_319)">
              <path d="M8.57829 8.57829C5.52816 11.6284 3.451 15.5145 2.60947 19.7452C1.76794 23.9758 2.19984 28.361 3.85056 32.3462C5.50128 36.3314 8.29667 39.7376 11.8832 42.134C15.4698 44.5305 19.6865 45.8096 24 45.8096C28.3135 45.8096 32.5302 44.5305 36.1168 42.134C39.7033 39.7375 42.4987 36.3314 44.1494 32.3462C45.8002 28.361 46.2321 23.9758 45.3905 19.7452C44.549 15.5145 42.4718 11.6284 39.4217 8.57829L24 24L8.57829 8.57829Z" fill="currentColor"></path>
            </g>
            <defs>
              <clipPath id="clip0_6_319"><rect width="48" height="48" fill="white"></rect></clipPath>
            </defs>
          </svg>
        </div>
        <h2 className="text-foreground text-lg font-bold leading-tight tracking-[-0.015em]">Cymbal Bank</h2>
      </div>
      <div className="flex flex-1 justify-end gap-8">
        <div className="flex items-center gap-9">
          <a className="text-foreground text-sm font-medium leading-normal" href="#">Home</a>
          <a className="text-foreground text-sm font-medium leading-normal" href="#">Accounts</a>
          <a className="text-foreground text-sm font-medium leading-normal" href="#">Transfers</a>
          <a className="text-foreground text-sm font-medium leading-normal" href="#">Payments</a>
          <a className="text-foreground text-sm font-medium leading-normal" href="#">Statements</a>
        </div>
        <button className="flex max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 bg-accent text-foreground gap-2 text-sm font-bold leading-normal tracking-[0.015em] min-w-0 px-2.5">
          <div className="text-foreground" data-icon="Bell" data-size="20px" data-weight="regular">
            {/* Bell SVG */}
            <svg xmlns="http://www.w3.org/2000/svg" width="20px" height="20px" fill="currentColor" viewBox="0 0 256 256">
              <path d="M221.8,175.94C216.25,166.38,208,139.33,208,104a80,80,0,1,0-160,0c0,35.34-8.26,62.38-13.81,71.94A16,16,0,0,0,48,200H88.81a40,40,0,0,0,78.38,0H208a16,16,0,0,0,13.8-24.06ZM128,216a24,24,0,0,1-22.62-16h45.24A24,24,0,0,1,128,216ZM48,184c7.7-13.24,16-43.92,16-80a64,64,0,1,1,128,0c0,36.05,8.28,66.73,16,80Z"></path>
            </svg>
          </div>
        </button>
        <div className="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-10" style={{ backgroundImage: `url(${profilePicture})` }}></div>
      </div>
    </header>
  );
};

export default Navbar;
