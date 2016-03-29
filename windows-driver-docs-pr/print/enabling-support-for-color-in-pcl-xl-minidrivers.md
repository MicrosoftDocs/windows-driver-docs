---
title: Enabling Support for Color in PCL XL Minidrivers
description: Enabling Support for Color in PCL XL Minidrivers
ms.assetid: 3287b070-76e3-4a28-a516-aa58905af224
keywords: ["PCL XL vector graphics WDK Unidrv , enabling color support"]
---

#  Enabling Support for Color in PCL XL Minidrivers


## <a href="" id="ddk-enabling-support-for-color-in-pcl-xl-minidrivers-gg"></a>


Developing a GPD file for color PCL XL is similar to developing a GPD file for monochrome PCL XL. The main differences are described in this topic. The sample GPD entries presented here might need to be modified appropriately for your device.

-   The GPD file must specify that the device is color.

    That is, the GPD file must contain a ColorMode [standard feature](standard-features.md). Note that the current implementation of PCL XL supports only 24 bits-per-pixel color. The following example shows a ColorMode feature that has two \*Option entries: Mono and 24bpp color.

```
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

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20%20Enabling%20Support%20for%20Color%20in%20PCL%20XL%20Minidrivers%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




