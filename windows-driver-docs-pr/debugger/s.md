---
title: S (Windows Debugger Glossary)
description: Glossary page - S
Robots: noindex, nofollow
ms.assetid: 94cbf33b-e975-49eb-a266-774798955a48
keywords: ["suspended thread", "suspended process"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# S


<span id="scope"></span><span id="SCOPE"></span>**scope**  
The context that defines the local variables. The scope has three components: a stack frame, a current instruction, and a register context.

Sometimes referred to as *local context* or *lexical scope*.

<span id="second_chance_exception"></span><span id="SECOND_CHANCE_EXCEPTION"></span>**second-chance exception**  
The second opportunity to handle an exception. This opportunity is only provided if the exception was not handled on the first chance.

<span id="smart_client"></span><span id="SMART_CLIENT"></span>**smart client**  
An instance of the debugger engine acting as a host. The smart client is connected to a process server. or a KD connection server.

<span id="specific_exception_filter"></span><span id="SPECIFIC_EXCEPTION_FILTER"></span>**specific exception filter**  
An event filter for an exception for which the engine has a built-in filter. Most specific exception filters refer to specific types of exceptions (identified by exception code), but the default exception filter also qualifies as a specific exception filter.

<span id="specific_event_filter"></span><span id="SPECIFIC_EVENT_FILTER"></span>**specific event filter**  
An event filter for an event which is not an exception. The specific event filters are listed in [**DEBUG\_FILTER\_XXX**](https://msdn.microsoft.com/library/windows/hardware/ff541490).

<span id="specific_filter"></span><span id="SPECIFIC_FILTER"></span>**specific filter**  
An event filter for an event for which the engine has a built-in filter.

<span id="software_breakpoint"></span><span id="SOFTWARE_BREAKPOINT"></span>**software breakpoint**  
A breakpoint that is implemented by the debugger engine temporarily modifying the target's executable code. The breakpoint is triggered when the code is executed. The code modification is invisible to users of the debugger or the debugger engine API.

<span id="stack"></span><span id="STACK"></span>**stack**  
See call stack.

<span id="stack_frame"></span><span id="STACK_FRAME"></span>**stack frame**  
The memory in the call stack containing the data for a single function call. This includes the return address, parameters passed to the function, and local variables.

<span id="stop_code"></span><span id="STOP_CODE"></span>**stop code**  
See bug check code.

<span id="stop_error"></span><span id="STOP_ERROR"></span>**stop error**  
See bug check.

<span id="stop_screen"></span><span id="STOP_SCREEN"></span>**stop screen**  
See blue screen.

<span id="subregister"></span><span id="SUBREGISTER"></span>**subregister**  
A register that is contained within another register. When the subregister changes, the portion of the register that contains the subregister also changes.

<span id="suspended"></span><span id="SUSPENDED"></span>**suspended**  
A target, process, or thread is suspended if it has been blocked it from executing.

<span id="symbol"></span><span id="SYMBOL"></span>**symbol**  
A unit of debugging information which provides interpretive information about the target in a debugging session. Examples of symbols include variables (local and global), functions, types and function entries. Information about symbols can include the name, type (if applicable), and the address or regisgter where it is stored, as well as any parent or child symbols. This information is stored in symbol files and is typically not available in the module itself.

The debugger engine can synthesize certain symbols when symbol files are not available (for example, exported symbols), but these symbols generally provide only minimal information.

<span id="symbol_file"></span><span id="SYMBOL_FILE"></span>**symbol file**  
A supplemental file created when an application, library, driver, or operating system is built. A symbol file contains data which is not actually needed when running the binaries, but which is very useful in the debugging process.

<span id="symbol_group"></span><span id="SYMBOL_GROUP"></span>**symbol group**  
A group of symbols, typically representing all the local variables in a scope.

<span id="symbol_type"></span><span id="SYMBOL_TYPE"></span>**symbol type**  
Descriptive information about a symbol's representation, such as its layout in memory. This is part of the information a compiler uses to generate code to manipulate the symbol. It is also used by the debugger engine to manipulate symbols. The symbol type is distributed in symbol files.

<span id="synthetic_module"></span><span id="SYNTHETIC_MODULE"></span>**synthetic module**  
A region of memory that the engine treats like a module. A synthetic module may contain synthetic symbols.

<span id="synthetic_symbol"></span><span id="SYNTHETIC_SYMBOL"></span>**synthetic symbol**  
A memory address that the engine treats like a symbol.

<span id="system_crash"></span><span id="SYSTEM_CRASH"></span>**system crash**  
See bug check.

 

 





