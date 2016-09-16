---
title: Device-Supplied Halftoning
author: windows-driver-content
description: Device-Supplied Halftoning
MS-HAID:
- 'nt5gpd\_b75cca34-5c19-41fb-be92-8b1ab5906e2d.xml'
- 'print.device\_supplied\_halftoning'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d1d7963e-c23e-4cb5-a33f-43fec5dc74d2
keywords: ["device-supplied halftoning WDK Unidrv"]
---

# Device-Supplied Halftoning


## <a href="" id="ddk-device-supplied-halftoning-gg"></a>


If your printer provides halftoning capabilities internally, your minidriver must specify the commands that Unidrv sends to the printer to activate these capabilities. For each halftoning option that is printer-supported, your GPD file's Halftone \*Feature entry must include \*Command entries for each device-supplied halftoning option, as follows:

```
*Feature: Halftone
{
    *Option: CustomHalftoneMethod1
    {
        *Name: "Custom Halftone Method 1"
        *Command: CmdSelect: "<printer command string>"
    }
    *Option: CustomHalftoneMethod2
    {
        *Name: "Custom Halftone Method 2"
        *Command: CmdSelect: "<printer command string>"
    }
}
```

ColorMode feature entries must also be specified, and they must include \*DevBPP and \*DevNumOfPlanes entries describing the input formats expected by the printer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Device-Supplied%20Halftoning%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


