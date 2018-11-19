---
title: Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD
description: Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD
ms.assetid: 2ca5a2fe-4c37-4b7f-bd9b-d41240f8843f
keywords:
- HP-GL/2 monochrome WDK Unidrv , enabling support
- PCL-5e WDK Unidrv , enabling support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD





To enable HP-GL/2 vector support on Windows XP, you must do two things:

1.  Set the **\*Personality** attribute to PERSONALITY\_HPGL2.

2.  Define a GraphicsMode customized feature that has an HPGL2MODE option. To provide raster graphics support as well, include a RASTERMODE option.

You can set the personality attribute in this way:

```cpp
*Personality: =PERSONALITY_HPGL2
```

The PERSONALITY\_HPGL2 constant is defined in stdnames.gpd.

The following GPD example demonstrates setting the \***Personality** attribute and defining a GraphicsMode customized feature with both a vector graphics mode, as well as a raster graphics mode. Note that the entire block is guarded by an \*Ifdef GPD compiler directive.

```cpp
*Ifdef: WINNT_51
*Personality: =PERSONALITY_HPGL2
*Feature: GraphicsMode
{
    *rcNameID: =GRAPHICSMODE_DISPLAY
    *FeatureType: DOC_PROPERTY
    *HelpIndex: 12000
    *DefaultOption: HPGL2MODE
    *Option: HPGL2MODE
    {
        *rcNameID: =GRAPHICSMODE_HPGL2_DISPLAY
    }
    *Option: RASTERMODE
    {
        *rcNameID: =GRAPHICSMODE_RASTER_DISPLAY
    }
}
*Endif:
```

The WINNT\_51 parameter used in the above directive applies to versions of Unidrv, rather than operating system versions. For a Windows XP Unidrv printer driver running on Windows 2000, the WINNT\_51 parameter is defined and the block is compiled. For earlier Unidrv versions, regardless of operating system version, this parameter is undefined, and the block is not compiled.

A GPD file for a color printer should also define a ColorMode feature, as shown in the following generic sample. Note that specific details of your printer might require changes to certain values.

```cpp
*Feature: ColorMode
{
  *rcNameID: =COLOR_PRINTING_MODE_DISPLAY
  *HelpIndex: 12004
  *DefaultOption: 24bpp
  *Option: Mono
   {
     *rcNameID: =MONO_DISPLAY
     *DevNumOfPlanes: 1
     *DevBPP: 1
     *Color?: FALSE
     *Command: CmdSelect
      {
        *Order: PAGE_SETUP.16 
        *Cmd: "<1B>&b1M"
      }
   }
  *Option: 24bpp
   {
     *rcNameID: =24BPP_DISPLAY
     *DevNumOfPlanes: 1
     *DevBPP: 24
     *DrvBPP: 24
     *PaletteSize: 256
     *PaletteProgrammable?: TRUE
     *Command: CmdDefinePaletteEntry
      {
        *Cmd : "<1B>*v" %d{RedValue}"a"
+                       %d{GreenValue}"b"
+                       %d{BlueValue}"c"
+                       %d{PaletteIndexToProgram}"I"
 }
     *Command: CmdSelectPaletteEntry { *Cmd : "<1B>*v" 
+                        %d{CurrentPaletteIndex}"S" }
     *Command: CmdSetSrcBmpWidth { *Cmd : "<1B>*r" 
+                        %d{RasterDataWidthInBytes / 3}"S" }
     *Command: CmdSelect
      {
        *Order: PAGE_SETUP.16
        *Cmd: "<1B>*v1N<1B>*v1O<1B>*l184O<1B>*v6W<000308080808>
+              <1B>*v0a0b0c7i255a255b255c"
      }
   }
}
```

 

 




