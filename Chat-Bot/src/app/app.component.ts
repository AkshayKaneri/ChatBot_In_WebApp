import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { ChatService } from './chat-service';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule, CommonModule, HttpClientModule],
  providers: [ChatService],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true,
})
export class AppComponent {
  title = 'Chat-Bot';
  messages: { text: string; sender: 'user' | 'bot' }[] = [];
  userInput: string = '';
  loading: boolean = false;

  @ViewChild('messagesContainer') messagesContainer!: ElementRef;


  constructor(
    private chatService: ChatService
  ) { }

  sendMessage() {
    if (this.userInput.trim() === '') return;

    // Add the user's message
    this.messages.push({ text: this.userInput, sender: 'user' });

    const userMessage = this.userInput; // Store the message
    this.userInput = ''; // Clear the input field

    // Scroll to the bottom after user's message
    setTimeout(() => this.scrollToBottom(), 0);

    // Show the loader while waiting for the bot's response
    this.loading = true;

    // Call the backend to get the bot response
    this.chatService.sendMessage(userMessage).subscribe(
      (response) => {
        this.loading = false; // Hide loader after receiving the response
        this.messages.push({ text: response.response, sender: 'bot' });

        // Scroll to the bottom after bot's response
        setTimeout(() => this.scrollToBottom(), 0);
      },
      (error) => {
        this.loading = false; // Hide loader if there's an error
        this.messages.push({ text: 'Something went wrong. Please try again.', sender: 'bot' });

        // Scroll to the bottom after error message
        setTimeout(() => this.scrollToBottom(), 0);
      }
    );
  }

  // Scroll to the bottom of the chat
  private scrollToBottom() {
    if (this.messagesContainer) {
      this.messagesContainer.nativeElement.scroll({
        top: this.messagesContainer.nativeElement.scrollHeight,
        behavior: 'smooth' // Smooth scrolling
      });
    }
  }
}
