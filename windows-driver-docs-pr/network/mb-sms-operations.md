---
title: MB SMS Operations
description: MB SMS Operations
ms.assetid: 9a21495c-ec3d-4277-b880-dbf5b081814a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB SMS Operations


This topic describes the operations to configure, read/receive, send, and delete messages using Short Message Service (SMS) capabilities of an MB device.

SMS support is mandatory. Miniport drivers must set the appropriate send and receive SMS capability flags that they support when processing [OID\_WWAN\_DEVICE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569824) query requests in the **WwanSmsCaps** member of the [**WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff571204) structure. If miniport drivers do not support SMS, they should specify WWAN\_SMS\_CAPS\_NONE and return WWAN\_STATUS\_SMS\_UNKNOWN\_ERROR for all SMS-related OIDs.

Miniport drivers should only process SMS operations after [OID\_WWAN\_READY\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569833) returns **WwanReadyStateInitialize** as the device ready-state. Miniport drivers should process some SMS operations, such as sending a SMS message, only after the device is registered on a provider network (though not necessarily data service registration).

The MB Service does not differentiate between different message stores available in the device. Therefore, miniport drivers must handle all message stores and project a single virtual message store accessed by means of a virtual index. For example, if the device has three message stores, the miniport driver must handle all of them collectively and present them as a single message store to the service.

The MB driver model supports the following SMS Operations:

-   SMS configuration

-   Read SMS

-   Send SMS

-   Delete SMS

We recommend miniport drivers support SMS configuration, read, send, and delete operations, as well as notifying the user of any new SMS message received by a device.

For more information about SMS operations, see [OID\_WWAN\_SMS\_CONFIGURATION](https://msdn.microsoft.com/library/windows/hardware/ff569837), [OID\_WWAN\_SMS\_READ](https://msdn.microsoft.com/library/windows/hardware/ff569839), [OID\_WWAN\_SMS\_SEND](https://msdn.microsoft.com/library/windows/hardware/ff569840), [OID\_WWAN\_SMS\_DELETE](https://msdn.microsoft.com/library/windows/hardware/ff569838), and [OID\_WWAN\_SMS\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff569841).

 

 





