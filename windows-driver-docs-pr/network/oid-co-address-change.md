---
title: OID_CO_ADDRESS_CHANGE
author: windows-driver-content
description: This topic describes the OID_CO_ADDRESS_CHANGE object identifier (OID).
ms.assetid: 18b185dd-b282-4182-a761-008e5d0c88d7
keywords:
- OID_CO_ADDRESS_CHANGE
ms.author: windowsdriverdev
ms.date: 11/03/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_CO_ADDRESS_CHANGE

The OID_CO_ADDRESS_CHANGE OID is sent by the call manager to each client that opened an address family with the call manager. This action is taken in response to a change in the switch address that the call manager uses. For example, the call manager sends this request if someone disconnects the NIC from one switch and plugs it into another switch. Each notified client must send an OID_CO_GET_ADDRESSES query to the call manager to retrieve a list of currently valid addresses.

The call manager also sends OID_CO_ADDRESS_CHANGE to a client immediately after the client opens an address family with the call manager. This ensures that a client that opens an address family after the switch address has changed is notified of the change. The client must then must then send an OID_CO_GET_ADDRESSES query to the call manager.

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")