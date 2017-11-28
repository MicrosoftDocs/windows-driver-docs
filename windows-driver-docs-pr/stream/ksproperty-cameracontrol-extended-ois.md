---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OIS
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OIS is a property ID that is used to control optical image stabilization (OIS) on the driver.
ms.assetid: CF4F1283-1517-4F93-8554-FBD4B068A655
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_OIS Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_OIS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OIS


**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_OIS** is a property ID that is used to control optical image stabilization (OIS) on the driver.

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
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

 

The following flags can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field to control optical image stabilization. The default should be AUTO if AUTO is supported, or ON otherwise.

``` syntax
#define KSCAMERA_EXTENDEDPROP_OIS_OFF    0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_OIS_ON    0x0000000000000001
#define KSCAMERA_EXTENDEDPROP_OIS_AUTO  0x0000000000000002 
```

If the driver supports this control, it must support OIS\_ON and OIS\_OFF.

If the driver does not support optical image stabilization, the driver should not implement this control.

The SET call of this control has no effect when the video or photo pin is in KSSTATE\_RUN state. The driver shall reject the SET call received if either video or photo pin is in running state and returns STATUS\_INVALID\_DEVICE\_STATE. In a GET call, driver should return the current settings in Flags field.

The following table describes the flag capabilities.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_OIS_OFF</p></td>
<td><p>This is a mandatory capability. When specified, the optical image stabilization is disabled in the driver.</p></td>
</tr>
<tr class="even">
<td><p>KSCAMERA_EXTENDEDPROP_OIS_ON</p></td>
<td><p>This is a mandatory capability. When specified, the optical image stabilization is enabled in the driver. This flag is mutually exclusive with the OIS_AUTO and OIS_OFF flags.</p></td>
</tr>
<tr class="odd">
<td><p>KSCAMERA_EXTENDEDPROP_OIS_AUTO</p></td>
<td><p>This capability is optional. When specified, the driver that supports such capability will determine whether optical image stabilization should be turned on or off. This flag is mutually exclusive with the OIS_ON and OIS_OFF flags.</p></td>
</tr>
</tbody>
</table>

 

The table below contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the control.

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
<td><p>This must be KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_VALUE).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be a bitwise OR of the supported KSCAMERA_EXTENDEDPROP_OIS_* flags defined above.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_OIS_* flags defined above.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_OIS%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




