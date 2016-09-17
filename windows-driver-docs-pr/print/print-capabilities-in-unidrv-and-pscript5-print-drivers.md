---
title: Print Capabilities in Unidrv and PScript5 Print Drivers
author: windows-driver-content
description: Print Capabilities in Unidrv and PScript5 Print Drivers
MS-HAID:
- 'drvarch\_2d3c985b-a56f-4e5d-bbd5-62e20d29a45b.xml'
- 'print.print\_capabilities\_in\_unidrv\_and\_pscript5\_print\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 70f8b846-3e05-4345-baad-a3db6b8df620
keywords: ["Print Capabilities WDK , Unidrv", "Print Capabilities WDK , PScript5"]
---

# Print Capabilities in Unidrv and PScript5 Print Drivers


The Unidrv and PScript5 minidrivers provide the Print Ticket and Print Capabilities interfaces that are required to support the Print Capabilities feature. These print drivers provide Print Ticket and Print Capabilities support for the features that are described in the [generic printer description (GPD) file](introduction-to-gpd-files.md) or the PostScript printer description (PPD) file, as appropriate, whether the feature information is in the public or private portion of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure.

[XPSDrv print drivers](xpsdrv-printer-drivers.md) can also use the Unidrv printer configuration DLL to provide the required support for both the GDI-based printer configuration interface and the [IPrintTicketProvider interface](https://msdn.microsoft.com/library/windows/hardware/ff554375). If you use the Unidrv configuration DLL, you can expedite the development of XPSDrv printer drivers for basic-functionality printers or pass-through print drivers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Print%20Capabilities%20in%20Unidrv%20and%20PScript5%20Print%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


