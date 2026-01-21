+++
title = 'Visão Geral do Angular'
date = '2026-01-20'
tags = ['notas de estudo', 'angular', 'front-end']
topics = ['personal']
weight = 1
enableComments = true
+++

# 🌐 Visão Geral do Angular

Essas são notas de estudo que fiz sobre Angular. Para saber mais, consulte a [documentação oficial](https://angular.dev).

## 📌 Conceitos Fundamentais

Angular é um **framework baseado em TypeScript e orientado a componentes**. Ele enfatiza:

- **Arquitetura de componentes**: UI dividida em blocos reutilizáveis e encapsulados.
- **Módulos (NgModules)**: Agrupamentos lógicos de componentes, diretivas e serviços.
- **Injeção de Dependência (DI)**: Serviços são injetados nos componentes para reutilização e testabilidade.
- **Programação reativa**: Streams RxJS para lidar com eventos assíncronos e dados.

## 🔗 Data Binding

O data binding conecta a lógica do componente com o template:

- **Interpolação (`{{value}}`)** → Insere valores do componente no HTML.
- **Property Binding (`[property]="value"`)** → Atualiza propriedades do DOM dinamicamente.
- **Event Binding (`(event)="handler()"`)** → Responde a ações do usuário como cliques.
- **Two-way Binding (`[(ngModel)]="value"`)** → Sincroniza o estado do componente com a UI, especialmente em formulários.

Isso torna o Angular altamente declarativo: os templates refletem o estado automaticamente.

## ⏳ Métodos de Ciclo de Vida

Os componentes Angular seguem um ciclo de vida. Os hooks permitem que desenvolvedores executem lógica em estágios específicos:

| Hook | Quando é Chamado | Uso Típico |
| ------ | ------------------ | ------------- |
| **`ngOnChanges()`** | Antes do `ngOnInit`, sempre que uma propriedade `@Input` muda | Reagir a mudanças de input |
| **`ngOnInit()`** | Uma vez, após o primeiro `ngOnChanges` | Inicializar dados, buscar recursos |
| **`ngDoCheck()`** | Em cada ciclo de detecção de mudanças | Detecção de mudanças personalizada |
| **`ngAfterContentInit()`** | Após o Angular projetar conteúdo externo no componente | Configurar conteúdo projetado |
| **`ngAfterContentChecked()`** | Após cada verificação do conteúdo projetado | Responder a mudanças de conteúdo |
| **`ngAfterViewInit()`** | Após a view do componente e views filhas serem inicializadas | Acessar componentes filhos |
| **`ngAfterViewChecked()`** | Após cada verificação da view do componente | Responder a mudanças da view |
| **`ngOnDestroy()`** | Logo antes do componente ser removido | Limpeza (cancelar inscrições, remover listeners) |

Esses hooks dão controle preciso sobre inicialização, atualizações e destruição.

## 🎨 Decorators

Decorators são anotações de metadados que definem o comportamento do Angular:

- **`@Component`** → Declara um componente (seletor, template, estilos).
- **`@NgModule`** → Agrupa componentes, diretivas e serviços em um módulo.
- **`@Injectable`** → Marca uma classe como disponível para DI.
- **`@Input` / `@Output`** → Habilitam comunicação entre componente pai e filho.
- **`@Directive`** → Estende o HTML com comportamento personalizado.

Decorators são a espinha dorsal do estilo declarativo do Angular.

## 🧩 Outros Conceitos Fundamentais

- **Roteamento** → O Angular Router mapeia URLs para componentes.
- **Serviços** → Encapsulam lógica de negócios e acesso a dados.
- **Diretivas** → Estruturais (`*ngIf`, `*ngFor`) e diretivas de atributo para manipulação do DOM.
- **Formulários** → Template-driven (simples) e reativos (complexos, escaláveis).
- **Detecção de Mudanças** → O Angular atualiza o DOM automaticamente quando o estado muda.
- **Testes** → Jasmine/Karma para testes unitários, Cypress/Playwright para E2E.

## 🛠️ Build & Ferramentas

O Angular fornece um **sistema de build poderoso** via Angular CLI:

### Angular CLI (`ng`)

- Comandos: `ng serve`, `ng build`, `ng test`, `ng generate`.
- Gerencia scaffolding, builds, testes e deploy.

### Processo de Build

- Usa **Webpack** internamente para bundling.
- Compilação TypeScript → transpila para JavaScript.
- Compilação Ahead-of-Time (AOT) → compila templates em tempo de build para execução mais rápida.
- Tree-shaking → remove código não utilizado.
- Differential loading → serve JS moderno para navegadores modernos, bundles legados para navegadores antigos.

### Ferramentas & Ecossistema

- **RxJS** → programação reativa.
- **Zone.js** → gerencia operações assíncronas para detecção de mudanças.
- **Angular DevTools** → extensão do Chrome para debugging.
- **Frameworks de teste** → Jasmine, Karma, Cypress.
- **Gerenciador de pacotes** → npm ou yarn para dependências.

O pipeline de build garante aplicações otimizadas e prontas para produção com configuração manual mínima.

## 📦 NgModules

### 🔑 O que é um NgModule?

- Um **NgModule** é uma **classe decorada com `@NgModule`**.  
- O decorator fornece **metadados** que dizem ao Angular como montar a aplicação:  
  - Quais componentes, diretivas e pipes pertencem ao módulo.  
  - Quais módulos externos são importados.  
  - Quais partes são expostas para outros módulos.  
  - Quais serviços estão disponíveis via injeção de dependência.  

Pense nele como um **blueprint** ou **container** que organiza funcionalidades em seções lógicas.

### 🧩 Responsabilidades de um NgModule

NgModules servem dois propósitos principais:

1. **Declarations** → Registram componentes, diretivas e pipes que pertencem ao módulo.  
2. **Providers** → Adicionam serviços ao injetor de dependências para que possam ser usados em toda a aplicação.  

Adicionalmente:

- **Imports** → Trazem outros módulos (ex: `FormsModule`, `RouterModule`).  
- **Exports** → Tornam declarations disponíveis para outros módulos.  
- **Bootstrap** → Define o componente raiz para iniciar a aplicação.  

### 🏗️ Tipos de NgModules

- **Root Module (`AppModule`)** → Inicializa a aplicação.  
- **Feature Modules** → Agrupam funcionalidades relacionadas (ex: `UserModule`, `AdminModule`).  
- **Shared Modules** → Contêm componentes, diretivas e pipes comuns usados em múltiplos módulos.  
- **Lazy-loaded Modules** → Carregados apenas quando necessários, melhorando a performance.  

### 📌 Exemplo

```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],   // Componentes, diretivas, pipes
  imports: [BrowserModule],       // Outros módulos
  providers: [],                  // Serviços
  bootstrap: [AppComponent]       // Componente raiz
})
export class AppModule {}
```

## 🧭 Standalone Components

### 🔑 O que são Standalone Components?

- Introduzidos no **Angular v14**, standalone components permitem que desenvolvedores construam aplicações **sem NgModules**.  
- Um standalone component é declarado com `standalone: true` no seu decorator `@Component`.  
- Ele pode importar diretamente outros componentes, diretivas e funcionalidades do Angular (como `RouterModule` ou `FormsModule`) sem precisar de um wrapper de módulo.

### ⚖️ Diferença Entre NgModules e Standalone Components

| Aspecto | NgModules | Standalone Components |
|--------|-----------|------------------------|
| **Estrutura** | Componentes agrupados dentro de módulos | Componentes são autocontidos |
| **Declaração** | Componentes devem ser declarados em um módulo | Declarados com `standalone: true` |
| **Imports** | Módulos importam outros módulos | Componentes importam dependências diretamente |
| **Bootstrapping** | Módulo raiz inicializa a app | Componente raiz inicializa a app |
| **Caso de Uso** | Apps grandes e enterprise com arquitetura modular | Apps mais simples, projetos modernos ou migração gradual |

### 📌 Exemplo de um Standalone Component

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
