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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY


The KSPROPERTY\_CAMERACONTROL\_AUTO\_EXPOSURE\_PRIORITY property specifies whether the device can dynamically vary the frame rate.

### Usage Summary Table

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564439" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564439)"><strong>KSPROPERTY_CAMERACONTROL_S</strong></a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff564420" data-raw-source="[&lt;strong&gt;KSPROPERTY_CAMERACONTROL_NODE_S&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564420)"><strong>KSPROPERTY_CAMERACONTROL_NODE_S</strong></a></p></td>
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

## See also


[**KSPROPERTY\_CAMERACONTROL\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564439)

[**KSPROPERTY\_CAMERACONTROL\_NODE\_S**](https://msdn.microsoft.com/library/windows/hardware/ff564420)

 

 






