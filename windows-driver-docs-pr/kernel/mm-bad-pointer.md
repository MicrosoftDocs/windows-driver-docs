---
title: Windows kernel macros
description: Windows kernel macros
ms.assetid: 91366400-3307-4F13-A839-50BA85B7F73E
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows kernel macros


The following table contains Windows kernel macros:

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Declared in</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong> macro returns the number of pages spanned by the virtual range defined by a virtual address and the size in bytes of a transfer request.</p>
<p><em>Va [in]</em></p>
<p><strong>PVOID</strong></p>
<p>Pointer to the virtual address that is the base of the range.</p>
<p><em>Size [in]</em></p>
<p><strong>ULONG</strong></p>
<p>Specifies the size in bytes of the transfer request.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG</strong></p>
<p><strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong> returns the number of pages spanned by the virtual range starting at <em>Va</em>.</p>
<p>Drivers that make DMA transfers call <strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong> to determine whether a transfer request must be split into a sequence of device DMA operations.</p>
<p>A driver can use the system-defined constant PAGE_SIZE to determine whether the number of bytes to be transferred is less than the virtual memory page size of the current platform.</p>
<p>Callers of <strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong> can be running at any IRQL. The caller must ensure that the specified parameters do not cause memory overflow.</p>
<p>Available starting with Windows 2000.</p></td>
</tr>
<tr class="even">
<td><strong>BYTE_OFFSET</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>BYTE_OFFSET</strong> macro takes a virtual address and returns the byte offset of that address within the page.</p>
<p><em>Va [in]</em></p>
<p><strong>PVOID</strong></p>
<p>Pointer to the virtual address.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG</strong></p>
<p><strong>BYTE_OFFSET</strong> returns the offset portion of the virtual address.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>BYTES_TO_PAGES</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>BYTES_TO_PAGES</strong> macro takes the size in bytes of the transfer request and calculates the number of pages required to contain the bytes.</p>
<p><em>Size [in]</em></p>
<p><strong>ULONG</strong></p>
<p>Specifies the size in bytes of the transfer request.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG</strong></p>
<p><strong>BYTES_TO_PAGES</strong> returns the number of pages required to contain the specified number of bytes.</p>
<p>The system-defined constant PAGE_SIZE can be used to determine whether a given length in bytes for a transfer is less than the virtual memory page size of the current platform.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>CONTAINING_RECORD</strong></td>
<td><p>Ntdef.h</p></td>
<td><p>The <strong>CONTAINING_RECORD</strong> macro returns the base address of an instance of a structure given the type of the structure and the address of a field within the containing structure.</p>
<p><em>Address [in]</em></p>
<p><strong>PCHAR</strong></p>
<p>A pointer to a field in an instance of a structure of type <em>Type</em>.</p>
<p><em>Type [in]</em></p>
<p><strong>TYPE</strong></p>
<p>The name of the type of the structure whose base address is to be returned.</p>
<p><em>Field [in]</em></p>
<p><strong>PCHAR</strong></p>
<p>The name of the field pointed to by <em>Address</em> and which is contained in a structure of type <em>Type</em>.</p>
<p><strong>Return value</strong></p>
<p><strong>PCHAR</strong></p>
<p>Returns the address of the base of the structure containing <em>Field</em>.</p>
<p>Called to determine the base address of a structure whose type is known when the caller has a pointer to a field inside such a structure. This macro is useful for symbolically accessing other fields in a structure of known type.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>IoSkipCurrentIrpStackLocation</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>IoSkipCurrentIrpStackLocation</strong> macro modifies the system&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659" data-raw-source="[&lt;strong&gt;IO_STACK_LOCATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550659)"><strong>IO_STACK_LOCATION</strong></a> array pointer, so that when the current driver calls the next-lower driver, that driver receives the same <strong>IO_STACK_LOCATION</strong> structure that the current driver received.</p>
<p><em>Irp [in, out]</em></p>
<p><strong>PIRP</strong></p>
<p>A pointer to the IRP.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>When your driver sends an IRP to the next-lower driver, your driver can call <strong>IoSkipCurrentIrpStackLocation</strong> if you do not intend to provide an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354" data-raw-source="[&lt;em&gt;IoCompletion&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548354)"><em>IoCompletion</em></a> routine (the address of which is stored in the driver&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659" data-raw-source="[&lt;strong&gt;IO_STACK_LOCATION&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff550659)"><strong>IO_STACK_LOCATION</strong></a> structure). If you call <strong>IoSkipCurrentIrpStackLocation</strong> before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548336)"><strong>IoCallDriver</strong></a>, the next-lower driver receives the same <strong>IO_STACK_LOCATION</strong> that your driver received.</p>
<p>If you intend to provide an <em>IoCompletion</em> routine for the IRP, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff548387" data-raw-source="[&lt;strong&gt;IoCopyCurrentIrpStackLocationToNext&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548387)"><strong>IoCopyCurrentIrpStackLocationToNext</strong></a> instead of <strong>IoSkipCurrentIrpStackLocation</strong>. If a badly written driver makes the mistake of calling <strong>IoSkipCurrentIrpStackLocation</strong> and then setting a completion routine, this driver might overwrite a completion routine set by the driver below it.</p>
<p>If the driver has pended an IRP, the driver should not be calling <strong>IoSkipCurrentIrpStackLocation</strong> before it passes the IRP to the next lower driver. If the driver calls <strong>IoSkipCurrentIrpStackLocation</strong> on a pended IRP before passing it to the next lower driver, the SL_PENDING_RETURNED flag is still set in the <strong>Control</strong> member of the I/O stack location for the next driver. Because the next driver owns that stack location and might modify it, it could potentially clear the pending flag. This situation might cause the operating system to issue a bug check or the processing of the IRP to never be completed.</p>
<p>Instead, a driver that has pended an IRP should call <strong>IoCopyCurrentIrpStackLocationToNext</strong> to set up a new stack location for the next lower driver before it calls <strong>IoCallDriver</strong>.</p>
<p>If your driver calls <strong>IoSkipCurrentIrpStackLocation</strong>, be careful not to modify the <strong>IO_STACK_LOCATION</strong> structure in a way that could unintentionally affect the lower driver or the system&#39;s behavior with respect to that driver. Examples include modifying the <strong>IO_STACK_LOCATION</strong> structure&#39;s <strong>Parameters</strong> union or calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422" data-raw-source="[&lt;strong&gt;IoMarkIrpPending&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549422)"><strong>IoMarkIrpPending</strong></a>.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>KeInitializeCallbackRecord</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>KeInitializeCallbackRecord</strong> macro initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551853" data-raw-source="[&lt;strong&gt;KBUGCHECK_CALLBACK_RECORD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551853)"><strong>KBUGCHECK_CALLBACK_RECORD</strong></a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff551873" data-raw-source="[&lt;strong&gt;KBUGCHECK_REASON_CALLBACK_RECORD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551873)"><strong>KBUGCHECK_REASON_CALLBACK_RECORD</strong></a> structure.</p>
<p><em>CallbackRecord [in]</em></p>
<p><strong>PKBUGCHECK_CALLBACK_RECORD</strong></p>
<p>Pointer to either a <strong>KBUGCHECK_CALLBACK_RECORD</strong> or a <strong>KBUGCHECK_REASON_CALLBACK_RECORD</strong> structure. The structure must be in resident memory, such as nonpaged pool.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>MM_BAD_POINTER</strong></td>
<td><p>Wdm.h</p></td>
<td><p>Your driver can use the <strong>MM_BAD_POINTER</strong> macro as a bad pointer value to assign to a pointer variable that is either uninitialized or no longer valid. An attempt to access the memory location pointed to by this invalid pointer variable will cause a bug check.</p>
<p>On many hardware platforms, address 0 (frequently represented as named constant <strong>NULL</strong>) is an invalid address, but driver developers should not assume that address 0 is universally invalid across all platforms. Setting uninitialized or invalid pointer variables to address 0 might not always guarantee that inappropriate accesses through these pointers will be detected.</p>
<p>In contrast, the value <strong>MM_BAD_POINTER</strong> is guaranteed to be an invalid address on every platform on which a driver runs.</p>
<p>On platforms on which address 0 is an invalid address, a driver that accesses address 0 at IRQL &lt; DISPATCH_LEVEL causes an exception (access violation) that can be inadvertently caught by a <code>try/except</code> statement. Thus, the driver&#39;s exception handling code might mask the invalid access and prevent it from being detected during debugging. However, an access of the <strong>MM_BAD_POINTER</strong> address is guaranteed to cause a bug check, which cannot be masked by an exception handler.</p>
<p>The following code example shows how to assign the value <strong>MM_BAD_POINTER</strong> to a pointer variable named <code>ptr</code>. The Ntdef.h header file defines the PUCHAR type to be a pointer to an <code>unsigned char</code>.</p>
<div class="code">
<code>cpp
PUCHAR ptr = (PUCHAR)MM_BAD_POINTER;  // Now <em>ptr is guaranteed to fault.</code>
</div>
<p>After <code>ptr</code> is set to <strong>MM_BAD_POINTER</strong>, an attempt to access the memory location pointed to by <code>ptr</code> will cause a bug check.</p>
<p>In fact, <strong>MM_BAD_POINTER</strong> is the base address of an entire page of invalid addresses. Therefore, any access of an address in the range <strong>MM_BAD_POINTER</strong> to (<strong>MM_BAD_POINTER</strong> + <strong>PAGE_SIZE</strong> - 1) will cause a bug check.</p>
<p>Starting with Windows 8.1, the <strong>MM_BAD_POINTER</strong> macro is defined in the Wdm.h header file. However, driver code that uses this macro definition can run in previous versions of Windows starting with Windows Vista.</p>
<p>Starting with Windows Vista, the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554494" data-raw-source="[&lt;strong&gt;MmBadPointer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554494)"><strong>MmBadPointer</strong></a> global variable is available as a pointer to a pointer value that is guaranteed to be an invalid address. However, starting with Windows 8.1, the use of <strong>MmBadPointer</strong> is deprecated, and you should update your drivers to use the <strong>MM_BAD_POINTER</strong> macro instead.</p>
Available starting with Windows 8.1. Compatible with previous versions of Windows starting with Windows Vista.</td>
</tr>
<tr class="even">
<td><strong>MmGetMdlByteCount</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmGetMdlByteCount</strong> macro returns the length, in bytes, of the buffer described by the specified MDL.</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff554414" data-raw-source="[&lt;strong&gt;MDL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554414)"><strong>MDL</strong></a> structure that describes the layout of a virtual memory buffer in physical memory. For more information, see <a href="using-mdls.md" data-raw-source="[Using MDLs](using-mdls.md)">Using MDLs</a>.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG</strong></p>
<p><strong>MmGetMdlByteCount</strong> returns the length, in bytes, of the buffer described by <em>Mdl</em>.</p>
<p>Callers of <strong>MmGetMdlByteCount</strong> can be running at any IRQL. Usually, callers are running at IRQL &lt;= DISPATCH_LEVEL.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>MmGetMdlByteOffset</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmGetMdlByteOffset</strong> macro returns the byte offset within the initial page of the buffer described by the given MDL.</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>Pointer to an MDL.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG</strong></p>
<p><strong>MmGetMdlByteOffset</strong> returns the offset in bytes.</p>
<p>Callers of <strong>MmGetMdlByteOffset</strong> can be running at any IRQL. Usually, callers are running at IRQL &lt;= DISPATCH_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>MmGetMdlPfnArray</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmGetMdlPfnArray</strong> macro returns a pointer to the beginning of the array of physical page numbers that are associated with a memory descriptor list (MDL).</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>A pointer to an MDL.</p>
<p><strong>Return value</strong></p>
<p><strong>PPFN_NUMBER</strong></p>
<p>A pointer to the beginning of the array of physical page numbers associated with the MDL. The number of entries in the array is <strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong>(<strong>MmGetMdlVirtualAddress</strong>(<em>Mdl</em>), <strong>MmGetMdlByteCount</strong>(<em>Mdl</em>)). Each array element is an integer value of type PFN_NUMBER, which is defined in Wdm.h as follows:</p>
<div class="code">
<code>cpp
typedef ULONG PFN_NUMBER, *PPFN_NUMBER;</code>
</div>
<div class="alert">
<strong>Note</strong>  Changing the contents of the array can cause subtle system problems that are difficult to diagnose. We recommend that you do not read or change the contents of this array.
</div>
<div>

