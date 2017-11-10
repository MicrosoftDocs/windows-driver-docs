---
title: OID_TCP_OFFLOAD_PARAMETERS
author: windows-driver-content
description: This topic describes the OID_TCP_OFFLOAD_PARAMETERS object identifier (OID). 
ms.assetid: 5D9B5F62-E506-4983-B247-A93B81E70A43
keywords:
- OID_TCP_OFFLOAD_PARAMETERS, WDK OIDs, WDK networking object identifiers, WDK networking OIDs
ms.author: windowsdriverdev
ms.date: 11/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# OID_TCP_OFFLOAD_PARAMETERS

Query requests are not supported.

As a set request, the OID_TCP_OFFLOAD_PARAMETERS OID sets the current TCP offload configuration of a miniport adapter. Protocol drivers or user-mode applications can set this OID to change the current TCP offload configuration. A system administrator can use this OID through the Microsoft Windows Management Instrumentation (WMI) interface.

## Remarks

OID_TCP_OFFLOAD_PARAMETERS is required for miniport drivers that support TCP offloads and optional for other miniport drivers. If a miniport driver does not support this OID, the driver should return NDIS_STATUS_NOT_SUPPORTED.

The **InformationBuffer** member of the [NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure. If the contents of **InformationBuffer** are invalid, the miniport driver should return NDIS_STATUS_INVALID_DATA in response to this OID.

While NDIS processes this OID and before it passes the OID to the miniport driver, NDIS updates the miniport adapter's offload standardized keywords with the new settings.

Miniport drivers must use the contents of the [NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure to update the currently reported TCP offload capabilities. After the update, the miniport driver must report the current task offload capabilities with the [NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md) status indication. This status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

Before setting OID_TCP_OFFLOAD_PARAMETERS, the overlying applications or drivers can use the [OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md) OID to determine what capabilities a miniport adapter's hardware can support. Use OID_TCP_OFFLOAD_PARAMETERS to enable capabilities that are reported as not enabled by the [OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md) OID.


### See also

[NDIS_OFFLOAD_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff566706)  
[NDIS_OID_REQUEST](https://msdn.microsoft.com/library/windows/hardware/ff566710)  
[NDIS_STATUS_TASK_OFFLOAD_CURRENT_CONFIG](ndis-status-task-offload-current-config.md)  
[OID_TCP_OFFLOAD_CURRENT_CONFIG](oid-tcp-offload-current-config.md)  
[OID_TCP_OFFLOAD_HARDWARE_CAPABILITIES](oid-tcp-offload-hardware-capabilities.md)

## Requirements

| | |
| --- | --- |
| Version | Windows Vista and later |
| Header | Ntddndis.h (include Ndis.h) |

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_WWAN_DEVICE_CAPS_EX%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")