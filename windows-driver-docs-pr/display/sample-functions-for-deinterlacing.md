---
title: Sample Functions for Deinterlacing
description: Sample Functions for Deinterlacing
ms.assetid: a91c0267-7a3e-4206-8680-6e87778a329d
keywords:
- deinterlacing WDK DirectX VA , sample functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Functions for Deinterlacing


## <span id="ddk_sample_functions_for_deinterlacing_gg"></span><span id="DDK_SAMPLE_FUNCTIONS_FOR_DEINTERLACING_GG"></span>


The sample deinterlacing functions in this section show how to implement deinterlacing and frame-rate conversion functionality. The sample functions map to the [motion compensation callback functions](motion-compensation-callbacks.md) defined in the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. You can implement each sample function and then use the motion-compensation code template to complete the implementation. For more information, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

### <span id="Deinterlace_Container_Device_Class_Sample_Functions"></span><span id="deinterlace_container_device_class_sample_functions"></span><span id="DEINTERLACE_CONTAINER_DEVICE_CLASS_SAMPLE_FUNCTIONS"></span>Deinterlace Container Device Class Sample Functions

The sample deinterlacing functions in the following table are member functions of *DXVA\_DeinterlaceContainerDeviceClass* (that is, they are called by using the deinterlace container device). For more information, see [Defining the Deinterlace Container Device Class](defining-the-deinterlace-container-device-class.md) and [Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563943" data-raw-source="[&lt;strong&gt;DeinterlaceQueryAvailableModes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563943)"><strong>DeinterlaceQueryAvailableModes</strong></a></p></td>
<td align="left"><p>Queries for available deinterlacing and frame-rate conversion modes.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563946" data-raw-source="[&lt;strong&gt;DeinterlaceQueryModeCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563946)"><strong>DeinterlaceQueryModeCaps</strong></a></p></td>
<td align="left"><p>Queries for the capabilities of a given deinterlacing and frame-rate conversion mode.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Deinterlace_Bob_Device_Class_Sample_Functions"></span><span id="deinterlace_bob_device_class_sample_functions"></span><span id="DEINTERLACE_BOB_DEVICE_CLASS_SAMPLE_FUNCTIONS"></span>Deinterlace Bob Device Class Sample Functions

The sample deinterlacing functions in the following table are member functions of *DXVA\_DeinterlaceBobDeviceClass* (that is, they are called by using the deinterlace bob device). For more information, see [Defining the Deinterlace Bob Device Class](defining-the-deinterlace-bob-device-class.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Member Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563935" data-raw-source="[&lt;strong&gt;DeinterlaceOpenStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563935)"><strong>DeinterlaceOpenStream</strong></a></p></td>
<td align="left"><p>Opens a video stream object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563924" data-raw-source="[&lt;strong&gt;DeinterlaceBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563924)"><strong>DeinterlaceBlt</strong></a></p></td>
<td align="left"><p>Provides bit-block deinterlacing of video stream objects.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563927" data-raw-source="[&lt;strong&gt;DeinterlaceBltEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563927)"><strong>DeinterlaceBltEx</strong></a></p></td>
<td align="left"><p><strong>Windows Server 2003 SP1 and later and Windows XP SP2 and later only.</strong></p>
<div>
 
</div>
Deinterlaces video and composites video substreams over the top of the video stream.</td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563931" data-raw-source="[&lt;strong&gt;DeinterlaceCloseStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563931)"><strong>DeinterlaceCloseStream</strong></a></p></td>
<td align="left"><p>Closes a video stream object.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Mapping_Sample_Functions_to_DD_MOTIONCOMPCALLBACKS"></span><span id="mapping_sample_functions_to_dd_motioncompcallbacks"></span><span id="MAPPING_SAMPLE_FUNCTIONS_TO_DD_MOTIONCOMPCALLBACKS"></span>Mapping Sample Functions to DD\_MOTIONCOMPCALLBACKS

The sample functions in this section map to the motion compensation callback functions as shown in the following table. That is, each sample function is called within its respective motion compensation callback.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">DD_MOTIONCOMPCALLBACKS Member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563943" data-raw-source="[&lt;strong&gt;DeinterlaceQueryAvailableModes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563943)"><strong>DeinterlaceQueryAvailableModes</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563946" data-raw-source="[&lt;strong&gt;DeinterlaceQueryModeCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563946)"><strong>DeinterlaceQueryModeCaps</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563935" data-raw-source="[&lt;strong&gt;DeinterlaceOpenStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563935)"><strong>DeinterlaceOpenStream</strong></a></p></td>
<td align="left"><p><strong>CreateMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563924" data-raw-source="[&lt;strong&gt;DeinterlaceBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563924)"><strong>DeinterlaceBlt</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563927" data-raw-source="[&lt;strong&gt;DeinterlaceBltEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563927)"><strong>DeinterlaceBltEx</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563931" data-raw-source="[&lt;strong&gt;DeinterlaceCloseStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563931)"><strong>DeinterlaceCloseStream</strong></a></p></td>
<td align="left"><p><strong>DestroyMoComp</strong></p></td>
</tr>
</tbody>
</table>

 

 

 





