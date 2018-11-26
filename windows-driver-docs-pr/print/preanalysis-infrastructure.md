---
title: Preanalysis Infrastructure
description: Preanalysis Infrastructure
ms.assetid: 4c07145a-9a08-4507-8bab-769617e73d77
keywords:
- banding WDK Unidrv
- preanalysis infrastructure WDK Unidrv
- black bands WDK Unidrv
- DrvStretchBlt
- OEMStretchBlt
- DrvStartBanding
- DrvNextBand
- DrvQueryPerBandInfo
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preanalysis Infrastructure





The preanalysis infrastructure is a mechanism by which Unidrv forces banding on a print job so that the first band replay of each page is a band that contains the entire page. The preanalysis pass does not allow any rendering and is done only to enable analysis of the objects on the page before the objects are rendered.

To allow a full-page preanalysis, Unidrv first specifies a full-page device surface within the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function, and then indicates that the first band is the size of the entire page by means of [*DrvQueryPerBandInfo*](https://msdn.microsoft.com/library/windows/hardware/ff556268). After preanalysis is complete, Unidrv uses *DrvQueryPerBandInfo* to restore the clipping region back to its size before the preanalysis was enabled; Unidrv subsequently renders to that surface. Due to implementation limitations of GDI, preanalysis can be enabled only when the N-up mode is ONE\_UP, or if the rendering band is the entire page.

The following pseudocode illustrates the logic used for preanalysis.

```cpp
DrvEnableSurface
if( preanalysis enabled )
   Use dummy device surface
DrvStartDoc
For each physical page 
{
   DrvStartPage
   DrvStartBanding
   For each banding surface 
   {
      DrvQueryPerBandInfo
// Set sizlBand member of PERBANDINFO
      if( preanalysis_pass ) 
         pbi.sizlBand = {whole page}
      else 
         pbi.sizlBand = {normal band}
      Carry out rendering operations
      if ( ( preanalysis pass && OEM preanalysis enabled ) || !preanalysis_pass ) {
         Call OEM hooks
         DrvNextBand
      }
      if ( ( preanalysis pass && OEM preanalysis enabled ) || !preanalysis_pass )
         Call OEMNextBand
      if( preanalysis pass ) {
         Disable preanalysis
         Switch from dummy device surface to real device surface
      }
      if( last band ) 
         Write end page character from GPD
   }  // for each banding surface

}  // for each physical page
DrvEndDoc
```

Because preanalysis functionality must work with current generic printer description (GPD) files and plug-ins, the text z-order, blank band detection, and other operations are implemented invisibly from the perspective of the minidriver. A minidriver can hook [**DrvStartBanding**](https://msdn.microsoft.com/library/windows/hardware/ff556292) and [**DrvNextBand**](https://msdn.microsoft.com/library/windows/hardware/ff556250), but it will not receive the first call to **DrvNextBand** because the first call to **DrvNextBand** does not include any rendering. The plug-in receives the first **DrvNextBand** call only if it sets the flag in the GPD that enables OEM object-level preanalysis (\***PreAnalysisOptions**: 8). In this case the plug-in must hook **DrvStartBanding** and **DrvNextBand**, and the plug-in must check the *pptl* parameter of the **DrvStartBanding** function. If the *pptl* parameter is non-**NULL**, preanalysis is disabled. If the *pptl* parameter is **NULL**, which indicates the start of the preanalysis pass. In this case the plug-in should assume that all of the calls to drawing DDIs that the plug-in has hooked result from the preanalysis pass. The preanalysis pass ends with the first call to the **DrvNextBand** function, and the rendering passes begin after the first call to the **DrvNextBand** function. Subsequent calls to this function will contain rendering data.

### <a href="" id="-preanalysisoptions-modes"></a>\*PreAnalysisOptions Modes

The preanalysis mode is controlled in the GPD file by the \***PreAnalysisOptions**: *n* attribute name and attribute parameter. The following table lists parameter values that can be used with the \***PreAnalysisOptions** attribute name. Two or more of these values can be combined to enable multiple options.

Parameter
Meaning
Value
0

Disable all preanalysis modes.

1

Default mode. Enable monochrome z-order text analysis and blank band optimization. This mode is enabled for devices with downloadable font or device font support and high resolution (600 dpi or higher), 24 BPP render modes.

2

Enable 1 BPP optimization for 24 BPP [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) callbacks.

4

Enable device StretchBlt operations.

8

Enable OEM object-level preanalysis.

 

### Monochrome Z-Order Text Analysis with Blank Band Optimization

```cpp
*PreAnalysisOptions: 1
```

Setting the \***PreAnalysisOptions** parameter to 1 allows Unidrv to perform the following operations:

-   Detect problems in z-order between text and graphic objects in monochrome printers.

-   Perform blank band optimization.

The first operation handles z-order problems that arise when text that is downloaded to a monochrome printer is later overwritten or otherwise interacts with graphics objects. Z-order problems are often caused by graphic objects that contain complex clips so that Unidrv is unable to download a white rectangle that clears previously downloaded text.

Unidrv performs a preanalysis pass on each page before it carries out a rendering pass. Unidrv does this to determine whether any text will be overlaid with a bit-block transfer (blt) object that uses a complex clip that cannot be simulated. Thus, the text is rendered onto the surface bitmap instead of being downloaded directly so that objects rendered later will interact with the text correctly.

In addition, for devices that do not support white rectangles, Unidrv checks for any text overlaid by blts, even when they do not contain complex clips. Unidrv renders the text onto the surface instead of downloading it directly to the printer.

The following drawing commands are tested against text that might be overlaid by subsequent blts:

-   [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180)

-   [**DrvStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556302)

-   [**DrvStretchBltROP**](https://msdn.microsoft.com/library/windows/hardware/ff556306)

-   [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311)

This mode, therefore, should correct all z-order problems between text and filled-region objects. Note that there can still be problems with text and overlaid lines. These situations are not included because such a solution can result in almost all text being downloaded instead of being drawn.

This functionality does not correct z-order problems associated with using device fonts. If the application or driver has selected device font mode, the driver cannot correct this problem and will be unable to render device fonts onto the surface.

The second operation allows Unidrv to optimize for blank regions on the page. In this mode, Unidrv skips over the empty top and bottom margins, as well as any large blank regions in the middle of the page. This mode, which is intended for use in color printing, improves performance by minimizing the number of band passes necessary to render the page.

During the preanalysis pass, Unidrv determines where drawing will occur on the page. Blank band optimization is enabled whenever preanalysis is enabled, or when the printer is using 24 BPP rendering bands at high resolution (600 dpi or higher).This should result in a noticeable performance gain on 24 BPP rendering for ink jet printers and requires no changes to existing OEM plug-ins.

### Black Band Optimization

```cpp
*PreAnalysisOptions: 2  *% 1 bpp ImageProcessing bitmaps
```

Setting the \***PreAnalysisOptions** parameter to 2 allows Unidrv to use a larger 1 BPP banding surface to render regions that contain only solid black objects, rather than rendering the entire page at 24 BPP. This mode is similar to blank band optimization, with the exception that it also determines solid black regions (as opposed to color regions) on the page. Only objects that are solid black (no gray shades) can be rendered in the 1 BPP banding surface because halftone set up for 24 BPP color is not rendered correctly in 1 BPP monochrome.

Unidrv creates two surfaces within the [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) function: one for color and the other for 1 BPP monochrome. Unidrv uses the same memory for each, so no additional memory is required. The page preanalysis determines whether the page contains solid black or blank regions, for which larger bands can be used than for regions that contain colors. Only the color regions require using the smaller color band surface.

Using the same amount of memory, a 1 BPP monochrome surface can be 24 times as large as a 24 BPP color surface. Thus, an image containing color only in the middle of the page can be divided into three regions: the top region, the region that contains the color, and the bottom region. These three regions can be banded as follows: the top region can be placed in a single monochrome band, the region that contains color can be divided into as many color bands as are needed to cover it, and the bottom region can be placed into a single monochrome band.

This functionality requires OEMs to support the **IPrintOemUni::ImageProcessing** callback and to handle the dump of the raster data. Current OEM plug-in support for the **IPrintOemUni::ImageProcessing** callback must be enhanced to accept either 24 BPP bands or 1 BPP solid black bands.

### Support for Device StretchBlt Operations

```cpp
*PreAnalysisOptions: 4
```

Setting the \***PreAnalysisOptions** parameter to 4 allows Unidrv to download [**DrvStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556302) calls directly to devices that support stretchblt operations.

When Unidrv generates 24 BPP color data, all stretchblt images are stretched to the resolution of the device, which results in very large quantities of raster data that must be downloaded. This can result in slow performance, in addition to out-of-memory conditions on many East Asian printers.

A minidriver render plug-in is required to take advantage of the stretchblt mode because it must hook [**OEMStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff559536) and provide its own image download commands. Unidrv allows the OEMStretchBlt hook only on calls that can be directly downloaded. Therefore, the plug-in is not responsible for handling z-order issues. The plug-in needs only to directly download the source image data contained in the OEMStretchBlt calls that it receives. The plug-in also has the option of punting the image back to Unidrv if the image is in a format that the plug-in does not support or cannot download.

Whenever objects are directly downloaded to a device while other data is rendered on the system, there can be z-order problems or halftone inconsistencies. This mode uses preanalysis to determine which stretchblts can be directly downloaded. Only stretchblts that contain no mask or complex clipping will be considered for direct download. If a later object overlays any of the stretchblts being considered for direct download, then no objects will be directly downloaded. This principle should improve performance and should ensure that no image includes halftone from both the system and from the device, which results in very poor quality print output.

### OEM Object-Level Preanalysis Hooks

```cpp
*PreAnalysisOptions: 8
```

Setting the \***PreAnalysisOptions** parameter to 8 allows the OEM to initiate a preanalysis pass so that all of the objects on the entire page are played after the [**DrvStartBanding**](https://msdn.microsoft.com/library/windows/hardware/ff556292) call without regard to band size. No drawing is allowed within Unidrv during the preanalysis pass, but OEMs can hook all of the DrvXxx drawing calls to analyze the objects on the page.

The functionality in this mode is focused on color ink jet printers so that OEMs can use object-based color correction or rendering. For example, certain printers need to handle black objects differently if they intersect with color objects, as opposed to black objects that appear by themselves. Other OEMs might want a halftone for stretchblt objects that are different from bitblt objects. Stretchblt objects can be in any graphics file format that Windows supports, such as .png or .jpg. Bitblt objects are exclusively bitmaps.

When this mode is enabled in the GPD, Unidrv defines the surface as a banding surface, but causes the first playback to be of the entire page. To do this, Unidrv sets the GDI clip window to the entire page. Unidrv allows all drawing commands to be hooked, but returns before any drawing can be performed. On following passes, Unidrv resets the clip window back to the normal band size and bands as usual.

OEMs are required to hook both **DrvStartBanding** and [**DrvNextBand**](https://msdn.microsoft.com/library/windows/hardware/ff556250) when they have enabled this mode in the GPD. They must test the *pptl* parameter of the **DrvStartBanding** function to determine whether Unidrv can enable preanalysis in this mode on the specified page. If the *pptl* parameter is **NULL**, then Unidrv has enabled preanalysis. Unidrv uses the *pptl* parameter because it has no meaning at this point (it has not been updated with the band position. For preanalysis, the band position is always set to (0, 0)). If the *pptl* parameter is **NULL**, then the OEM should consider all drawing calls prior to the first **DrvNextBand** to be part of preanalysis and should permit no drawing onto the surface.

The end of preanalysis is signaled by a call to the **OEMNextBand** function. The *pptl* parameter that is passed to **OEMNextBand** is not **NULL**. This call is used only to return the appropriate *pptl* value to Unidrv. Plug-ins can set the *pptl* value themselves or can call back into Unidrv (like the preceding pseudocode example at the beginning of this topic does). Because the banding surface that the *pso* parameter of **OEMNextBand** specified in the first call to **OEMNextBand** has not rendered yet, a plug-in should not send its contents to the device.

 

 




