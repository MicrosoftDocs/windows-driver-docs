---
title: ATA port driver support routines
description: Describes the ATA port driver routines
keywords:
- ATA driver support routines
- storage WDK
- storage support routines
ms.date: 10/08/2019
ms.localizationpriority: medium
---

# ATA port driver support routines

This page categorizes the support routines provided by the system-supplied ATA port driver.

For a list of ATA driver miniport routines, see [ATA Miniport Drivers](ata-miniport-drivers.md).

## Initialization Routine

ATA port driver provides the following initialization routine.

| Routine | Description |
| ------- | ----------- |
| **AtaPortInitializeEx** | Initializes the port and miniport drivers. |

## Routines for PCI Config Space Access

ATA port driver provides the following routines to help you read and modify the contents of the device's PCI configuration space.

| Routine | Description |
| ------- | ----------- |
| **AtaPortGetBusData** | Retrieves data from the specified location within the device's PCI configuration space. |
| **AtaPortSetBusData** | stores the data in the indicated device's PCI configuration space at the specified offset. |
|

## Routines for Processing I/O Requests

ATA port driver provides the following I/O request processing support routines.

| Routine | Description |
| ------- | ----------- |
| **AtaPortGetScatterGatherList** | Retrieves the scatter/gather list associated with this request. |
| **AtaPortGetPhysicalAddress** | Converts the virtual address range to the physical address range. |
| **AtaPortGetDeviceBase** | Returns a mapped logical base address that is used to communicate with a host bus adapter (HBA). |
| **AtaPortGetUncachedExtension** | Allocates an uncached common buffer that is shared by the CPU and the device. |
| **AtaPortBuildRequestSenseIrb** | Builds and returns an IRB for operation code SCSIOP_REQUEST_SENSE. |
| **AtaPortReleaseRequestSenseIrb** | Frees the request sense IRB that is allocated by using **AtaPortBuildRequestSenseIrb**. |
| **AtaPortCompleteAllActiveRequests** | Completes all active IRBs for the indicated device. |
| **AtaPortCompleteRequest** | Completes the indicated IRB. |

## Callback Routines

The miniport driver uses several routines to request a callback from the port driver.

| Routine | Description |
| ------- | ----------- |
| **AtaPortRequestWorkerRoutine** | Requests a worker routine. |
| **AtaPortRequestSynchronizedRoutine** | Requests synchronization with the interrupt service routine (ISR). |
| **AtaPortControllerSyncRoutine** | Provides synchronized access to data structures that are shared across all channels on a controller. |
| **AtaPortRequestTimer** | Requests a timer callback. |

## Routines that Report a Configuration Change

The following routines enable the miniport driver to notify the ATA port driver of changes to the configuration of the devices that are attached to the channel.

| Routine | Description |
| ------- | ----------- |
| **AtaPortBusChangeDetected** | Notifies the port driver of changes in the device configuration on the indicated channel. |
| **AtaPortRequestPowerStateChange** | Requests a power state transition for the indicated device. |

## Routines to Control Request Queues

The port driver maintains one per logical unit number (LUN) request queue and one request queue for each channel. The miniport driver can use the following routines to pause and resume the different request queues.

| Routine | Description |
| ------- | ----------- |
| **AtaPortDeviceBusy** | Informs the port driver that the indicated device is busy. |
| **AtaPortDeviceReady** | Informs the port driver that the indicated device is ready to accept new requests. |

## Utility Routines

The following routines are general utility support functions for miniport drivers.

| Routine | Description |
| ------- | ----------- |
| **AtaPortCopyMemory** | Copies data from one location to another. |
| **AtaPortMoveMemory routine | Copies data from one location to another. |
| **AtaPortConvertUlongToPhysicalAddress** | Converts a given ULONG address into a value of type IDE_PHYSICAL_ADDRESS. |
| **AtaPortConvertPhysicalAddressToUlong** | Truncates an address of type IDE_PHYSICAL_ADDRESS to a ULONG. |
| **AtaPortStallExecution** | Stalls in the miniport driver. |
| **AtaPortInitializeQueueTag** | Initializes the queue tag list for the specified device. |
| **AtaPortAllocateQueueTag** | Returns a queue tag for the specified device. |
| **AtaPortReleaseQueueTag** | Releases the specified queue tag. |

