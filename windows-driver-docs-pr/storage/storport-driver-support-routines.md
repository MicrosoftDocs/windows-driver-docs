---
title: Storport driver support routines
description: Learn about the Storport driver routines, such as direct memory access and I/O request processing support routines.
keywords:
- Storport driver support routines
- storage WDK
- storage support routines
ms.date: 03/16/2021
ms.localizationpriority: medium
---

# Storport driver support routines

This page categorizes some of the support routines provided to miniports by the system-supplied Storport driver. See [storport.h](/windows-hardware/drivers/ddi/storport) for a complete list.

For a list of Storport driver miniport routines, see [Storport Miniport Driver Routines](storport-miniport-driver-routines.md).

## Direct Memory Access Support Routines

Storport driver provides the following direct memory access (DMA) support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortBuildScatterGatherList** | Creates a scatter/gather list for the specified data buffer. |
| **StorPortGetScatterGatherList** | Retrieves the associated scatter/gather list for the specified SCSI request block (SRB). |
| **StorPortPutScatterGatherList** | Releases any resources associated with a scatter/gather list that was previously created by a call to the **StorPortBuildScatterGatherList** routine. |

## General Support Routines

Storport provides the following general support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortDebugPrint** | Prints a debug string to the kernel debugger, if the debugger is attached. |
| **StorPortEtwEvent2** | Publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are expressed as two name-value pairs. |
| **StorPortEtwEvent4** | Publishes an ETW event to a storage trace channel. The miniport can log four general purpose ETW parameters. The ETW parameters are expressed as four name-value pairs. |
| **StorPortEtwEvent8** | Publishes an ETW event to a storage trace channel. The miniport can log eight general purpose ETW parameters. The ETW parameters are expressed as eight name-value pairs. |
| **StorPortGetActivityIdSrb** | Retrieves the ETW activity ID associated with a request block. |
| **StorPortGetDeviceObjects** | Returns the device objects that are associated with the adapter device stack. The device objects that will be returned are the functional and physical device objects of the adapter and the device object to which the functional device object is attached. |
| **StorPortGetSystemPortNumber** | Retrieves the system assigned port number for a storage adapter. |
| **StorPortInitializeSListHead** | Initializes the head of a Storport-managed singly linked list. |
| **StorPortInterlockedFlushSList** | Removes all items from a Storport-managed singly linked list. Access to the list is synchronized on a multiprocessor system |
| **StorPortInterlockedPopEntrySList** | Removes an item from the front of a Storport-managed singly linked list. Access to the list is synchronized on a multiprocessor system.  |
| **StorPortInterlockedPushEntrySList** | Inserts an item at the front of a Storport-managed singly linked list. Access to the list is synchronized on a multiprocessor system. |
| **StorPortInvokeAcpiMethod** | Executes an ACPI method for a storage device. |
| **StorPortIsCurrentOsInstallationUpgrade** | Checks if the current installation of Windows is an upgrade from a previous version or not. |
| **StorPortIsDeviceOperationAllowed** | Allows a miniport to determine if operations for a certain device management class are allowed. |
| **StorPortLogError** | Notifies the port driver that an error occurred. |
| **StorPortLogSystemEvent** | Gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues. It provides a better alternative to **StorPortLogError**. |
| **StorPortQueryDepthSList** | Retrieves the number of entries in a Storport-managed singly linked list. |
| **StorPortQueryPerformanceCounter** | Queries and returns the current system performance counter value. |
| **StorPortQuerySystemTime** | Obtains the current system time. |
| **StorPortRegistryRead** | Reads the registry data for the indicated device and value. |
| **StorPortRegistryReadAdapterKey** | Reads the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/\<Instance path>/DeviceParameters/....|
| **StorPortRegistryWriteAdapterKey** | Writes the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/\<Instance path>/DeviceParameters/.... |
| **StorPortRegistryWrite** | Converts the registry data contained in a specified buffer from ASCII to Unicode and then writes the data to the miniport driver's per-HBA storage area. |

