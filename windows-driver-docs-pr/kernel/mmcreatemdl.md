---
title: Windows kernel obsolete routines
author: windows-driver-content
description: Windows kernel obsolete routines
MS-HAID:
- 'k106\_0948e076-31cf-4fda-8922-d167918c1cff.xml'
- 'kernel.mmcreatemdl'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 876f48be-1d8f-4c65-bc84-e35c31919c47
---

# Windows kernel obsolete routines


The following obsolete routines are exported to support existing binaries:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Obsolete routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ExAcquireResourceExclusive</strong></td>
<td><p>Use [<strong>ExAcquireResourceExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544351) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExAcquireResourceShared</strong></td>
<td><p>Use [<strong>ExAcquireResourceSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544363) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="even">
<td><strong>ExConvertExclusiveToShared</strong></td>
<td><p>Use [<strong>ExConvertExclusiveToSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544558) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExDeleteResource</strong></td>
<td><p>Use [<strong>ExDeleteResourceLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544578) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="odd">
<td><strong>ExFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeResource</strong></td>
<td><p>Use [<strong>ExInitializeResourceLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545317) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInitializeWorkItem</strong></td>
<td><p>Use [<strong>IoAllocateWorkItem</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548276) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedDecrementLong</strong></td>
<td><p>Use [<strong>InterlockedDecrement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547871) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExchangeAddLargeInteger</strong></td>
<td><p>For more information about atomically adding two 64-bit numbers, see [InterlockedExchangeAdd64](http://go.microsoft.com/fwlink/p/?linkid=71056).</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedExchangeUlong</strong></td>
<td><p>Use [<strong>InterlockedExchange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547892) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedIncrementLong</strong></td>
<td><p>Use [<strong>InterlockedIncrement</strong>](https://msdn.microsoft.com/library/windows/hardware/ff547910) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsFullZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsObjectInFirstZoneSegment</strong></td>
<td><p>Use lookaside lists instead. For more information, see [Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667).</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquired</strong></td>
<td><p>Use [<strong>ExIsResourceAcquiredLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545466) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsResourceAcquiredExclusive</strong></td>
<td><p>Use [<strong>ExIsResourceAcquiredExclusiveLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545458) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquiredShared</strong></td>
<td><p>Use [<strong>ExIsResourceAcquiredSharedLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545477) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExReleaseResource</strong></td>
<td><p>Use [<strong>ExReleaseResourceLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545597) instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExReleaseResourceForThread</strong></td>
<td><p>Use [<strong>ExReleaseResourceForThreadLite</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545585) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAllocateAdapterChannel</strong></td>
<td><p>Use [<strong>AllocateAdapterChannel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff540573) instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoAssignResources</strong></td>
<td><p>Drivers of PnP devices are assigned resources by the PnP manager, which passes resource lists with each [<strong>IRP_MN_START_DEVICE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. Drivers that must support a legacy device that cannot be enumerated by the PnP manager should use [<strong>IoReportDetectedDevice</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549597) and [<strong>IoReportResourceForDetection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549608) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAttachDeviceByPointer</strong></td>
<td><p>Use [<strong>IoAttachDeviceToDeviceStack</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548300) instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFlushAdapterBuffers</strong></td>
<td><p>Use [<strong>FlushAdapterBuffers</strong>](https://msdn.microsoft.com/library/windows/hardware/ff545917) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoFreeAdapterChannel</strong></td>
<td><p>Use [<strong>FreeAdapterChannel</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546507) instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFreeMapRegisters</strong></td>
<td><p>Use [<strong>FreeMapRegisters</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546513) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoMapTransfer</strong></td>
<td><p>Use [<strong>MapTransfer</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554402) instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoQueryDeviceDescription</strong></td>
<td><p>This routine retrieves hardware configuration information about a given bus, controller or peripheral object, or any combination of these three types from the <strong>\Registry\Machine\Hardware\Description</strong> tree. Drivers that require hardware configuration information should use [<strong>IoGetDeviceProperty</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549203) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReportResourceUsage</strong></td>
<td><p>This routine claims hardware resources, such as an interrupt vector, device memory range or a particular DMA controller channel in the <strong>\Registry\Machine\Hardware\ResourceMap</strong> tree, so that a subsequently loaded driver cannot attempt to use the same resources. If a new driver must support a legacy device that is not PnP-enumerable, the driver should call [<strong>IoReportResourceForDetection</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549608) to claim resources for the device.</p></td>
</tr>
<tr class="even">
<td><strong>KeGetDcacheFillSize</strong></td>
<td><p>Drivers should call [<strong>GetDmaAlignment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff546530) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>MmCreateMdl</strong></td>
<td><p>Use [<strong>IoAllocateMdl</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548263) instead.</p></td>
</tr>
<tr class="even">
<td><strong>MmIsNonPagedSystemAddressValid</strong></td>
<td></td>
</tr>
</tbody>
</table>

 

## Related topics
[**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573)  
[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)  
[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)  
[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)  
[**ExConvertExclusiveToSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544558)  
[**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578)  
[**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317)  
[**ExIsResourceAcquiredExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff545458)  
[**ExIsResourceAcquiredSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff545477)  
[**ExReleaseResourceForThreadLite**](https://msdn.microsoft.com/library/windows/hardware/ff545585)  
[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)  
[**InterlockedDecrement**](https://msdn.microsoft.com/library/windows/hardware/ff547871)  
[**InterlockedExchange**](https://msdn.microsoft.com/library/windows/hardware/ff547892)  
[**InterlockedIncrement**](https://msdn.microsoft.com/library/windows/hardware/ff547910)  
[**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917)  
[**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507)  
[**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513)  
[**GetDmaAlignment**](https://msdn.microsoft.com/library/windows/hardware/ff546530)  
[InterlockedExchangeAdd64](http://go.microsoft.com/fwlink/p/?linkid=71056)  
[**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263)  
[**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276)  
[**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300)  
[**IoGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff549203)  
[**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597)  
[**IoReportResourceForDetection**](https://msdn.microsoft.com/library/windows/hardware/ff549608)  
[**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749)  
[**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20kernel%20obsolete%20routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


