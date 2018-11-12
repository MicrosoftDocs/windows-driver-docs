---
title: Access Memory by Using a BUS_INTERFACE_STANDARD
description: Access PCMCIA Attribute Memory by Using a BUS_INTERFACE_STANDARD Interface
ms.assetid: 2696a9ca-38b5-47f2-9639-029bba1173b5
keywords:
- attribute memory WDK PCMCIA bus , BUS_INTERFACE_STANDARD interface
- BUS_INTERFACE_STANDARD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Access PCMCIA Attribute Memory by Using a BUS\_INTERFACE\_STANDARD Interface





This section describes how a PC Card or CardBus card driver can use the BUS\_INTERFACE\_STANDARD interface to access attribute memory.

A driver should use a BUS\_INTERFACE\_STANDARD interface if the overhead of an I/O request is unacceptable. This method is like the I/O request method, in that it passes a buffer pointer. However, this method calls an interface routine, which eliminates the overhead of an I/O request. A driver must use this method if it accesses attribute memory while running at IRQL DISPATCH\_LEVEL − for example, within a deferred procedure call (DPC).

A driver can use this method while running at IRQL &lt;= DISPTACH\_LEVEL.

A driver usually obtains a BUS\_INTERFACE\_STANDARD interface during its initialization. The driver uses an [**IRP\_MN\_QUERY\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff551687) request to obtain the interface from the PCMCIA bus driver. The query interface request must be sent at IRQL PASSIVE\_LEVEL.

After the driver obtains the standard bus interface, the driver can call the interface routines **GetBusData** or **SetBusData** to access attribute memory.

 

 





