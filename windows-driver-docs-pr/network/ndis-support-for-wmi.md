---
title: NDIS Support for WMI
description: NDIS Support for WMI
ms.assetid: ce35ddb4-bf18-4ba1-bc6f-dbe659f5d781
keywords:
- Windows Management Instrumentation WDK networking
- miniport drivers WDK networking , WMI support
- NDIS miniport drivers WDK , WMI support
- WMI WDK networking
- protocol drivers WDK networking , WMI support
- NDIS protocol drivers WDK , WMI support
- i
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Support for WMI





Through NDIS, clients of Windows Management Instrumentation (WMI) can obtain and set information that NDIS and NDIS drivers service. WMI clients can also register to receive status updates.

NDIS automatically registers miniport adapters, named virtual connections (VCs), and a set of globally unique identifiers (GUIDs) for each miniport adapter with WMI. For more information about these GUIDs, see [Standard Miniport Driver OIDs Registered with WMI](standard-miniport-driver-oids-registered-with-wmi.md). Miniport drivers can also provide support for custom object identifiers (OIDs) and custom status indications, as the [Customized OIDs and Status Indications](customized-oids-and-status-indications.md) topic describes.

NDIS does not provide WMI support for protocol drivers. A protocol driver, or an intermediate driver, can create a device object for itself and register directly with WMI. For more information about registering directly with WMI, see [Registering as a WMI Data Provider](https://msdn.microsoft.com/library/windows/hardware/ff560870).

For more information about the WMI architecture, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139).

This section includes:

[Registration and Deregistration of NDIS Miniport Drivers with WMI](registration-and-deregistration-of-ndis-miniport-drivers-with-wmi.md)

[Mapping of GUIDs to OIDs and Miniport Driver Status](mapping-of-guids-to-oids-and-miniport-driver-status.md)

[Support for Named VCs](support-for-named-vcs.md)

[NDIS-Supported WMI Operations](ndis-supported-wmi-operations.md)

[Standard WMI OIDs and Status Indications](standard-wmi-oids-and-status-indications.md)

[Customized OIDs and Status Indications](customized-oids-and-status-indications.md)

[NDIS WMI GUIDs](ndis-wmi-guids.md)

 

 





