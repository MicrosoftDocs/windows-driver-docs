---
title: NDIS 6.0 Task Offload Backward Compatibility
description: NDIS 6.0 Task Offload Backward Compatibility
ms.assetid: c87ab12e-b387-4fb5-ae14-b78e050f6b77
keywords:
- task offload porting WDK networking , backward compatibility
- TCP/IP offload service porting WDK networking , backward compatibility
- offload service porting WDK networking , backward compatibility
- porting task offload services WDK networking , backwa
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS 6.0 Task Offload Backward Compatibility





Because the NDIS 6.0 support for task offload services is updated, NDIS 6.0 does require some restrictions on NDIS 5.*x* drivers that are present in an NDIS 6.0 driver stack. This topic describes those backward compatibility issues.

NDIS is responsible for translating the task offload object identifiers (OIDs) for the NDIS 5.*x* miniport drivers that do not support the NDIS 6.0 OIDs. For example, if an NDIS 5.*x* driver is present in a driver stack with NDIS 6.0 drivers, NDIS translates the OIDs appropriately to be backward compatible with the NDIS 5.*x* design. For more information about the NDIS 5.*x* task offload design, see [Task Offload (NDIS 5.1)](https://msdn.microsoft.com/library/windows/hardware/ff564239).

The following compatibility restrictions apply to NDIS 5.*x* drivers:

-   NDIS 6.0 does not support offload on TokenRing networks.

-   For NDIS 5.*x* miniport drivers, NDIS 6.0 does not support logical link control (LLC) Snap Headers for offload.

-   The maximum size of an offload data packet for an NDIS 5.*x* large send offload (LSO)-capable miniport adapter is fixed at 64 KB.

-   Protocol drivers must handle the case where a miniport driver reports offload capabilities but all of the values are zero. All values set to zero does not indicate that there is an error.

 

 