## Debug and Error Reporting Routines

The following routine can be used for debug and error reporting.

| Routine | Description |
| ------- | ----------- |
| **AtaPortDebugPrint** | Passes a message string to the kernel debugger for the debugger to print. |

## Routines for Device Port and Register Access

ATA port driver provides the following port and register access support routines.

| Routine | Description |
| ------- | ----------- |
| **AtaPortReadPortBufferUchar** | Transfers a given number of unsigned byte values from the HBA to a buffer. |
| **AtaPortReadPortBufferUlong** | Transfers a given number of ULONG values from the HBA to a buffer. |
| **AtaPortReadPortBufferUshort** | Transfers a given number of USHORT values from the HBA to a buffer. |
| **AtaPortReadPortUchar** | Reads an unsigned byte value from the HBA. |
| **AtaPortReadPortUlong** | Reads a ULONG value from the HBA. |
| **AtaPortReadPortUshort** | Reads a USHORT value from the HBA. |
| **AtaPortReadRegisterBufferUchar** | Transfers a specified number of unsigned bytes from the HBA to a buffer. |
| **AtaPortReadRegisterBufferUlong** | Transfers a specified number of ULONG from the HBA to a buffer. |
| **AtaPortReadRegisterBufferUshort** | Transfers a specified number of USHORT from the HBA to a buffer. |
| **AtaPortReadRegisterUchar** | Reads an unsigned byte value from the HBA. |
| **AtaPortReadRegisterUlong** | Reads a ULONG value from the HBA. |
| **AtaPortReadRegisterUshort** | Reads a USHORT value from the HBA. |
| **AtaPortWritePortBufferUchar** | Writes a value to a specified register address. |
| **AtaPortWritePortBufferUlong** | Writes a value to a specified register address. |
| **AtaPortWritePortBufferUshort** | Writes a value to a specified register address. |
| **AtaPortWritePortUchar** | Transfers an unsigned byte value to the HBA. |
| **AtaPortWritePortUlong** | Transfers a ULONG value to the HBA. |
| **AtaPortWritePortUshort** | Transfers a USHORT value to the HBA. |
| **AtaPortWriteRegisterBufferUchar** | Transfers the specified number of unsigned bytes from a buffer to the HBA. |
| **AtaPortWriteRegisterBufferUlong** | Transfers the specified number of ULONG values from a buffer to the HBA. |
| **AtaPortWriteRegisterBufferUshort** | Transfers the specified number of USHORT values from a buffer to the HBA. |
| **AtaPortWriteRegisterUchar** | Transfers an unsigned byte to the HBA address. |
| **AtaPortWriteRegisterUlong** | Transfers a ULONG value to the HBA address. |
| **AtaPortWriteRegisterUshort** | Transfers a USHORT value to the HBA address.|

## Routines for Registry Access

A miniport driver that implements the channel interface can call the following routines to access the Windows registry. Miniport drivers that only implement the controller interface routines cannot access these routines.

| Routine | Description |
| ------- | ----------- |
| **AtaPortRegistryAllocateBuffer** | Allocates a buffer for registry operations. |
| **AtaPortRegistryFreeBuffer** | Frees the registry buffer that was allocated by using **AtaPortRegistryAllocateBuffer**. |
| **AtaPortRegistryControllerKeyRead** | Reads the data that is associated with the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*, where *N* is the number of the controller. |
| **AtaPortRegistryContrlollerKeyWrite** | Writes the data to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*, where *N* is the number of the controller. |
| **AtaPortRegistryControllerKeyWriteDeferred** | Writes the data asynchronously to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*, where *N* is the number of the controller. |
| **AtaPortRegistryChannelSubKeyRead** | Reads the data that is associated with the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*\Channel*M*, where *N* is the number of the controller and *M* is the number of the channel. |
| **AtaPortRegistryChannelSubKeyWrite** | Writes the data to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*\Channel*M*, where *N* is the number of the controller and *M* is the number of the channel. |
| **AtaPortRegistryChannelSubKeyWriteDeferred** | Writes the data asynchronously to the indicated value name under the registry key HKLM\\CurrentControlSet\\Services\\&lt;service name&gt;\Controller*N*\Channel*M*, where *N* is the number of the controller and *M* is the number of the channel. |
