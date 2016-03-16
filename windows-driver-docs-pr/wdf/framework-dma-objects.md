---
title: Framework DMA Objects
description: Framework DMA Objects
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: a5073bb0-a8c9-49fc-b280-e781f9f9c256
keywords: ["DMA operations WDK KMDF objects", "bus master DMA WDK KMDF objects", "DMA enabler objects WDK KMDF", "DMA transaction objects WDK KMDF", "common buffer objects WDK KMDF", "framework objects WDK KMDF DMA objects", "enabler objects WDK KMDF", "transaction objects WDK KMDF"]
---

# Framework DMA Objects


\[Applies to KMDF only\]

## <a href="" id="ddk-framework-dma-objects-df"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Framework%20DMA%20Objects%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




