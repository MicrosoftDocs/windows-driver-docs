---
title: V4 Printer Driver Rendering
author: windows-driver-content
description: For rendering print jobs into the page description language for a print device, the v4 print driver model uses the XPSDrv Render Module.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8952063C-3706-43A0-BA6B-231E7CD01514
---

# V4 Printer Driver Rendering


For rendering print jobs into the page description language for a print device, the v4 print driver model uses the [XPSDrv Render Module](xpsdrv-render-module.md).

The v4 driver model does not use the XPSDrv render module for any other purpose. So drivers for XPS-direct devices do not have to include any filters. But drivers for all other devices must either include filters that render into the device PDL, or they must utilize existing rendering support from a Print Class driver by using the **RequiredClass** directive in the v4 manifest file.

This section provides more information about v4 driver rendering in the following topics.

[V4 Printer Driver Rendering Architecture](v4-driver-rendering-architecture.md)

[Improvements in XPSDrv](improvements-in-xpsdrv.md)

[Standard XPS Filters](standard-xps-filters.md)

[V4 Print Class Driver Rendering](print-class-driver-rendering.md)

## Related topics
[Supported PrintTicket Features](supported-printticket-features.md)  
[V4 Printer Driver](v4-printer-driver.md)  
[XPSDrv Render Module](xpsdrv-render-module.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20V4%20Printer%20Driver%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


