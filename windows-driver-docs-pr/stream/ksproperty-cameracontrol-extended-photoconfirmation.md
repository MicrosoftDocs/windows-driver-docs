---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION property ID that is defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to set and get the photo confirmation settings in the driver.
ms.assetid: 3EF6FF15-6805-4D91-B053-1BF6C5D5BEF2
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION
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

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION** property ID that is defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used to set and get the photo confirmation settings in the driver.

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

 

For the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136), the following flag values are used to turn photo confirmation on or off. By default, the driver should have **KSPROPERTY\_PHOTOCONFIRMATION\_ON** set. The flag values are defined as follows.

``` syntax
#define KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_OFF    0x0000000000000000 
#define KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_ON    0x0000000000000001
```

If the photo confirmation is set to **KSCAMERA\_EXTENDEDPROP\_PHOTOCONFIRMATION\_OFF**, the driver preview pin must not produce a photo frame or produce the [**KSCAMERA\_METADATA\_PHOTOCONFIRMATION**](https://msdn.microsoft.com/library/windows/hardware/dn925187) structure that contains photo confirmation metadata. If the photo confirmation is set to **KSCAMERA\_EXTENDEDPROP\_PHOTOCONFIRMATION\_ON**, the driver preview pin must produce a photo frame and produce the **KSCAMERA\_METADATA\_PHOTOCONFIRMATION** structure that contains photo confirmation metadata.

The table below contains the descriptions and requirements for the **KSCAMERA\_EXTENDEDPROP\_HEADER** structure fields when using the **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PHOTOCONFIRMATION** property.

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
<td><p>This must be <strong>KSCAMERA_EXTENDEDPROP_FILTERSCOPE</strong> (0xFFFFFFFF),</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof([<strong>KSCAMERA_EXTENDEDPROP_VALUE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567565)).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>This contains the error results of the last SET operation. If no SET operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>This must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any of the <strong>KSCAMERA_EXTENDEDPROP_PHOTOCONFIRMATION_Xxx</strong> flags defined above.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_PHOTOCONFIRMATION%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




