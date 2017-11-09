---
title: OID_TCP_CONNECTION_OFFLOAD_PARAMETERS
author: windows-driver-content
description: This topic describes the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS object identifier (OID). 
ms.assetid: 6481D565-900A-4B75-A60F-72701FB45FAD
keywords:
- OID_TCP_CONNECTION_OFFLOAD_PARAMETERS, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.author: windowsdriverdev
ms.date: 11/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP_CONNECTION_OFFLOAD_PARAMETERS

As a query request, overlying drivers can use the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID to determine the current connection offload settings of an underlying miniport adapter. NDIS handles this OID query for miniport drivers.

As a set request, NDIS and overlying drivers use the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID to set the connection offload configuration parameters of an underlying miniport adapter. Miniport drivers that support connection offload must handle this OID set request. Otherwise, the OID_TCP_CONNECTION_OFFLOAD_PARAMETERS OID is optional for miniport drivers.

## Remarks

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_TCP_CONNECTION_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff567876) structure.

> [!NOTE]
> Do not confuse OID_TCP_CONNECTION_OFFLOAD_PARAMETERS with the [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) OID that administrative applications use to enable or disable TCP offload features.

### See also

[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md)

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")