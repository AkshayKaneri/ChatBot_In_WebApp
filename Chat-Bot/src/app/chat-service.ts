import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class ChatService {
    private apiUrl = 'http://localhost:3000/chat'; // Your API URL

    constructor(private http: HttpClient) { }

    sendMessage(prompt: string) {
        return this.http.post<{ response: string }>(this.apiUrl, { prompt });
    }
}