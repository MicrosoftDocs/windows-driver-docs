---
title: Starting a Device in a Bus Driver
author: windows-driver-content
description: Starting a Device in a Bus Driver
ms.assetid: 1babeabb-1866-4ca5-b5a3-380c246596e5
keywords: ["bus drivers WDK PnP"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Starting a Device in a Bus Driver


## <a href="" id="ddk-starting-a-device-in-a-bus-driver-kg"></a>


A bus driver starts a child device (child [*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) with a procedure such as the following in its [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine:

1.  Start the device.

    The exact steps vary from device to device.

    For example, the PCI bus driver programs its mapping registers to enable requests on the PCI bus. The PnP ISA bus driver enables the PnP ISA card so the function driver can access it.

2.  Complete the IRP.

    If the bus driver's start operations were successful, the driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS and calls [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) specifying a priority boost of IO\_NO\_INCREMENT. The bus driver returns STATUS\_SUCCESS from its *DispatchPnP* routine.

    If the bus driver encounters an error during its start operations, the driver sets an error status in the IRP, calls **IoCompleteRequest** with IO\_NO\_INCREMENT, and returns the error from its *DispatchPnP* routine.

If a bus driver requires some time to start the device, it can mark the IRP as pending and return STATUS\_PENDING.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Starting%20a%20Device%20in%20a%20Bus%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


