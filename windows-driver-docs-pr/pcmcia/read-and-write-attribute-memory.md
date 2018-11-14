---
title: Read and Write Attribute Memory
description: Read and Write Attribute Memory
ms.assetid: 8e430057-b68a-4edc-8755-1d7255412269
keywords:
- PCMCIA WDK buses , attribute memory
- attribute memory WDK PCMCIA bus , read and write
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Read and Write Attribute Memory





This section describes how a PCMCIA driver can read and write the attribute memory on a PCMCIA memory card.

Windows 2000 and later operating systems treat attribute memory on a PC Card or CardBus card as configuration space.

In general, to access attribute memory, drivers must create an IRP using a major function code of IRP\_MJ\_PNP and a minor function code of [**IRP\_MN\_READ\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551727) or [**IRP\_MN\_WRITE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551769).

If necessary, a driver can access attribute memory directly by means of a permanent memory window. See [Access PCMCIA Attribute Memory Through a Permanent Memory Window](https://msdn.microsoft.com/library/windows/hardware/ff536901) for further details.

The PCMCIA memory card driver carries out the following operations:

-   Creates and initializes the new IRP.

-   Gets the next stack location.

-   Sets the following members of the new stack location:
    -   The **ReadWriteConfig.WhichSpace** member specifies the value PCCARD\_ATTRIBUTE\_MEMORY.
    -   The **Buffer** member points to a driver-allocated, nonpaged buffer for a read or a write operation. For a write operation, the buffer contains the data to write to the configuration space. For a read operation, the buffer is a zero-filled buffer. On completion of the IRP, this buffer is set to a copy of the attribute memory read from the device.
    -   The **Offset** member specifies the byte offset from the base of the attribute memory where the read or write operation begins.
    -   The **Length** member specifies the size, in bytes, of the buffer that is specified at **Buffer**.
-   Sets a completion routine.

-   Sends the request down the drive stack.

A driver must be running at IRQL &lt; DISPATCH\_LEVEL to send this request down the driver stack.

 

 





