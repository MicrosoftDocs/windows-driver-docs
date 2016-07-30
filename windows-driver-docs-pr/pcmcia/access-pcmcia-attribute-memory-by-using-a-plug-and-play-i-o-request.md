---
title: Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request
description: Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request
MS-HAID:
- 'pamch1\_a0d06d64-03b6-4376-8865-ea042b631dca.xml'
- 'PCMCIA.access\_pcmcia\_attribute\_memory\_by\_using\_a\_plug\_and\_play\_i\_o\_request'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ee2f9d9f-9e2b-4ecf-ba6d-4baad3653301
keywords: ["attribute memory WDK PCMCIA bus , Plug and Play I/O requests", "Plug and Play WDK PCMCIA bus", "PnP WDK PCMCIA bus"]
---

# Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request


## <a href="" id="ddk-access-pcmcia-attribute-memory-by-using-a-plug-and-play-i-o-reques"></a>


This section describes how a PC Card or Cardbus card driver can use Plug and Play I/O requests to access attribute memory.

A driver typically uses this method to initialize a device, to configure a device, or to obtain information from a device. A driver should use this method if the I/O overhead is acceptable, and the access can be done at IRQL &lt; DISPATCH\_LEVEL.

A driver can only use this method while running at IRQL &lt; DISPATCH\_LEVEL.

A driver performs the following sequence of operations:

-   Creates and initializes a new IRP\_MJ\_PNP request.

    The driver specifies either an [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) or an [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769) minor function.

-   Gets the next stack location.

-   Sets the following members of the **Parameters.ReadWriteConfig** structure in the new stack location:

    <a href="" id="whichspace"></a>**WhichSpace**  
    Specifies the value PCCARD\_ATTRIBUTE\_MEMORY.

    <a href="" id="buffer"></a>**Buffer**  
    Pointer to a paged-memory buffer that the driver allocates for the access. For a write operation, the buffer contains the data to write to the configuration space. For a read operation, the buffer is a zero-filled buffer. After the request completes, this buffer holds a copy of the attribute memory read from the device.

    <a href="" id="offset"></a>**Offset**  
    Specifies the WORD offset from the base of the attribute memory where the read or write operation begins.

    <a href="" id="length"></a>**Length**  
    Specifies the size in bytes of the buffer that the driver allocates for the request.

-   Sets a completion routine.

-   Sends the request down the device stack.

 

 





