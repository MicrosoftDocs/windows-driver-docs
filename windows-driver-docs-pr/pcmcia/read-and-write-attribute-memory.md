---
title: Read and Write Attribute Memory
description: Read and Write Attribute Memory
MS-HAID:
- 'mcch2\_dcba1d53-cf45-471f-9deb-66db8d957c9c.xml'
- 'PCMCIA.read\_and\_write\_attribute\_memory'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8e430057-b68a-4edc-8755-1d7255412269
keywords: ["PCMCIA WDK buses , attribute memory", "attribute memory WDK PCMCIA bus , read and write"]
---

# Read and Write Attribute Memory


## <a href="" id="ddk-read-and-write-attribute-memory-kr"></a>


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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Read%20and%20Write%20Attribute%20Memory%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




