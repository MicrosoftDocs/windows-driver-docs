---
title: NDIS_STATUS_WWAN_PCO_STATUS
ms.topic: reference
description: Miniport drivers use the NDIS_STATUS_WWAN_PCO_STATUS notification to inform the MB service about the completion of a previous OID_WWAN_PCO query request.
keywords:
- NDIS_STATUS_WWAN_PCO_STATUS, PCO status notification, Mobile Broadband PCO status notification, MB PCO status notification
ms.date: 08/08/2017
---

# NDIS_STATUS_WWAN_PCO_STATUS

The **NDIS_STATUS_WWAN_PCO_STATUS** notification is sent by a modem miniport driver to inform the OS of the current Protocol Configuration Options (PCO) state in the modem. Modem miniport drivers will send this notification in the following three scenarios:

1.	When a new PCO value has arrived on an activated connection.
2.	When the modem has PCO value readily available when a connection is activated or bridged by the host.
3.	In response to an [OID_WWAN_PCO](oid-wwan-pco.md) query request from the host.

When a new PCO value has arrived, this notification will be unsolicited and sent with the latest PCO value from the network. The notification will come up with the NDIS port number that corresponds to the activated connection’s PDN.

When a connection is activated or bridged from the host, the modem should check whether it has the PCO value cached or not. If it does, it will send up a notification to the host with the NDIS port number that corresponds to the PDN that the host has activated or bridged.

This notification will be used to notify the host that an **OID_WWAN_PCO** query request has been completed, with the PCO value included in the notification. The host expects the modem to pass the complete structure of PCO values on the PDN corresponding to the port number.

If PCO functionality is supported by the modem but no PCO value is received from the network when the host sends an **OID_WWAN_PCO** query request, the modem should return an **NDIS_STATUS_WWAN_PCO_STATUS** notification with an empty [WWAN_PCO_VALUE](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_pco_value) payload. 

This notification uses the [NDIS_WWAN_PCO_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pco_status) structure.

> [!NOTE]
> Currently, in Windows 10, version 1709 and later, some modems are only able to provide operator specific PCO elements. If a PCO data structure is received by modem but there is no applicable operator specific PCO element, to avoid unnecessary device wakeup, the modem should not advertise the PCO notification to the OS. 

## Requirements

**Version**: Windows 10, version 1709
**Header**: Ndis.h

## See also

[OID_WWAN_PCO](oid-wwan-pco.md)

[NDIS_WWAN_PCO_STATUS](/windows-hardware/drivers/ddi/ndiswwan/ns-ndiswwan-_ndis_wwan_pco_status)

[WWAN_PCO_VALUE](/windows-hardware/drivers/ddi/wwan/ns-wwan-_wwan_pco_value)

[MB Protocol Configuration Options (PCO) operations](mb-protocol-configuration-options-pco-operations.md)
