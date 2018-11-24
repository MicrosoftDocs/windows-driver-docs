---
title: Video Content for Deinterlace and Frame-Rate Conversion
description: Video Content for Deinterlace and Frame-Rate Conversion
ms.assetid: 627b394e-c2e1-4327-adaa-0c3436ba3d1a
keywords:
- deinterlacing WDK DirectX VA , received video content
- frame-rate conversion WDK DirectX VA
- received video content WDK DirectX VA
- video content for deinterlacing WDK DirectX VA
- video content for frame-rate conversion WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Content for Deinterlace and Frame-Rate Conversion


## <span id="ddk_video_content_for_deinterlace_and_frame_rate_conversion_gg"></span><span id="DDK_VIDEO_CONTENT_FOR_DEINTERLACE_AND_FRAME_RATE_CONVERSION_GG"></span>


The driver receives a description of video content so that it can determine how it should deinterlace or frame-rate convert such content. The driver receives this video content as a pointer to a [**DXVA\_VideoDesc**](https://msdn.microsoft.com/library/windows/hardware/ff564070) structure in the following function calls:

-   [**DeinterlaceQueryAvailableModes**](https://msdn.microsoft.com/library/windows/hardware/ff563943)

-   [**DeinterlaceQueryModeCaps**](https://msdn.microsoft.com/library/windows/hardware/ff563946)

-   [**DeinterlaceOpenStream**](https://msdn.microsoft.com/library/windows/hardware/ff563935)

The following examples indicate how the driver performs deinterlacing and frame-rate conversion on the received video content.

### <span id="Deinterlacing_720_x_480i_Content_Example"></span><span id="deinterlacing_720_x_480i_content_example"></span><span id="DEINTERLACING_720_X_480I_CONTENT_EXAMPLE"></span>Deinterlacing 720 x 480i Content Example

The DXVA\_VideoDesc structure is filled as follows to direct the driver to deinterlace 720 x 480i content that is sourced as two fields per sample at a frequency of 29.97 Hz.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>SampleWidth</strong></p></td>
<td align="left"><p>720</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SampleHeight</strong></p></td>
<td align="left"><p>480</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>SampleFormat</strong></p></td>
<td align="left"><p><strong>DXVA_SampleFieldInterleavedOddFirst</strong> enumerator in <a href="https://msdn.microsoft.com/library/windows/hardware/ff564045" data-raw-source="[&lt;strong&gt;DXVA_SampleFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564045)"><strong>DXVA_SampleFormat</strong></a></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>d3dFormat</strong></p></td>
<td align="left"><p>D3DFMT_YUY2 defined in the <em>d3d8types.h</em> and <em>d3d9types.h</em> header files</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>InputSampleFreq.Numerator</strong></p></td>
<td align="left"><p>30000 (29.97-Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>InputSampleFreq.Denominator</strong></p></td>
<td align="left"><p>1001</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OutputFrameFreq.Numerator</strong></p></td>
<td align="left"><p>60000 (59.94-Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OutputFrameFreq.Denominator</strong></p></td>
<td align="left"><p>1001</p></td>
</tr>
</tbody>
</table>

 

### <span id="Deinterlacing_and_Frame-Rate_Conversion_of_720_x_480i_Content_Example"></span><span id="deinterlacing_and_frame-rate_conversion_of_720_x_480i_content_example"></span><span id="DEINTERLACING_AND_FRAME-RATE_CONVERSION_OF_720_X_480I_CONTENT_EXAMPLE"></span>Deinterlacing and Frame-Rate Conversion of 720 x 480i Content Example

The **OutputFrameFreq** member of the DXVA\_VideoDesc structure is filled as follows to direct the driver to deinterlace and frame-rate convert 720 x 480i content.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OutputFrameFreq.Numerator</strong></p></td>
<td align="left"><p>85 (85-Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OutputFrameFreq.Denominator</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

### <span id="Deinterlacing_a_Single_Field_to_a_Progressive_Frame_Example"></span><span id="deinterlacing_a_single_field_to_a_progressive_frame_example"></span><span id="DEINTERLACING_A_SINGLE_FIELD_TO_A_PROGRESSIVE_FRAME_EXAMPLE"></span>Deinterlacing a Single Field to a Progressive Frame Example

The **OutputFrameFreq** member of the DXVA\_VideoDesc structure is filled as follows to direct the driver to deinterlace a single field to a progressive frame for later MPEG encoding.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>OutputFrameFreq.Numerator</strong></p></td>
<td align="left"><p>30000 (29.97-Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OutputFrameFreq.Denominator</strong></p></td>
<td align="left"><p>1001</p></td>
</tr>
</tbody>
</table>

 

### <span id="Frame-Rate_Conversion_of__480p_Content_Example"></span><span id="frame-rate_conversion_of__480p_content_example"></span><span id="FRAME-RATE_CONVERSION_OF__480P_CONTENT_EXAMPLE"></span>Frame-Rate Conversion of 480p Content Example

The DXVA\_VideoDesc structure is filled as follows to direct the driver to perform frame-rate conversion on 480p content and to match the monitor display frequency.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>SampleWidth</strong></p></td>
<td align="left"><p>720</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>SampleHeight</strong></p></td>
<td align="left"><p>480</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>SampleFormat</strong></p></td>
<td align="left"><p><strong>DXVA_SampleProgressiveFrame</strong> enumerator in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff564045" data-raw-source="[&lt;strong&gt;DXVA_SampleFormat&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564045)"><strong>DXVA_SampleFormat</strong></a> enumeration</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>d3dFormat</strong></p></td>
<td align="left"><p>D3DFMT_YUY2 defined in the d3d8types.h and d3d9types.h header files</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>InputSampleFreq.Numerator</strong></p></td>
<td align="left"><p>60 (60 Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>InputSampleFreq.Denominator</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>OutputFrameFreq.Numerator</strong></p></td>
<td align="left"><p>85 (85 Hz monitor frequency)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>OutputFrameFreq.Denominator</strong></p></td>
<td align="left"><p>1</p></td>
</tr>
</tbody>
</table>

 

 

 





