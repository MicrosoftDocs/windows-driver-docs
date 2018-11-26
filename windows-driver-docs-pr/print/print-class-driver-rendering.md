---
title: V4 Print Class Driver Rendering
description: For rendering, the v4 printer driver can utilize the existing rendering capabilities of a Print Class driver.
ms.assetid: F8178988-1C11-4B21-B250-6626528E0AE5
ms.date: 07/13/2018
ms.localizationpriority: medium
---

# V4 Print Class Driver Rendering


For rendering, the v4 printer driver can utilize the existing rendering capabilities of a Print Class driver.

To utilize the existing rendering capabilities of a print class driver, a v4 printer driver can use the **RequiredClass** v4 manifest directive. Using the **RequiredClass** directive causes the driver to include all the files from the specified class driver, using the driver/friendly name of the device and its GUID as key. That is the mechanism for linking a print class driver to a model-specific printer driver.

For example, a company called Fabrikam with a print class driver named *PCL5e*, could use the following sample print driver manifest to link their print class driver to their printer driver:

```Text
[DriverConfig]
DataFile=FAPDL.gpd
RequiredFiles=UNIRES.DLL,STDNAMES.GPD,STDDTYPE.GDL,STDSCHEM.GDL,STDSCHMX.GDL,MSXPSINC.GPD
RequiredClass="Fabrikam PCL5e Class Driver",{9343720D-B67E-4451-B93F-6F721C439771} ; This links the print class driver to this printer driver
ResourceFile=FARC.dll
PropertyBag=FAProperty.dpb
PrinterDriverID={GUID}
DriverCategory=PrintFax.Printer
ConstraintScript=faconst.js
EventFile=faevents.xml
PrinterExtensionUrl="http://www.fabrikam.com/download.asp?uiapp=120"

[BidiFiles]
BidiSPMFile=FABidiSPM.xml
BidiWSDFile=FABidiWSD.xml
BidiUSBFile=FaBidiUSB.xml
BidiUSBJSFile=FABidiUSBJS.js 

[DriverRender]
PageOutputQuality.Draft=MxdcImageType.JPEGHigh
PageOutputQuality.Normal= MxdcImageType.JPEGMedium
PageOutputQuality.High=MxdcImageType.PNG

[PrinterExtensions]
DriverEvent=FAapp.exe,{GUID}
PrintPreferences=FAapp.exe,{GUID2}
```

> [!NOTE]
> The **RequiredClass** directive cannot be used by a class driver. When you use **RequiredClass**, you should avoid file name collisions between the printer driver and the print class driver to which you're linking. Although files with similar names won't overwrite each other, it may be difficult during troubleshooting, to distinguish between the class driver package file and the file from the v4 printer driver.

 
For more information about v4 printer driver manifest directives, see [V4 Driver Manifest](v4-driver-manifest.md).

## Related topics

[V4 Driver Manifest](v4-driver-manifest.md)  



