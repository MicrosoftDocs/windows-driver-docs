---
title: Framework DMA Objects
description: Framework DMA Objects
ms.assetid: a5073bb0-a8c9-49fc-b280-e781f9f9c256
keywords:
- DMA operations WDK KMDF , objects
- bus-master DMA WDK KMDF , objects
- DMA enabler objects WDK KMDF
- DMA transaction objects WDK KMDF
- common buffer objects WDK KMDF
- framework objects WDK KMDF , DMA objects
- enabler objects WDK KMDF
- transaction objects WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework DMA Objects


\[Applies to KMDF only\]




To handle bus-master and system-mode DMA operations in a framework-based driver, the framework provides three objects:

<a href="" id="dma-enabler-object"></a>**DMA enabler object**  
The framework's DMA enabler object enables a driver to use the framework's DMA support for a particular device. The driver must create a DMA enabler object for each of its devices that supports DMA operations.

<a href="" id="dma-transaction-object"></a>**DMA transaction object**  
The framework's DMA transaction object represents a single DMA I/O operation. A framework-based driver typically creates a DMA transaction object for each I/O request that it receives, if the device uses DMA to perform the requested operation.

<a href="" id="common-buffer-object"></a>**Common buffer object**  
The framework's common buffer object represents an area of computer memory that is mapped for simultaneous access by both the driver and a device. Some drivers [use common buffers](using-common-buffers.md) when they set up I/O operations for DMA devices.

For information about the interfaces that these objects export, see:

[Framework DMA Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265634)

[Framework Common Buffer Object Reference](https://msdn.microsoft.com/library/windows/hardware/dn265627)

 

 





