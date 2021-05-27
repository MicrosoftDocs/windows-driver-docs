---
title: Checked Build ASSERTs
description: Checked Build ASSERTs
keywords:
- checked builds WDK , ASSERTs
- ASSERTs WDK checked builds
- errors WDK checked builds
ms.date: 05/08/2020
ms.localizationpriority: medium
---

# Checked Build ASSERTs


## <span id="ddk_checked_build_asserts_tools"></span><span id="DDK_CHECKED_BUILD_ASSERTS_TOOLS"></span>


This topic contains a list of common [**ASSERT**](/previous-versions/windows/hardware/previsioning-framework/ff542107(v=vs.85))s encountered by driver writers.

For some tips on how to handle these asserts (and others not listed), see [How the Checked Build Indicates a Problem](how-the-checked-build-indicates-a-problem.md).

The routine listed in the "Routine Called" column is the most common routine that driver writers or system components would call to provoke this error. Some of the routines listed below are documented routines that drivers call. Others are internal routines that only system components can call. Keep in mind that calling some other function from your driver might result in the called function internally calling one of the listed functions, which could in turn issue the **ASSERT**.

> [!NOTE]
> Checked builds were available on older versions of Windows, before Windows 10 version 1803.
> Use tools such as Driver Verifier and GFlags to check driver code in later versions of Windows.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Routine Called</th>
<th align="left">ASSERT text</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl" data-raw-source="[&lt;strong&gt;IoAllocateMdl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl)"><strong>IoAllocateMdl</strong></a></p></td>
<td align="left"><p>ASSERT(Length)</p></td>
<td align="left"><p>The length of the user buffer being described is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack" data-raw-source="[&lt;strong&gt;IoAttachDeviceToDeviceStack&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)"><strong>IoAttachDeviceToDeviceStack</strong></a></p></td>
<td align="left"><p>ASSERT( sourceExtension-&gt;AttachedTo == <strong>NULL</strong> )</p></td>
<td align="left"><p>The device object that is being attached (the source device) is already attached to another device object.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver" data-raw-source="[&lt;strong&gt;IoCallDriver&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)"><strong>IoCallDriver</strong></a></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Type == IO_TYPE_IRP )</p></td>
<td align="left"><p>The PIRP argument does not point to an IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp" data-raw-source="[&lt;strong&gt;IoCancelIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocancelirp)"><strong>IoCancelIrp</strong></a></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Type == IO_TYPE_IRP )</p></td>
<td align="left"><p>The PIRP argument does not point to an IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest" data-raw-source="[&lt;strong&gt;IoCompleteRequest&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest)"><strong>IoCompleteRequest</strong></a></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Type == IO_TYPE_IRP )</p></td>
<td align="left"><p>The PIRP argument does not point to an IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IoCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT( !Irp-&gt;CancelRoutine )</p></td>
<td align="left"><p>There is a cancel routine present in the IRP.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT( Irp-&gt;IoStatus.Status != STATUS_PENDING )</p></td>
<td align="left"><p>An attempt to complete an IRP with STATUS_PENDING.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IoCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT( Irp-&gt;IoStatus.Status != 0xffffffff )</p></td>
<td align="left"><p>An attempt to complete an IRP with an invalid status code.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Tail.Overlay.AuxiliaryBuffer != <strong>NULL</strong> )</p></td>
<td align="left"><p>An IRP is being completed with STATUS_REPARSE, IO_REPARSE_TAG_MOUNT_POINT, and the auxillary buffer is <strong>NULL</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice" data-raw-source="[&lt;strong&gt;IoCreateDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice)"><strong>IoCreateDevice</strong></a></p></td>
<td align="left"><p>ASSERT((DriverObject-&gt;Flags & DRVO_UNLOAD_INVOKED) == 0)</p></td>
<td align="left"><p>A device object has been created, but the driver creating it is marked for unload.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp" data-raw-source="[&lt;strong&gt;IoFreeIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp)"><strong>IoFreeIrp</strong></a></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Type == IO_TYPE_IRP )</p></td>
<td align="left"><p>The PIRP does not point to an IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IoFreeIrp</strong></p></td>
<td align="left"><p>ASSERT(IsListEmpty(&(Irp)-&gt;ThreadListEntry))</p></td>
<td align="left"><p>The IRP being freed is still on a thread's IRP list, and therefore still in use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoFreeIrp</strong></p></td>
<td align="left"><p>ASSERT( Irp-&gt;CurrentLocation &gt;= Irp-&gt;StackCount )</p></td>
<td align="left"><p>An IRP is being freed, but I/O completion has not yet finished for all drivers that processed this IRP.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreuseirp" data-raw-source="[&lt;strong&gt;IoReuseIrp&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreuseirp)"><strong>IoReuseIrp</strong></a></p></td>
<td align="left"><p>ASSERT(Irp-&gt;CancelRoutine == <strong>NULL</strong>)</p></td>
<td align="left"><p>There is a cancel routine remaining in the IRP that is been requested to reuse.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IoReuseIrp</strong></p></td>
<td align="left"><p>ASSERT(IsListEmpty(&Irp-&gt;ThreadListEntry))</p></td>
<td align="left"><p>The IRP being reused is still on a thread's IRP list, and therefore still in use.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iosetharderrororverifydevice" data-raw-source="[&lt;strong&gt;IoSetHardErrorOrVerifyDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iosetharderrororverifydevice)"><strong>IoSetHardErrorOrVerifyDevice</strong></a></p></td>
<td align="left"><p>ASSERT( Irp-&gt;Tail.Overlay.Thread != <strong>NULL</strong> )</p></td>
<td align="left"><p>The IRP is not on any thread's IRP list.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IopLoadDriver</strong></p></td>
<td align="left"><p>ASSERT(driverObject-&gt;MajorFunction[i] != <strong>NULL</strong>)</p></td>
<td align="left"><p>The driver set a dispatch entry point to <strong>NULL</strong> in its <strong>DriverEntry</strong> routine.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IopCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT( irp-&gt;IoStatus.Status != 0xffffffff)</p></td>
<td align="left"><p>An IRP was completed with an obviously invalid status.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IopCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT(reparseBuffer-&gt;ReparseTag == IO_REPARSE_TAG_MOUNT_POINT)</p></td>
<td align="left"><p>An IRP was completed with Status == STATUS_REPARSE and Information == IO_REPARSE_TAG_MOUNT_POINT, but the ReparseTag is not for a MOUNT_POINT.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IopCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT(reparseBuffer-&gt;ReparseDataLength &lt; MAXIMUM_REPARSE_DATA_BUFFER_SIZE)</p></td>
<td align="left"><p>An IRP was completed with Status == STATUS_REPARSE and Information == IO_REPARSE_TAG_MOUNT_POINT, but the returned tag has an invalid length.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>IopCompleteRequest</strong></p></td>
<td align="left"><p>ASSERT(reparseBuffer-&gt;Reserved &lt; MAXIMUM_REPARSE_DATA_BUFFER_SIZE)</p></td>
<td align="left"><p>An IRP was completed with Status == STATUS_REPARSE and Information == IO_REPARSE_TAG_MOUNT_POINT, but the returned tag has an invalid length.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>IopSynchronousServiceTail</strong></p></td>
<td align="left"><p>ASSERT( !Irp-&gt;PendingReturned )</p></td>
<td align="left"><p>An IRP was marked pending, but synchronously dispatch routine returned with status != STATUS_PENDING.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages" data-raw-source="[&lt;strong&gt;MmProbeAndLockPages&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages)"><strong>MmProbeAndLockPages</strong></a></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;ByteCount != 0)</p></td>
<td align="left"><p>The byte count in the passed-in MDL is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmProbeAndLockPages</strong></p></td>
<td align="left"><p>ASSERT (((ULONG)MemoryDescriptorList-&gt;ByteOffset & ~(PAGE_SIZE - 1)) == 0)</p></td>
<td align="left"><p>The offset into the first page in the MDL is &gt;= PAGE_SIZE; the MDL is incorrectly formed.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmProbeAndLockPages</strong></p></td>
<td align="left"><p>ASSERT (((ULONG_PTR)MemoryDescriptorList-&gt;StartVa & (PAGE_SIZE - 1)) == 0)</p></td>
<td align="left"><p>The starting VA in the MDL is not page aligned; the MDL is incorrectly formed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmProbeAndLockPages</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & ( MDL_PAGES_LOCKED | MDL_MAPPED_TO_SYSTEM_VA | MDL_SOURCE_IS_NONPAGED_POOL | MDL_PARTIAL | MDL_IO_SPACE)) == 0)</p></td>
<td align="left"><p>The MDL is not in proper state for this function call.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmProbeAndLockPages</strong></p></td>
<td align="left"><p>ASSERT (NumberOfPagesToLock != 0)</p></td>
<td align="left"><p>The MDL describes a range of pages with zero pages to lock.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmProbeAndLockPages</strong></p></td>
<td align="left"><p>ASSERT (<strong>FALSE</strong>)</p></td>
<td align="left"><p>A page in the buffer described by the MDL has been locked into memory an unusually high number of times.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpages" data-raw-source="[&lt;strong&gt;MmUnlockPages&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunlockpages)"><strong>MmUnlockPages</strong></a></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & MDL_PAGES_LOCKED) != 0)</p></td>
<td align="left"><p>The pages that comprise the buffer described by this MDL have not been locked.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & MDL_SOURCE_IS_NONPAGED_POOL) == 0)</p></td>
<td align="left"><p>The MDL describes a buffer from nonpaged pool.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & MDL_PARTIAL) == 0)</p></td>
<td align="left"><p>The MDL was built by calling <strong>IoBuildPartialMdl</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;ByteCount != 0)</p></td>
<td align="left"><p>The MDL describes a buffer that is zero bytes long.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT (NumberOfPages != 0)</p></td>
<td align="left"><p>The MDL does not contain any pages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT ((SPFN_NUMBER)Process-&gt;NumberOfLockedPages &gt;= 0)</p></td>
<td align="left"><p>The process associated with the MDL does not have any pages locked.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmUnlockPages</strong></p></td>
<td align="left"><p>ASSERT (<em>Page &lt;= MmHighestPhysicalPage)</p></td>
<td align="left"><p>A page frame pointer in the MDL is not valid.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmbuildmdlfornonpagedpool" data-raw-source="[&lt;strong&gt;MmBuildMdlForNonPagedPool&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmbuildmdlfornonpagedpool)"><strong>MmBuildMdlForNonPagedPool</strong></a></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;ByteCount != 0)</p></td>
<td align="left"><p>The buffer described by the MDL is zero bytes long.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmBuildMdlForNonPagedPool</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & (MDL_PAGES_LOCKED | MDL_MAPPED_TO_SYSTEM_VA | MDL_SOURCE_IS_NONPAGED_POOL | MDL_PARTIAL)) == 0)</p></td>
<td align="left"><p>The MDL is not in a proper state for this function call</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmBuildMdlForNonPagedPool</strong></p></td>
<td align="left"><p>ASSERT (NumberOfPages != 0)</p></td>
<td align="left"><p>The MDL describes a buffer with zero pages.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache" data-raw-source="[&lt;strong&gt;MmMapLockedPagesSpecifyCache&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache)"><strong>MmMapLockedPagesSpecifyCache</strong></a></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;ByteCount != 0)</p></td>
<td align="left"><p>The MDL has zero length.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmMapLockedPagesSpecifyCache</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & MDL_MAPPED_TO_SYSTEM_VA) == 0)</p></td>
<td align="left"><p>The buffer described by this MDL is already mapped into kernel virtual address space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmMapLockedPagesSpecifyCache</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & ( MDL_MAPPED_TO_SYSTEM_VA | MDL_SOURCE_IS_NONPAGED_POOL | MDL_PARTIAL_HAS_BEEN_MAPPED)) == 0)</p></td>
<td align="left"><p>The MDL is not in a proper state for this function call.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmMapLockedPagesSpecifyCache</strong></p></td>
<td align="left"><p>ASSERT ((MemoryDescriptorList-&gt;MdlFlags & ( MDL_PAGES_LOCKED | MDL_PARTIAL)) != 0)</p></td>
<td align="left"><p>The MDL is not in a proper state for this operation.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmMapLockedPagesSpecifyCache</strong></p></td>
<td align="left"><p>ASSERT (PointerPte-&gt;u.Hard.Valid == 0)</p></td>
<td align="left"><p>The buffer described by the MDL contains a page that is not resident in memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmMapLockedPagesSpecifyCache</strong></p></td>
<td align="left"><p>ASSERT (Pfn2-&gt;u3.e2.ReferenceCount != 0)</p></td>
<td align="left"><p>The buffer described by the MDL contains a page that is not locked in memory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmaplockedpages" data-raw-source="[&lt;strong&gt;MmUnmapLockedPages&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmaplockedpages)"><strong>MmUnmapLockedPages</strong></a></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;ByteCount != 0)</p></td>
<td align="left"><p>The MDL describes a buffer that is zero bytes long.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmUnmapLockedPages</strong></p></td>
<td align="left"><p>ASSERT (MemoryDescriptorList-&gt;MdlFlags & MDL_MAPPED_TO_SYSTEM_VA)</p></td>
<td align="left"><p>The parameter passed to this function to specify the base address indicated an address in kernel virtual address space, but this does not agree with the buffer description in the MDL.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmUnmapLockedPages</strong></p></td>
<td align="left"><p>ASSERT (PointerPte-&gt;u.Hard.Valid == 1)</p></td>
<td align="left"><p>A page in the buffer described by the MDL is not resident in memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmUnmapLockedPages</strong></p></td>
<td align="left"><p>ASSERT (</em>Page == MI_GET_PAGE_FRAME_FROM_PTE (PointerPte))</p></td>
<td align="left"><p>A page frame pointer in the MDL is not valid.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmUnmapLockedPages</strong></p></td>
<td align="left"><p>ASSERT (Pfn3-&gt;u3.e2.ReferenceCount != 0)</p></td>
<td align="left"><p>The buffer described by the MDL contains a page that is not locked in memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace" data-raw-source="[&lt;strong&gt;MmMapIoSpace&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace)"><strong>MmMapIoSpace</strong></a></p></td>
<td align="left"><p>ASSERT (PhysicalAddress.HighPart == 0)</p></td>
<td align="left"><p>This is running on an x86-based system with not more than 4 GB of physical memory, but the parameter passed to this function to specify the high 32 bits of the I/O space address is nonzero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmMapIoSpace</strong></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to map is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmMapIoSpace</strong></p></td>
<td align="left"><p>ASSERT (PointerPte-&gt;u.Hard.Valid == 0)</p></td>
<td align="left"><p>A page in the address rage is not in I/O space.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace" data-raw-source="[&lt;strong&gt;MmUnmapIoSpace&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace)"><strong>MmUnmapIoSpace</strong></a></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to unmap is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory" data-raw-source="[&lt;strong&gt;MmAllocateContiguousMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory)"><strong>MmAllocateContiguousMemory</strong></a></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to allocate is zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MemorySpecifyCache</strong></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to allocate is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmallocatenoncachedmemory" data-raw-source="[&lt;strong&gt;MmAllocateNonCachedMemory&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmallocatenoncachedmemory)"><strong>MmAllocateNonCachedMemory</strong></a></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to allocate is zero.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>MmFreeNonCachedMemory</strong></p></td>
<td align="left"><p>ASSERT (NumberOfBytes != 0)</p></td>
<td align="left"><p>The parameter passed to this function to specify the number of bytes to free is zero.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>MmFreeNonCachedMemory</strong></p></td>
<td align="left"><p>ASSERT (PAGE_ALIGN (BaseAddress) == BaseAddress)</p></td>
<td align="left"><p>The parameter passed to this function to specify the base address is not valid.</p></td>
</tr>
</tbody>
</table>

 

