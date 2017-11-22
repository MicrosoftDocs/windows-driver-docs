---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EVCOMPENSATION
description: The EV Compensation property allows adjustment of exposure control by increments of exposure units or by the Zone system.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1109C533-89CA-4A23-BCF9-D44C28C0C6BF
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_EVCOMPENSATION


The EV Compensation property allows adjustment of exposure control by increments of exposure units or by the Zone system.

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
<td><p>Filter</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567563)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) contains a [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) structure and a [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561) structure.

The total property data size is **sizeof**(KSCAMERA\_EXTENDEDPROP\_HEADER) + **sizeof**(KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION). The **Size** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) is set to this total property data size.

The **Capability** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains a bitwise OR combination of one or more of the following compensation settings.

| EV compensation stepping                    | Description                                                             |
|---------------------------------------------|-------------------------------------------------------------------------|
| KSCAMERA\_EXTENDEDPROP\_EVCOMP\_SIXTHSTEP   | EV compensation changes in one sixth (1/6) step of the exposure value.  |
| KSCAMERA\_EXTENDEDPROP\_EVCOMP\_QUARTERSTEP | EV compensation changes in one fourth (1/4) step of the exposure value. |
| KSCAMERA\_EXTENDEDPROP\_EVCOMP\_THIRDSTEP   | EV compensation changes in one third (1/3) step of the exposure value.  |
| KSCAMERA\_EXTENDEDPROP\_EVCOMP\_HALFSTEP    | EV compensation changes in one half (1/2) step of the exposure value.   |
| KSCAMERA\_EXTENDEDPROP\_EVCOMP\_FULLSTEP    | EV compensation changes in one (1/1) step of the exposure value.        |

 

The **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) contains the current EV compensation stepping for the camera (one value).Drivers are recommended to advertise support for only for the lowest EV compensation step sizes.

This property control is asynchronous.

Remarks
-------

### <span id="Getting_the_property"></span><span id="getting_the_property"></span><span id="GETTING_THE_PROPERTY"></span>Getting the property

When responding to a KSPROPERTY\_TYPE\_GET request, the driver sets the members of the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) to the following.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Member</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Version</td>
<td>1</td>
</tr>
<tr class="even">
<td>PinId</td>
<td>KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF).</td>
</tr>
<tr class="odd">
<td>Size</td>
<td><p>sizeof(KSCAMERA_EXTENDEDPROP_HEADER) + sizeof(KSCAMERA_EXTENDEDPROP_EVCOMPENSATION)</p></td>
</tr>
<tr class="even">
<td>Result</td>
<td>0</td>
</tr>
<tr class="odd">
<td>Capability</td>
<td>Stepping flags supported by the driver.</td>
</tr>
<tr class="even">
<td>Flags</td>
<td>The current stepping value set.</td>
</tr>
</tbody>
</table>

 

The driver sets the current EV compensation stepping in **Flags**. The members of [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561) indicate the current step unit ranges and number of step used in for compensation

### <span id="Setting_the_property"></span><span id="setting_the_property"></span><span id="SETTING_THE_PROPERTY"></span>Setting the property

When the property is set, a KSPROPERTY\_TYPE\_SET request, the **Flags** member of [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563) will contain the EV compensation stepping to use. The new number of step units used for compensation are set in **Value** member of [**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561).

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
<td><p>Available starting with Windows 8.1.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn567563)

[**KSCAMERA\_EXTENDEDPROP\_EVCOMPENSATION**](https://msdn.microsoft.com/library/windows/hardware/dn567561)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_EVCOMPENSATION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





