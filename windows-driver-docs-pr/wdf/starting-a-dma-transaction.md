---
title: Starting a DMA Transaction
description: Starting a DMA Transaction
ms.assetid: fa26ef08-01c0-4502-9cb3-865000242e4a
keywords:
- DMA transactions WDK KMDF , starting
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
- starting DMA transactions WDK KMDF
- scatter/gather DMA WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Starting a DMA Transaction


\[Applies to KMDF only\]




After your driver has [created and initialized a DMA transaction](creating-and-initializing-a-dma-transaction.md), the driver can call the [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062) method to start the transaction. This method builds a scatter/gather list for the first [DMA transfer](dma-transactions-and-dma-transfers.md) that is associated with the transaction. Next, the method calls the [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function that the driver registered for the transaction. The callback function [programs the DMA hardware](programming-dma-hardware.md) to start the transfer.

Before your driver calls **WdfDmaTransactionExecute**, the driver must store the DMA transaction handle so that it can be retrieved later when the driver completes each DMA transfer that is associated with the transaction. A good place to store the transaction handle is in the context memory of a framework object, typically the device's framework device object. For more information about using object context memory, see [Framework Object Context Space](framework-object-context-space.md).

The following code example from the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample shows how to initialize and then execute a DMA transaction. This code appears in the *Read.c* file.

```cpp
VOID PLxEvtIoRead(
    IN WDFQUEUE         Queue,
    IN WDFREQUEST       Request,
    IN size_t           Length
    )
{
    NTSTATUS            status = STATUS_UNSUCCESSFUL;
    PDEVICE_EXTENSION   devExt;
    // Get the DevExt from the queue handle
    devExt = PLxGetDeviceContext(WdfIoQueueGetDevice(Queue));
    do {
        // Validate the Length parameter.
        if (Length > PCI9656_SRAM_SIZE)  {
            status = STATUS_INVALID_BUFFER_SIZE;
            break;
        }
        // Initialize the DmaTransaction.
        status = 
           WdfDmaTransactionInitializeUsingRequest(
                 devExt->ReadDmaTransaction,
                 Request, 
                 PLxEvtProgramReadDma, 
                 WdfDmaDirectionReadFromDevice 
           );
        if(!NT_SUCCESS(status)) {
            . . . //Error-handling code omitted
            break; 
        }
        // Execute this DmaTransaction.
        status = WdfDmaTransactionExecute( devExt->ReadDmaTransaction, 
                                           WDF_NO_CONTEXT);
        if(!NT_SUCCESS(status)) {
            . . . //Error-handling code omitted
            break; 
        }
        // Indicate that the DMA transaction started successfully.
        // The DPC routine will complete the request when the DMA
        // transaction is complete.
        status = STATUS_SUCCESS;
    } while (0);
    // If there are errors, clean up and complete the request.
    if (!NT_SUCCESS(status )) {
        WdfDmaTransactionRelease(devExt->ReadDmaTransaction); 
        WdfRequestComplete(Request, status);
    }
    return;
}
```









