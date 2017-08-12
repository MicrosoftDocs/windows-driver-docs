---
title: NDIS_STATUS_WWAN_PCO_STATUS
author: windows-driver-content
description: Miniport drivers use the NDIS_STATUS_WWAN_PCO_STATUS notification to inform the MB service about the completion of a previous OID_WWAN_PCO query request.
ms.assetid: E0F70FAE-B7C6-4BE4-B89A-88084463EEA5
keywords:
- NDIS_STATUS_WWAN_PCO_STATUS, PCO status notification, Mobile Broadband PCO status notification, MB PCO status notification
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NDIS_STATUS_WWAN_PCO_STATUS

The **NDIS_STATUS_WWAN_PCO_STATUS** notification is sent by a modem miniport driver to inform the OS of the current PCO state in the modem. Modem miniport drivers will send this notification in the following three scenarios:

1.	When a new PCO value has arrived on an activated connection.
2.	When the modem has PCO value readily available when a connection is activated or bridged by the host.
3.	In response to an [OID_WWAN_PCO](oid-wwan-pco.md) query request from the host.

When a new PCO value has arrived, this notification will be unsolicited and sent with the latest PCO value from the network. The notification will come up with the NDIS port number that corresponds to the activated connection’s PDN.

When a connection is activated or bridged from the host, the modem should check whether it has the PCO value cached or not. If it does, it will send up a notification to the host with the NDIS port number that corresponds to the PDN that the host has activated or bridged.

This notification will be used to notify the host that an **OID_WWAN_PCO** query request has been completed, with the PCO value included in the notification. The host expects the modem to pass the complete structure of PCO values on the PDN corresponding to the port number.

If PCO functionality is supported by the modem but no PCO value is received from the network when the host sends an **OID_WWAN_PCO** query request, the modem should return an **NDIS_STATUS_WWAN_PCO_STATUS** notification with an empty [WWAN_PCO_VALUE](TBD) payload. 

This notification uses the [NDIS_WWAN_PCO_STATUS](TBD) structure.

> [!NOTE]
> Currently, in Windows 10, version 1709, some modems are only able to provide operator specific PCO elements. If a PCO data structure is received by modem but there is no applicable operator specific PCO element, to avoid unnecessary device wakeup, the modem should not advertise the PCO notification to the OS. 

## Requirements

| | |
| --- | --- |
| Version | Windows 10, version 1709 |
| Header | Ntddndis.h (include Ndis.h) |

## See also

[OID_WWAN_PCO](oid-wwan-pco.md)

[**NDIS_WWAN_PCO_STATUS**](TBD)

[WWAN_PCO_VALUE](TBD)

[MB Protocol Configuration Option (PCO) Operations](mb-protocol-configuration-option-pco-operations.md)
 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_STATUS_WWAN_PCO_STATUS%20%20RELEASE:%20%287/5/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")