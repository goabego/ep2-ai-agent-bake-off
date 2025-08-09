import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import { Input } from '@/components/ui/input';

const RobotIcon = () => (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <rect x="2" y="8" width="20" height="10" rx="2" ry="2"></rect>
        <path d="M6 8V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v2"></path>
        <circle cx="8" cy="13" r="1"></circle>
        <circle cx="16" cy="13" r="1"></circle>
        <path d="M10 17h4"></path>
    </svg>
);

const Chatbot: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([
        {
            sender: 'bot',
            text: 'Hello, I am Cymbal Chat and can get you answers about your transaction history, your current assets, or any information related to your financial footprint.'
        }
    ]);
    const [inputValue, setInputValue] = useState('');

    const toggleChat = () => {
        setIsOpen(!isOpen);
    };

    const handleSendMessage = () => {
        if (inputValue.trim()) {
            const newMessages = [...messages, { sender: 'user', text: inputValue }];
            if (inputValue === 'What is my average cash flow?') {
                newMessages.push({ sender: 'bot', text: 'Answer 1' });
            } else if (inputValue === 'What was my most recent subscription?') {
                newMessages.push({ sender: 'bot', text: 'Answer 2' });
            }
            setMessages(newMessages);
            setInputValue('');
        }
    };

    return (
        <div className="flex-1 v-full w-full">
            <Button
                onClick={toggleChat}
                className="absolute bottom-10 right-10 w-16 h-16 rounded-full bg-primary text-primary-foreground shadow-lg hover:bg-primary/90"
            >
                <RobotIcon />
            </Button>

            {isOpen && (
                <Card className="absolute bottom-28 right-10 w-96 bg-card text-card-foreground shadow-2xl">
                    <CardHeader>
                        <CardTitle>Cymbal Chat</CardTitle>
                    </CardHeader>
                    <CardContent className="h-80 overflow-y-auto">
                        <div className="space-y-4">
                            {messages.map((msg, index) => (
                                <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                                    <div className={`p-3 rounded-lg ${msg.sender === 'user' ? 'bg-primary text-primary-foreground' : 'bg-muted text-muted-foreground'}`}>
                                        {msg.text}
                                    </div>
                                </div>
                            ))}
                        </div>
                    </CardContent>
                    <CardFooter>
                        <div className="flex w-full space-x-2">
                            <Input
                                value={inputValue}
                                onChange={(e) => setInputValue(e.target.value)}
                                onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                                placeholder="Type a message..."
                            />
                            <Button onClick={handleSendMessage}>Send</Button>
                        </div>
                    </CardFooter>
                </Card>
            )}
        </div>
    );
};

export default Chatbot;
