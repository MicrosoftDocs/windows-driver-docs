---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY
description: The KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY property ID defined in the KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY enumeration is used to configure the focus priority.
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
ms.date: 09/10/2018
ms.localizationpriority: medium
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY


The **KSPROPERTY\_CAMERACONTROL\_EXTENDED\_FOCUSPRIORITY** property ID defined in the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/dn917962) enumeration is used to configure the focus priority. When focus priority is set, focusing will take priority over the picture taken to ensure that the picture taken is always in focus. Otherwise, the picture will be taken immediately regardless of whether the picture is in focus . The behavior in handling a failed focus and whether timeout is required is internal to the driver and up to the OEM.

## Usage summary table


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

For the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_header), the following flags are defined as values. In a get call, the camera driver returns its current focus priority configuration using one of these flags. In a set call, the camera driver sets the new focus priority configuration using one of these flags.

```cpp
#define KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_OFF     0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_FOCUSPRIORITY_ON      0x0000000000000001
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
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>)+sizeof(<a href="https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value" data-raw-source="[&lt;strong&gt;KSCAMERA_EXTENDEDPROP_VALUE&lt;/strong&gt;](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ksmedia/ns-ksmedia-tagkscamera_extendedprop_value)"><strong>KSCAMERA_EXTENDEDPROP_VALUE</strong></a>),</p></td>
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

 

## Requirements

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
