---
title: MM_BAD_POINTER macro
description: MM_BAD_POINTER macro
ms.localizationpriority: medium
ms.date: 07/16/2021
---

# MM_BAD_POINTER

> [!NOTE]
> This page previously contained a list of kernel macros, not just **MM_BAD_POINTER**. Those macros have now been broken out into their own individual pages. For links, use the See Also section below, or search the web.

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


## See also

* [**ADDRESS_AND_SIZE_TO_SPAN_PAGES**](/windows-hardware/drivers/ddi/wdm/nf-wdm-address_and_size_to_span_pages)
* [**BYTE_OFFSET**](/windows-hardware/drivers/ddi/wdm/nf-wdm-byte_offset)
* [**BYTES_TO_PAGES**](/windows-hardware/drivers/ddi/wdm/nf-wdm-bytes_to_pages)
* [**IoSkipCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioskipcurrentirpstacklocation)
* [**KeInitializeCallbackRecord**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializecallbackrecord)
* [**MmGetMdlByteCount**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlbytecount)
* [**MmGetMdlByteOffset**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlbyteoffset)
* [**MmGetMdlPfnArray**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlpfnarray)
* [**MmGetMdlVirtualAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlvirtualaddress)
* [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe)
* [**MmInitializeMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mminitializemdl)
* [**MmPrepareMdlForReuse**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmpreparemdlforreuse)
* [**PAGE_ALIGN**](/windows-hardware/drivers/ddi/wdm/nf-wdm-page_align)
* [**PAGED_CODE**](./paged_code.md)
* [**PAGED_CODE_LOCKED**](./paged_code_locked.md)
* [**PoSetDeviceBusy**](/windows-hardware/drivers/ddi/wdm/nf-wdm-posetdevicebusy)
* [**PsGetCurrentProcess**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentprocess)
* [**READ_REGISTER_BUFFER_ULONG64**](/windows-hardware/drivers/ddi/wdm/nf-wdm-read_register_buffer_ulong64)
* [**READ_REGISTER_ULONG64**](/windows-hardware/drivers/ddi/wdm/nf-wdm-read_register_ulong64)
* [**ROUND_TO_PAGES**](/windows-hardware/drivers/ddi/wdm/nf-wdm-round_to_pages)
* [**RtlEqualLuid**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlequalluid)
* [**RtlInitEmptyAnsiString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlinitemptyansistring)
* [**RtlInitEmptyUnicodeString**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlinitemptyunicodestring)
* [**RtlIsZeroLuid**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtliszeroluid)
* [**RtlRetrieveUlong**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlretrieveulong)
* [**RtlRetrieveUshort**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlretrieveushort)
* [**RtlStoreUlong**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlstoreulong)
* [**RtlStoreUlonglong**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlstoreulonglong)
* [**RtlStoreUlongPtr**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlstoreulongptr)
* [**RtlStoreUshort**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlstoreushort)
* [**WRITE_REGISTER_BUFFER_ULONG64**](/windows-hardware/drivers/ddi/wdm/nf-wdm-write_register_buffer_ulong64)
* [**WRITE_REGISTER_ULONG64**](/windows-hardware/drivers/ddi/wdm/nf-wdm-write_register_ulong64)
* [**ZwCurrentProcess**](./zwcurrentprocess.md)
* [**ZwCurrentThread**](./zwcurrentthread.md)
