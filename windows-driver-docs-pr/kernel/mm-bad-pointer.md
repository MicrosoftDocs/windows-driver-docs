---
title: Windows kernel macros
description: Windows kernel macros
ms.localizationpriority: High
ms.date: 10/17/2018
---

# Windows kernel macros


The following list contains Windows kernel macros:


## **ADDRESS_AND_SIZE_TO_SPAN_PAGES**

Defined in: Wdm.h

The **ADDRESS_AND_SIZE_TO_SPAN_PAGES** macro returns the number of pages spanned by the virtual range defined by a virtual address and the size in bytes of a transfer request.

_Va [in]_

**PVOID**

Pointer to the virtual address that is the base of the range.

_Size [in]_

**ULONG**

Specifies the size in bytes of the transfer request.

**Return value**

**ULONG**

**ADDRESS_AND_SIZE_TO_SPAN_PAGES** returns the number of pages spanned by the virtual range starting at _Va_.

Drivers that make DMA transfers call **ADDRESS_AND_SIZE_TO_SPAN_PAGES** to determine whether a transfer request must be split into a sequence of device DMA operations.

A driver can use the system-defined constant PAGE_SIZE to determine whether the number of bytes to be transferred is less than the virtual memory page size of the current platform.

Callers of **ADDRESS_AND_SIZE_TO_SPAN_PAGES** can be running at any IRQL. The caller must ensure that the specified parameters do not cause memory overflow.

Available starting with Windows 2000.


## **BYTE_OFFSET**

Defined in: Wdm.h

The **BYTE_OFFSET** macro takes a virtual address and returns the byte offset of that address within the page.

_Va [in]_

**PVOID**

Pointer to the virtual address.

**Return value**

**ULONG**

**BYTE_OFFSET** returns the offset portion of the virtual address.

Available starting with Windows 2000.

IRQL: Any level


## **BYTES_TO_PAGES**

Defined in: Wdm.h

The **BYTES_TO_PAGES** macro takes the size in bytes of the transfer request and calculates the number of pages required to contain the bytes.

_Size [in]_

**ULONG**

Specifies the size in bytes of the transfer request.

**Return value**

**ULONG**

**BYTES_TO_PAGES** returns the number of pages required to contain the specified number of bytes.

The system-defined constant PAGE_SIZE can be used to determine whether a given length in bytes for a transfer is less than the virtual memory page size of the current platform.

Available starting with Windows 2000.

IRQL: Any level


## **CONTAINING_RECORD**

Defined in: Ntdef.h

The **CONTAINING_RECORD** macro returns the base address of an instance of a structure given the type of the structure and the address of a field within the containing structure.

_Address [in]_

**PCHAR**

A pointer to a field in an instance of a structure of type _Type_.

_Type [in]_

**TYPE**

The name of the type of the structure whose base address is to be returned.

_Field [in]_

**PCHAR**

The name of the field pointed to by _Address_ and which is contained in a structure of type _Type_.

**Return value**

**PCHAR**

Returns the address of the base of the structure containing _Field_.

Called to determine the base address of a structure whose type is known when the caller has a pointer to a field inside such a structure. This macro is useful for symbolically accessing other fields in a structure of known type.

Available starting with Windows 2000.

IRQL: Any level


## **IoSkipCurrentIrpStackLocation**

Defined in: Wdm.h

\nThe **IoSkipCurrentIrpStackLocation** macro modifies the system's [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) array pointer, so that when the current driver calls the next-lower driver, that driver receives the same **IO_STACK_LOCATION** structure that the current driver received.

_Irp [in, out]_

**PIRP**

A pointer to the IRP.

**Return value**

**VOID**

