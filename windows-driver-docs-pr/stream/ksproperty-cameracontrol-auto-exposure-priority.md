---
title: KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY
description: The KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY property specifies whether the device can dynamically vary the frame rate.
ms.assetid: 0e20a4ee-b672-4c9a-9003-c2defd378e7c
keywords: ["KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY


The KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY property specifies whether the device can dynamically vary the frame rate.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>Yes</p></td>
<td><p>Filter or node</p></td>
<td><p>[<strong>KSPROPERTY_CAMERACONTROL_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564439), [<strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564420)</p></td>
<td><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a ULONG that specifies whether frame rate can be dynamically varied by the device.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>0</p></td>
<td><p>Frame rate must remain constant.</p></td>
</tr>
<tr class="even">
<td><p>1</p></td>
<td><p>Frame rate can be dynamically varied by the device.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Auto-exposure priority determines whether the camera can dynamically vary the frame rate depending on lighting conditions.

Without auto-exposure, for instance, if the frame rate is 30 fps, the exposure time cannot exceed 33 ms.

With auto-exposure priority, however, the camera could compensate for low lighting by decreasing the frame rate. For instance, the camera could reduce frame rate to 25 fps, thereby lengthening exposure time to 40 ms.

KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY maps to the **Low-Light Compensation** check box on the USB Video Class property page.

In order to use KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY, you must set [**KSPROPERTY\_CAMERACONTROL\_EXPOSURE**](ksproperty-cameracontrol-exposure.md) to auto. In other words, the camera must be in auto-exposure mode for the auto-exposure-priority mode to be a valid option.

The default value for KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY is zero.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available for Windows Vista and later versions of the Windows operating system.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY\_CAMERACONTROL\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564439)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_AUTO_EXPOSURE_PRIORITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





