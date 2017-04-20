---
title: V4 Print Class Driver Rendering
author: windows-driver-content
description: For rendering, the v4 printer driver can utilize the existing rendering capabilities of a Print Class driver.
ms.assetid: F8178988-1C11-4B21-B250-6626528E0AE5
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# V4 Print Class Driver Rendering


For rendering, the v4 printer driver can utilize the existing rendering capabilities of a Print Class driver.

To utilize the existing rendering capabilities of a print class driver, a v4 printer driver can use the **RequiredClass** v4 manifest directive. Using the **RequiredClass** directive causes the driver to include all the files from the specified class driver, using the driver name and the friendly name of the device as a key. That is the mechanism for linking a print class driver to a model-specific printer driver.

For example, a company called Fabrikam with a print class driver named *PCL5e*, could use the following sample print driver manifest to link their print class driver to their printer driver:

```Text
[DriverConfig]
DataFile=FAPDL.gpd
RequiredFiles=UNIRES.DLL,STDNAMES.GPD,STDDTYPE.GDL,STDSCHEM.GDL,STDSCHMX.GDL,MSXPSINC.GPD
RequiredClass="Fabrikam PCL5e Class Driver" ; This links the print class driver to this printer driver
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

**Note**  The **RequiredClass** directive cannot be used by a class driver. When you use **RequiredClass**, you should avoid file name collisions between the printer driver and the print class driver to which you're linking. Although files with similar names won't overwrite each other, it may be difficult during troubleshooting, to distinguish between the class driver package file and the file from the v4 printer driver.

 

For more information about v4 printer driver manifest directives, see [V4 Driver Manifest](v4-driver-manifest.md).

## Related topics
[V4 Driver Manifest](v4-driver-manifest.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20V4%20Print%20Class%20Driver%20Rendering%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


