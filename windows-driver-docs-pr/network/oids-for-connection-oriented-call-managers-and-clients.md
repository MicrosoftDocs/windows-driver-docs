---
title: OIDs for connection-oriented call managers and clients
author: windows-driver-content
description: This topic describes OIDs for connection-oriented call managers and clients.
ms.assetid: a2ffbfd4-a63e-41d1-ab57-0c23661148ca
keywords:
- General operational OIDs connection-oriented miniport drivers
ms.author: windowsdriverdev
ms.date: 11/02/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OIDs for connection-oriented call managers and clients

The following table summarizes the OIDs that connection-oriented clients can send to call managers or MCM drivers and that call managers or MCM drivers can send to connection-oriented clients. 

> [!TIP] 
> A connection-oriented miniport driver handles such requests in its [MiniportCoOidRequest](https://msdn.microsoft.com/library/windows/hardware/ff559362) callback function.

In this table, M indicates an OID is mandatory, while O indicates it is optional.

| Length | Query | Set | Name |
| --- | --- | --- | --- |
| Varies |   | O | [OID_CO_ADD_ADDRESS](oid-co-add-address.md) |
| Varies |   | O | [OID_CO_ADD_PVC](oid-co-add-pvc.md) |
| 0 |   | O | [OID_CO_ADDRESS_CHANGE](oid-co-address-change.md) |
| 0 |   | M | [OID_CO_AF_CLOSE](oid-co-af-close.md) |
| Varies |   | O | [OID_CO_DELETE_ADDRESS](oid-co-delete-address.md) |
| Varies |   | O | [OID_CO_DELETE_PVC](oid-co-delete-pvc.md) |
| Varies | O |   | [OID_CO_GET_ADDRESSES](oid-co-get-addresses.md) |
|   |   |   | [OID_CO_GET_CALL_INFORMATION](oid-co-get-call-information.md) |
| 0 |   | O | [OID_CO_SIGNALING_DISABLED](oid-co-signaling-disabled.md) |
| 0 |   | O | [OID_CO_SIGNALING_ENABLED](oid-co-signaling-enabled.md) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")