</div>
<p>For pageable memory, the contents of the array are valid only for a buffer locked with <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664" data-raw-source="[&lt;strong&gt;MmProbeAndLockPages&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554664)"><strong>MmProbeAndLockPages</strong></a>. For nonpaged pool, the contents of the array are valid only for an MDL updated with <a href="https://msdn.microsoft.com/library/windows/hardware/ff554498" data-raw-source="[&lt;strong&gt;MmBuildMdlForNonPagedPool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554498)"><strong>MmBuildMdlForNonPagedPool</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554489" data-raw-source="[&lt;strong&gt;MmAllocatePagesForMdlEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554489)"><strong>MmAllocatePagesForMdlEx</strong></a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554482" data-raw-source="[&lt;strong&gt;MmAllocatePagesForMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554482)"><strong>MmAllocatePagesForMdl</strong></a>.</p>
<p>For more information about MDLs, see <a href="using-mdls.md" data-raw-source="[Using MDLs](using-mdls.md)">Using MDLs</a>.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>MmGetMdlVirtualAddress</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmGetMdlVirtualAddress</strong> macro returns the base virtual address of a buffer described by an MDL.</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>Pointer to an MDL that describes the buffer for which to return the initial virtual address.</p>
<p><strong>Return value</strong></p>
<p><strong>PVOID</strong></p>
<p><strong>MmGetMdlVirtualAddress</strong> returns the starting virtual address of the MDL.</p>
<p><strong>MmGetMdlVirtualAddress</strong> returns a virtual address that is not necessarily valid in the current thread context. Lower-level drivers should not attempt to use the returned virtual address to access memory, particularly user memory space.</p>
<p>The returned address, used as an index to a physical address entry in the MDL, can be input to <a href="https://msdn.microsoft.com/library/windows/hardware/ff554402" data-raw-source="[&lt;strong&gt;MapTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554402)"><strong>MapTransfer</strong></a>.</p>
<p>Callers of <strong>MmGetMdlVirtualAddress</strong> can be running at any IRQL. Usually, the caller is running at IRQL = DISPATCH_LEVEL because this routine is commonly called to obtain the <em>CurrentVa</em> parameter to <strong>MapTransfer</strong>.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>MmGetSystemAddressForMdlSafe</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmGetSystemAddressForMdlSafe</strong> macro returns a nonpaged system-space virtual address for the buffer that the specified MDL describes.</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>Pointer to a buffer whose corresponding base virtual address is to be mapped.</p>
<p><em>Priority [in]</em></p>
<p><strong>MM_PAGE_PRIORITY</strong></p>
<p>Specifies an <strong>MM_PAGE_PRIORITY</strong> value that indicates the importance of success under low available PTE conditions. Specify a priority value of <strong>LowPagePriority</strong>, <strong>NormalPagePriority</strong>, or <strong>HighPagePriority</strong>. Starting with Windows 8, the specified priority value can be bitwise-ORed with the <strong>MdlMappingNoWrite</strong> or <strong>MdlMappingNoExecute</strong> flags.</p>
<ul>
<li><p><strong>LowPagePriority</strong> indicates that the mapping request can fail if the system is fairly low on resources. An example of this situation is a noncritical network connection where the driver can handle the mapping failure.</p></li>
<li><p><strong>NormalPagePriority</strong> indicates that the mapping request can fail if the system is very low on resources. An example of this situation is a noncritical local file system request.</p></li>
<li><p><strong>HighPagePriority</strong> indicates that the mapping request must not fail unless the system is completely out of resources. An example of this situation is the paging file path in a driver.</p></li>
<li><p><strong>MdlMappingNoWrite</strong> indicates that the mapped physical pages are to be configured as no-write (read only) memory. Starting with Windows 8, this flag bit can be bitwise-ORed with the <strong>MM_PAGE_PRIORITY</strong> value to specify memory in which writes are disabled.</p></li>
<li><p><strong>MdlMappingNoExecute</strong> indicates that the mapped physical pages are to be configured as no-execute memory. Starting with Windows 8, this flag bit can be bitwise-ORed with the <strong>MM_PAGE_PRIORITY</strong> value to specify memory in which instruction execution is disabled. As a best practice, drivers written for Windows 8 and later versions of Windows should always specify no-execute memory unless executable memory is explicitly required.</p></li>
<li><p><strong>Return value</strong></p>
<p><strong>PVOID</strong></p>
<p><strong>MmGetSystemAddressForMdlSafe</strong> returns the base system-space virtual address that maps the physical pages that the specified MDL describes. If the pages are not already mapped to system address space and the attempt to map them fails, <strong>NULL</strong> is returned.</p></li>
</ul>
<p>This routine maps the physical pages that are described by the specified MDL into system address space, if they are not already mapped to system address space.</p>
<p>Drivers of programmed-I/O (PIO) devices call this routine to map a user-mode buffer, which is described by the MDL at <strong>Irp-&gt;MdlAddress</strong> and which is already mapped to a user-mode virtual address range, to a range in system address space.</p>
<p>On entry to this routine, the specified MDL must describe physical pages that are locked down. A locked-down MDL can be built by using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554664" data-raw-source="[&lt;strong&gt;MmProbeAndLockPages&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554664)"><strong>MmProbeAndLockPages</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff554498" data-raw-source="[&lt;strong&gt;MmBuildMdlForNonPagedPool&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554498)"><strong>MmBuildMdlForNonPagedPool</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548324" data-raw-source="[&lt;strong&gt;IoBuildPartialMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548324)"><strong>IoBuildPartialMdl</strong></a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff554489" data-raw-source="[&lt;strong&gt;MmAllocatePagesForMdlEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554489)"><strong>MmAllocatePagesForMdlEx</strong></a> routine.</p>
<p>When the system-address-space mapping that is returned by <strong>MmGetSystemAddressForMdlSafe</strong> is no longer needed, it must be released. The steps that are required to release the mapping depend on how the MDL was built. These are the four possible cases:</p>
<ul>
<li><p>If the MDL was built by a call to the <strong>MmProbeAndLockPages</strong> routine, it is not necessary to explicitly release the system-address-space mapping. Instead, a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556381" data-raw-source="[&lt;strong&gt;MmUnlockPages&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556381)"><strong>MmUnlockPages</strong></a> routine releases the mapping, if one was allocated.</p></li>
<li><p>If the MDL was built by a call to the <strong>MmBuildMdlForNonPagedPool</strong> routine, <strong>MmGetSystemAddressForMdlSafe</strong> reuses the existing system-address-space mapping instead of creating a new one. In this case, no cleanup is required (that is, unlocking and unmapping are not necessary).</p></li>
<li><p>If the MDL was built by a call to the <strong>IoBuildPartialMdl</strong> routine, the driver must call either the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554660" data-raw-source="[&lt;strong&gt;MmPrepareMdlForReuse&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554660)"><strong>MmPrepareMdlForReuse</strong></a> routine or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549126" data-raw-source="[&lt;strong&gt;IoFreeMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549126)"><strong>IoFreeMdl</strong></a> routine to release the system-address-space mapping.</p></li>
<li><p>If the MDL was built by a call to the <strong>MmAllocatePagesForMdlEx</strong> routine, the driver must call the <strong>MmUnmapLockedPages</strong> routine to release the system-address-space mapping. If <strong>MmGetSystemAddressForMdlSafe</strong> is called more than one time for an MDL, subsequent <strong>MmGetSystemAddressForMdlSafe</strong> calls simply return the mapping that was created by the first call. One call to <strong>MmUnmapLockedPages</strong> is sufficient to release this mapping.</p></li>
</ul>
<p>Starting with Windows 7 and Windows Server 2008 R2, it is not necessary to explicitly call <strong>MmUnmapLockedPages</strong> for an MDL that was created by <strong>MmAllocatePagesForMdlEx</strong>. Instead, a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554521" data-raw-source="[&lt;strong&gt;MmFreePagesFromMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554521)"><strong>MmFreePagesFromMdl</strong></a> routine releases the system-address-space mapping, if one was allocated.</p>
<p>To create a new system-address-space mapping, <strong>MmGetSystemAddressForMdlSafe</strong> calls <strong>MmMapLockedPagesSpecifyCache</strong> with the <em>CacheType</em> parameter set to <strong>MmCached</strong>. A driver that requires a cache type other than <strong>MmCached</strong> should call <strong>MmMapLockedPagesSpecifyCache</strong> directly instead of calling <strong>MmGetSystemAddressForMdlSafe</strong>. For more information about the <em>CacheType</em> parameter, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629" data-raw-source="[&lt;strong&gt;MmMapLockedPagesSpecifyCache&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554629)"><strong>MmMapLockedPagesSpecifyCache</strong></a>.</p>
<p>In a call to <strong>MmMapLockedPagesSpecifyCache</strong>, the specified cache type is used only if the pages that are described by the MDL do not already have a cache type associated with them. However, in nearly all cases, the pages already have an associated cache type, and this cache type is used by the new mapping. An exception to this rule is for pages that are allocated by <strong>MmAllocatePagesForMdl</strong>, which sets the cache type to <strong>MmCached</strong> regardless of the original cache type of the pages.</p>
<p>Only one thread at a time can safely call <strong>MmGetSystemAddressForMdlSafe</strong> for a particular MDL because this routine assumes that the calling thread owns the MDL. However, <strong>MmGetSystemAddressForMdlSafe</strong> can be called more than one time for the same MDL either by making all calls from the same thread or, if the calls are from multiple threads, by explicitly synchronizing the calls.</p>
<p>If a driver must split a request into smaller requests, the driver can allocate additional MDLs, or the driver can use the <strong>IoBuildPartialMdl</strong> routine.</p>
<p>The returned base address has the same offset as the virtual address in the MDL.</p>
<p>Windows 98 does not support <strong>MmGetSystemAddressForMdlSafe</strong>. Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554556" data-raw-source="[&lt;strong&gt;MmGetSystemAddressForMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554556)"><strong>MmGetSystemAddressForMdl</strong></a> instead.</p>
<p>Because this macro calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff554629" data-raw-source="[&lt;strong&gt;MmMapLockedPagesSpecifyCache&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554629)"><strong>MmMapLockedPagesSpecifyCache</strong></a>, using it may require linking to NtosKrnl.lib.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL &lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><strong>MmInitializeMdl</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmInitializeMdl</strong> macro initializes the header of an MDL.</p>
<p><em>MemoryDescriptorList [in]</em></p>
<p><strong>PMDL</strong></p>
<p>A pointer to the buffer to initialize as an MDL. For more information, see the following section.</p>
<p><em>BaseVa [in]</em></p>
<p><strong>PVOID</strong></p>
<p>A pointer to the base virtual address of a buffer.</p>
<p><em>Length [in]</em></p>
<p><strong>SIZE_T</strong></p>
<p>Specifies the length, in bytes, of the buffer to be described by the MDL. This routine supports a maximum buffer length of MAXULONG bytes.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The buffer that <em>MemoryDescriptorList</em> points to must be allocated in nonpaged memory. The size, in bytes, of this buffer must be at least <strong>sizeof</strong>(MDL) + <strong>sizeof</strong>(PFN_NUMBER)</em><strong>ADDRESS_AND_SIZE_TO_SPAN_PAGES</strong>(<em>BaseVa</em>, <em>Length</em>).</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL &lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="even">
<td><strong>MmPrepareMdlForReuse</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>MmPrepareMdlForReuse</strong> macro releases the resources that are associated with a partial MDL so that the MDL can be reused.</p>
<p><em>Mdl [in]</em></p>
<p><strong>PMDL</strong></p>
<p>A pointer to a partial MDL that is to be prepared for reuse.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>This macro is used by drivers that repeatedly use the same allocated MDL for the <em>TargetMdl</em> parameter in calls to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548324" data-raw-source="[&lt;strong&gt;IoBuildPartialMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548324)"><strong>IoBuildPartialMdl</strong></a> routine. If, in a call to <strong>MmPrepareMdlForReuse</strong>, the specified partial MDL has an associated mapping to system address space, <strong>MmPrepareMdlForReuse</strong> releases the mapping so that the MDL can be reused.</p>
<p><strong>MmPrepareMdlForReuse</strong> accepts only partial MDLs that are built by <strong>IoBuildPartialMdl</strong>. If <strong>MmPrepareMdlForReuse</strong> receives an MDL that is mapped to the system address space but was not built by <strong>IoBuildPartialMdl</strong>, <strong>MmPrepareMdlForReuse</strong> does not release the mapping, and, in checked builds, causes an assertion to fail.</p>
<p>For more information about partial MDLs, see <a href="using-mdls.md" data-raw-source="[Using MDLs](using-mdls.md)">Using MDLs</a>.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL &lt;= DISPATCH_LEVEL</p></td>
</tr>
<tr class="odd">
<td><strong>PAGE_ALIGN</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>PAGE_ALIGN</strong> macro returns a page-aligned virtual address for a given virtual address.</p>
<p><em>Va [in]</em></p>
<p><strong>PVOID</strong></p>
<p>Pointer to the virtual address.</p>
<p><strong>Return value</strong></p>
<p><strong>PVOID</strong></p>
<p><strong>PAGE_ALIGN</strong> returns a pointer to the page-aligned virtual address.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>PAGED_CODE</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>PAGED_CODE</strong> macro ensures that the calling thread is running at an IRQL that is low enough to permit paging.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>If the IRQL &gt; APC_LEVEL, the <strong>PAGED_CODE</strong> macro causes the system to ASSERT.</p>
<p>A call to this macro should be made at the beginning of every driver routine that either contains pageable code or accesses pageable code.</p>
<p>The <strong>PAGED_CODE</strong> macro checks the IRQL only at the point at which the driver code executes the macro. If the code subsequently raises the IRQL, the macro will not detect this change. Driver developers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff552808" data-raw-source="[Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808)">Static Driver Verifier</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff545448" data-raw-source="[Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448)">Driver Verifier</a> to detect when the IRQL is raised improperly during the execution of a driver routine.</p>
<p>The <strong>PAGED_CODE</strong> macro works only in checked builds.</p>
<p>Available starting with Windows 2000.</p></td>
</tr>
<tr class="odd">
<td><strong>PAGED_CODE_LOCKED</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>PAGED_CODE_LOCKED</strong> macro asserts that the currently running code section is pageable and must have been locked into memory before it was run.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>Pageable code must obey certain restrictions (such as IRQL &lt;= APC_LEVEL), unless it is locked into place. A pageable routine that must be locked into place to work correctly should begin with a call to <strong>PAGED_CODE_LOCKED</strong>.</p>
<p>For more information about locking a code section into place, see <a href="locking-pageable-code-or-data.md" data-raw-source="[Locking Pageable Code or Data](locking-pageable-code-or-data.md)">Locking Pageable Code or Data</a>.</p></td>
</tr>
<tr class="even">
<td><strong>PoSetDeviceBusy</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>PoSetDeviceBusy</strong> macro notifies the <a href="power-manager.md" data-raw-source="[power manager](power-manager.md)">power manager</a> that the device associated with <em>IdlePointer</em> is busy.</p>
<p><em>IdlePointer [in, out]</em></p>
<p><strong>PULONG</strong></p>
<p>Specifies a non-<strong>NULL</strong> idle pointer that was previously returned by <a href="https://msdn.microsoft.com/library/windows/hardware/ff559721" data-raw-source="[&lt;strong&gt;PoRegisterDeviceForIdleDetection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559721)"><strong>PoRegisterDeviceForIdleDetection</strong></a>. Note that <strong>PoRegisterDeviceForIdleDetection</strong> might return a <strong>NULL</strong> pointer. A caller of <strong>PoSetDeviceBusy</strong> must verify that the pointer is non-<strong>NULL</strong> before passing it to <strong>PoSetDeviceBusy</strong>.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<div class="alert">
<strong>Note</strong>   The <a href="https://msdn.microsoft.com/library/windows/hardware/ff559759" data-raw-source="[&lt;strong&gt;PoSetDeviceBusyEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff559759)"><strong>PoSetDeviceBusyEx</strong></a> routine is a direct replacement for the <strong>PoSetDeviceBusy</strong> macro. If you are writing new driver code for Windows Vista with Service Pack 1 (SP1) and later versions of Windows, call <strong>PoSetDeviceBusyEx</strong> instead of <strong>PoSetDeviceBusy</strong>.
</div>
<div>