## I/O Request Processing Support Routines

Storport provides the following I/O request processing support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortBusy** | Notifies the port driver that the adapter is currently busy, handling outstanding requests. |
| **StorPortCompleteRequest** | Completes all outstanding requests setting the SRB status value to SrbStatus. |
| **StorPortCompleteServiceIrp** | Called by a Storport virtual miniport driver when it needs to complete a request that it received in its HwStorProcessServiceRequest callback routine. |
| **StorPortDeviceBusy** | Notifies the port driver that the specified logical unit is currently busy, handling outstanding requests. |
| **StorPortDeviceReady** | Notifies the port driver that the indicated logical unit is ready to handle new requests. |
| **StorPortFreeWorker** | Frees a Storport work item previously allocated by the **StorPortInitializeWorker** routine. |
| **StorPortGetRequestInfo** | Retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a STOR_REQUEST_INFO structure. |
| **StorPortInitializeWorker** | Creates a new Storport work item that runs in a system worker thread. |
| **StorPortQueueWorkItem** | Schedules a Storport work item to execute within the context of a system worker thread. |
| **StorPortPause** | Pauses an adapter for the specified period of time. |
| **StorPortPauseDevice** | Pauses a specific logical unit device for the specified period of time. |
| **StorPortReady** | Notifies the port driver that the adapter is no longer busy. |
| **StorPortResume** | Resumes a paused adapter. |
| **StorPortResumeDevice** | Resumes a previously paused logical unit. |

## Initialization Support Routines

Storport driver provides the following initialization support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortEnablePassiveInitialization** | Enables the miniport's HwStorPassiveInitializeRoutine callback routine to execute at PASSIVE_LEVEL during miniport initialization. |
| **StorPortGetActiveGroupCount** | Returns the number of processor groups that are present in the system. |
| **StorPortGetActiveNodeCount** | Returns the number of nodes that are present in the system. |
| **StorPortGetBusData** | Retrieves the bus-specific configuration information necessary to initialize the HBA. |
| **StorPortGetCurrentProcessorNumber** | Retrieves the current processor number from the kernel. |
| **StorPortGetGroupAffinity** | Constructs a mask of the active processors in a requested group. |
| **StorPortGetHighestNodeNumber** | Returns the largest possible node number on the system. |
| **StorPortGetLogicalProcessorRelationship** | Returns relationship information for one or more specified types. These types include groups, physical packages, and nodes in the host system. The information that is returned includes processor affinity masks that are composed of the logical processors in the host system. These logical processors share the specified relationship types. |
| **StorPortGetLogicalUnit** | Returns a pointer to the miniport driver's per-logical-unit storage area. |
| **StorPortGetNodeAffinity** | Constructs a mask of the active processors in a requested non-uniform memory access (NUMA) node. |
| **StorPortGetStartIoPerfParams** | Places the performance parameters for a given I/O request in a STARTIO_PERFORMANCE_PARAMETERS structure. |
| **StorPortInitialize** | Initializes the port driver parameters and extension data. **StorPortInitilize** also saves the adapter information provided from the miniport driver. |
| **StorPortInitializePerfOpts** | Initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF_CONFIGURATION_DATA structure. |
| **StorPortSetAdapterBusType** | Used to adjust the BusType of the adapter depending on its current configuration. Setting the BusType with this routine will allow you to override the global property set in the miniport INF without having to re-install the driver. This is useful for scenarios such as RAID support or support for multiple adapters with a different bus type. |
| **StorPortSetBusDataByOffset** | Writes bus-specific configuration information. |
| **StorPortSetDeviceQueueDepth** | Sets the maximum depth of the device queue for the indicated device. |
| **StorPortSetPowerSettingNotificationGuids** | Enables a miniport to receive power setting notifications. The miniport registers an array of GUIDs which identify the power settings to receive power change notifications for. |
| **StorPortSetUnitAttributes** | Registers the power attributes of a storage unit device with the Storport driver. |

