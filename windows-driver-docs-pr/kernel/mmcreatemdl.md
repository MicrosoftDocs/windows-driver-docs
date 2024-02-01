---
title: Windows Kernel Obsolete Routines
description: Windows kernel obsolete routines
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
<td><p>Use <a href="/previous-versions/ff544351(v=vs.85)" data-raw-source="[&lt;strong&gt;ExAcquireResourceExclusiveLite&lt;/strong&gt;](/previous-versions/ff544351(v=vs.85))"><strong>ExAcquireResourceExclusiveLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExAcquireResourceShared</strong></td>
<td><p>Use <a href="/previous-versions/ff544363(v=vs.85)" data-raw-source="[&lt;strong&gt;ExAcquireResourceSharedLite&lt;/strong&gt;](/previous-versions/ff544363(v=vs.85))"><strong>ExAcquireResourceSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExConvertExclusiveToShared</strong></td>
<td><p>Use <a href="/previous-versions/ff544558(v=vs.85)" data-raw-source="[&lt;strong&gt;ExConvertExclusiveToSharedLite&lt;/strong&gt;](/previous-versions/ff544558(v=vs.85))"><strong>ExConvertExclusiveToSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExDeleteResource</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite" data-raw-source="[&lt;strong&gt;ExDeleteResourceLite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite)"><strong>ExDeleteResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeResource</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializeresourcelite" data-raw-source="[&lt;strong&gt;ExInitializeResourceLite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializeresourcelite)"><strong>ExInitializeResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInitializeWorkItem</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem" data-raw-source="[&lt;strong&gt;IoAllocateWorkItem&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem)"><strong>IoAllocateWorkItem</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExInitializeZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedAllocateFromZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedDecrementLong</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement" data-raw-source="[&lt;strong&gt;InterlockedDecrement&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement)"><strong>InterlockedDecrement</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExchangeAddLargeInteger</strong></td>
<td><p>For more information about atomically adding two 64-bit numbers, see <a href="/windows/win32/api/winnt/nf-winnt-interlockedexchangeadd64" data-raw-source="[InterlockedExchangeAdd64](/windows/win32/api/winnt/nf-winnt-interlockedexchangeadd64)">InterlockedExchangeAdd64</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedExchangeUlong</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedexchange" data-raw-source="[&lt;strong&gt;InterlockedExchange&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedexchange)"><strong>InterlockedExchange</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedExtendZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExInterlockedFreeToZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExInterlockedIncrementLong</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement" data-raw-source="[&lt;strong&gt;InterlockedIncrement&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement)"><strong>InterlockedIncrement</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsFullZone</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsObjectInFirstZoneSegment</strong></td>
<td><p>Use lookaside lists instead. For more information, see <a href="/windows-hardware/drivers/ddi/index" data-raw-source="[Buffer Management](/windows-hardware/drivers/ddi/index)">Buffer Management</a>.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquired</strong></td>
<td><p>Use <a href="/previous-versions/windows/hardware/drivers/ff545466(v=vs.85)" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredLite&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff545466(v=vs.85))"><strong>ExIsResourceAcquiredLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExIsResourceAcquiredExclusive</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredexclusivelite" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredExclusiveLite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredexclusivelite)"><strong>ExIsResourceAcquiredExclusiveLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExIsResourceAcquiredShared</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredsharedlite" data-raw-source="[&lt;strong&gt;ExIsResourceAcquiredSharedLite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredsharedlite)"><strong>ExIsResourceAcquiredSharedLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>ExReleaseResource</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite" data-raw-source="[&lt;strong&gt;ExReleaseResourceLite&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite)"><strong>ExReleaseResourceLite</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>ExReleaseResourceForThread</strong></td>
<td><p>Use <a href="/previous-versions/ff545585(v=vs.85)" data-raw-source="[&lt;strong&gt;ExReleaseResourceForThreadLite&lt;/strong&gt;](/previous-versions/ff545585(v=vs.85))"><strong>ExReleaseResourceForThreadLite</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAllocateAdapterChannel</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel" data-raw-source="[&lt;strong&gt;AllocateAdapterChannel&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel)"><strong>AllocateAdapterChannel</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoAssignResources</strong></td>
<td><p>Drivers of PnP devices are assigned resources by the PnP manager, which passes resource lists with each <a href="/windows-hardware/drivers/kernel/irp-mn-start-device" data-raw-source="[&lt;strong&gt;IRP_MN_START_DEVICE&lt;/strong&gt;](./irp-mn-start-device.md)"><strong>IRP_MN_START_DEVICE</strong></a> request. Drivers that must support a legacy device that cannot be enumerated by the PnP manager should use <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportdetecteddevice" data-raw-source="[&lt;strong&gt;IoReportDetectedDevice&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportdetecteddevice)"><strong>IoReportDetectedDevice</strong></a> and <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportresourcefordetection" data-raw-source="[&lt;strong&gt;IoReportResourceForDetection&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportresourcefordetection)"><strong>IoReportResourceForDetection</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoAttachDeviceByPointer</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack" data-raw-source="[&lt;strong&gt;IoAttachDeviceToDeviceStack&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)"><strong>IoAttachDeviceToDeviceStack</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFlushAdapterBuffers</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers" data-raw-source="[&lt;strong&gt;FlushAdapterBuffers&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers)"><strong>FlushAdapterBuffers</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoFreeAdapterChannel</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel" data-raw-source="[&lt;strong&gt;FreeAdapterChannel&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel)"><strong>FreeAdapterChannel</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoFreeMapRegisters</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers" data-raw-source="[&lt;strong&gt;FreeMapRegisters&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers)"><strong>FreeMapRegisters</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoMapTransfer</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer" data-raw-source="[&lt;strong&gt;MapTransfer&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer)"><strong>MapTransfer</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>IoQueryDeviceDescription</strong></td>
<td><p>This routine retrieves hardware configuration information about a given bus, controller or peripheral object, or any combination of these three types from the <strong>\Registry\Machine\Hardware\Description</strong> tree. Drivers that require hardware configuration information should use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty" data-raw-source="[&lt;strong&gt;IoGetDeviceProperty&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty)"><strong>IoGetDeviceProperty</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReportResourceUsage</strong></td>
<td><p>This routine claims hardware resources, such as an interrupt vector, device memory range or a particular DMA controller channel in the <strong>\Registry\Machine\Hardware\ResourceMap</strong> tree, so that a subsequently loaded driver cannot attempt to use the same resources. If a new driver must support a legacy device that is not PnP-enumerable, the driver should call <a href="/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportresourcefordetection" data-raw-source="[&lt;strong&gt;IoReportResourceForDetection&lt;/strong&gt;](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportresourcefordetection)"><strong>IoReportResourceForDetection</strong></a> to claim resources for the device.</p></td>
</tr>
<tr class="even">
<td><strong>KeGetDcacheFillSize</strong></td>
<td><p>Drivers should call <a href="/windows-hardware/drivers/ddi/wdm/nc-wdm-pget_dma_alignment" data-raw-source="[&lt;strong&gt;GetDmaAlignment&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nc-wdm-pget_dma_alignment)"><strong>GetDmaAlignment</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>MmCreateMdl</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl" data-raw-source="[&lt;strong&gt;IoAllocateMdl&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl)"><strong>IoAllocateMdl</strong></a> instead.</p></td>
</tr>
<tr class="even">
<td><strong>MmIsNonPagedSystemAddressValid</strong></td>
<td></td>
</tr>
</tbody>
</table>

 

