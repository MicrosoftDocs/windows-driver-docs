---
title: Creating and Initializing a DMA Transaction
description: Creating and Initializing a DMA Transaction
ms.assetid: 1982c3fa-9e4a-4b26-8902-321223d9159f
keywords: ["DMA transactions WDK KMDF , initializing", "DMA operations WDK KMDF , transactions", "bus-master DMA WDK KMDF , transactions", "DMA transactions WDK KMDF , creating", "initializing DMA transactions WDK KMDF"]
---

# Creating and Initializing a DMA Transaction


\[Applies to KMDF only\]

## <a href="" id="ddk-creating-and-initializing-a-dma-transaction-df"></a>


Before your driver can send an I/O request to a DMA device, the driver must:

1.  Call [**WdfDmaTransactionCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547027) to create a DMA transaction object for the request.

2.  Call [**WdfDmaTransactionInitializeUsingRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547107), [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099), or [**WdfDmaTransactionInitializeUsingOffset**](https://msdn.microsoft.com/library/windows/hardware/hh451182) to initialize the transaction object.

Typically, your driver creates a [DMA transaction](dma-transactions-and-dma-transfers.md) because a [request handler](request-handlers.md) has received a [framework request object](framework-request-objects.md) and must pass the request to the hardware. In this case, the driver should call [**WdfDmaTransactionInitializeUsingRequest**](https://msdn.microsoft.com/library/windows/hardware/ff547107), which accepts a request object handle as input and extracts the request's address parameters from the request object.

If your driver must create a DMA transaction that is *not* based on a framework request object that the driver received, the driver can call either [**WdfDmaTransactionInitialize**](https://msdn.microsoft.com/library/windows/hardware/ff547099) or [**WdfDmaTransactionInitializeUsingOffset**](https://msdn.microsoft.com/library/windows/hardware/hh451182). Both methods accept address parameters that the driver provides.

All three initialization methods require the address of an [*EvtProgramDma*](https://msdn.microsoft.com/library/windows/hardware/ff541816) event callback function as an input parameter. This callback function programs the device, and the framework calls the callback function each time a [DMA transfer](dma-transactions-and-dma-transfers.md) is available.

When your driver calls [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983) to create a DMA enabler object, the driver supplies a [**WDF\_DMA\_ENABLER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551290) structure that contains the device's maximum transfer length. The framework uses this value as the default maximum length for all DMA transfers.

For some types of DMA transactions, you might need to specify a maximum transfer length that is different from the device's default maximum length. You can use [**WdfDmaTransactionSetMaximumLength**](https://msdn.microsoft.com/library/windows/hardware/ff547127) to set a maximum transfer length for an individual transaction. The framework uses the specified maximum transfer length only while it processes the specified transaction.

Note that the maximum transfer length is limited by the number of [map registers](https://msdn.microsoft.com/library/windows/hardware/ff554406) that the operating system makes available to the DMA enabler object. To determine the maximum transfer length that is available, your driver can call [**WdfDmaEnablerGetFragmentLength**](https://msdn.microsoft.com/library/windows/hardware/ff546986). If the value that **WdfDmaEnablerGetFragmentLength** returns is less than the maximum transfer length that the driver supplied to [**WdfDmaEnablerCreate**](https://msdn.microsoft.com/library/windows/hardware/ff546983), the framework uses the smaller value.

After your driver creates and initializes a DMA transaction, the driver must [start the transaction](starting-a-dma-transaction.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20and%20Initializing%20a%20DMA%20Transaction%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




