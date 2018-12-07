---
title: Reserving DMA Resources
description: Reserving DMA Resources
ms.assetid: 8C5FF779-8D54-47D9-8EC6-7D4921F8F697
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





