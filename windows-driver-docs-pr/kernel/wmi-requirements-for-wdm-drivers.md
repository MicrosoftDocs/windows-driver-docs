---
title: WMI Requirements for WDM Drivers
author: windows-driver-content
description: WMI Requirements for WDM Drivers
MS-HAID:
- 'WMI\_fa77d4c0-cd42-467d-9fa6-db77b212fb3f.xml'
- 'kernel.wmi\_requirements\_for\_wdm\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8290e570-acd9-4047-bd0b-c1c74847f243
keywords: ["WMI WDK kernel , WDM drivers", "WDM drivers WDK WMI", "IRPs WDK WMI", "requests WDK WMI", "WMI WDK kernel , requests", "data providers WDK WMI"]
---

# WMI Requirements for WDM Drivers


## <a href="" id="ddk-wmi-requirements-for-wdm-drivers-kg"></a>


A driver that handles IRPs registers with WMI as a *data provider*. System-supplied storage port drivers, class drivers, and NDIS protocol drivers fall into this category. For information about registering as a WMI data provider, see [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

A driver that does not handle IRPs should simply forward WMI requests to the next-lower driver in the driver stack. The next-lower driver then registers with WMI and handles WMI requests on the first driver's behalf. For instance, SCSI miniport drivers and NDIS miniport drivers can register as WMI providers and supply WMI data to their corresponding class drivers.

A driver that supplies WMI data to a class or port driver must support the driver-type-specific WMI interfaces that are defined by the class or port driver. For example, a SCSI miniport driver must set **WmiDataProvider** to **TRUE** in the [**PORT\_CONFIGURATION\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff563900) structure and handle SRB\_FUNCTION\_WMI requests from the SCSI port driver.

Similarly, a connection-oriented NDIS miniport driver that defines custom data blocks must support [OID\_GEN\_CO\_SUPPORTED\_GUIDS](https://msdn.microsoft.com/library/windows/hardware/ff569566); otherwise, NDIS maps those OIDs and status indications returned from OID\_GEN\_SUPPORTED\_LIST that are common and known to NDIS to GUIDs defined by NDIS.

The following sections describe how to support WMI in a driver that handles IRPs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20WMI%20Requirements%20for%20WDM%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


