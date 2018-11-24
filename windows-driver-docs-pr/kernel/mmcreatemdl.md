---
title: Windows kernel obsolete routines
description: Windows kernel obsolete routines
ms.assetid: 876f48be-1d8f-4c65-bc84-e35c31919c47
ms.localizationpriority: medium
ms.date: 10/17/2018
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
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544351" data-raw-source="[&lt;strong&gt;ExAcquireResourceExclusiveLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544351)"><strong>ExAcquireResourceExclusiveLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExAcquireResourceShared</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544363" data-raw-source="[&lt;strong&gt;ExAcquireResourceSharedLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544363)"><strong>ExAcquireResourceSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExConvertExclusiveToShared</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544558" data-raw-source="[&lt;strong&gt;ExConvertExclusiveToSharedLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544558)"><strong>ExConvertExclusiveToSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExDeleteResource</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff544578" data-raw-source="[&lt;strong&gt;ExDeleteResourceLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff544578)"><strong>ExDeleteResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeResource</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545317" data-raw-source="[&lt;strong&gt;ExInitializeResourceLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545317)"><strong>ExInitializeResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInitializeWorkItem</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548276" data-raw-source="[&lt;strong&gt;IoAllocateWorkItem&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548276)"><strong>IoAllocateWorkItem</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedDecrementLong</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff547871" data-raw-source="[&lt;strong&gt;InterlockedDecrement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547871)"><strong>InterlockedDecrement</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExchangeAddLargeInteger</strong></td>
<td><p>For more information about atomically adding two 64-bit numbers, see <a href="http://go.microsoft.com/fwlink/p/?linkid=71056" data-raw-source="[InterlockedExchangeAdd64](http://go.microsoft.com/fwlink/p/?linkid=71056)">InterlockedExchangeAdd64</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedExchangeUlong</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff547892" data-raw-source="[&lt;strong&gt;InterlockedExchange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547892)"><strong>InterlockedExchange</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedIncrementLong</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff547910" data-raw-source="[&lt;strong&gt;InterlockedIncrement&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff547910)"><strong>InterlockedIncrement</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsFullZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsObjectInFirstZoneSegment</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540667" data-raw-source="[Buffer Management](https://msdn.microsoft.com/library/windows/hardware/ff540667)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquired</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545466" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545466)"><strong>ExIsResourceAcquiredLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsResourceAcquiredExclusive</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545458" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredExclusiveLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545458)"><strong>ExIsResourceAcquiredExclusiveLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquiredShared</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545477" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredSharedLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545477)"><strong>ExIsResourceAcquiredSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExReleaseResource</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545597" data-raw-source="[&lt;strong&gt;ExReleaseResourceLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545597)"><strong>ExReleaseResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExReleaseResourceForThread</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545585" data-raw-source="[&lt;strong&gt;ExReleaseResourceForThreadLite&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545585)"><strong>ExReleaseResourceForThreadLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAllocateAdapterChannel</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff540573" data-raw-source="[&lt;strong&gt;AllocateAdapterChannel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff540573)"><strong>AllocateAdapterChannel</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoAssignResources</strong></td>
<td><p>Drivers of PnP devices are assigned resources by the PnP manager, which passes resource lists with each <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749" data-raw-source="[&lt;strong&gt;IRP_MN_START_DEVICE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff551749)"><strong>IRP_MN_START_DEVICE</strong></a> request. Drivers that must support a legacy device that cannot be enumerated by the PnP manager should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549597" data-raw-source="[&lt;strong&gt;IoReportDetectedDevice&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549597)"><strong>IoReportDetectedDevice</strong></a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff549608" data-raw-source="[&lt;strong&gt;IoReportResourceForDetection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549608)"><strong>IoReportResourceForDetection</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAttachDeviceByPointer</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548300" data-raw-source="[&lt;strong&gt;IoAttachDeviceToDeviceStack&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548300)"><strong>IoAttachDeviceToDeviceStack</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFlushAdapterBuffers</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff545917" data-raw-source="[&lt;strong&gt;FlushAdapterBuffers&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff545917)"><strong>FlushAdapterBuffers</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoFreeAdapterChannel</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff546507" data-raw-source="[&lt;strong&gt;FreeAdapterChannel&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546507)"><strong>FreeAdapterChannel</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFreeMapRegisters</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff546513" data-raw-source="[&lt;strong&gt;FreeMapRegisters&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546513)"><strong>FreeMapRegisters</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoMapTransfer</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff554402" data-raw-source="[&lt;strong&gt;MapTransfer&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554402)"><strong>MapTransfer</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoQueryDeviceDescription</strong></td>
<td><p>This routine retrieves hardware configuration information about a given bus, controller or peripheral object, or any combination of these three types from the <strong>\Registry\Machine\Hardware\Description</strong> tree. Drivers that require hardware configuration information should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff549203" data-raw-source="[&lt;strong&gt;IoGetDeviceProperty&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549203)"><strong>IoGetDeviceProperty</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReportResourceUsage</strong></td>
<td><p>This routine claims hardware resources, such as an interrupt vector, device memory range or a particular DMA controller channel in the <strong>\Registry\Machine\Hardware\ResourceMap</strong> tree, so that a subsequently loaded driver cannot attempt to use the same resources. If a new driver must support a legacy device that is not PnP-enumerable, the driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549608" data-raw-source="[&lt;strong&gt;IoReportResourceForDetection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff549608)"><strong>IoReportResourceForDetection</strong></a> to claim resources for the device.</p></td>
</tr>
<tr class="even">
<td><strong>KeGetDcacheFillSize</strong></td>
<td><p>Drivers should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff546530" data-raw-source="[&lt;strong&gt;GetDmaAlignment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff546530)"><strong>GetDmaAlignment</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>MmCreateMdl</strong></td>
<td><p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/ff548263" data-raw-source="[&lt;strong&gt;IoAllocateMdl&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548263)"><strong>IoAllocateMdl</strong></a> instead.</p></td>
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



