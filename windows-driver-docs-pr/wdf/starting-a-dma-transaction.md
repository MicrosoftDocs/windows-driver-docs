---
title: Starting a DMA Transaction
description: Starting a DMA Transaction
ms.assetid: fa26ef08-01c0-4502-9cb3-865000242e4a
keywords: ["DMA transactions WDK KMDF starting", "DMA operations WDK KMDF transactions", "bus master DMA WDK KMDF transactions", "starting DMA transactions WDK KMDF", "scatter/gather DMA WDK KMDF"]
---

# Starting a DMA Transaction


\[Applies to KMDF only\]

## <a href="" id="ddk-starting-a-dma-transaction-df"></a>


After your driver has [created and initialized a DMA transaction](creating-and-initializing-a-dma-transaction.md), the driver can call the [**WdfDmaTransactionExecute**](https://msdn.microsoft.com/library/windows/hardware/ff547062) method to start the transaction. This method builds a scatter/gather list for the first [DMA transfer](dma-transactions-and-dma-transfers.md) that is associated with the transaction. Next, the method calls the [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) callback function that the driver registered for the transaction. The callback function [programs the DMA hardware](programming-dma-hardware.md) to start the transfer.

Before your driver calls **WdfDmaTransactionExecute**, the driver must store the DMA transaction handle so that it can be retrieved later when the driver completes each DMA transfer that is associated with the transaction. A good place to store the transaction handle is in the context memory of a framework object, typically the device's framework device object. For more information about using object context memory, see [Framework Object Context Space](framework-object-context-space.md).

The following code example from the [PLX9x5x](http://go.microsoft.com/fwlink/p/?linkid=256157) sample shows how to initialize and then execute a DMA transaction. This code appears in the *Read.c* file.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Starting%20a%20DMA%20Transaction%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




