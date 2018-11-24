---
title: Device-Supplied Halftoning
description: Device-Supplied Halftoning
ms.assetid: d1d7963e-c23e-4cb5-a33f-43fec5dc74d2
keywords:
- device-supplied halftoning WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device-Supplied Halftoning





If your printer provides halftoning capabilities internally, your minidriver must specify the commands that Unidrv sends to the printer to activate these capabilities. For each halftoning option that is printer-supported, your GPD file's Halftone \*Feature entry must include \*Command entries for each device-supplied halftoning option, as follows:

```cpp
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

 

 




