---
title: Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD
author: windows-driver-content
description: Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD
MS-HAID:
- 'nt5gpd\_3a94800e-d1b8-4a08-b0ff-ed786dafdb83.xml'
- 'print.enabling\_hp\_gl\_2\_vector\_graphics\_support\_\_pcl\_5e\_\_in\_the\_gpd'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2ca5a2fe-4c37-4b7f-bd9b-d41240f8843f
keywords: ["HP-GL/2 monochrome WDK Unidrv , enabling support", "PCL-5e WDK Unidrv , enabling support"]
---

# Enabling HP-GL/2 Vector Graphics Support (PCL-5e) in the GPD


## <a href="" id="ddk-enabling-hp-gl-2-vector-graphics-support-pcl-5e-in-the-gpd-gg"></a>


To enable HP-GL/2 vector support on Windows XP, you must do two things:

1.  Set the **\*Personality** attribute to PERSONALITY\_HPGL2.

2.  Define a GraphicsMode customized feature that has an HPGL2MODE option. To provide raster graphics support as well, include a RASTERMODE option.

You can set the personality attribute in this way:

```
*Personality: =PERSONALITY_HPGL2
```

The PERSONALITY\_HPGL2 constant is defined in stdnames.gpd.

The following GPD example demonstrates setting the \***Personality** attribute and defining a GraphicsMode customized feature with both a vector graphics mode, as well as a raster graphics mode. Note that the entire block is guarded by an \*Ifdef GPD compiler directive.

```
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

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Enabling%20HP-GL/2%20Vector%20Graphics%20Support%20%28PCL-5e%29%20in%20the%20GPD%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


