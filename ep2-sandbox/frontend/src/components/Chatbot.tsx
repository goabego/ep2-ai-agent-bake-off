import React, { useState, useEffect } from 'react';
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

interface Message {
    sender: 'user' | 'bot';
    text: string;
    messageId?: string;
    contextId?: string;
}

const Chatbot: React.FC = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<Message[]>([
        {
            sender: 'bot',
            text: 'Hello, I am Cymbal Chat and can get you answers about your transaction history, your current assets, or any information related to your financial footprint.'
        }
    ]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [contextId, setContextId] = useState<string | null>(null);

    // Generate unique message ID
    const generateMessageId = () => `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;

    // Send message to A2A API
    const sendMessageToAPI = async (messageText: string): Promise<string> => {
        // Use Vite proxy in development, direct API in production
        const API_ENDPOINT = import.meta.env.DEV 
            ? '/api'  // This will be proxied to the A2A API
            : 'https://a2a-426194555180.us-central1.run.app';
        
        // Note: In production, you'd need to implement proper authentication
        // For now, we'll send without auth header (API may reject this)
        const payload = {
            jsonrpc: "2.0",
            method: "message/send",
            params: {
                message: {
                    messageId: generateMessageId(),
                    role: "user",
                    parts: [
                        {
                            text: messageText
                        }
                    ]
                }
            },
            id: "1"
        };

        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // TODO: Add proper authentication header
                    // 'Authorization': `Bearer ${authToken}`
                    'Authorization': `Bearer ${import.meta.env.VITE_A2A_API_KEY}`
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`API request failed: ${response.status}`);
            }

            const data = await response.json();
            
            // Extract response text from the JSON-RPC result
            if (data.result && data.result.artifacts && data.result.artifacts.length > 0) {
                const responseText = data.result.artifacts[0].parts[0].text;
                
                // Store context ID for future requests if available
                if (data.result.contextId) {
                    setContextId(data.result.contextId);
                }
                
                return responseText;
            } else {
                throw new Error('Invalid response format from API');
            }
        } catch (error) {
            console.error('Error sending message to API:', error);
            return 'Sorry, I encountered an error while processing your request. Please try again.';
        }
    };

    const handleSendMessage = async () => {
        if (inputValue.trim() && !isLoading) {
            const userMessage: Message = {
                sender: 'user',
                text: inputValue,
                messageId: generateMessageId()
            };

            // Add user message immediately
            setMessages(prev => [...prev, userMessage]);
            setInputValue('');
            setIsLoading(true);

            try {
                // Send to API and get response
                const apiResponse = await sendMessageToAPI(inputValue);
                
                const botMessage: Message = {
                    sender: 'bot',
                    text: apiResponse,
                    messageId: generateMessageId(),
                    contextId: contextId || undefined
                };

                setMessages(prev => [...prev, botMessage]);
            } catch (error) {
                console.error('Error handling message:', error);
                const errorMessage: Message = {
                    sender: 'bot',
                    text: 'Sorry, I encountered an error. Please try again.',
                    messageId: generateMessageId()
                };
                setMessages(prev => [...prev, errorMessage]);
            } finally {
                setIsLoading(false);
            }
        }
    };

    const toggleChat = () => {
        setIsOpen(!isOpen);
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
                                    <div className={`p-3 rounded-lg max-w-xs break-words ${msg.sender === 'user' ? 'bg-primary text-primary-foreground' : 'bg-muted text-muted-foreground'}`}>
                                        {msg.text}
                                    </div>
                                </div>
                            ))}
                            {isLoading && (
                                <div className="flex justify-start">
                                    <div className="p-3 rounded-lg bg-muted text-muted-foreground">
                                        <div className="flex space-x-1">
                                            <div className="w-2 h-2 bg-current rounded-full animate-bounce"></div>
                                            <div className="w-2 h-2 bg-current rounded-full animate-bounce" style={{animationDelay: '0.1s'}}></div>
                                            <div className="w-2 h-2 bg-current rounded-full animate-bounce" style={{animationDelay: '0.2s'}}></div>
                                        </div>
                                    </div>
                                </div>
                            )}
                        </div>
                    </CardContent>
                    <CardFooter>
                        <div className="flex w-full space-x-2">
                            <Input
                                value={inputValue}
                                onChange={(e) => setInputValue(e.target.value)}
                                onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
                                placeholder="Type a message..."
                                disabled={isLoading}
                            />
                            <Button onClick={handleSendMessage} disabled={isLoading || !inputValue.trim()}>
                                Send
                            </Button>
                        </div>
                    </CardFooter>
                </Card>
            )}
        </div>
    );
};

export default Chatbot;
