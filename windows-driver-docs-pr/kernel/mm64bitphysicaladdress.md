---
title: Windows kernel global variables
author: windows-driver-content
description: Kernel global variables.
MS-HAID:
- 'k106\_e5cdef6e-32bf-45ae-86b9-1f5a0c76f938.xml'
- 'kernel.mm64bitphysicaladdress'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1ea5c4e3-ed70-449c-a49e-b1e3c892e981
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
<p>For more information about how to use this variable in your driver, see [Performing DMA in 64-Bit Windows](performing-dma-in-64-bit-windows.md).</p></td>
</tr>
<tr class="even">
<td><strong>MmBadPointer</strong></td>
<td><code>PVOID MmBadPointer;</code>
<p>Declared in Wdm.h</p></td>
<td><p>A pointer to a memory location that is guaranteed to be invalid.</p>
<div class="alert">
<strong>Note</strong>  Starting with Windows 8.1, <strong>MmBadPointer</strong> is deprecated. Drivers should use the [<strong>MM_BAD_POINTER</strong>](mm-bad-pointer.md) macro instead.
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
<td><p>Points to the [<strong>EPROCESS</strong>](eprocess.md) structure for the system process.</p></td>
</tr>
<tr class="even">
<td><strong>NLS_MB_CODE_PAGE_TAG</strong></td>
<td><code>extern BOOLEAN  NLS_MB_CODE_PAGE_TAG;</code></td>
<td><p>Specifies whether a code page is a single-byte or multibyte code page.</p>
<p><strong>NLS_MB_CODE_PAGE_TAG</strong> is <strong>TRUE</strong> for multibyte code pages and <strong>FALSE</strong> for single-byte code pages.</p>
<p>NLS_MB_CODE_PAGE_TAG is reserved for system use. From user mode, call [GetCPInfoEx](http://go.microsoft.com/fwlink/p/?linkid=121902) instead.</p>
<p>When possible, your application should use Unicode instead of code pages.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**EPROCESS**](eprocess.md)  
[GetCPInfoEx](http://go.microsoft.com/fwlink/p/?linkid=121902)  
[**MM\_BAD\_POINTER**](mm-bad-pointer.md)  
[Performing DMA in 64-Bit Windows](performing-dma-in-64-bit-windows.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20kernel%20global%20variables%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


