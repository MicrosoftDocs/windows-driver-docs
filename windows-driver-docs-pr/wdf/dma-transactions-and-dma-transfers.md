---
title: DMA Transactions and DMA Transfers
description: DMA Transactions and DMA Transfers
ms.assetid: afcbe756-1a45-410b-8260-2c2c611e6a70
keywords:
- DMA transactions WDK KMDF
- DMA operations WDK KMDF , transactions
- bus-master DMA WDK KMDF , transactions
- DMA operations WDK KMDF , transfers
- bus-master DMA WDK KMDF , transfers
- DMA transfers WDK KMDF
- DMA transactions WDK KMDF , about DMA transactions
- DMA transfers WDK KMDF , about DMA transfers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DMA Transactions and DMA Transfers


\[Applies to KMDF only\]




To understand how the framework handles bus-master and system-mode DMA operations, you must know the following two terms:

<a href="" id="dma-transaction"></a>**DMA transaction**  
A DMA transaction is a complete I/O operation, such as a single read or write request from an application.

<a href="" id="dma-transfer"></a>**DMA transfer**  
A DMA transfer is a single hardware operation that transfers data from computer memory to a device or from the device to computer memory.

A single DMA transaction always consists of at least one DMA transfer, but a transaction can consist of many transfers.

When a framework-based driver receives an I/O request, the driver typically creates a single DMA transaction object to represent the request. When the framework begins servicing the transaction, it determines if the device can handle the entire transaction in a single transfer. If the transaction is too large, the framework breaks the transaction into multiple transfers.

 

 





