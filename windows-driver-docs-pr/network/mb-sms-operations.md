---
title: MB SMS Operations
description: MB SMS Operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB SMS Operations


This topic describes the operations to configure, read/receive, send, and delete messages using Short Message Service (SMS) capabilities of an MB device.

SMS support is mandatory. Miniport drivers must set the appropriate send and receive SMS capability flags that they support when processing [OID\_WWAN\_DEVICE\_CAPS](./oid-wwan-device-caps.md) query requests in the **WwanSmsCaps** member of the [**WWAN\_DEVICE\_CAPS**](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_device_caps) structure. If miniport drivers do not support SMS, they should specify WWAN\_SMS\_CAPS\_NONE and return WWAN\_STATUS\_SMS\_UNKNOWN\_ERROR for all SMS-related OIDs.

Miniport drivers should only process SMS operations after [OID\_WWAN\_READY\_INFO](./oid-wwan-ready-info.md) returns **WwanReadyStateInitialize** as the device ready-state. Miniport drivers should process some SMS operations, such as sending a SMS message, only after the device is registered on a provider network (though not necessarily data service registration).

The MB Service does not differentiate between different message stores available in the device. Therefore, miniport drivers must handle all message stores and project a single virtual message store accessed by means of a virtual index. For example, if the device has three message stores, the miniport driver must handle all of them collectively and present them as a single message store to the service.

The MB driver model supports the following SMS Operations:

-   SMS configuration

-   Read SMS

-   Send SMS

-   Delete SMS

We recommend miniport drivers support SMS configuration, read, send, and delete operations, as well as notifying the user of any new SMS message received by a device.

For more information about SMS operations, see [OID\_WWAN\_SMS\_CONFIGURATION](./oid-wwan-sms-configuration.md), [OID\_WWAN\_SMS\_READ](./oid-wwan-sms-read.md), [OID\_WWAN\_SMS\_SEND](./oid-wwan-sms-send.md), [OID\_WWAN\_SMS\_DELETE](./oid-wwan-sms-delete.md), and [OID\_WWAN\_SMS\_STATUS](./oid-wwan-sms-status.md).

 

