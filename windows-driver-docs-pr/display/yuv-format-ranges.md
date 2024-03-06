---
title: YUV Format Ranges in Windows 8.1
description: How User-mode display drivers take advantage of YUV video formats
keywords:
- full-range YUV WDK display
- extended-range YUV WDK display
- studio luminance range YUV WDK display
- YUV formats and WMF support WDK display
ms.date: 04/20/2017
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

## Converting extended-range YUV format

These images show how YUV extended-range content that ranges from dark to light values is converted (interpreted) to RGB format:

* The top image shows extended-range content interpreted incorrectly, as if it were studio range.
* The bottom image shows extended-range content interpreted correctly.

The incorrect interpretation in the top image shows increased contrast and highlights become excessively bright before pure white is reached.

:::image type="content" source="images/extended-range-yuv.png" alt-text="Two images comparing incorrect and correct interpretation of extended-range YUV content in RGB format.":::

## Extended-range YUV interface

Before Windows 8.1, Media Foundation only supported studio luminance range, so interpretations of extended-range images resulted in increased contrast, as shown in the first image above. Starting with Windows 8.1, the Media Foundation pipeline uses these structures and enumerations to indicate to Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers whether extended-range or studio-range YUV content is being played or captured:

### New enumerations

* [**D3D11_1DDI_VIDEO_PROCESSOR_NOMINAL_RANGE**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d11_1ddi_video_processor_nominal_range)
* [**DXVAHDDDI_NOMINAL_RANGE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_dxvahdddi_nominal_range)

### Changed structures and enumerations

* [**D3D11_1DDI_VIDEO_PROCESSOR_COLOR_SPACE**](/windows-hardware/drivers/ddi/d3d10umddi/ns-d3d10umddi-d3d11_1ddi_video_processor_color_space)
* [**D3D11_1DDI_VIDEO_PROCESSOR_DEVICE_CAPS**](/windows-hardware/drivers/ddi/d3d10umddi/ne-d3d10umddi-d3d11_1ddi_video_processor_device_caps)
* [**DXVAHDDDI_BLT_STATE_OUTPUT_COLOR_SPACE_DATA**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_blt_state_output_color_space_data)
* [**DXVAHDDDI_STREAM_STATE_INPUT_COLOR_SPACE_DATA**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_stream_state_input_color_space_data)
* [**DXVAHDDDI_VPDEVCAPS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_dxvahdddi_vpdevcaps)

WDDM 1.3 and greater user-mode display drivers must support all of these new and changed structures and enumerations.

See [YUV-RGB data range conversions](yuv-rgb-data-range-conversions.md) for details on how to convert between different input RGB and YUV formats.
