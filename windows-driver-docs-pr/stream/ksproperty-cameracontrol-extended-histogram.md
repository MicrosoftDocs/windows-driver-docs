---
title: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM
description: KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM is a property ID that will be used to control the histogram metadata produced by the driver. This is a pin level control for the preview pin only.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 638AA1AA-F8E5-4FD7-9283-CF1F23266474
keywords: ["KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM
api_location:
- Ksmedia.h
api_type:
- HeaderDef
---

# KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM


**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_HISTOGRAM** is a property ID that will be used to control the histogram metadata produced by the driver. This is a pin level control for the preview pin only.

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
<td><p>Pin</p></td>
<td><p>Synchronous</p></td>
</tr>
</tbody>
</table>

 

The following flags can be placed in the **KSCAMERA\_EXTENDEDPROP\_HEADER.Flags** field to control the histogram metadata in driver. The default is **HISTOGRAM\_OFF**.

``` syntax
#define KSCAMERA_EXTENDEDPROP_HISTOGRAM_OFF      0x0000000000000000
#define KSCAMERA_EXTENDEDPROP_HISTOGRAM_ON       0x0000000000000001
```

This control must be used before the [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](ksproperty-cameracontrol-extended-metadata.md) control to ensure the proper sized metadata buffer is allocated.

If set to **HISTOGRAM\_OFF**, the driver shall not deliver the histogram metadata on the preview pin. The driver should not include the histogram metadata size in its metadata buffer size requirement.

If set to **HISTOGRAM\_ON**, the driver shall deliver the histogram metadata on the preview pin. The driver must include the histogram metadata size in its metadata buffer size requirement.

If the driver does not have the capability to produce histogram metadata, the driver should not implement this control. If the driver supports this control, it must also support [**KSPROPERTY\_CAMERACONTROL\_EXTENDED\_METADATA**](ksproperty-cameracontrol-extended-metadata.md) control.

The **SET** call of this control has no effect when the preview pin is in any state higher than the KSSTATE\_STOP state. The driver shall reject the **SET** call received if preview is not in the stop state and returns **STATUS\_INVALID\_DEVICE\_STATE**. In a **GET** call, driver should return the current settings in **Flags** field.

The following table contains the descriptions and requirements for the [**KSCAMERA\_EXTENDEDPROP\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/dn925136) structure fields when using the control.

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
<td><p>Must be the Pin ID associated with the preview pin.</p></td>
</tr>
<tr class="odd">
<td><p>Size</p></td>
<td><p>This must be sizeof(<strong>KSCAMERA_EXTENDEDPROP_HEADER</strong>) + sizeof([<strong>KSCAMERA_EXTENDEDPROP_VALUE</strong>](https://msdn.microsoft.com/library/windows/hardware/dn567565)).</p></td>
</tr>
<tr class="even">
<td><p>Result</p></td>
<td><p>Indicates the error results of the last <strong>SET</strong> operation. If no <strong>SET</strong> operation has taken place, this must be 0.</p></td>
</tr>
<tr class="odd">
<td><p>Capability</p></td>
<td><p>Must be 0.</p></td>
</tr>
<tr class="even">
<td><p>Flags</p></td>
<td><p>This is a read/write field. This can be any one of the <strong>KSCAMERA_EXTENDEDPROP_HISTOGRAM_*</strong> flags defined above.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_CAMERACONTROL_EXTENDED_HISTOGRAM%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




