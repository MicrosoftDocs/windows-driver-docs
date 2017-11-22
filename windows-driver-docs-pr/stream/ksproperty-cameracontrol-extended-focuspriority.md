---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY property ID defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to configure the focus priority.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7E3558A1-0D0D-4470-B9C9-61EA359E92C5
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY** property ID defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used to configure the focus priority. When focus priority is set, focusing will take priority over the picture taken to ensure that the picture taken is always in focus. Otherwise, the picture will be taken immediately regardless of whether the picture is in focus . The behavior in handling a failed focus and whether timeout is required is internal to the driver and up to the OEM.

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

 

To configure the focus priority, the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY** property ID must be used. When focus priority is set, focusing will take priority over picture taken to ensure that the picture taken is always in focus. If focus priority is not set, the picture will be taken immediately regardless of whether the picture was in focus. The behavior in handling a failed focus failed and timeouts are determined by the OEM and is internal to the driver.

For the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136), the following flags are defined as values. In a get call, the camera driver returns its current focus priority configuration using one of these flags. In a set call, the camera driver sets the new focus priority configuration using one of these flags.

``` syntax
#define KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_OFF 0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_ON 0x0000000000000001
```

**Note**  
This is a synchronous control and there are no capabilities defined for this control.

 

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the focus priority control.

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
<td><p>This must be 1,</p></td>
</tr>
<tr class="even">
<td><p>PinId</p></td>
<td><p>This must be KSCAMERA_EXTENDEDPROP_FILTERSCOPE (0xFFFFFFFF),</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof([<strong>KSCAMERA_EXTENDEDPROP_VALUE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567565)),</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This indicates the error results,</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be 0,</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_Xxx flags defined above.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_FOCUSPRIORITY%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




