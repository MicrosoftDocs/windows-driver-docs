---
title: Scopes and Symbol Groups
description: Scopes and Symbol Groups
keywords: ["Debugger Engine API, symbols, symbol groups", "symbol group, scopes", "Debugger Engine API, symbols, scopes", "scopes"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Scopes and Symbol Groups


## <span id="ddk_scopes_and_symbol_groups_dbx"></span><span id="DDK_SCOPES_AND_SYMBOL_GROUPS_DBX"></span>


A *symbol group* contains a set of symbols for efficient manipulation as a group. A symbol group can be created and populated manually or can be automatically generated and updated based on symbols in lexical scopes, such as local variables and function arguments. The interface [IDebugSymbolGroup](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugsymbolgroup) is used to represent a symbol group.

There are two ways to create a symbol group. An empty symbol group is returned by [**CreateSymbolGroup**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-createsymbolgroup), and the symbol group for the current lexical scope is returned by [**GetScopeSymbolGroup**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getscopesymbolgroup).

**Note**   The symbol group generated from the current scope is a snapshot of the local variables. If any execution occurs in the target, the symbols may no longer be accurate. Also, if the current scope changes, the symbol group will no longer represent the *current* scope (because it will continue to represent the scope for which it was created).

 

Symbols can be added to a symbol group using [**AddSymbol**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-addsymbol), and removed using [**RemoveSymbolByIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-removesymbolbyindex) or [**RemoveSymbolByName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-removesymbolbyname). The method [**OutputAsType**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-outputastype) tells the debugger to use a different symbol type when handling a symbol's data.

**Note**   The values for scoped symbols may not be accurate. In particular, the machine architecture and compiler optimizations may prevent the debugger from accurately determining a symbol's value.

 

The *symbol entry information* is a description of a symbol, including its location and its type. To find this information for a symbol in a module, use the [**IDebugSymbols3::GetSymbolEntryInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolentryinformation). To find this information for a symbol in a symbol group, use [**IDebugSymbolGroup2::GetSymbolEntryInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolentryinformation). See [**DEBUG\_SYMBOL\_ENTRY**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_symbol_entry) for details of the symbol entry information.

The following methods return information about a symbol in a symbol group:

-   [**GetSymbolName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolname) returns the name of the symbol.

-   [**GetSymbolOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymboloffset) returns the absolute address in the target's virtual address space of the symbol, if the symbol has an absolute address.

-   [**GetSymbolRegister**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolregister) returns the register containing the symbol, if the symbol is contained in a register.

-   [**GetSymbolSize**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolsize) returns the size of the data for the symbol.

-   [**GetSymbolTypeName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymboltypename) returns the name of the symbol's type.

-   [**GetSymbolValueText**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolvaluetext) returns the value of the symbol as a string.

If a symbol is stored in a register or in a memory location known to the debugger engine, its value can be changed using [**WriteSymbol**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-writesymbol).

A symbol is a *parent symbol* if it contains other symbols. For example, a structure contains its members. A symbol is a *child symbol* if it is contained in another symbol. A symbol may be both a parent and child symbol. Each symbol group has a flat structure and contains parent symbols and their children. Each symbol has a *depth* -- symbols without parents in the symbol group have a depth of zero, and the depth of each child symbol is one greater than the depth of its parent. The children of a parent symbol may or may not be present in the symbol group. When the children are present in the symbol group, the parent symbol is referred to as *expanded*. To add or remove the children of a symbol in a symbol group, use [**ExpandSymbol**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-expandsymbol).

The number of symbols in a symbol group is returned by [**GetNumberSymbols**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getnumbersymbols). The *index* of a symbol in a symbol group is an identification number; the index ranges from zero to the number of symbols minus one. Each time a symbol is added to or removed from a symbol group -- for example, by expanding a symbol -- the index of all the symbols in the symbol group may change.

The symbol parameters, including information about parent-child relationships, can be found by using [**GetSymbolParameters**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-getsymbolparameters). This method returns a [**DEBUG\_SYMBOL\_PARAMETERS**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_symbol_parameters) structure.

The symbols in a symbol group can be printed to the debugger's output stream using the method [**OutputSymbols**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbolgroup2-outputsymbols).

### <span id="scopes"></span><span id="SCOPES"></span>Scopes

The *current scope*, or *current local context*, determines the local variables exposed by the debugger engine. The scope has three components:

1.  A stack frame.

2.  A current instruction.

3.  A register context.

If the stack frame is at the top of the call stack, the current instruction is the instruction that resulted in the last event. Otherwise the current instruction is the function call which resulted in the next higher stack frame.

The methods [**GetScope**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getscope) and [**SetScope**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-setscope) can be used to get and set the current scope. When an event occurs, the current scope is set to the scope of the event. The current scope can be reset to the scope of the last event using [**ResetScope**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-resetscope).

### <span id="thread-context"></span><span id="THREAD_CONTEXT"></span>Thread Context

The *thread context* is the state preserved by Windows when switching threads. This is similar to the register context, except that there is some kernel-only processor state that is part of the register context but not the thread context. This extra state is available as registers during kernel-mode debugging.

The thread context is represented by the CONTEXT structure defined in ntddk.h. This structure is platform-dependent and its interpretation depends on the effective processor type. The methods [**GetThreadContext**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-getthreadcontext) and [**SetThreadContext**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugadvanced3-setthreadcontext) can be used to get and set the thread context.

 

