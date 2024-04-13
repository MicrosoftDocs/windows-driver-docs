---
title: Device-Supplied Halftoning
description: Device-Supplied Halftoning
keywords:
- device-supplied halftoning WDK Unidrv
ms.date: 01/27/2023
---

# Device-Supplied Halftoning

[!include[Print Support Apps](../includes/print-support-apps.md)]

If your printer provides halftoning capabilities internally, your minidriver must specify the commands that Unidrv sends to the printer to activate these capabilities. For each halftoning option that is printer-supported, your GPD file's Halftone \*Feature entry must include \*Command entries for each device-supplied halftoning option, as follows:

```GPD
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
