---
title: DMA Transactions and DMA Transfers
description: DMA Transactions and DMA Transfers
ms.assetid: afcbe756-1a45-410b-8260-2c2c611e6a70
keywords: ["DMA transactions WDK KMDF", "DMA operations WDK KMDF , transactions", "bus-master DMA WDK KMDF , transactions", "DMA operations WDK KMDF , transfers", "bus-master DMA WDK KMDF , transfers", "DMA transfers WDK KMDF", "DMA transactions WDK KMDF , about DMA transactions", "DMA transfers WDK KMDF , about DMA transfers"]
---

# DMA Transactions and DMA Transfers


\[Applies to KMDF only\]

## <a href="" id="ddk-dma-transactions-and-dma-transfers-df"></a>


To understand how the framework handles bus-master and system-mode DMA operations, you must know the following two terms:

<a href="" id="dma-transaction"></a>**DMA transaction**  
A DMA transaction is a complete I/O operation, such as a single read or write request from an application.

<a href="" id="dma-transfer"></a>**DMA transfer**  
A DMA transfer is a single hardware operation that transfers data from computer memory to a device or from the device to computer memory.

A single DMA transaction always consists of at least one DMA transfer, but a transaction can consist of many transfers.

When a framework-based driver receives an I/O request, the driver typically creates a single DMA transaction object to represent the request. When the framework begins servicing the transaction, it determines if the device can handle the entire transaction in a single transfer. If the transaction is too large, the framework breaks the transaction into multiple transfers.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20DMA%20Transactions%20and%20DMA%20Transfers%20%20RELEASE:%20%283/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




