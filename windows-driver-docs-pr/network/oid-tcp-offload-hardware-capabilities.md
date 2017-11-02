---
title: OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES
author: windows-driver-content
description: This topic describes the OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES object identifier (OID). 
ms.assetid: 9958F93C-0D68-428B-A25C-7FF6E4F37702
keywords:
- OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.author: windowsdriverdev
ms.date: 11/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES

As a query request, the OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES OID reports the task offload hardware capabilities of a miniport adapter's hardware. User-mode applications (or possibly overlying drivers) can query this OID to determine the task offload hardware capabilities of an underlying miniport adapter. A system administrator can use this OID through the Windows Management Instrumentation (WMI) interface.

Set requests are not supported.

## Remarks

NDIS handles this OID for miniport drivers. Miniport drivers report miniport adapter hardware capabilities to NDIS. For information about reporting task offload hardware capabilites to NDIS from a miniport driver and from NDIS to overlying drivers, see [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599).

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599) structure. NDIS returns NDIS_STATUS_BUFFER_TOO_SHORT if the buffer is not big enough.

After determining the miniport adapter's hardware capabilities, the overlying applications or drivers can use the [OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md) OID to enable capabilities that are currently reported as not enabled by the [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md) OID.

### See also

[NDIS_OFFLOAD](https://msdn.microsoft.com/library/windows/hardware/ff566599)  
[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md)  
[OID_TCP_OFFLOAD_PARAMETERS](oid-tcp-offload-parameters.md)  

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")