## Interrupt Support Routines

Storport driver provides the following interrupt support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortGetMSIInfo** | Retrieves the message signaled interrupt (MSI) information for the specified message. |
| **StorPortSynchronizeAccess** | Provides synchronized access to a miniport driver's device extension. |
| **StorPortInitializeDpc** | Initializes a StorPort deferred procedure call (DPC.) |
| **StorPortIssueDpc** | Issues a Storport DPC. |
| **StorPortStallExecution** | Stalls the miniport driver. |

## Locking Support Routines

Storport driver provides the following locking support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortAcquireMSISpinLock** | Acquires the message signaled interrupt (MSI) spin lock that is associated with the specified message. |
| **StorPortAcquireSpinLock** | Acquires the specified spin lock. |
| **StorPortReleaseMSISpinLock** | Releases a previously acquired MSI spin lock for the specified message. |
| **StorPortReleaseSpinLock** | Releases a spinlock acquired by **StorPortAcquireSpinLock**. |

## Memory Management Support Routines

Storport driver provides the following memory management support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortAllocateContiguousMemorySpecifyCacheNode** | Allocates a range of physically contiguous noncached, nonpaged memory. |
| **StorPortAllocateMdl** | Allocates an MDL to describe the given non-paged pool memory. |
| **StorPortAllocatePool** | Allocates a block of non-contiguous, non-paged pool memory. |
| **StorPortAllocateRegistryBuffer** | Allocates a buffer that can a miniport can use to read and write registry data. |
| **StorPortBuildMdlForNonPagedPool** | Updates the MDL to describe the associated non-paged memory. |
| **StorPortConvertUlongToPhysicalAddress** | Converts an unsigned long address into a physical address. |
| **StorPortConvertPhysicalAddressToULong64** | Converts a physical address to a ULONG64 value. |
| **StorPortFreeMdl** | Frees a memory descriptor list (MDL) describing non-paged pool memory. |
| **StorPortFreeContiguousMemorySpecifyCache** | Deallocates a range of noncached memory in the nonpaged portion of the system address space. |
| **StorPortFreePool** | Frees a block of memory that was previously allocated by a call to the **StorPortAllocatePool** routine. |
| **StorPortFreeRegistryBuffer** | Frees the buffer that was allocated for storing registry data. |
| **StorPortGetDataInBufferMdl** | Returns an MDL associated with the input data buffer of a SCSI request block (SRB). |
| **StorPortGetDataInBufferScatterGatherList** | Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB). |
| **StorPortGetDataInBufferSystemAddress** | Returns the system address for the input data buffer of a SCSI request block (SRB). |
| **StorPortGetOriginalMdl** | Returns the MDL associated with the given SRB. |
| **StorPortGetVirtualAddress** | Obtains a virtual address that maps to the indicated physical address. |
| **StorPortGetPhysicalAddress** | Converts a given virtual address range to a physical address range for a DMA operation. |
| **StorPortGetSystemAddress** | Returns a virtual address in system space for the data buffer of the specified SCSI request block (SRB). |
| **StorPortGetUncachedExtension** | Allocates an uncached common buffer to be shared by the CPU and the device. |
| **StorPortMarkDumpMemory** | A miniport should mark memory used for the dump file or the hibernation file. Marked memory is retained and remains valid after a resume from hibernation operation. The memory to mark is specified by an address and range length in a call to **StorPortMarkDumpMemory**. |
| **StorPortMoveMemory** | Copies memory from one buffer to another. |

## Notification Support Routines

Storport driver provides the following notification support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortAsyncNotificationDetected** | Notifies the Storport driver of a storage device status change event. |
| **StorPortNotification** | Notifies the Storport driver of certain events and conditions. |
| **StorPortStateChangeDetected** | Notifies the Storport port driver of a state change for a logical unit number (LUN), host bus adapter (HBA) port, or target device. |

## Port and Register I/O Support Routines

