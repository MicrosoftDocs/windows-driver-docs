---
title: Reserving DMA Resources
description: Reserving DMA Resources
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 8C5FF779-8D54-47D9-8EC6-7D4921F8F697
---

# Reserving DMA Resources


\[Applies to KMDF only\]

Typically, framework-based drivers do not reserve map registers ahead of time. However, in certain circumstances, drivers may need to reserve these resources in advance.

Framework-based drivers running on Windows 8 or later can reserve a specified number of map registers for a DMA enabler that specifies a packet or system profile. To do so, the driver calls [**WdfDmaTransactionAllocateResources**](https://msdn.microsoft.com/library/windows/hardware/hh451123) and registers an [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425) callback function.

The framework calls the driver's [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425) function when it has reserved the map registers and the WDM DMA adapter's lock. The driver can then initialize and initiate the transaction multiple times using the same transaction object before finally releasing the transaction object. To release the DMA resources back to the system, the driver calls [**WdfDmaTransactionFreeResources**](https://msdn.microsoft.com/library/windows/hardware/hh451177).

To determine the number of map registers required for a transaction, the driver can call [**WdfDmaTransactionGetTransferInfo**](https://msdn.microsoft.com/library/windows/hardware/hh451179) before calling [**WdfDmaTransactionAllocateResources**](https://msdn.microsoft.com/library/windows/hardware/hh451123). The driver must initialize the transaction before calling **WdfDmaTransactionGetTransferInfo**.

The following steps demonstrate how a driver can reserve and release a DMA enabler for exclusive use with a specified transaction:

1.  The driver receives an I/O request.

2.  The driver's [request handler](request-handlers.md) calls [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create a DMA transaction object for the request.

3.  The driver's [request handler](request-handlers.md) calls [**WdfDmaTransactionAllocateResources**](https://msdn.microsoft.com/library/windows/hardware/hh451123) to reserve resources.

4.  The framework calls [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425) when it has reserved the requested resources.

5.  In [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425), the driver calls [**WdfDmaTransactionInitializeUsingRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547107) or [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099) to initialize the transaction object.

6.  In [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425), the driver calls the [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062) method to start the transaction. Because the transaction has reserved resources, the framework immediately calls the driver's [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function.

7.  From [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDmaTransactionDmaTransferComplete*](https://msdn.microsoft.com/library/windows/hardware/hh406418), the driver calls [**WdfDmaTransactionDmaCompleted**](https://msdn.microsoft.com/library/windows/hardware/ff547039), [**WdfDmaTransactionDmaCompletedWithLength**](https://msdn.microsoft.com/library/windows/hardware/ff547052), or [**WdfDmaTransactionDmaCompletedFinal**](https://msdn.microsoft.com/library/windows/hardware/ff547049), followed by [**WdfObjectDelete**](https://msdn.microsoft.com/library/windows/hardware/ff548734) or [**WdfDmaTransactionRelease**](https://msdn.microsoft.com/library/windows/hardware/ff547114). The driver must not delete or release the transaction until the transaction has been completed or canceled. After the completion of this step, the map registers remain reserved.

8.  The driver can repeat steps 5–7 as many times as necessary.

    When the driver no longer needs the reservation, the driver calls [**WdfDmaTransactionFreeResources**](https://msdn.microsoft.com/library/windows/hardware/hh451177) from [*EvtInterruptDpc*](https://msdn.microsoft.com/library/windows/hardware/ff541721) or [*EvtDmaTransactionDmaTransferComplete*](https://msdn.microsoft.com/library/windows/hardware/hh406418). Alternatively, the driver can call **WdfDmaTransactionFreeResources** from its [*EvtReserveDma*](https://msdn.microsoft.com/library/windows/hardware/hh406425) event callback function.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Reserving%20DMA%20Resources%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




