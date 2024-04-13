---
title: Access Memory by Using a PnP I/O Request
description: Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request
keywords:
- attribute memory WDK PCMCIA bus , Plug and Play I/O requests
- Plug and Play WDK PCMCIA bus
- PnP WDK PCMCIA bus
ms.date: 03/03/2023
---

# Access PCMCIA Attribute Memory by Using a Plug and Play I/O Request





This section describes how a PC Card or Cardbus card driver can use Plug and Play I/O requests to access attribute memory.

A driver typically uses this method to initialize a device, to configure a device, or to obtain information from a device. A driver should use this method if the I/O overhead is acceptable, and the access can be done at IRQL &lt; DISPATCH\_LEVEL.

A driver can only use this method while running at IRQL &lt; DISPATCH\_LEVEL.

A driver performs the following sequence of operations:

-   Creates and initializes a new IRP\_MJ\_PNP request.

    The driver specifies either an [**IRP\_MN\_READ\_CONFIG**](../kernel/irp-mn-read-config.md) or an [**IRP\_MN\_WRITE\_CONFIG**](../kernel/irp-mn-write-config.md) minor function.

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

 

