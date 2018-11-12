---
title: Choosing Which Public Symbols to Remove
description: Choosing Which Public Symbols to Remove
ms.assetid: 0de89f65-ebb5-4186-a6f9-6676f86a75f1
keywords: ["PDBCopy, removing public symbols", "symbols, AgeStore"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Choosing Which Public Symbols to Remove


PDBCopy supplies the -f and -F options so that you can remove an arbitrary set of public symbols from a stripped symbol file, leaving only those symbols that your audience needs to access in order to perform their debugging.

A common use of PDBCopy is to create a special version of your symbol file for use by Microsoft in its Online Crash Analysis (OCA) program. OCA can designate certain functions as *inert*, which means that if the function is found on the stack trace it is ignored. A function would typically be declared inert if it is simply a wrapper or "pass-through" function that performs no significant computations. If such a function is found on the stack in a failure analysis, it can be assumed that this function itself was not at fault, and at most it passed on invalid or corrupt data that it received from routines earlier on the stack. By ignoring such functions, OCA can better determine the actual cause of the error or corruption.

Naturally, any function that you wish to declare "inert" needs to be included in the public symbol table of the symbol file used by OCA. However, these are not the only functions that need to be included, as the following example shows.

Suppose that you write a Windows driver and you use PDBCopy to remove all public symbols from its symbol file, except for **FunctionOne** and **FunctionSix**, two inert functions. Your expectation is that if either **FunctionOne** or **FunctionSix** are found on the stack after a crash, they will be ignored by OCA. If any other part of your driver is on the stack, Microsoft will supply you with the corresponding memory address and you can use the address to debug your driver.

However, let us suppose that your driver occupies memory in the following layout:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Address</th>
<th align="left">Contents of memory</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1000</p></td>
<td align="left"><p>Base address of the module</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2000</p></td>
<td align="left"><p>Beginning of <strong>FunctionOne</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x203F</p></td>
<td align="left"><p>End of <strong>FunctionOne</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x3000</p></td>
<td align="left"><p>Beginning of <strong>FunctionSix</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x305F</p></td>
<td align="left"><p>End of <strong>FunctionSix</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7FFF</p></td>
<td align="left"><p>End of the module in memory</p></td>
</tr>
</tbody>
</table>

 

If the debugger finds an address on the stack, it selects the symbol with the next lower address. Since the public symbol table contains the address of each symbol but no size information, there is no way for the debugger to know if an address actually falls within the boundaries of any specific symbol.

Therefore, if a fault occurs at address 0x2031, the debugger run by Microsoft OCA correctly identifies the fault as lying within **FunctionOne**. Since this is an inert function, the debugger continues walking the stack to find the cause of the crash.

However, if a fault occurs at 0x2052, the debugger still matches this address to **FunctionOne**, even though it lies beyond the actual end of this function (0x203F).

Consequently, you must include in your stripped symbol file not only the functions you wish to expose, but also the symbols immediately following these functions. In this example, you would wish to expose **FunctionOne**, **FunctionTwo**, **FunctionSix**, and **FunctionSeven**:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Address</th>
<th align="left">Contents of memory</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x1000</p></td>
<td align="left"><p>Base address of the module</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2000</p></td>
<td align="left"><p>Beginning of <strong>FunctionOne</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x203F</p></td>
<td align="left"><p>End of <strong>FunctionOne</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x2040</p></td>
<td align="left"><p>Beginning of <strong>FunctionTwo</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3000</p></td>
<td align="left"><p>Beginning of <strong>FunctionSix</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x305F</p></td>
<td align="left"><p>End of <strong>FunctionSix</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x3060</p></td>
<td align="left"><p>Beginning of <strong>FunctionSeven</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>0x7FFF</p></td>
<td align="left"><p>End of the module in memory</p></td>
</tr>
</tbody>
</table>

 

If you include all four of these functions in the stripped symbol file, then the Microsoft OCA analysis will not mistakenly treat the address 0x2052 as part of **FunctionOne**. In this example it will assume that this address is part of **FunctionTwo**, but that is not important because you have not registered **FunctionTwo** with OCA as an inert function. The important thing is that the address 0x2052 is recognized as not falling within an inert function, and therefore OCA will recognize this as a meaningful fault within your driver and can inform you of the fault.

If you do not wish to publicize the names of the functions following each inert function, you can insert unimportant functions into your code following each inert function so that the names of these functions can be included in your public symbol file. Be sure to verify that these added functions do indeed follow your inert functions in your binary's address space, since some optimization routines may alter this, or even remove some functions entirely.

 

 





