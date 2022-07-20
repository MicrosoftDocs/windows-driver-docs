---
title: Evaluate HVCI driver compatibility
description: Follow these steps to use to evaluate HVCI driver compatibility of your driver code.
ms.date: 05/26/2020
---

# Evaluate HVCI driver compatibility

## Overview

After checking that your driver meets the below criteria for HVCI-compatible code, utilize the [HyperVisor Code Integrity Readiness Test](/windows-hardware/test/hlk/testref/b972fc52-2468-4462-9799-6a1898808c86) to confirm that your driver works with HVCI. 

## Implement HVCI compatible code

To implement HVCI compatible code, make sure your driver code does the following:

- Opts in to NX by default
- Uses NX APIs/flags for memory allocation (NonPagedPoolNx)
- Does not use sections that are both writable and executable
- Does not attempt to directly modify executable system memory
- Does not use dynamic code in kernel
- Does not load data files as executable
- Section alignment is a multiple of 0x1000 (PAGE\_SIZE). E.g. DRIVER\_ALIGNMENT=0x1000

The following list of DDIs that are not reserved for system use may be impacted:

|       DDI name                                                                                                  |
|------------------------------------------------------------------------------------------------------|
| [**ExAllocatePool**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepool)                                                          |
| [**ExAllocatePoolWithQuota**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquota)                                        |
| [**ExAllocatePoolWithQuotaTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithquotatag)                                  |
| [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag)                                            |
| [**ExAllocatePoolWithTagPriority**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtagpriority)                            |
| [**ExInitializeNPagedLookasideList**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializenpagedlookasidelist)                        |
| [**ExInitializeLookasideListEx**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exinitializelookasidelistex)                                |
| [**MmAllocateContiguousMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory)                                  |
| [**MmAllocateContiguousMemorySpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemoryspecifycache)          |
| [**MmAllocateContiguousMemorySpecifyCacheNode**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemoryspecifycachenode)  |
| [**MmAllocateContiguousNodeMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousnodememory)                          |
| [**MmCopyMemory**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmcopymemory)                                                              |
| [**MmMapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace)                                                              |
| [**MmMapLockedPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpages)                                                      |
| [**MmMapLockedPagesSpecifyCache**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache)                              |
| [**MmProtectMdlSystemAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprotectmdlsystemaddress)                                    |
| [**ZwAllocateVirtualMemory**](/previous-versions/ff566416(v=vs.85))                                        |
| [**ZwCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection)                                                        |
| [**ZwMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)                                                  |
| [**NtCreateSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatesection)                                                        |
| [**NtMapViewOfSection**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection)                                                  |
| [**ClfsCreateMarshallingArea**](/windows-hardware/drivers/ddi/wdm/nf-wdm-clfscreatemarshallingarea)                                    |
| NDIS                                                                                                 |
| [**NdisAllocateMemoryWithTagPriority**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisallocatememorywithtagpriority)                  |
| Storage                                                                                              |
| [**StorPortGetDataInBufferSystemAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetdatainbuffersystemaddress)             |
| [**StorPortGetSystemAddress**](/windows-hardware/drivers/ddi/storport/nf-storport-storportgetsystemaddress)                                     |
| [**ChangerClassAllocatePool**](/windows-hardware/drivers/ddi/mcd/nf-mcd-changerclassallocatepool)                                     |
| Display                                                                                              |
| [*DxgkCbMapMemory*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkcb_map_memory)                                                         |
| [**VideoPortAllocatePool**](/windows-hardware/drivers/ddi/video/nf-video-videoportallocatepool)                                           |
| Audio Miniport                                                                                       |
| [**IMiniportDMus::NewStream**](/windows-hardware/drivers/ddi/dmusicks/nf-dmusicks-iminiportdmus-newstream)                                        |
| [**IMiniportMidi::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportmidi-newstream)                                        |
| [**IMiniportWaveCyclic::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavecyclic-newstream)                            |
| [**IPortWavePci::NewMasterDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iportwavepci-newmasterdmachannel)                      |
| [**IMiniportWavePci::NewStream**](/windows-hardware/drivers/ddi/portcls/nf-portcls-iminiportwavepci-newstream)                                  |
| Audio Port Class                                                                                     |
| [**PcNewDmaChannel**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewdmachannel)                                                         |
| [**PcNewResourceList**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcelist)                                                     |
| [**PcNewResourceSublist**](/windows-hardware/drivers/ddi/portcls/nf-portcls-pcnewresourcesublist)                                               |
| IFS                                                                                                  |
| [**FltAllocatePoolAlignedWithTag**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatepoolalignedwithtag)                              |
| [**FltAllocateContext**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltallocatecontext)                                                    |
| WDF                                                                                                  |
| [**WdfLookasideListCreate**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdflookasidelistcreate)                                             |
| [**WdfMemoryCreate**](/windows-hardware/drivers/ddi/wdfmemory/nf-wdfmemory-wdfmemorycreate)                                                           |
| [**WdfDeviceAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandqueryproperty)                             |
| [**WdfDeviceAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceallocandquerypropertyex)                         |
| [**WdfFdoInitAllocAndQueryProperty**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandqueryproperty)                           |
| [**WdfFdoInitAllocAndQueryPropertyEx**](/windows-hardware/drivers/ddi/wdffdo/nf-wdffdo-wdffdoinitallocandquerypropertyex)                       |
| [**WdfIoTargetAllocAndQueryTargetProperty**](/windows-hardware/drivers/ddi/wdfiotarget/nf-wdfiotarget-wdfiotargetallocandquerytargetproperty)             |
| [**WdfRegistryQueryMemory**](/windows-hardware/drivers/ddi/wdfregistry/nf-wdfregistry-wdfregistryquerymemory)                                             |




## Driver Verifier code integrity

Use the Driver Verifier code integrity option flag (0x02000000) to enable extra checks that validate compliance with this feature. To enable this from the command line, use the following command.

```console
verifier.exe /flags 0x02000000 /driver <driver.sys>
```

To choose this option if using the verifier GUI, select *Create custom settings* (for code developers), select *Next*, and then select _Code integrity checks_.

You can use the verifier command line /query option to display the current driver verifier information.

```console
verifier /query
```

### See Also

[Driver security checklist](driver-security-checklist.md)
