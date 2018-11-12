---
title: P (Windows Debugger Glossary)
description: Glossary page - P
Robots: noindex, nofollow
ms.assetid: 4cfad26c-d8c0-4f80-aa54-b9cadbc84df3
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# P


<span id="page_table"></span><span id="PAGE_TABLE"></span>**page table**  
A process-specific table that maps virtual memory addresses to physical memory addresses.

<span id="page_table_entry__pte_"></span><span id="PAGE_TABLE_ENTRY__PTE_"></span>**Page Table Entry (PTE)**  
An item in the page table.

<span id="paged_pool"></span><span id="PAGED_POOL"></span>**paged pool**  
A portion of system memory that can be paged to disk.

Note that this term does not only refer to memory that actually has actually been paged out to the disk - it includes any memory that the operating system is permitted to page.

<span id="paging"></span><span id="PAGING"></span>**paging**  
A virtual memory operation in which the memory manager transfers pages from memory to disk when physical memory becomes full. A *page fault* occurs when a thread accesses a page that is not in memory.

<span id="parent_symbol"></span><span id="PARENT_SYMBOL"></span>**parent symbol**  
A *symbol* that is contains in other symbols, for example, a structure contains its member.

See also *child symbol*.

For more information, see [Scopes and Symbol Groups](scopes-and-symbol-groups.md).

<span id="primary_client"></span><span id="PRIMARY_CLIENT"></span>**primary client**  
A client object that has joined the current debugging session

For more information, see [Client Objects](client-objects.md).

<span id="process_server"></span><span id="PROCESS_SERVER"></span>**process server**  
An instance of the debugger engine acting as a proxy, listening for connections from smart client and performing memory, processor, or Windows operations as requested by these remote clients.

See also *debugging server*.

For more information, see [Process Servers (User Mode)](process-servers--user-mode-.md) and Process Server and Smart Client.

<span id="processor_breakpoint"></span><span id="PROCESSOR_BREAKPOINT"></span>**processor breakpoint**  
A breakpoint that is implemented by the processor. The debugger engine instructs the target's processor to insert this breakpoint.

See also software breakpoint. See also *software breakpoint*.

For more information, see [Using Breakpoints](using-breakpoints.md).

 

 





