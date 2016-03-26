---
title: Handling I/O Requests in a KMDF Driver for a Bus-Master DMA Device
description: This topics in this section describe how a KMDF driver for a bus-master DMA device processes an I/O request. If you are writing a KMDF driver that implements system-mode DMA, see Supporting System-Mode DMA.
ms.assetid: c94819c5-212d-404f-a7c7-b736e0832282
keywords: ["DMA operations WDK KMDF , I/O requests", "bus-master DMA WDK KMDF , I/O requests", "I/O requests WDK KMDF , DMA devices", "request processing WDK KMDF , DMA devices"]
---

# Handling I/O Requests in a KMDF Driver for a Bus-Master DMA Device


\[Applies to KMDF only\]

This topics in this section describe how a KMDF driver for a bus-master DMA device processes an I/O request. If you are writing a KMDF driver that implements system-mode DMA, see [Supporting System-Mode DMA](supporting-system-mode-dma.md).

## <a href="" id="ddk-how-to-program-an-i-o-request-for-a-dma-device-df"></a>


Handling I/O requests in a KMDF driver for a bus-master DMA device requires code in several of the driver’s event callback functions, as shown in the following figure:

![dma implementation in kmdf drivers](images/dma-implementation-in-kmdf.png)

As shown above, DMA-related processing takes place in four phases:

1.  Your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) or [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function must [enable DMA transactions](enabling-dma-transactions.md) for the device, so that your driver can use the framework's DMA capabilities. The same callback function must also [create a common buffer](using-common-buffers.md) if your device and driver require access to a shared memory buffer.

2.  When your driver receives an I/O request that requires the device to perform a DMA operation, one of the driver's [request handlers](request-handlers.md) must [create and initialize a new DMA transaction](creating-and-initializing-a-dma-transaction.md). (Note that if your driver [reuses DMA transaction objects](reusing-dma-transaction-objects.md), your driver's [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function can create the transaction objects.) Then, the request handler must [initiate the DMA transaction](starting-a-dma-transaction.md) so that the framework can begin breaking the transaction into smaller DMA transfers, if necessary, and call the driver's [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function.

3.  Your driver's [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function [programs the DMA hardware](programming-dma-hardware.md) for a single DMA transfer and enables device interrupts.

4.  When the device interrupts, the framework calls your driver's [*EvtInterruptIsr*](https://msdn.microsoft.com/library/windows/hardware/ff541735) callback function, which saves volatile device information and schedules execution of the driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function.

    Your driver's [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) callback function [completes each DMA transfer](completing-a-dma-transfer.md) after the hardware finishes processing it. After a DMA transaction's final transfer is complete, the *EvtInterruptDpc* callback function [completes the DMA transaction](completing-a-dma-transaction.md).

Your driver might [reuse its DMA transaction objects](reusing-dma-transaction-objects.md) to ensure that they can operate when memory resources are low.

Your driver can provide a set of callback functions that handle [DMA-specific power management operations](supporting-power-management-for-dma-devices.md).

Some drivers [use common buffers](using-common-buffers.md) that both a device and the driver can access.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Handling%20I/O%20Requests%20in%20a%20KMDF%20Driver%20for%20a%20Bus-Master%20DMA%20Device%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




