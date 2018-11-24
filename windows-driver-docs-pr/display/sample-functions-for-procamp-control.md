---
title: Sample Functions for ProcAmp Control
description: Sample Functions for ProcAmp Control
ms.assetid: d158216e-9a34-48a4-adca-e3c20b5e4487
keywords:
- ProcAmp WDK DirectX VA , sample functions
- ranges WDK ProcAmp
- properties WDK ProcAmp
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Functions for ProcAmp Control


## <span id="ddk_sample_functions_for_procamp_control_gg"></span><span id="DDK_SAMPLE_FUNCTIONS_FOR_PROCAMP_CONTROL_GG"></span>


The sample ProcAmp functions in this section show how to implement ProcAmp control functionality. These sample functions map to the [motion compensation callback functions](motion-compensation-callbacks.md) defined in the [**DD\_MOTIONCOMPCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff551660) structure. You can implement each sample function, and then use a motion-compensation code template to complete the implementation. For more information, see [Example Code for DirectX VA Devices](example-code-for-directx-va-devices.md).

### <span id="Deinterlace_Container_Device_Class_Sample_Functions"></span><span id="deinterlace_container_device_class_sample_functions"></span><span id="DEINTERLACE_CONTAINER_DEVICE_CLASS_SAMPLE_FUNCTIONS"></span>Deinterlace Container Device Class Sample Functions

The sample ProcAmp control functions in the following table are member functions of *DXVA\_DeinterlaceContainerDeviceClass* (that is, they are called using the deinterlace container device). For more information, see [Defining the Deinterlace Container Device Class](defining-the-deinterlace-container-device-class.md) and [Performing ProcAmp Control and Deinterlacing Operations](performing-procamp-control-and-deinterlacing-operations.md).

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563949" data-raw-source="[&lt;strong&gt;ProcAmpControlQueryCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563949)"><strong>ProcAmpControlQueryCaps</strong></a></p></td>
<td align="left"><p>Queries the driver to determine input requirements of the ProcAmp control device.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563950" data-raw-source="[&lt;strong&gt;ProcAmpControlQueryRange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563950)"><strong>ProcAmpControlQueryRange</strong></a></p></td>
<td align="left"><p>Queries the driver to determine the minimum, maximum, step size, and default value for each ProcAmp property.</p></td>
</tr>
</tbody>
</table>

 

### <span id="ProcAmp_Control_Device_Class_Sample_Functions"></span><span id="procamp_control_device_class_sample_functions"></span><span id="PROCAMP_CONTROL_DEVICE_CLASS_SAMPLE_FUNCTIONS"></span>ProcAmp Control Device Class Sample Functions

The sample ProcAmp control functions in the following table are member functions of *DXVA\_ProcAmpControlDeviceClass* (that is, they are called using the ProcAmp control device). For more information, see [Defining the ProcAmp Control Device Class](defining-the-procamp-control-device-class.md).

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564026" data-raw-source="[&lt;strong&gt;ProcAmpControlOpenStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564026)"><strong>ProcAmpControlOpenStream</strong></a></p></td>
<td align="left"><p>Creates a ProcAmp stream object.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564022" data-raw-source="[&lt;strong&gt;ProcAmpControlBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564022)"><strong>ProcAmpControlBlt</strong></a></p></td>
<td align="left"><p>Performs the ProcAmp adjustment operation by writing the output to the destination surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564025" data-raw-source="[&lt;strong&gt;ProcAmpControlCloseStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564025)"><strong>ProcAmpControlCloseStream</strong></a></p></td>
<td align="left"><p>Closes the ProcAmp stream object and instructs the device driver to release hardware resources associated with the stream.</p></td>
</tr>
</tbody>
</table>

 

### <span id="Mapping_Sample_Functions_to_DD_MOTIONCOMPCALLBACKS"></span><span id="mapping_sample_functions_to_dd_motioncompcallbacks"></span><span id="MAPPING_SAMPLE_FUNCTIONS_TO_DD_MOTIONCOMPCALLBACKS"></span>Mapping Sample Functions to DD\_MOTIONCOMPCALLBACKS

The sample functions in this section map to the motion compensation callback functions as follows. That is, each sample function is called within its respective motion-compensation callback.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">DD_MOTIONCOMPCALLBACKS member</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563949" data-raw-source="[&lt;strong&gt;ProcAmpControlQueryCaps&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563949)"><strong>ProcAmpControlQueryCaps</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff563950" data-raw-source="[&lt;strong&gt;ProcAmpControlQueryRange&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563950)"><strong>ProcAmpControlQueryRange</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564026" data-raw-source="[&lt;strong&gt;ProcAmpControlOpenStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564026)"><strong>ProcAmpControlOpenStream</strong></a></p></td>
<td align="left"><p><strong>CreateMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564022" data-raw-source="[&lt;strong&gt;ProcAmpControlBlt&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564022)"><strong>ProcAmpControlBlt</strong></a></p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564025" data-raw-source="[&lt;strong&gt;ProcAmpControlCloseStream&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564025)"><strong>ProcAmpControlCloseStream</strong></a></p></td>
<td align="left"><p><strong>DestroyMoComp</strong></p></td>
</tr>
</tbody>
</table>

 

 

 





