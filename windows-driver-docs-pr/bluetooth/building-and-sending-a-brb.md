---
title: Building and Sending a BRB
description: Building and Sending a BRB
ms.assetid: 53a692e7-9c71-4dca-9331-32ac97b94179
keywords:
- Bluetooth WDK , Bluetooth request blocks
- BRBs WDK
- Bluetooth WDK , request blocks
- sending BRBs
- return values WDK Bluetooth
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Building and Sending a BRB


The following procedure outlines the general process that a profile driver follows to build and send a Bluetooth request block (BRB). A BRB is a block of data that describes the Bluetooth operation to perform.

### <span id="to_build_and_send_a_brb"></span><span id="TO_BUILD_AND_SEND_A_BRB"></span>To Build and Send a BRB

1.  Allocate an IRP. For more information about how to use IRPs, see [Handling IRPs](https://msdn.microsoft.com/library/windows/hardware/ff546847).

2.  Allocate a BRB. To allocate BRBs, call the [**BthAllocateBrb**](https://msdn.microsoft.com/library/windows/hardware/ff536634) function that the Bluetooth driver stack exports for use by profile drivers. To obtain a pointer to the *BthAllocateBrb* function, see [Querying for Bluetooth Interfaces](querying-for-bluetooth-interfaces.md).

3.  Initialize the parameters of the BRB. Each BRB uses a corresponding structure. Set the members of the structure according to the intended use. For a list of BRBs and their corresponding structures see [Using the Bluetooth Driver Stack](using-the-bluetooth-driver-stack.md).

4.  Initialize the parameters of the IRP. Set the **MajorFunction** member of the IRP to IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL. Set the **Parameters.DeviceIoControl.IoControlCode** member to IOCTL\_INTERNAL\_BTH\_SUBMIT\_BRB. Set the **Parameters.Others.Argument1** member to point to the BRB.

5.  Pass the IRP down the driver stack. Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to send the IRP to the next-lower driver.

The following pseudocode example demonstrates how to set up a L2CAP Ping BRB for the Bluetooth driver stack to process.

**Note**  For readability, the following pseudocode example does not demonstrate error handling.

 

```
#include <bthddi.h>

// Code for obtaining the BthInterface pointer

// Define a custom pool tag to identify your profile driver&#39;s dynamic memory allocations.
// You should change this tag to easily identify your driver&#39;s allocations from other drivers.
#define PROFILE_DRIVER_POOL_TAG &#39;_htB&#39;

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[bltooth\bltooth]:%20Building%20and%20Sending%20a%20BRB%20%20RELEASE:%20%283/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




