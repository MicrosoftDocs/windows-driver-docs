---
title: Windows kernel global variables
description: Kernel global variables.
ms.assetid: 1ea5c4e3-ed70-449c-a49e-b1e3c892e981
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows kernel global variables


Kernel global variables.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Variable</th>
<th>Declaration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Mm64BitPhysicalAddress</strong></td>
<td><code>PBOOLEAN Mm64BitPhysicalAddress</code>
<p>Declared in Wdm.h</p></td>
<td><p>Specifies whether the hardware and operating system support 64-bit physical addresses. Points to a value that is <strong>TRUE</strong> if the hardware and operating system support 64-bit physical addresses, and is <strong>FALSE</strong> otherwise.</p>
<p>For more information about how to use this variable in your driver, see <a href="performing-dma-in-64-bit-windows.md" data-raw-source="[Performing DMA in 64-Bit Windows](performing-dma-in-64-bit-windows.md)">Performing DMA in 64-Bit Windows</a>.</p></td>
</tr>
<tr class="even">
<td><strong>MmBadPointer</strong></td>
<td><code>PVOID MmBadPointer;</code>
<p>Declared in Wdm.h</p></td>
<td><p>A pointer to a memory location that is guaranteed to be invalid.</p>
<div class="alert">
<strong>Note</strong>  Starting with Windows 8.1, <strong>MmBadPointer</strong> is deprecated. Drivers should use the <a href="mm-bad-pointer.md" data-raw-source="[&lt;strong&gt;MM_BAD_POINTER&lt;/strong&gt;](mm-bad-pointer.md)"><strong>MM_BAD_POINTER</strong></a> macro instead.
</div>
<div>
 
</div>
<p>The operating system generates a bug check if the memory address that is specified by the <strong>MmBadPointer</strong> variable is accessed.</p>
<p>You can use <strong>MmBadPointer</strong> to debug your driver code. Set any uninitialized pointer variables to <strong>MmBadPointer</strong> to find the first time that your code tries to dereference an invalid pointer.</p>
<p>All addresses within PAGE_SIZE of <strong>MmBadPointer</strong> are guaranteed to be invalid. For example, if <em>Address</em> is a pointer and if <strong>MmBadPointer</strong> &lt;= <em>Address</em> &lt; <strong>MmBadPointer</strong> + PAGE_SIZE, attempts to access *<em>Address</em> causes the operating system to generate a bug check. <strong>MmBadPointer</strong> + PAGE_SIZE is not guaranteed to be invalid.</p></td>
</tr>
<tr class="odd">
<td><strong>PsInitialSystemProcess</strong></td>
<td><code>PEPROCESS PsInitialSystemProcess;</code>
<p>Declared in Ntddk.h</p></td>
<td><p>Points to the <a href="eprocess.md" data-raw-source="[&lt;strong&gt;EPROCESS&lt;/strong&gt;](eprocess.md)"><strong>EPROCESS</strong></a> structure for the system process.</p></td>
</tr>
<tr class="even">
<td><strong>NLS_MB_CODE_PAGE_TAG</strong></td>
<td><code>extern BOOLEAN  NLS_MB_CODE_PAGE_TAG;</code></td>
<td><p>Specifies whether a code page is a single-byte or multibyte code page.</p>
<p><strong>NLS_MB_CODE_PAGE_TAG</strong> is <strong>TRUE</strong> for multibyte code pages and <strong>FALSE</strong> for single-byte code pages.</p>
<p>NLS_MB_CODE_PAGE_TAG is reserved for system use. From user mode, call <a href="http://go.microsoft.com/fwlink/p/?linkid=121902" data-raw-source="[GetCPInfoEx](http://go.microsoft.com/fwlink/p/?linkid=121902)">GetCPInfoEx</a> instead.</p>
<p>When possible, your application should use Unicode instead of code pages.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**EPROCESS**](eprocess.md)  
[GetCPInfoEx](http://go.microsoft.com/fwlink/p/?linkid=121902)  
[**MM\_BAD\_POINTER**](mm-bad-pointer.md)  
[Performing DMA in 64-Bit Windows](performing-dma-in-64-bit-windows.md)  