## Related topics
[**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel)  
[**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))  
[**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85))  
[**ExConvertExclusiveToSharedLite**](/previous-versions/ff544558(v=vs.85))  
[**ExDeleteResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exdeleteresourcelite)  
[**ExInitializeResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializeresourcelite)  
[**ExIsResourceAcquiredExclusiveLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredexclusivelite)  
[**ExIsResourceAcquiredSharedLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exisresourceacquiredsharedlite)  
[**ExReleaseResourceForThreadLite**](/previous-versions/ff545585(v=vs.85))  
[**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite)  
[**InterlockedDecrement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockeddecrement)  
[**InterlockedExchange**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedexchange)  
[**InterlockedIncrement**](/windows-hardware/drivers/ddi/wdm/nf-wdm-interlockedincrement)  
[**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers)  
[**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel)  
[**FreeMapRegisters**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers)  
[**GetDmaAlignment**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pget_dma_alignment)  
[InterlockedExchangeAdd64](/windows/win32/api/winnt/nf-winnt-interlockedexchangeadd64)  
[**IoAllocateMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl)  
[**IoAllocateWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateworkitem)  
[**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)  
[**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty)  
[**IoReportDetectedDevice**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportdetecteddevice)  
[**IoReportResourceForDetection**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioreportresourcefordetection)  
[**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md)  
[**MapTransfer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer)
