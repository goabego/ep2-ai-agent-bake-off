import React, { useEffect, useState } from 'react';
import { Outlet, useSearchParams } from 'react-router-dom';
import Navbar from './Navbar';
import { fetchUser } from '@/services/api';

interface User {
  name: string;
  profile_picture: string;
}

const Layout: React.FC = () => {
  const [user, setUser] = useState<User | null>(null);
  const [searchParams] = useSearchParams();
  const userId = searchParams.get('userId');

  useEffect(() => {
    if (userId) {
      const loadUser = async () => {
        try {
          const userData = await fetchUser(userId);
          setUser(userData);
        } catch (err) {
          console.error("Failed to load user data");
        }
      };
      loadUser();
    }
  }, [userId]);

  return (
    <div className="relative flex size-full min-h-screen flex-col bg-slate-50 group/design-root overflow-x-hidden " style={{fontFamily: '"Public Sans", "Noto Sans", sans-serif'}}>
      <Navbar userName={user?.name} profilePicture={user?.profile_picture} />
      <main className="flex-1 pb-20">
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;