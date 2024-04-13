---
title: Building and Sending a Bluetooth Request Block (BRB)
description: Building and sending a Bluetooth request block (BRB)
keywords:
- Bluetooth WDK , Bluetooth request blocks
- BRBs WDK
- Bluetooth WDK , request blocks
- sending BRBs
- return values WDK Bluetooth
ms.date: 01/10/2024
---

# Building and sending a Bluetooth request block (BRB)

The following procedure outlines the general process that a profile driver follows to build and send a Bluetooth request block (BRB). A BRB is a block of data that describes the Bluetooth operation to perform.

## To build and send a BRB

1. Allocate an IRP. For more information about how to use IRPs, see [Handling IRPs](../kernel/handling-irps.md).
1. Allocate a BRB. To allocate BRBs, call the [**BthAllocateBrb**](/windows-hardware/drivers/ddi/bthddi/nc-bthddi-pfnbth_allocate_brb) function that the Bluetooth driver stack exports for use by profile drivers. To obtain a pointer to the *BthAllocateBrb* function, see [Querying for Bluetooth Interfaces](querying-for-bluetooth-interfaces.md).
1. Initialize the parameters of the BRB. Each BRB uses a corresponding structure. Set the members of the structure according to the intended use. For a list of BRBs and their corresponding structures see [Using the Bluetooth Driver Stack](using-the-bluetooth-driver-stack.md).
1. Initialize the parameters of the IRP. Set the **MajorFunction** member of the IRP to IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL. Set the **Parameters.DeviceIoControl.IoControlCode** member to IOCTL\_INTERNAL\_BTH\_SUBMIT\_BRB. Set the **Parameters.Others.Argument1** member to point to the BRB.
1. Pass the IRP down the driver stack. Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to send the IRP to the next-lower driver.

The following pseudocode example demonstrates how to set up a L2CAP Ping BRB for the Bluetooth driver stack to process. For readability, the example does not demonstrate error handling.

```cpp
#include <bthddi.h>

// Code for obtaining the BthInterface pointer

// Define a custom pool tag to identify your profile driver's dynamic memory allocations.
// You should change this tag to easily identify your driver's allocations from other drivers.
#define PROFILE_DRIVER_POOL_TAG '_htB'

PIRP Irp;
Irp = IoAllocateIrp( DeviceExtension->ParentDeviceObject->StackSize, FALSE );

PBRB_L2CA_PING BrbPing; // Define storage for a L2CAP Ping BRB

// Allocate the Ping BRB
BrbPing = BthInterface->BthAllocateBrb( BRB_L2CA_PING, PROFILE_DRIVER_POOL_TAG );

// Set up the next IRP stack location
PIO_STACK_LOCATION NextIrpStack;
NextIrpStack = IoGetNextIrpStackLocation( Irp );
NextIrpStack->MajorFunction = IRP_MJ_INTERNAL_DEVICE_CONTROL;
NextIrpStack->Parameters.DeviceIoControl.IoControlCode = IOCTL_INTERNAL_BTH_SUBMIT_BRB;
NextIrpStack->Parameters.Others.Argument1 = BrbPing;

// Pass the IRP down the driver stack
NTSTATUS Status;
Status = IoCallDriver( DeviceExtension->NextLowerDriver, Irp );
```
