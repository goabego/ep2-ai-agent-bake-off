import React from 'react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-muted text-foreground pt-16 pb-12 relative overflow-hidden">
      <div className="absolute inset-0 z-0 opacity-50">
        <svg width="100%" height="100%" viewBox="0 0 1440 300" preserveAspectRatio="none" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M-2,146.5Q358.5,312,720,146.5T1442,146.5V300H-2V146.5Z" fill="var(--color-accent)"/>
        </svg>
      </div>
      <div className="container mx-auto px-6 relative z-10">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Column 1: About */}
          <div className="flex flex-col">
            <h2 className="text-foreground text-4xl font-bold leading-tight tracking-[-0.015em]">Cymbal Bank</h2>
            <p className="mt-4 text-sm text-muted-foreground max-w-xs">
              Cymbal Bank is a residential mortgage servicer, lender, and insurance agency. Our mission is to empower every homeowner. We’re creating a world where homeownership comes with ease, security, and financial know-how.
            </p>
          </div>

          {/* Column 2 & 3: Links */}
          <div className="md:col-span-2 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-8">
            <div>
              <h3 className="font-semibold text-foreground">Homeowners</h3>
              <ul className="mt-4 space-y-2 text-sm">
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Manage your Mortgage</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Get a Mortgage</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Get Insured</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Help Center</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Tools & Resources</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Contact Us</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Complaints</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Fees</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Financial Hardship Assistance</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Homeowner Assistance Fund</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-foreground">Company</h3>
              <ul className="mt-4 space-y-2 text-sm">
                <li><a href="#" className="text-muted-foreground hover:text-foreground">About Us</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Careers</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Blog</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Partners</a></li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-foreground">Legal</h3>
              <ul className="mt-4 space-y-2 text-sm">
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Legal Disclosures</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Licenses</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Privacy Policy</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Terms and Conditions</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Electronic Communications Disclosure</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Mobile and Telephone Notifications</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">Security and Privacy</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">NMLS Consumer Access</a></li>
                <li><a href="#" className="text-muted-foreground hover:text-foreground">NYC Rules on Language Services</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
