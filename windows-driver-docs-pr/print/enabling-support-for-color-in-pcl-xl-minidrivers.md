---
title: Enabling Support for Color in PCL XL Minidrivers
description: Enabling Support for Color in PCL XL Minidrivers
ms.assetid: 3287b070-76e3-4a28-a516-aa58905af224
keywords:
- PCL XL vector graphics WDK Unidrv , enabling color support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

#  Enabling Support for Color in PCL XL Minidrivers





Developing a GPD file for color PCL XL is similar to developing a GPD file for monochrome PCL XL. The main differences are described in this topic. The sample GPD entries presented here might need to be modified appropriately for your device.

-   The GPD file must specify that the device is color.

    That is, the GPD file must contain a ColorMode [standard feature](standard-features.md). Note that the current implementation of PCL XL supports only 24 bits-per-pixel color. The following example shows a ColorMode feature that has two \*Option entries: Mono and 24bpp color.

```cpp
*Feature: ColorMode
{
    *rcNameID: =COLOR_PRINTING_MODE_DISPLAY
    *DefaultOption: 24bpp
    *Option: Mono
    {
        *rcNameID: =MONO_DISPLAY
        *DevNumOfPlanes: 1
        *DevBPP: 24
        *DrvBPP: 24
        *Color? : FALSE
        *PaletteSize: 1
        *PaletteProgrammable? : TRUE
        *Command: CmdDefinePaletteEntry { *Cmd: "" }
    }
    *Option: 24bpp
    {
        *rcNameID: =24BPP_DISPLAY
        *DevNumOfPlanes: 1
        *DevBPP: 24
        *DrvBPP: 24
        *PaletteSize: 256
        *PaletteProgrammable? : TRUE
        *Command: CmdDefinePaletteEntry { *Cmd: "" }
    }
}
```

-   Some commands might need to be changed for color printing.

    For example, if the GPD file allows the user to choose between printing color and monochrome (as in the previous example), the page setup command will be dependent on whether the user is printing in monochrome or in color. In this case the **CmdStartPage** command (see [Printer Configuration Commands](printer-configuration-commands.md)) must be placed within a \*Switch: ColorMode statement, as in the following example. (Note that the number 4 in the \*Order: PAGE\_SETUP.4 command attribute may need to be modified, depending on your GPD file and device.) For more information about the PAGE\_SETUP syntax, see [Command Execution Order](command-execution-order.md).

```cpp
*Switch: ColorMode
{
  *Case: Mono
  {
    *Command: CmdStartPage
    {
    *Order: PAGE_SETUP.4
    *Cmd: =real32_xy "<0000803f><0000803f>" =attr_ubyte =PageScale =SetPageScale
+         =ubyte =eGray =attr_ubyte =ColorSpace =SetColorSpace
    }
  }
  *Case: 24bpp
  {
    *Command: CmdStartPage
    {
    *Order: PAGE_SETUP.4
    *Cmd: =real32_xy "<0000803f><0000803f>" =attr_ubyte =PageScale =SetPageScale
+         =ubyte =eRGB =attr_ubyte =ColorSpace =SetColorSpace
    }
  }
}
```

-   Some commands or information in your GPD that cater to monochrome devices may need to be removed or modified.

    For example, if you modify the p6sample.gpd sample GPD file to add color information, you might want to remove the \*Feature: Dither [customized feature](customized-features.md) or constrain it so that it is used only when printing in monochrome mode.

 

 




