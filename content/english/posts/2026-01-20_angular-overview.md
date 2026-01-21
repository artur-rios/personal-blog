+++
title = 'Angular Overview'
date = '2026-01-20'
tags = ['study notes', 'angular', 'front-end']
topics = ['personal']
weight = 1
enableComments = true
+++

# 🌐 Angular Overview

These are study notes I made about Angular. To know more, check the [official documentation](https://angular.dev).

## 📌 Core Concepts

Angular is a **TypeScript-based, component-driven framework**. It emphasizes:

- **Component architecture**: UI broken into reusable, encapsulated blocks.
- **Modules (NgModules)**: Logical groupings of components, directives, and services.
- **Dependency Injection (DI)**: Services are injected into components for reusability and testability.
- **Reactive programming**: RxJS streams for handling async events and data.

## 🔗 Data Binding

Data binding connects component logic with the template:

- **Interpolation (`{{value}}`)** → Inserts component values into HTML.
- **Property Binding (`[property]="value"`)** → Updates DOM properties dynamically.
- **Event Binding (`(event)="handler()"`)** → Responds to user actions like clicks.
- **Two-way Binding (`[(ngModel)]="value"`)** → Synchronizes component state and UI, especially in forms.

This makes Angular highly declarative: templates reflect state automatically.

## ⏳ Lifecycle Methods

Angular components follow a lifecycle. Hooks allow developers to run logic at specific stages:

| Hook | When It’s Called | Typical Use |
| ------ | ------------------ | ------------- |
| **`ngOnChanges()`** | Before `ngOnInit`, whenever an `@Input` property changes | React to input changes |
| **`ngOnInit()`** | Once, after first `ngOnChanges` | Initialize data, fetch resources |
| **`ngDoCheck()`** | On every change detection cycle | Custom change detection |
| **`ngAfterContentInit()`** | After Angular projects external content into component | Setup projected content |
| **`ngAfterContentChecked()`** | After every check of projected content | Respond to content changes |
| **`ngAfterViewInit()`** | After component’s view and child views are initialized | Access child components |
| **`ngAfterViewChecked()`** | After every check of component’s view | Respond to view changes |
| **`ngOnDestroy()`** | Just before component is removed | Cleanup (unsubscribe, detach listeners) |

These hooks give precise control over initialization, updates, and teardown.

## 🎨 Decorators

Decorators are metadata annotations that define Angular behavior:

- **`@Component`** → Declares a component (selector, template, styles).
- **`@NgModule`** → Groups components, directives, and services into a module.
- **`@Injectable`** → Marks a class as available for DI.
- **`@Input` / `@Output`** → Enable parent-child communication.
- **`@Directive`** → Extends HTML with custom behavior.

Decorators are the backbone of Angular’s declarative style.

## 🧩 Other Core Concepts

- **Routing** → Angular Router maps URLs to components.
- **Services** → Encapsulate business logic and data access.
- **Directives** → Structural (`*ngIf`, `*ngFor`) and attribute directives for DOM manipulation.
- **Forms** → Template-driven (simple) and reactive (complex, scalable).
- **Change Detection** → Angular updates the DOM automatically when state changes.
- **Testing** → Jasmine/Karma for unit tests, Cypress/Playwright for E2E.

## 🛠️ Build & Tooling

Angular provides a **powerful build system** via the Angular CLI:

### Angular CLI (`ng`)

- Commands: `ng serve`, `ng build`, `ng test`, `ng generate`.
- Handles scaffolding, builds, testing, and deployment.

### Build Process

- Uses **Webpack** under the hood for bundling.
- TypeScript compilation → transpiles to JavaScript.
- Ahead-of-Time (AOT) compilation → compiles templates at build time for faster runtime.
- Tree-shaking → removes unused code.
- Differential loading → serves modern JS to modern browsers, legacy bundles to older ones.

### Tools & Ecosystem

- **RxJS** → reactive programming.
- **Zone.js** → manages async operations for change detection.
- **Angular DevTools** → Chrome extension for debugging.
- **Testing frameworks** → Jasmine, Karma, Cypress.
- **Package manager** → npm or yarn for dependencies.

The build pipeline ensures optimized, production-ready applications with minimal manual configuration.

## 📦 NgModules

### 🔑 What is an NgModule?

- An **NgModule** is a **class decorated with `@NgModule`**.  
- The decorator provides **metadata** that tells Angular how to assemble the application:  
  - Which components, directives, and pipes belong to the module.  
  - Which external modules are imported.  
  - Which parts are exposed to other modules.  
  - Which services are available via dependency injection.  

Think of it as a **blueprint** or **container** that organizes functionality into logical sections.

### 🧩 Responsibilities of an NgModule

NgModules serve two main purposes:

1. **Declarations** → Register components, directives, and pipes that belong to the module.  
2. **Providers** → Add services to the dependency injector so they can be used across the app.  

Additionally:

- **Imports** → Bring in other modules (e.g., `FormsModule`, `RouterModule`).  
- **Exports** → Make declarations available to other modules.  
- **Bootstrap** → Define the root component to launch the application.  

### 🏗️ Types of NgModules

- **Root Module (`AppModule`)** → Bootstraps the application.  
- **Feature Modules** → Group related functionality (e.g., `UserModule`, `AdminModule`).  
- **Shared Modules** → Contain common components, directives, and pipes used across multiple modules.  
- **Lazy-loaded Modules** → Loaded only when needed, improving performance.  

### 📌 Example

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],   // Components, directives, pipes
  imports: [BrowserModule],       // Other modules
  providers: [],                  // Services
  bootstrap: [AppComponent]       // Root component
})
export class AppModule {}
```

## 🧭 Standalone Components

### 🔑 What are Standalone Components?

- Introduced in **Angular v14**, standalone components allow developers to build applications **without NgModules**.  
- A standalone component is declared with `standalone: true` in its `@Component` decorator.  
- It can directly import other components, directives, and Angular features (like `RouterModule` or `FormsModule`) without needing a module wrapper.

### ⚖️ Difference Between NgModules and Standalone Components

| Aspect | NgModules | Standalone Components |
|--------|-----------|------------------------|
| **Structure** | Components grouped inside modules | Components are self-contained |
| **Declaration** | Components must be declared in a module | Declared with `standalone: true` |
| **Imports** | Modules import other modules | Components import dependencies directly |
| **Bootstrapping** | Root module bootstraps the app | Root component bootstraps the app |
| **Use Case** | Large, enterprise apps with modular architecture | Simpler apps, modern projects, or gradual migration |

### 📌 Example of a Standalone Component

```typescript
import { Component } from '@angular/core'; 
import { CommonModule } from '@angular/common'; 

@Component({ 
    selector: 'app-hello', 
    standalone: true, 
    imports: [CommonModule], 
    template: `<h1>Hello Angular!</h1>` 
}) 
export class HelloComponent {}
```