</div>
<p>A driver uses <strong>PoSetDeviceBusy</strong> along with <strong>PoRegisterDeviceForIdleDetection</strong> to enable system idle detection for its device. If a device that is registered for idle detection becomes idle, the power manager sends an <a href="https://msdn.microsoft.com/library/windows/hardware/ff551744" data-raw-source="[&lt;strong&gt;IRP_MN_SET_POWER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551744)"><strong>IRP_MN_SET_POWER</strong></a> request to put the device in a requested sleep state.</p>
<p><strong>PoSetDeviceBusy</strong> reports that the device is busy, so that the power manager can restart its idle countdown. If the device is not powered up, <strong>PoSetDeviceBusy</strong> does not change its state. That is, it does not cause the system to send a power-on request.</p>
<p>A driver should call <strong>PoSetDeviceBusy</strong> on every I/O request.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>PsGetCurrentProcess</strong></td>
<td><p>Ntddk.h</p></td>
<td><p>Returns a pointer to the process of the current thread.</p>
<p><strong>Return value</strong></p>
<p>A pointer to an opaque process object.</p>
<div class="alert">
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>READ_REGISTER_BUFFER_ULONG64</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>READ_REGISTER_BUFFER_ULONG64</strong> macro reads a number of ULONG64 values from the specified register address into a buffer.</p>
<p><em>Register [in]</em></p>
<p><strong>PULONG64</strong></p>
<p>Pointer to the register, which must be a mapped range in memory space.</p>
<p><em>Buffer [out]</em></p>
<p><strong>PULONG64</strong></p>
<p>Pointer to a buffer that an array of ULONG64 values is read into.</p>
<p><em>Count [in]</em></p>
<p><strong>ULONG</strong></p>
<p>Specifies the number of ULONG64 values to be read into the buffer.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The size of the <em>Buffer</em> buffer must be large enough to contain at least the specified number of ULONG64 values.</p>
<p>Callers of the <strong>READ_REGISTER_BUFFER_ULONG64</strong> macro can be running at any IRQL, assuming that the <em>Buffer</em> buffer is resident and the <em>Register</em> register is resident, mapped device memory.</p>
<p>Available only in 64-bit versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>READ_REGISTER_ULONG64</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>READ_REGISTER_ULONG64</strong> macro reads a ULONG64 value from the specified register address.</p>
<p><em>volatile *Register [in]</em></p>
<p><strong>ULONG64</strong></p>
<p>Pointer to the register address, which must be a mapped range in memory space.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG64</strong></p>
<p><strong>READ_REGISTER_ULONG64</strong> returns the ULONG64 value that is read from the specified register address.</p>
<p>Callers of the <strong>READ_REGISTER_ULONG64</strong> macro can be running at any IRQL, assuming the <em>Register</em> address is resident, mapped device memory.</p>
<p>Available only in 64-bit versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>ROUND_TO_PAGES</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>ROUND_TO_PAGES</strong> macro takes a size in bytes and rounds it up to the next full page.</p>
<p><em>Size [in]</em></p>
<p><strong>ULONG_PTR</strong></p>
<p>Specifies the size in bytes to round up to a page multiple.</p>
<p><strong>Return value</strong></p>
<p><strong>ULONG_PTR</strong></p>
<p><strong>ROUND_TO_PAGES</strong> returns the input size rounded up to a multiple of the virtual memory page size for the current platform.</p>
<p>Callers of <strong>ROUND_TO_PAGES</strong> can be running at any IRQL. The caller must ensure that the supplied parameter cannot cause memory overflow.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>RtlEqualLuid</strong></td>
<td><p>Wdm.h</p></td>
<td><p><em></em></p>
<p><strong></strong></p>
<p></p>
<p><strong>Return value</strong></p>
<p><strong></strong></p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>RtlInitEmptyAnsiString</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlInitEmptyAnsiString</strong> macro initializes an empty counted ANSI string.</p>
<p><em>DestinationString [out]</em></p>
<p><strong>PANSI_STRING</strong></p>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff540605" data-raw-source="[&lt;strong&gt;ANSI_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540605)"><strong>ANSI_STRING</strong></a> structure to be initialized.</p>
<p><em>Buffer [in]</em></p>
<p><strong>PCHAR</strong></p>
<p>Pointer to a caller-allocated buffer to be used to contain a WCHAR string.</p>
<p><em>BufferSize [in]</em></p>
<p><strong>USHORT</strong></p>
<p>Length, in bytes, of the buffer that <em>Buffer</em> points to.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The members of the structure that the <em>DestinationString</em> parameter points to are initialized as follows.</p>
<ul>
<li><p><strong>Length</strong>. Zero.</p></li>
<li><p><strong>MaximumLength</strong>. <em>BufferSize</em>.</p></li>
<li><p><strong>Buffer</strong>. <em>SourceString</em>.</p></li>
</ul>
<p>To initialize a non-empty counted Unicode string, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff561918" data-raw-source="[&lt;strong&gt;RtlInitAnsiString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561918)"><strong>RtlInitAnsiString</strong></a>.</p>
<p>Available in Microsoft Windows XP and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>RtlInitEmptyUnicodeString</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlInitEmptyUnicodeString</strong> macro initializes an empty counted Unicode string.</p>
<p><em>DestinationString [out]</em></p>
<p><strong>PUNICODE_STRING</strong></p>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879" data-raw-source="[&lt;strong&gt;UNICODE_STRING&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564879)"><strong>UNICODE_STRING</strong></a> structure to be initialized.</p>
<p><em>Buffer [in]</em></p>
<p><strong>PWCHAR</strong></p>
<p>Pointer to a caller-allocated buffer to be used to contain a WCHAR string.</p>
<p><em>BufferSize [in]</em></p>
<p><strong>USHORT</strong></p>
<p>Length, in bytes, of the buffer that <em>Buffer</em> points to.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The members of the structure that the <em>DestinationString</em> parameters points to are initialized as follows.</p>
<ul>
<li><p><strong>Length</strong>. Zero.</p></li>
<li><p><strong>MaximumLength</strong>. <em>BufferSize</em>.</p></li>
<li><p><strong>Buffer</strong>. <em>SourceString</em>.</p></li>
</ul>
<p>To initialize a non-empty counted Unicode string, call <a href="https://msdn.microsoft.com/library/windows/hardware/ff561934" data-raw-source="[&lt;strong&gt;RtlInitUnicodeString&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561934)"><strong>RtlInitUnicodeString</strong></a>.</p>
<p>Available starting with Windows XP.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>RtlIsZeroLuid</strong></td>
<td><p>Ntddk.h</p></td>
<td><p>The <strong>RtlIsZeroLuid</strong> macro determines if the specified LUID is the zero LUID.</p>
<p><em>L1 [in]</em></p>
<p><strong>PLUID</strong></p>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554334" data-raw-source="[&lt;strong&gt;LUID&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554334)"><strong>LUID</strong></a> to check.</p>
<p><strong>Return value</strong></p>
<p><strong>BOOLEAN</strong></p>
<p><strong>RtlIsZeroLuid</strong> returns <strong>TRUE</strong> if <em>L1</em> is zero, and returns <strong>FALSE</strong> otherwise.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>RtlRetrieveUlong</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlRetrieveUlong</strong> macro retrieves a ULONG value from the source address, avoiding alignment faults. The destination address is assumed to be aligned.</p>
<p><em>DestinationAddress [out]</em></p>
<p><strong>PULONG</strong></p>
<p>Pointer to a ULONG-aligned location in which to store the ULONG value.</p>
<p><em>SourceAddress [in]</em></p>
<p><strong>PULONG</strong></p>
<p>Pointer to a location from which to retrieve the ULONG value.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>Callers of <strong>RtlRetrieveUlong</strong> can be running at any IRQL if the given addresses are in nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td><strong>RtlRetrieveUshort</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlRetrieveUshort</strong> macro retrieves a USHORT value from the source address, avoiding alignment faults.</p>
<p><em>DestinationAddress [out]</em></p>
<p><strong>PUSHORT</strong></p>
<p>Pointer to a USHORT-aligned location in which to store the value.</p>
<p><em>SourceAddress [in]</em></p>
<p><strong>PUSHORT</strong></p>
<p>Pointer to a location from which to retrieve the value.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>Callers of <strong>RtlRetrieveUshort</strong> can be running at any IRQL if the given addresses are in nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>RtlStoreUlong</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlStoreUlong</strong> macro stores a ULONG value at a particular address, avoiding alignment faults.</p>
<p><em>Address [out]</em></p>
<p><strong>PULONG</strong></p>
<p>A pointer to a location in which to store the specified ULONG value.</p>
<p><em>Value [in]</em></p>
<p><strong>ULONG</strong></p>
<p>Specifies a ULONG value to be stored.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The caller can be running at any IRQL if <em>Address</em> points to nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>RtlStoreUlonglong</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlStoreUlonglong</strong> macro stores a specified ULONGLONG value at a specified memory address, avoiding memory alignment faults.</p>
<p><em>Address [out]</em></p>
<p><strong>PULONGLONG</strong></p>
<p>A pointer to a location in which to store the specified ULONGLONG value.</p>
<p><em>Value [in]</em></p>
<p><strong>ULONGLONG</strong></p>
<p>The ULONGLONG value to be stored.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p><strong>RtlStoreUlonglong</strong> avoids memory alignment faults. If the address specified by <em>Address</em> is not aligned to the storage requirements of a ULONGLONG, <strong>RtlStoreUlonglong</strong> stores the bytes of <em>Value</em> beginning at the memory location (PUCHAR)<em>Address</em>.</p>
<p><strong>RtlStoreUlonglong</strong> runs at any IRQL if <em>Address</em> points to nonpaged pool; otherwise, it must run at IRQL &lt;= APC_LEVEL.</p>
<p>Available starting with Windows 2000.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>RtlStoreUlongPtr</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlStoreUlongPtr</strong> macro stores a specified ULONG_PTR value at a specified memory location, avoiding memory alignment faults.</p>
<p><em>Address [out]</em></p>
<p><strong>PULONG_PTR</strong></p>
<p>A pointer to a location in which to store the ULONG_PTR value.</p>
<p><em>Value [in]</em></p>
<p><strong>ULONG_PTR</strong></p>
<p>Specifies the ULONG_PTR value to be stored.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p><strong>RtlStoreUlongPtr</strong> avoids memory alignment faults. If the value of <em>Address</em> is not aligned to the storage requirements of a ULONG_PTR, <strong>RtlStoreUlongPtr</strong> stores the bytes of <em>Value</em> beginning at the memory location (PUCHAR)<em>Address</em>.</p>
<p><strong>RtlStoreUlongPtr</strong> runs at any IRQL if <em>Address</em> points to nonpaged pool; otherwise it must run at IRQL &lt;= APC_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>RtlStoreUshort</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>RtlStoreUshort</strong> macro stores a USHORT value at a particular address, avoiding alignment faults.</p>
<p><em>Address [out]</em></p>
<p><strong>PUSHORT</strong></p>
<p>A pointer to a location in which to store the specified USHORT value.</p>
<p><em>Value [in]</em></p>
<p><strong>USHORT</strong></p>
<p>Specifies a USHORT value to be stored.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The caller can be running at any IRQL if <em>Address</em> points to nonpaged pool. Otherwise, the caller must be running at IRQL &lt;= APC_LEVEL.</p>
<p>Available in Windows 2000 and later versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>WRITE_REGISTER_BUFFER_ULONG64</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>WRITE_REGISTER_BUFFER_ULONG64</strong> macro writes a number of ULONG64 values from a buffer to the specified register.</p>
<p><em>Register [in]</em></p>
<p><strong>PULONG64</strong></p>
<p>Pointer to the register, which must be a mapped range in memory space.</p>
<p><em>Buffer [in]</em></p>
<p><strong>PULONG64</strong></p>
<p>Pointer to a buffer that an array of ULONG64 values is to be written to.</p>
<p><em>Count [in]</em></p>
<p><strong>ULONG</strong></p>
<p>Specifies the number of ULONG64 values to be written to the register.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>The size of the <em>Buffer</em> buffer must be large enough to contain at least the specified number of ULONG64 values.</p>
<p>Callers of the <strong>WRITE_REGISTER_BUFFER_ULONG64</strong> macro can be running at any IRQL, assuming that the <em>Buffer</em> buffer is resident and the <em>Register</em> register is resident, mapped device memory.</p>
<p>Available only in 64-bit versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>WRITE_REGISTER_ULONG64</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>WRITE_REGISTER_ULONG64</strong> macro writes a ULONG64 value to the specified address.</p>
<p><em>volatile *Register [in]</em></p>
<p><strong>ULONG64</strong></p>
<p>Pointer to the register, which must be a mapped range in memory space.</p>
<p><em>Value [in]</em></p>
<p><strong>ULONG64</strong></p>
<p>Specifies a ULONG64 value to write to the register.</p>
<p><strong>Return value</strong></p>
<p><strong>VOID</strong></p>
<p>Callers of the <strong>WRITE_REGISTER_ULONG64</strong> macro can be running at any IRQL, assuming the <em>Register</em> register is resident, mapped device memory.</p>
<p>Available only in 64-bit versions of Windows.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="even">
<td><strong>ZwCurrentProcess</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>ZwCurrentProcess</strong> macro returns a handle to the current process.</p>
<p><strong>Return value</strong></p>
<p><strong>HANDLE</strong></p>
<p><strong>ZwCurrentProcess</strong> returns a special handle value that represents the current process.</p>
<p>The returned value is not a true handle, but it is a special value that always represents the current process.</p>
<p><strong>NtCurrentProcess</strong> and <strong>ZwCurrentProcess</strong> are two versions of the same Windows Native System Services routine. The <strong>NtCurrentProcess</strong> routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling <strong>ZwCurrentProcess</strong>.</p>
<p>For calls from kernel-mode drivers, the <strong>Nt<em>Xxx</em></strong> and <strong>Zw<em>Xxx</em></strong> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <strong>Nt<em>Xxx</em></strong> and <strong>Zw<em>Xxx</em></strong> versions of a routine, see <a href="using-nt-and-zw-versions-of-the-native-system-services-routines.md" data-raw-source="[Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md)">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>
<p>All supported operating systems.</p>
<p>IRQL: Any level</p></td>
</tr>
<tr class="odd">
<td><strong>ZwCurrentThread</strong></td>
<td><p>Wdm.h</p></td>
<td><p>The <strong>ZwCurrentThread</strong> macro returns a handle to the current thread.</p>
<p><strong>Return value</strong></p>
<p><strong>HANDLE</strong></p>
<p><strong>ZwCurrentThread</strong> returns a special handle value that represents the current thread.</p>
<p>The returned value is not a true handle, but it is a special value that always represents the current thread.</p>
<p><strong>NtCurrentThread</strong> and <strong>ZwCurrentThread</strong> are two versions of the same Windows Native System Services routine. The <strong>NtCurrentThread</strong> routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling the <strong>ZwCurrentThread</strong> routine.</p>
<p>For calls from kernel-mode drivers, the <strong>Nt<em>Xxx</em></strong> and <strong>Zw<em>Xxx</em></strong> versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the <strong>Nt<em>Xxx</em></strong> and <strong>Zw<em>Xxx</em></strong> versions of a routine, see <a href="using-nt-and-zw-versions-of-the-native-system-services-routines.md" data-raw-source="[Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md)">Using Nt and Zw Versions of the Native System Services Routines</a>.</p>
<p>All supported operating systems.</p>
<p>IRQL: Any level</p></td>
</tr>
</tbody>
</table>










