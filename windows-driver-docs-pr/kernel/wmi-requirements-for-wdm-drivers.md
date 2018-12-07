---
title: WMI Requirements for WDM Drivers
description: WMI Requirements for WDM Drivers
ms.assetid: 8290e570-acd9-4047-bd0b-c1c74847f243
keywords: ["WMI WDK kernel , WDM drivers", "WDM drivers WDK WMI", "IRPs WDK WMI", "requests WDK WMI", "WMI WDK kernel , requests", "data providers WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# WMI Requirements for WDM Drivers





A driver that handles IRPs registers with WMI as a *data provider*. System-supplied storage port drivers, class drivers, and NDIS protocol drivers fall into this category. For information about registering as a WMI data provider, see [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

A driver that does not handle IRPs should simply forward WMI requests to the next-lower driver in the driver stack. The next-lower driver then registers with WMI and handles WMI requests on the first driver's behalf. For instance, SCSI miniport drivers and NDIS miniport drivers can register as WMI providers and supply WMI data to their corresponding class drivers.

A driver that supplies WMI data to a class or port driver must support the driver-type-specific WMI interfaces that are defined by the class or port driver. For example, a SCSI miniport driver must set **WmiDataProvider** to **TRUE** in the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure and handle SRB\_FUNCTION\_WMI requests from the SCSI port driver.

Similarly, a connection-oriented NDIS miniport driver that defines custom data blocks must support [OID\_GEN\_CO\_SUPPORTED\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569566); otherwise, NDIS maps those OIDs and status indications returned from OID\_GEN\_SUPPORTED\_LIST that are common and known to NDIS to GUIDs defined by NDIS.

The following sections describe how to support WMI in a driver that handles IRPs.

 

 




