---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration provides OEMs with capabilities to fine tune the scene mode along with any other ISP control parameters as needed.
ms.assetid: CB3F89AD-4B53-4E47-B60E-4B584DB8418B
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration provides OEMs with capabilities to fine tune the scene mode along with any other ISP control parameters as needed.

## <span id="Usage_summary_table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage summary table


<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Scope</th>
<th>Control</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version 1</p></td>
<td><p>Filter</p></td>
<td><p>Asynchronous</p></td>
</tr>
</tbody>
</table>

 

The scene mode is used as a hint to guide the camera system to optimize its operation for certain conditions. Scene mode and other ISP controls such as White Balance, ISO, Exposure time, and EV compensation must be able to work independently without impacting each other.

-   The changing of any other ISP control parameters must not change the existing scene mode. The driver is not required to change the scene mode to MANUAL after other ISP parameters are modified.

-   Setting the auto scene mode must not change the existing settings for any other ISP controls. The driver is not required to revert to full auto mode for any other ISP controls.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_AUTO**

This flag indicates the auto scene mode. The camera driver will automatically determine the best scene mode settings based on the scene and optimize the various ISP settings as needed for the scene.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MANUAL**

This flag is not applicable.

**KSCAMERA\_EXTENDEDPROP\_SCENEMODE\_MACRO\\PORTRAIT\\SPORT\\SNOW\\NIGHT\\BEACH\\SUNSET\\CANDLELIGHT\\LANDSCAPE\\NIGHTPORTRAIT\\BACKLIT**

These flags indicate the corresponding scene mode as defined. The camera driver will use the scene mode specified as a hint to optimize the various ISP settings as needed (for example, for NIGHT, the ISP settings are optimized for night time environment).

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE** property. The [**KSCAMERA\_EXTENDEDPROP\_VALUE**](https://msdn.microsoft.com/library/windows/hardware/dn567565) structure is ignored for **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_SCENEMODE**.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>This must be 1.</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>This must be <strong>KSCAMERA_EXTENDEDPROP_FILTERSCOPE</strong> (0xFFFFFFFF).</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + sizeof(<strong>KSCAMERA_EXTENDEDPROP_VALUE</strong>).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0. The value 0 indicates no errors were detected.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be a bitwise OR of <strong>KSCAMERA_EXTENDEDPROP_CAPS_ASYNCCONTROL</strong> and any of the supported scene modes defined above. <strong>KSCAMERA_EXTENDEDPROP_SCENEMODE_AUTO</strong> must be supported if the camera driver supports this control.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This can be any of the supported scene modes shown above.</p></td>
</tr>
</tbody>
</table>

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_SCENEMODE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




