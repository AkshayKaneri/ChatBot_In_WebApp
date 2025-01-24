import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true, // This makes it a standalone component
})
export class AppComponent {
  title = 'Chat-Bot';
  userInput: string = "";
  messages: { role: string; content: string }[] = [];

  constructor(private http: HttpClient) { }

  sendMessage() {
    const userMessage = this.userInput;
    this.messages.push({ role: "User", content: userMessage });

    this.http
      .post("http://localhost:3000/chat", { prompt: userMessage })
      .subscribe((response: any) => {
        this.messages.push({ role: "Bot", content: response.response });
      });

    this.userInput = "";
  }
}