Storport driver provides the following port and register I/O support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortGetDeviceBase** | Maps an I/O address to system address space. |
| **StorPortFreeDeviceBase** | Frees a range of device I/O memory that was mapped by StorPortGetDeviceBase. |
| **StorPortReadPortBufferUchar** | Reads a value from a specified port address |
| **StorPortReadPortBufferUlong** | Reads a value from a specified port address. |
| **StorPortReadPortBufferUshort** | Reads a value from a specified port address. |
| **StorPortReadPortUchar** | Reads a value from a specified port address |
| **StorPortReadPortUlong** | Reads a value from a specified port address. |
| **StorPortReadPortUshort** | Reads a value from a specified port address. |
| **StorPortReadRegisterBufferUchar** | Reads a value from a specified register address. |
| **StorPortReadRegisterBufferUlong** | Reads a value from a specified register address. |
| **StorPortReadRegisterBufferUlong64** | Reads a number of ULONG64 values from the specified 64-bit register address into a buffer. |
| **StorPortReadRegisterBufferUshort** | Reads a value from a specified register address. |
| **StorPortReadRegisterUchar** | Reads a value from a specified register address. |
| **StorPortReadRegisterUlong** | Reads a value from a specified register address. |
| **StorPortReadRegisterUlong64** | Reads a 64-bit value from a specified 64-bit register address. |
| **StorPortReadRegisterUshort** | Reads a value from a specified register address. |
| **StorPortValidateRange** | Determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems. |
| **StorPortWritePortBufferUchar** | Writes a value to a specified register address. |
| **StorPortWritePortBufferUlong** | Writes a value to a specified register address. |
| **StorPortWritePortBufferUshort** | Writes a value to a specified register address. |
| **StorPortWritePortUchar** | Writes a value to a specified register address. |
| **StorPortWritePortUlong** | Writes a value to a specified register address. |
| **StorPortWritePortUshort** | Writes a value to a specified register address. |
| **StorPortWriteRegisterBufferUchar** | Transfers a given number of unsigned bytes from a buffer to the HBA. |
| **StorPortWriteRegisterBufferUlong** | Transfers a given number of ULONG values from a buffer to the HBA. |
| **StorPortWriteRegisterBufferUlong64** | Writes a number of ULONG64 values from a the specified 64-bit register address. |
| **StorPortWriteRegisterBufferUshort** | Transfers a given number of USHORT values from a buffer to the HBA. |
| **StorPortWriteRegisterUchar** | Transfers a given number of character values from a buffer to the indicated HBA register address. |
| **StorPortWriteRegisterUlong** | Transfers a ULONG value to the indicated HBA register address. |
| **StorPortWriteRegisterUlong64** | Writes a ULONG64 value to the specified register address. |
| **StorPortWriteRegisterUshort** | Transfers a ULONG value to the indicated HBA register address.|

## Runtime Power Management Support Routines

Storport driver provides the following runtime power management support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortInitializePoFxPower** | Registers a storage device with the power management framework (PoFx). |
| **StorPortPoFxActivateComponent** | Increments the activation reference count on the specified component of a storage device. |
| **StorPortPoFxIdleComponent** | Decrements the activation reference count of a specified component of a storage device. |
| **StorPortPoFxPowerControl** | Sends a power control request to the power management framework (PoFx) to forward to the power engine plug-in (PEP). |
| **StorPortPoFxSetComponentLatency** | Specifies the maximum latency that can be tolerated in the transition from the idle condition to the active condition in the specified storage device component. |
| **StorPortPoFxSetComponentResidency** | Sets the estimated time for how long a storage device component is likely to remain idle after the component enters the idle condition. |

## Timer Support Routines

Storport driver provides the following timer support routines.

| Routine | Description |
| ------- | ----------- |
| **StorPortFreeTimer** | Frees a Storport timer context object previously created by the **StorPortInitializeTimer** routine. |
| **StorPortInitializeTimer** | Creates a Storport timer context object. |
| **StorPortRequestTimer** | Schedules a callback event for a Storport timer context object. |
