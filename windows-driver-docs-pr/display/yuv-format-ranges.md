---
title: YUV format ranges in Windows 8.1
ms.assetid: D76FFB8C-CA42-446E-826F-52982B1849E5
description: How User-mode display drivers take advantage of YUV video formats
keywords:
- full-range YUV WDK display
- extended-range YUV WDK display
- studio luminance range YUV WDK display
- YUV formats and WMF support WDK display
ms.date: 04/20/2017
keywords: ["full-range YUV WDK display", "extended-range YUV WDK display", "studio luminance range YUV WDK display", "YUV formats and WMF support WDK display"]
ms.localizationpriority: medium
---

# YUV format ranges in Windows 8.1


Apps can signal user-mode display drivers to take advantage of extended-range \[0, 255\] YUV video formats starting in Windows 8.1, as shown in this table:

| YUV range                | Input data range | Typical usage                                           | Standard                                                  |
|--------------------------|------------------|---------------------------------------------------------|-----------------------------------------------------------|
| *extended range*         | \[0, 255\]       | consumer equipment: webcams and point-and-shoot cameras | JFIF standard, and MJPEG video format uses as the default |
| *studio luminance range* | \[16, 235\]      | professional cameras and video equipment                | ITU BT.601 and BT.709                                     |

 

Most video produced by the content and broadcast industry is in studio range, while video produced by individual consumers is in extended range. Extended range is also called *full luminance range*.

Before Windows 8.1, the Microsoft Media Foundation video processing pipeline acted on all input data as if it were in studio range, which results in reduced dynamic range and often harsh contrast if the input data was actually in extended range.

Starting in Windows 8.1, when video input YUV formats are in extended range, apps can notify drivers of this higher dynamic range.

## <span id="Converting_extended-range_YUV_format"></span><span id="converting_extended-range_yuv_format"></span><span id="CONVERTING_EXTENDED-RANGE_YUV_FORMAT"></span>Converting extended-range YUV format


These images show how YUV extended-range content that ranges from dark to light values is converted (interpreted) to RGB format:

-   The top image shows extended-range content interpreted incorrectly, as if it were studio range.
-   The bottom image shows extended-range content interpreted correctly.

The incorrect interpretation in the top image shows increased contrast and highlights become excessively bright before pure white is reached.

![comparison of incorrect and correct interpretation of extended-range yuv content](images/extended-range-yuv.png)

## <span id="Extended-range_YUV_interface"></span><span id="extended-range_yuv_interface"></span><span id="EXTENDED-RANGE_YUV_INTERFACE"></span>Extended-range YUV interface


Before Windows 8.1, Media Foundation only supported studio luminance range, so interpretations of extended-range images resulted in increased contrast, as shown in the first image above. Starting with Windows 8.1, the Media Foundation pipeline uses these structures and enumerations to indicate to Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers whether extended-range or studio-range YUV content is being played or captured:

### <span id="New_enumerations"></span><span id="new_enumerations"></span><span id="NEW_ENUMERATIONS"></span>New enumerations

-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_NOMINAL\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/dn265173)
-   [**DXVAHDDDI\_NOMINAL\_RANGE**](https://msdn.microsoft.com/library/windows/hardware/dn265432)

### <span id="Changed_structures_and_enumerations"></span><span id="changed_structures_and_enumerations"></span><span id="CHANGED_STRUCTURES_AND_ENUMERATIONS"></span>Changed structures and enumerations

-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_COLOR\_SPACE**](https://msdn.microsoft.com/library/windows/hardware/hh450970)
-   [**D3D11\_1DDI\_VIDEO\_PROCESSOR\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/hh450978)
-   [**DXVAHDDDI\_BLT\_STATE\_OUTPUT\_COLOR\_SPACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff563002)
-   [**DXVAHDDDI\_STREAM\_STATE\_INPUT\_COLOR\_SPACE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff563084)
-   [**DXVAHDDDI\_VPDEVCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff563113)

**Note**  WDDM 1.3 and greater user-mode display drivers must support all of these new and changed structures and enumerations.

 

See [YUV-RGB data range conversions](yuv-rgb-data-range-conversions.md) for details on how to convert between different input RGB and YUV formats.

 

 





