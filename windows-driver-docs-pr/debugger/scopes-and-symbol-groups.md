---
title: Scopes and Symbol Groups
description: Scopes and Symbol Groups
ms.assetid: f14b6361-9962-4fa3-bb1a-dfde066754b9
keywords: ["Debugger Engine API, symbols, symbol groups", "symbol group, scopes", "Debugger Engine API, symbols, scopes", "scopes"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Scopes and Symbol Groups


## <span id="ddk_scopes_and_symbol_groups_dbx"></span><span id="DDK_SCOPES_AND_SYMBOL_GROUPS_DBX"></span>


A *symbol group* contains a set of symbols for efficient manipulation as a group. A symbol group can be created and populated manually or can be automatically generated and updated based on symbols in lexical scopes, such as local variables and function arguments. The interface [IDebugSymbolGroup](https://msdn.microsoft.com/library/windows/hardware/ff550838) is used to represent a symbol group.

There are two ways to create a symbol group. An empty symbol group is returned by [**CreateSymbolGroup**](https://msdn.microsoft.com/library/windows/hardware/ff540093), and the symbol group for the current lexical scope is returned by [**GetScopeSymbolGroup**](https://msdn.microsoft.com/library/windows/hardware/ff548280).

**Note**   The symbol group generated from the current scope is a snapshot of the local variables. If any execution occurs in the target, the symbols may no longer be accurate. Also, if the current scope changes, the symbol group will no longer represent the *current* scope (because it will continue to represent the scope for which it was created).

 

Symbols can be added to a symbol group using [**AddSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff537925), and removed using [**RemoveSymbolByIndex**](https://msdn.microsoft.com/library/windows/hardware/ff554510) or [**RemoveSymbolByName**](https://msdn.microsoft.com/library/windows/hardware/ff554518). The method [**OutputAsType**](https://msdn.microsoft.com/library/windows/hardware/ff553191) tells the debugger to use a different symbol type when handling a symbol's data.

**Note**   The values for scoped symbols may not be accurate. In particular, the machine architecture and compiler optimizations may prevent the debugger from accurately determining a symbol's value.

 

The *symbol entry information* is a description of a symbol, including its location and its type. To find this information for a symbol in a module, use the [**IDebugSymbols3::GetSymbolEntryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548484). To find this information for a symbol in a symbol group, use [**IDebugSymbolGroup2::GetSymbolEntryInformation**](https://msdn.microsoft.com/library/windows/hardware/ff548487). See [**DEBUG\_SYMBOL\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/ff541662) for details of the symbol entry information.

The following methods return information about a symbol in a symbol group:

-   [**GetSymbolName**](https://msdn.microsoft.com/library/windows/hardware/ff549121) returns the name of the symbol.

-   [**GetSymbolOffset**](https://msdn.microsoft.com/library/windows/hardware/ff549135) returns the absolute address in the target's virtual address space of the symbol, if the symbol has an absolute address.

-   [**GetSymbolRegister**](https://msdn.microsoft.com/library/windows/hardware/ff549165) returns the register containing the symbol, if the symbol is contained in a register.

-   [**GetSymbolSize**](https://msdn.microsoft.com/library/windows/hardware/ff549169) returns the size of the data for the symbol.

-   [**GetSymbolTypeName**](https://msdn.microsoft.com/library/windows/hardware/ff549188) returns the name of the symbol's type.

-   [**GetSymbolValueText**](https://msdn.microsoft.com/library/windows/hardware/ff549201) returns the value of the symbol as a string.

If a symbol is stored in a register or in a memory location known to the debugger engine, its value can be changed using [**WriteSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff561457).

A symbol is a *parent symbol* if it contains other symbols. For example, a structure contains its members. A symbol is a *child symbol* if it is contained in another symbol. A symbol may be both a parent and child symbol. Each symbol group has a flat structure and contains parent symbols and their children. Each symbol has a *depth* -- symbols without parents in the symbol group have a depth of zero, and the depth of each child symbol is one greater than the depth of its parent. The children of a parent symbol may or may not be present in the symbol group. When the children are present in the symbol group, the parent symbol is referred to as *expanded*. To add or remove the children of a symbol in a symbol group, use [**ExpandSymbol**](https://msdn.microsoft.com/library/windows/hardware/ff543271).

The number of symbols in a symbol group is returned by [**GetNumberSymbols**](https://msdn.microsoft.com/library/windows/hardware/ff547975). The *index* of a symbol in a symbol group is an identification number; the index ranges from zero to the number of symbols minus one. Each time a symbol is added to or removed from a symbol group -- for example, by expanding a symbol -- the index of all the symbols in the symbol group may change.

The symbol parameters, including information about parent-child relationships, can be found by using [**GetSymbolParameters**](https://msdn.microsoft.com/library/windows/hardware/ff549146). This method returns a [**DEBUG\_SYMBOL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff541673) structure.

The symbols in a symbol group can be printed to the debugger's output stream using the method [**OutputSymbols**](https://msdn.microsoft.com/library/windows/hardware/ff553264).

### <span id="scopes"></span><span id="SCOPES"></span>Scopes

The *current scope*, or *current local context*, determines the local variables exposed by the debugger engine. The scope has three components:

1.  A stack frame.

2.  A current instruction.

3.  A register context.

If the stack frame is at the top of the call stack, the current instruction is the instruction that resulted in the last event. Otherwise the current instruction is the function call which resulted in the next higher stack frame.

The methods [**GetScope**](https://msdn.microsoft.com/library/windows/hardware/ff548270) and [**SetScope**](https://msdn.microsoft.com/library/windows/hardware/ff556773) can be used to get and set the current scope. When an event occurs, the current scope is set to the scope of the event. The current scope can be reset to the scope of the last event using [**ResetScope**](https://msdn.microsoft.com/library/windows/hardware/ff554577).

### <span id="thread-context"></span><span id="THREAD_CONTEXT"></span>Thread Context

The *thread context* is the state preserved by Windows when switching threads. This is similar to the register context, except that there is some kernel-only processor state that is part of the register context but not the thread context. This extra state is available as registers during kernel-mode debugging.

The thread context is represented by the CONTEXT structure defined in ntddk.h. This structure is platform-dependent and its interpretation depends on the effective processor type. The methods [**GetThreadContext**](https://msdn.microsoft.com/library/windows/hardware/ff549291) and [**SetThreadContext**](https://msdn.microsoft.com/library/windows/hardware/ff556829) can be used to get and set the thread context.

 

 





