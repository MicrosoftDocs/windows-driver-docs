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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Access%20PCMCIA%20Attribute%20Memory%20by%20Using%20a%20Plug%20and%20Play%20I/O%20Request%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




