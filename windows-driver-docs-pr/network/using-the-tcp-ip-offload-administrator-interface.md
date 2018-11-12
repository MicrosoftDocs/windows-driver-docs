---
title: Using the TCP/IP Offload Administrator Interface
description: Using the TCP/IP Offload Administrator Interface
ms.assetid: 2418e577-17cd-4db7-adb0-44b705e29d38
keywords:
- TCP/IP offload WDK networking , administrator interface
- offload WDK TCP/IP transport , administrator interface
- task offload WDK TCP/IP transport , administrator interface
- connection offload WDK TCP/IP transport , administrator interface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the TCP/IP Offload Administrator Interface





In NDIS 6.0 and later versions, user-mode applications (or overlying drivers) can enable or disable TCP/IP offload capabilities. A system administrator can access the settings through the Microsoft Windows Management Instrumentation (WMI) interface. There might also be capabilities that are disabled through registry settings that can be enabled if they are supported in the hardware.

In response to an [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) object identifier (OID) set request, a miniport driver uses the settings in the [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure to set the current offload or connection offload configuration of the miniport adapter.

NDIS retains the requested settings in the registry in the offload standardized keywords. When NDIS restarts the miniport adapter, the miniport driver reads the offload standardized keywords and uses them to set the default offload configuration of the NIC. If the miniport driver also supports non-standard keywords, the miniport driver is responsible for updating the registry when it changes the task offload settings. For more information about the standardized keywords, see [Standardized INF Keywords for Network Devices](standardized-inf-keywords-for-network-devices.md).

The miniport drivers must use the contents of the [**NDIS\_OFFLOAD\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566706) structure to update the currently reported offload configuration. The miniport driver must report the current configuration with the task offload [**NDIS\_STATUS\_TASK\_OFFLOAD\_CURRENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff567424) or connection offload NDIS\_STATUS\_OFFLOAD\_RESUME status indication. (For information on NDIS\_STATUS\_OFFLOAD\_RESUME, see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md).) The status indication ensures that all of the overlying protocol drivers are updated with the new capabilities information.

Before user-mode applications (or overlying drivers) set [OID\_TCP\_OFFLOAD\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569807) they can use the [OID\_TCP\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569806) OID or [OID\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES](https://msdn.microsoft.com/library/windows/hardware/ff569803) OID to determine what capabilities a miniport adapter's hardware can support. Use the OID\_TCP\_OFFLOAD\_PARAMETERS OID to enable capabilities that the [OID\_TCP\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569805) OID or [OID\_TCP\_CONNECTION\_OFFLOAD\_CURRENT\_CONFIG](https://msdn.microsoft.com/library/windows/hardware/ff569802) OID reports as not currently enabled.

If the hardware capabilities change (for example, because a MUX intermediate driver switches to a difference underlying miniport adapter), the intermediate driver must report any changes in offload hardware capabilities with the [**NDIS\_STATUS\_TASK\_OFFLOAD\_HARDWARE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567425) or [**NDIS\_STATUS\_TCP\_CONNECTION\_OFFLOAD\_HARDWARE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff567828) status indication.

NDIS and overlying drivers can use the [OID\_OFFLOAD\_ENCAPSULATION](https://msdn.microsoft.com/library/windows/hardware/ff569762) OID to set or query the task offload encapsulation settings of an underlying miniport adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure contains an [**NDIS\_OFFLOAD\_ENCAPSULATION**](https://msdn.microsoft.com/library/windows/hardware/ff566702) structure.

 

 