When your driver sends an IRP to the next-lower driver, your driver can call **IoSkipCurrentIrpStackLocation** if you do not intend to provide an [_IoCompletion_](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine (the address of which is stored in the driver's [**IO_STACK_LOCATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_stack_location) structure). If you call **IoSkipCurrentIrpStackLocation** before calling [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver), the next-lower driver receives the same **IO_STACK_LOCATION** that your driver received.

If you intend to provide an _IoCompletion_ routine for the IRP, your driver should call [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) instead of **IoSkipCurrentIrpStackLocation**. If a badly written driver makes the mistake of calling **IoSkipCurrentIrpStackLocation** and then setting a completion routine, this driver might overwrite a completion routine set by the driver below it.

If the driver has pended an IRP, the driver should not be calling **IoSkipCurrentIrpStackLocation** before it passes the IRP to the next lower driver. If the driver calls **IoSkipCurrentIrpStackLocation** on a pended IRP before passing it to the next lower driver, the SL_PENDING_RETURNED flag is still set in the **Control** member of the I/O stack location for the next driver. Because the next driver owns that stack location and might modify it, it could potentially clear the pending flag. This situation might cause the operating system to issue a bug check or the processing of the IRP to never be completed.

Instead, a driver that has pended an IRP should call **IoCopyCurrentIrpStackLocationToNext** to set up a new stack location for the next lower driver before it calls **IoCallDriver**.

If your driver calls **IoSkipCurrentIrpStackLocation**, be careful not to modify the **IO_STACK_LOCATION** structure in a way that could unintentionally affect the lower driver or the system's behavior with respect to that driver. Examples include modifying the **IO_STACK_LOCATION** structure's **Parameters** union or calling [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending).

Available starting with Windows 2000.

IRQL: Any level


## **KeInitializeCallbackRecord**

Defined in: Wdm.h

The **KeInitializeCallbackRecord** macro initializes a [**KBUGCHECK_CALLBACK_RECORD**](./eprocess.md) or [**KBUGCHECK_REASON_CALLBACK_RECORD**](./eprocess.md) structure.

_CallbackRecord [in]_

**PKBUGCHECK_CALLBACK_RECORD**

Pointer to either a **KBUGCHECK_CALLBACK_RECORD** or a **KBUGCHECK_REASON_CALLBACK_RECORD** structure. The structure must be in resident memory, such as nonpaged pool.

**Return value**

**VOID**

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **MM_BAD_POINTER**

Defined in: Wdm.h

Your driver can use the **MM_BAD_POINTER** macro as a bad pointer value to assign to a pointer variable that is either uninitialized or no longer valid. An attempt to access the memory location pointed to by this invalid pointer variable will cause a bug check.

On many hardware platforms, address 0 (frequently represented as named constant **NULL**) is an invalid address, but driver developers should not assume that address 0 is universally invalid across all platforms. Setting uninitialized or invalid pointer variables to address 0 might not always guarantee that inappropriate accesses through these pointers will be detected.

In contrast, the value **MM_BAD_POINTER** is guaranteed to be an invalid address on every platform on which a driver runs.

On platforms on which address 0 is an invalid address, a driver that accesses address 0 at IRQL < DISPATCH_LEVEL causes an exception (access violation) that can be inadvertently caught by a `try/except` statement. Thus, the driver's exception handling code might mask the invalid access and prevent it from being detected during debugging. However, an access of the **MM_BAD_POINTER** address is guaranteed to cause a bug check, which cannot be masked by an exception handler.

The following code example shows how to assign the value **MM_BAD_POINTER** to a pointer variable named `ptr`. The Ntdef.h header file defines the PUCHAR type to be a pointer to an `unsigned char`.

`PUCHAR ptr = (PUCHAR)MM_BAD_POINTER; // Now _ptr is guaranteed to fault._`

After `ptr` is set to **MM_BAD_POINTER**, an attempt to access the memory location pointed to by `ptr` will cause a bug check.

In fact, **MM_BAD_POINTER** is the base address of an entire page of invalid addresses. Therefore, any access of an address in the range **MM_BAD_POINTER** to (**MM_BAD_POINTER** + **PAGE_SIZE** - 1) will cause a bug check.

Starting with Windows 8.1, the **MM_BAD_POINTER** macro is defined in the Wdm.h header file. However, driver code that uses this macro definition can run in previous versions of Windows starting with Windows Vista.

Starting with Windows Vista, the [**MmBadPointer**](./mm64bitphysicaladdress.md) global variable is available as a pointer to a pointer value that is guaranteed to be an invalid address. However, starting with Windows 8.1, the use of **MmBadPointer** is deprecated, and you should update your drivers to use the **MM_BAD_POINTER** macro instead.

Available starting with Windows 8.1\. Compatible with previous versions of Windows starting with Windows Vista._


## **MmGetMdlByteCount**

Defined in: Wdm.h

The **MmGetMdlByteCount** macro returns the length, in bytes, of the buffer described by the specified MDL.

_Mdl [in]_

**PMDL**

A pointer to an [**MDL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_mdl) structure that describes the layout of a virtual memory buffer in physical memory. For more information, see [Using MDLs](using-mdls.md).

**Return value**

**ULONG**

**MmGetMdlByteCount** returns the length, in bytes, of the buffer described by _Mdl_.

Callers of **MmGetMdlByteCount** can be running at any IRQL. Usually, callers are running at IRQL <= DISPATCH_LEVEL.

Available starting with Windows 2000.

IRQL: Any level


## **MmGetMdlByteOffset**

Defined in: Wdm.h

The **MmGetMdlByteOffset** macro returns the byte offset within the initial page of the buffer described by the given MDL.

_Mdl [in]_

**PMDL**

Pointer to an MDL.

**Return value**

**ULONG**

**MmGetMdlByteOffset** returns the offset in bytes.

Callers of **MmGetMdlByteOffset** can be running at any IRQL. Usually, callers are running at IRQL <= DISPATCH_LEVEL.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **MmGetMdlPfnArray**

Defined in: Wdm.h

The **MmGetMdlPfnArray** macro returns a pointer to the beginning of the array of physical page numbers that are associated with a memory descriptor list (MDL).

_Mdl [in]_

**PMDL**

A pointer to an MDL.

**Return value**

**PPFN_NUMBER**

A pointer to the beginning of the array of physical page numbers associated with the MDL. The number of entries in the array is **ADDRESS_AND_SIZE_TO_SPAN_PAGES**(**MmGetMdlVirtualAddress**(_Mdl_), **MmGetMdlByteCount**(_Mdl_)). Each array element is an integer value of type PFN_NUMBER, which is Defined in: Wdm.h as follows:

`cpp typedef ULONG PFN_NUMBER, *PPFN_NUMBER;`

**Note** Changing the contents of the array can cause subtle system problems that are difficult to diagnose. We recommend that you do not read or change the contents of this array.

For pageable memory, the contents of the array are valid only for a buffer locked with [**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages). For nonpaged pool, the contents of the array are valid only for an MDL updated with [**MmBuildMdlForNonPagedPool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmbuildmdlfornonpagedpool), [**MmAllocatePagesForMdlEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatepagesformdlex), or [**MmAllocatePagesForMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatepagesformdl).

For more information about MDLs, see [Using MDLs](using-mdls.md).

Available starting with Windows 2000.

IRQL: Any level


## **MmGetMdlVirtualAddress**

Defined in: Wdm.h

The **MmGetMdlVirtualAddress** macro returns the base virtual address of a buffer described by an MDL.

_Mdl [in]_

**PMDL**

Pointer to an MDL that describes the buffer for which to return the initial virtual address.

**Return value**

**PVOID**

**MmGetMdlVirtualAddress** returns the starting virtual address of the MDL.

**MmGetMdlVirtualAddress** returns a virtual address that is not necessarily valid in the current thread context. Lower-level drivers should not attempt to use the returned virtual address to access memory, particularly user memory space.

The returned address, used as an index to a physical address entry in the MDL, can be input to [**MapTransfer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer).

Callers of **MmGetMdlVirtualAddress** can be running at any IRQL. Usually, the caller is running at IRQL = DISPATCH_LEVEL because this routine is commonly called to obtain the _CurrentVa_ parameter to **MapTransfer**.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **MmGetSystemAddressForMdlSafe**

Defined in: Wdm.h

The **MmGetSystemAddressForMdlSafe** macro returns a nonpaged system-space virtual address for the buffer that the specified MDL describes.

_Mdl [in]_

**PMDL**

Pointer to a buffer whose corresponding base virtual address is to be mapped.

_Priority [in]_

**MM_PAGE_PRIORITY**

Specifies an **MM_PAGE_PRIORITY** value that indicates the importance of success under low available PTE conditions. Specify a priority value of **LowPagePriority**, **NormalPagePriority**, or **HighPagePriority**. Starting with Windows 8, the specified priority value can be bitwise-ORed with the **MdlMappingNoWrite** or **MdlMappingNoExecute** flags.

*   **LowPagePriority** indicates that the mapping request can fail if the system is fairly low on resources. An example of this situation is a noncritical network connection where the driver can handle the mapping failure.

*   **NormalPagePriority** indicates that the mapping request can fail if the system is very low on resources. An example of this situation is a noncritical local file system request.

*   **HighPagePriority** indicates that the mapping request must not fail unless the system is completely out of resources. An example of this situation is the paging file path in a driver.

*   **MdlMappingNoWrite** indicates that the mapped physical pages are to be configured as no-write (read only) memory. Starting with Windows 8, this flag bit can be bitwise-ORed with the **MM_PAGE_PRIORITY** value to specify memory in which writes are disabled.

*   **MdlMappingNoExecute** indicates that the mapped physical pages are to be configured as no-execute memory. Starting with Windows 8, this flag bit can be bitwise-ORed with the **MM_PAGE_PRIORITY** value to specify memory in which instruction execution is disabled. As a best practice, drivers written for Windows 8 and later versions of Windows should always specify no-execute memory unless executable memory is explicitly required.

*   **Return value**

    **PVOID**

    **MmGetSystemAddressForMdlSafe** returns the base system-space virtual address that maps the physical pages that the specified MDL describes. If the pages are not already mapped to system address space and the attempt to map them fails, **NULL** is returned.

This routine maps the physical pages that are described by the specified MDL into system address space, if they are not already mapped to system address space.

Drivers of programmed-I/O (PIO) devices call this routine to map a user-mode buffer, which is described by the MDL at **Irp->MdlAddress** and which is already mapped to a user-mode virtual address range, to a range in system address space.

On entry to this routine, the specified MDL must describe physical pages that are locked down. A locked-down MDL can be built by using the [**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages), [**MmBuildMdlForNonPagedPool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmbuildmdlfornonpagedpool), [**IoBuildPartialMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildpartialmdl), or [**MmAllocatePagesForMdlEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatepagesformdlex) routine.

When the system-address-space mapping that is returned by **MmGetSystemAddressForMdlSafe** is no longer needed, it must be released. The steps that are required to release the mapping depend on how the MDL was built. These are the four possible cases:

*   If the MDL was built by a call to the **MmProbeAndLockPages** routine, it is not necessary to explicitly release the system-address-space mapping. Instead, a call to the [**MmUnlockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpages) routine releases the mapping, if one was allocated.

*   If the MDL was built by a call to the **MmBuildMdlForNonPagedPool** routine, **MmGetSystemAddressForMdlSafe** reuses the existing system-address-space mapping instead of creating a new one. In this case, no cleanup is required (that is, unlocking and unmapping are not necessary).

*   If the MDL was built by a call to the **IoBuildPartialMdl** routine, the driver must call either the **MmPrepareMdlForReuse** routine or the [**IoFreeMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreemdl) routine to release the system-address-space mapping.

*   If the MDL was built by a call to the **MmAllocatePagesForMdlEx** routine, the driver must call the **MmUnmapLockedPages** routine to release the system-address-space mapping. If **MmGetSystemAddressForMdlSafe** is called more than one time for an MDL, subsequent **MmGetSystemAddressForMdlSafe** calls simply return the mapping that was created by the first call. One call to **MmUnmapLockedPages** is sufficient to release this mapping.

Starting with Windows 7 and Windows Server 2008 R2, it is not necessary to explicitly call **MmUnmapLockedPages** for an MDL that was created by **MmAllocatePagesForMdlEx**. Instead, a call to the [**MmFreePagesFromMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreepagesfrommdl) routine releases the system-address-space mapping, if one was allocated.

To create a new system-address-space mapping, **MmGetSystemAddressForMdlSafe** calls **MmMapLockedPagesSpecifyCache** with the _CacheType_ parameter set to **MmCached**. A driver that requires a cache type other than **MmCached** should call **MmMapLockedPagesSpecifyCache** directly instead of calling **MmGetSystemAddressForMdlSafe**. For more information about the _CacheType_ parameter, see [**MmMapLockedPagesSpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache).

In a call to **MmMapLockedPagesSpecifyCache**, the specified cache type is used only if the pages that are described by the MDL do not already have a cache type associated with them. However, in nearly all cases, the pages already have an associated cache type, and this cache type is used by the new mapping. An exception to this rule is for pages that are allocated by **MmAllocatePagesForMdl**, which sets the cache type to **MmCached** regardless of the original cache type of the pages.

Only one thread at a time can safely call **MmGetSystemAddressForMdlSafe** for a particular MDL because this routine assumes that the calling thread owns the MDL. However, **MmGetSystemAddressForMdlSafe** can be called more than one time for the same MDL either by making all calls from the same thread or, if the calls are from multiple threads, by explicitly synchronizing the calls.

If a driver must split a request into smaller requests, the driver can allocate additional MDLs, or the driver can use the **IoBuildPartialMdl** routine.

The returned base address has the same offset as the virtual address in the MDL.

Windows 98 does not support **MmGetSystemAddressForMdlSafe**. Use [**MmGetSystemAddressForMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdl) instead.

Because this macro calls [**MmMapLockedPagesSpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache), using it may require linking to NtosKrnl.lib.

Available starting with Windows 2000.

IRQL <= DISPATCH_LEVEL


## **MmInitializeMdl**

Defined in: Wdm.h

The **MmInitializeMdl** macro initializes the header of an MDL.

_MemoryDescriptorList [in]_

**PMDL**

A pointer to the buffer to initialize as an MDL. For more information, see the following section.

_BaseVa [in]_

**PVOID**

A pointer to the base virtual address of a buffer.

_Length [in]_

**SIZE_T**

Specifies the length, in bytes, of the buffer to be described by the MDL. This routine supports a maximum buffer length of MAXULONG bytes.

**Return value**

**VOID**

The buffer that _MemoryDescriptorList_ points to must be allocated in nonpaged memory. The size, in bytes, of this buffer must be at least **sizeof**(MDL) + **sizeof**(PFN_NUMBER) * **ADDRESS_AND_SIZE_TO_SPAN_PAGES**(_BaseVa_, _Length_).

Available in Windows 2000 and later versions of Windows.

IRQL <= DISPATCH_LEVEL


## **MmPrepareMdlForReuse**

Defined in: Wdm.h

The **MmPrepareMdlForReuse** macro releases the resources that are associated with a partial MDL so that the MDL can be reused.

_Mdl [in]_

**PMDL**

A pointer to a partial MDL that is to be prepared for reuse.

**Return value**

**VOID**

This macro is used by drivers that repeatedly use the same allocated MDL for the _TargetMdl_ parameter in calls to the [**IoBuildPartialMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildpartialmdl) routine. If, in a call to **MmPrepareMdlForReuse**, the specified partial MDL has an associated mapping to system address space, **MmPrepareMdlForReuse** releases the mapping so that the MDL can be reused.

**MmPrepareMdlForReuse** accepts only partial MDLs that are built by **IoBuildPartialMdl**. If **MmPrepareMdlForReuse** receives an MDL that is mapped to the system address space but was not built by **IoBuildPartialMdl**, **MmPrepareMdlForReuse** does not release the mapping.

For more information about partial MDLs, see [Using MDLs](using-mdls.md).

Available in Windows 2000 and later versions of Windows.

IRQL <= DISPATCH_LEVEL


## **PAGE_ALIGN**

Defined in: Wdm.h

The **PAGE_ALIGN** macro returns a page-aligned virtual address for a given virtual address.

_Va [in]_

**PVOID**

Pointer to the virtual address.

**Return value**

**PVOID**

**PAGE_ALIGN** returns a pointer to the page-aligned virtual address.

Available starting with Windows 2000.

IRQL: Any level


## **PAGED_CODE**

Defined in: Wdm.h

The **PAGED_CODE** macro ensures that the calling thread is running at an IRQL that is low enough to permit paging.

**Return value**

**VOID**

If the IRQL > APC_LEVEL, the **PAGED_CODE** macro causes the system to ASSERT.

A call to this macro should be made at the beginning of every driver routine that either contains pageable code or accesses pageable code.

The **PAGED_CODE** macro checks the IRQL only at the point at which the driver code executes the macro. If the code subsequently raises the IRQL, the macro will not detect this change. Driver developers should use [Static Driver Verifier](../devtest/static-driver-verifier.md) and [Driver Verifier](../devtest/driver-verifier.md) to detect when the IRQL is raised improperly during the execution of a driver routine.

The **PAGED_CODE** macro works only in checked builds.

Available starting with Windows 2000.


## **PAGED_CODE_LOCKED**

Defined in: Wdm.h

The **PAGED_CODE_LOCKED** macro asserts that the currently running code section is pageable and must have been locked into memory before it was run.

**Return value**

**VOID**

Pageable code must obey certain restrictions (such as IRQL <= APC_LEVEL), unless it is locked into place. A pageable routine that must be locked into place to work correctly should begin with a call to **PAGED_CODE_LOCKED**.

For more information about locking a code section into place, see [Locking Pageable Code or Data](locking-pageable-code-or-data.md).


## **PoSetDeviceBusy**

Defined in: Wdm.h

The **PoSetDeviceBusy** macro notifies the [power manager](power-manager.md) that the device associated with _IdlePointer_ is busy.

_IdlePointer [in, out]_

**PULONG**

Specifies a non-**NULL** idle pointer that was previously returned by [**PoRegisterDeviceForIdleDetection**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-poregisterdeviceforidledetection). Note that **PoRegisterDeviceForIdleDetection** might return a **NULL** pointer. A caller of **PoSetDeviceBusy** must verify that the pointer is non-**NULL** before passing it to **PoSetDeviceBusy**.

**Return value**

**VOID**

**Note** The [**PoSetDeviceBusyEx**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-posetdevicebusyex) routine is a direct replacement for the **PoSetDeviceBusy** macro. If you are writing new driver code for Windows Vista with Service Pack 1 (SP1) and later versions of Windows, call **PoSetDeviceBusyEx** instead of **PoSetDeviceBusy**.

A driver uses **PoSetDeviceBusy** along with **PoRegisterDeviceForIdleDetection** to enable system idle detection for its device. If a device that is registered for idle detection becomes idle, the power manager sends an [**IRP_MN_SET_POWER**](./irp-mn-set-power.md) request to put the device in a requested sleep state.

**PoSetDeviceBusy** reports that the device is busy, so that the power manager can restart its idle countdown. If the device is not powered up, **PoSetDeviceBusy** does not change its state. That is, it does not cause the system to send a power-on request.

A driver should call **PoSetDeviceBusy** on every I/O request.

Available starting with Windows 2000.

IRQL: Any level


## **PsGetCurrentProcess**

Defined in: Ntddk.h

Returns a pointer to the process of the current thread.

**Return value**

**PEPROCESS**

A pointer to an opaque process object.



Available starting with Windows 2000.

IRQL: Any level


## **READ_REGISTER_BUFFER_ULONG64**

Defined in: Wdm.h

The **READ_REGISTER_BUFFER_ULONG64** macro reads a number of ULONG64 values from the specified register address into a buffer.

_Register [in]_

**PULONG64**

Pointer to the register, which must be a mapped range in memory space.

_Buffer [out]_

**PULONG64**

Pointer to a buffer that an array of ULONG64 values is read into.

_Count [in]_

**ULONG**

Specifies the number of ULONG64 values to be read into the buffer.

**Return value**

**VOID**

The size of the _Buffer_ buffer must be large enough to contain at least the specified number of ULONG64 values.

Callers of the **READ_REGISTER_BUFFER_ULONG64** macro can be running at any IRQL, assuming that the _Buffer_ buffer is resident and the _Register_ register is resident, mapped device memory.

Available only in 64-bit versions of Windows.

IRQL: Any level


## **READ_REGISTER_ULONG64**

Defined in: Wdm.h

The **READ_REGISTER_ULONG64** macro reads a ULONG64 value from the specified register address.

_volatile *Register [in]_

**ULONG64**

Pointer to the register address, which must be a mapped range in memory space.

**Return value**

**ULONG64**

**READ_REGISTER_ULONG64** returns the ULONG64 value that is read from the specified register address.

Callers of the **READ_REGISTER_ULONG64** macro can be running at any IRQL, assuming the _Register_ address is resident, mapped device memory.

Available only in 64-bit versions of Windows.

IRQL: Any level


## **ROUND_TO_PAGES**

Defined in: Wdm.h

The **ROUND_TO_PAGES** macro takes a size in bytes and rounds it up to the next full page.

_Size [in]_

**ULONG_PTR**

Specifies the size in bytes to round up to a page multiple.

**Return value**

**ULONG_PTR**

**ROUND_TO_PAGES** returns the input size rounded up to a multiple of the virtual memory page size for the current platform.

Callers of **ROUND_TO_PAGES** can be running at any IRQL. The caller must ensure that the supplied parameter cannot cause memory overflow.

IRQL: Any level


## **RtlEqualLuid**

Defined in: Wdm.h

**Return value**

Available starting with Windows 2000.

IRQL: Any level


## **RtlInitEmptyAnsiString**

Defined in: Wdm.h

The **RtlInitEmptyAnsiString** macro initializes an empty counted ANSI string.

_DestinationString [out]_

**PANSI_STRING**

Pointer to the [**ANSI_STRING**](/windows/win32/api/ntdef/ns-ntdef-string) structure to be initialized.

_Buffer [in]_

**PCHAR**

Pointer to a caller-allocated buffer to be used to contain a WCHAR string.

_BufferSize [in]_

**USHORT**

Length, in bytes, of the buffer that _Buffer_ points to.

**Return value**

**VOID**

The members of the structure that the _DestinationString_ parameter points to are initialized as follows.

*   **Length**. Zero.

*   **MaximumLength**. _BufferSize_.

*   **Buffer**. _SourceString_.

To initialize a non-empty counted Unicode string, call [**RtlInitAnsiString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlinitansistring).

Available in Microsoft Windows XP and later versions of Windows.

IRQL: Any level


## **RtlInitEmptyUnicodeString**

Defined in: Wdm.h

The **RtlInitEmptyUnicodeString** macro initializes an empty counted Unicode string.

_DestinationString [out]_

**PUNICODE_STRING**

Pointer to the [**UNICODE_STRING**](/windows-hardware/drivers/ddi/wudfwdm/ns-wudfwdm-_unicode_string) structure to be initialized.

_Buffer [in]_

**PWCHAR**

Pointer to a caller-allocated buffer to be used to contain a WCHAR string.

_BufferSize [in]_

**USHORT**

Length, in bytes, of the buffer that _Buffer_ points to.

**Return value**

**VOID**

The members of the structure that the _DestinationString_ parameters points to are initialized as follows.

*   **Length**. Zero.

*   **MaximumLength**. _BufferSize_.

*   **Buffer**. _SourceString_.

To initialize a non-empty counted Unicode string, call [**RtlInitUnicodeString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlinitunicodestring).

Available starting with Windows XP.

IRQL: Any level


## **RtlIsZeroLuid**

Defined in: Ntddk.h

The **RtlIsZeroLuid** macro determines if the specified LUID is the zero LUID.

_L1 [in]_

**PLUID**

Specifies the [**LUID**](/windows/win32/api/ntdef/ns-ntdef-luid) to check.

**Return value**

**BOOLEAN**

**RtlIsZeroLuid** returns **TRUE** if _L1_ is zero, and returns **FALSE** otherwise.

IRQL: Any level


## **RtlRetrieveUlong**

Defined in: Wdm.h

The **RtlRetrieveUlong** macro retrieves a ULONG value from the source address, avoiding alignment faults. The destination address is assumed to be aligned.

_DestinationAddress [out]_

**PULONG**

Pointer to a ULONG-aligned location in which to store the ULONG value.

_SourceAddress [in]_

**PULONG**

Pointer to a location from which to retrieve the ULONG value.

**Return value**

**VOID**

Callers of **RtlRetrieveUlong** can be running at any IRQL if the given addresses are in nonpaged pool. Otherwise, the caller must be running at IRQL <= APC_LEVEL.

Available in Windows 2000 and later versions of Windows.


## **RtlRetrieveUshort**

Defined in: Wdm.h

The **RtlRetrieveUshort** macro retrieves a USHORT value from the source address, avoiding alignment faults.

_DestinationAddress [out]_

**PUSHORT**

Pointer to a USHORT-aligned location in which to store the value.

_SourceAddress [in]_

**PUSHORT**

Pointer to a location from which to retrieve the value.

**Return value**

**VOID**

Callers of **RtlRetrieveUshort** can be running at any IRQL if the given addresses are in nonpaged pool. Otherwise, the caller must be running at IRQL <= APC_LEVEL.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **RtlStoreUlong**

Defined in: Wdm.h

The **RtlStoreUlong** macro stores a ULONG value at a particular address, avoiding alignment faults.

_Address [out]_

**PULONG**

A pointer to a location in which to store the specified ULONG value.

_Value [in]_

**ULONG**

Specifies a ULONG value to be stored.

**Return value**

**VOID**

The caller can be running at any IRQL if _Address_ points to nonpaged pool. Otherwise, the caller must be running at IRQL <= APC_LEVEL.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **RtlStoreUlonglong**

Defined in: Wdm.h

The **RtlStoreUlonglong** macro stores a specified ULONGLONG value at a specified memory address, avoiding memory alignment faults.

_Address [out]_

**PULONGLONG**

A pointer to a location in which to store the specified ULONGLONG value.

_Value [in]_

**ULONGLONG**

The ULONGLONG value to be stored.

**Return value**

**VOID**

**RtlStoreUlonglong** avoids memory alignment faults. If the address specified by _Address_ is not aligned to the storage requirements of a ULONGLONG, **RtlStoreUlonglong** stores the bytes of _Value_ beginning at the memory location (PUCHAR)_Address_.

**RtlStoreUlonglong** runs at any IRQL if _Address_ points to nonpaged pool; otherwise, it must run at IRQL <= APC_LEVEL.

Available starting with Windows 2000.

IRQL: Any level


## **RtlStoreUlongPtr**

Defined in: Wdm.h

The **RtlStoreUlongPtr** macro stores a specified ULONG_PTR value at a specified memory location, avoiding memory alignment faults.

_Address [out]_

**PULONG_PTR**

A pointer to a location in which to store the ULONG_PTR value.

_Value [in]_

**ULONG_PTR**

Specifies the ULONG_PTR value to be stored.

**Return value**

**VOID**

**RtlStoreUlongPtr** avoids memory alignment faults. If the value of _Address_ is not aligned to the storage requirements of a ULONG_PTR, **RtlStoreUlongPtr** stores the bytes of _Value_ beginning at the memory location (PUCHAR)_Address_.

**RtlStoreUlongPtr** runs at any IRQL if _Address_ points to nonpaged pool; otherwise it must run at IRQL <= APC_LEVEL.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **RtlStoreUshort**

Defined in: Wdm.h

The **RtlStoreUshort** macro stores a USHORT value at a particular address, avoiding alignment faults.

_Address [out]_

**PUSHORT**

A pointer to a location in which to store the specified USHORT value.

_Value [in]_

**USHORT**

Specifies a USHORT value to be stored.

**Return value**

**VOID**

The caller can be running at any IRQL if _Address_ points to nonpaged pool. Otherwise, the caller must be running at IRQL <= APC_LEVEL.

Available in Windows 2000 and later versions of Windows.

IRQL: Any level


## **WRITE_REGISTER_BUFFER_ULONG64**

Defined in: Wdm.h

The **WRITE_REGISTER_BUFFER_ULONG64** macro writes a number of ULONG64 values from a buffer to the specified register.

_Register [in]_

**PULONG64**

Pointer to the register, which must be a mapped range in memory space.

_Buffer [in]_

**PULONG64**

Pointer to a buffer that an array of ULONG64 values is to be written to.

_Count [in]_

**ULONG**

Specifies the number of ULONG64 values to be written to the register.

**Return value**

**VOID**

The size of the _Buffer_ buffer must be large enough to contain at least the specified number of ULONG64 values.

Callers of the **WRITE_REGISTER_BUFFER_ULONG64** macro can be running at any IRQL, assuming that the _Buffer_ buffer is resident and the _Register_ register is resident, mapped device memory.

Available only in 64-bit versions of Windows.

IRQL: Any level


## **WRITE_REGISTER_ULONG64**

Defined in: Wdm.h

The **WRITE_REGISTER_ULONG64** macro writes a ULONG64 value to the specified address.

_volatile *Register [in]_

**ULONG64**

Pointer to the register, which must be a mapped range in memory space.

_Value [in]_

**ULONG64**

Specifies a ULONG64 value to write to the register.

**Return value**

**VOID**

Callers of the **WRITE_REGISTER_ULONG64** macro can be running at any IRQL, assuming the _Register_ register is resident, mapped device memory.

Available only in 64-bit versions of Windows.

IRQL: Any level


## **ZwCurrentProcess**

Defined in: Wdm.h

The **ZwCurrentProcess** macro returns a handle to the current process.

**Return value**

**HANDLE**

**ZwCurrentProcess** returns a special handle value that represents the current process.

The returned value is not a true handle, but it is a special value that always represents the current process.

**NtCurrentProcess** and **ZwCurrentProcess** are two versions of the same Windows Native System Services routine. The **NtCurrentProcess** routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling **ZwCurrentProcess**.

For calls from kernel-mode drivers, the **Nt_Xxx_** and **Zw_Xxx_** versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the **Nt_Xxx_** and **Zw_Xxx_** versions of a routine, see [Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md).

All supported operating systems.

IRQL: Any level


## **ZwCurrentThread**

Defined in: Wdm.h

The **ZwCurrentThread** macro returns a handle to the current thread.

**Return value**

**HANDLE**

**ZwCurrentThread** returns a special handle value that represents the current thread.

The returned value is not a true handle, but it is a special value that always represents the current thread.

**NtCurrentThread** and **ZwCurrentThread** are two versions of the same Windows Native System Services routine. The **NtCurrentThread** routine in the Windows kernel is not directly accessible to kernel-mode drivers. However, kernel-mode drivers can access this routine indirectly by calling the **ZwCurrentThread** routine.

For calls from kernel-mode drivers, the **Nt_Xxx_** and **Zw_Xxx_** versions of a Windows Native System Services routine can behave differently in the way that they handle and interpret input parameters. For more information about the relationship between the **Nt_Xxx_** and **Zw_Xxx_** versions of a routine, see [Using Nt and Zw Versions of the Native System Services Routines](using-nt-and-zw-versions-of-the-native-system-services-routines.md).

All supported operating systems.

IRQL: Any level
