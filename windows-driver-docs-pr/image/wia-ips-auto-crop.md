---
title: WIA\_IPS\_AUTO\_CROP
description: The WIA\_IPS\_AUTO\_CROP property is used to enable automatic detection and cropping by the device of the scan region. The WIA minidriver creates and maintains this property.
ms.assetid: 5D7D2911-1535-4E67-9EBF-2B59D87F4F1B
keywords: ["WIA_IPS_AUTO_CROP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_AUTO_CROP
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_AUTO\_CROP


The **WIA\_IPS\_AUTO\_CROP** property is used to enable automatic detection and cropping by the device of the scan region. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_AUTO\_CROP** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_AUTO_CROP_DISABLED</p></td>
<td><p>Auto-crop is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_AUTO_CROP_SINGLE</p></td>
<td><p>Auto-crop is enabled. One scan region is detected and cropped on each document page.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_AUTO_CROP_MULTI</p></td>
<td><p>Auto-crop is enabled. One or multiple scan regions are detected and cropped on each document page. Each cropped scan region is transferred to the WIA application client as one single-page file or as a new page in a multi-page file.</p></td>
</tr>
</tbody>
</table>

 

This property is valid and optional for the Feeder (WIA\_CATEGORY\_FEEDER) item, where it can be implemented with or without the WIA\_PAGE\_AUTO value for the [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md) property. This property is also valid (and optional) for the Flatbed (WIA\_CATEGORY\_FLATBED) and Film (WIA\_CATEGORY\_FILM) items, but only if segmentation is not supported by the WIA mini-driver for the WIA\_CATEGORY\_FLATBED and WIA\_CATEGORY\_FILM input sources. If WIA\_IPS\_SEGEMENTATION is supported then WIA\_IPS\_AUTO\_CROP is invalid and cannot be supported at the same time.

When the property is supported, WIA\_AUTO\_CROP\_DISABLED and at least one of the other two possible values (WIA\_AUTO\_CROP\_SINGLE and/or WIA\_AUTO\_CROP\_MULTI) are required, with WIA\_AUTO\_CROP\_DISABLED being the required default.

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
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





