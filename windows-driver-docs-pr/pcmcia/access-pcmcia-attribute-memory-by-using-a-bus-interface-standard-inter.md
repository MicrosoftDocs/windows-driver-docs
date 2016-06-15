---
title: Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface
description: Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface
MS-HAID:
- 'pamch1\_8f8d04fa-c8f9-46e5-be60-0f72f75dc7fc.xml'
- 'PCMCIA.access\_pcmcia\_attribute\_memory\_by\_using\_a\_bus\_interface\_standard\_inter'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2696a9ca-38b5-47f2-9639-029bba1173b5
keywords: ["attribute memory WDK PCMCIA bus , BUS_INTERFACE_STANDARD interface", "BUS_INTERFACE_STANDARD"]
---

# Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface


## <a href="" id="ddk-access-pcmcia-attribute-memory-by-using-a-bus-interface-standard-i"></a>


This section describes how a PC Card or CardBus card driver can use the BUS\_INTERFACE\_STANDARD interface to access attribute memory.

A driver should use a BUS\_INTERFACE\_STANDARD interface if the overhead of an I/O request is unacceptable. This method is like the I/O request method, in that it passes a buffer pointer. However, this method calls an interface routine, which eliminates the overhead of an I/O request. A driver must use this method if it accesses attribute memory while running at IRQL DISPATCH\_LEVEL − for example, within a deferred procedure call (DPC).

A driver can use this method while running at IRQL &lt;= DISPTACH\_LEVEL.

A driver usually obtains a BUS\_INTERFACE\_STANDARD interface during its initialization. The driver uses an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to obtain the interface from the PCMCIA bus driver. The query interface request must be sent at IRQL PASSIVE\_LEVEL.

After the driver obtains the standard bus interface, the driver can call the interface routines **GetBusData** or **SetBusData** to access attribute memory.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BPCMCIA\buses%5D:%20Access%20PCMCIA%20Attribute%20Memory%20by%20Using%20a%20BUS_INTERFACE_STANDARD%20Interface%20%20RELEASE:%20%285/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




