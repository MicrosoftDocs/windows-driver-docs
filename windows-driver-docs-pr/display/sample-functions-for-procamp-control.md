---
title: Sample Functions for ProcAmp Control
description: Sample Functions for ProcAmp Control
ms.assetid: d158216e-9a34-48a4-adca-e3c20b5e4487
keywords: ["ProcAmp WDK DirectX VA , sample functions", "ranges WDK ProcAmp", "properties WDK ProcAmp"]
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
<td align="left"><p>[<strong>ProcAmpControlQueryCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563949)</p></td>
<td align="left"><p>Queries the driver to determine input requirements of the ProcAmp control device.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ProcAmpControlQueryRange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563950)</p></td>
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
<td align="left"><p>[<strong>ProcAmpControlOpenStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564026)</p></td>
<td align="left"><p>Creates a ProcAmp stream object.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ProcAmpControlBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564022)</p></td>
<td align="left"><p>Performs the ProcAmp adjustment operation by writing the output to the destination surface.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ProcAmpControlCloseStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564025)</p></td>
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
<td align="left"><p>[<strong>ProcAmpControlQueryCaps</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563949)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ProcAmpControlQueryRange</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563950)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ProcAmpControlOpenStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564026)</p></td>
<td align="left"><p><strong>CreateMoComp</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>ProcAmpControlBlt</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564022)</p></td>
<td align="left"><p><strong>RenderMoComp</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>ProcAmpControlCloseStream</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564025)</p></td>
<td align="left"><p><strong>DestroyMoComp</strong></p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Sample%20Functions%20for%20ProcAmp%20Control%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




