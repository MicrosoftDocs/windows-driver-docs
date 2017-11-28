---
title: WIA\_IPS\_FILM\_SCAN\_MODE
description: The WIA\_IPS\_FILM\_SCAN\_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.
ms.assetid: 3bbe362e-1868-4327-a862-8711f09969f7
keywords: ["WIA_IPS_FILM_SCAN_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_FILM_SCAN_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_FILM\_SCAN\_MODE


The WIA\_IPS\_FILM\_SCAN\_MODE property contains the current film scan configuration settings. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_IPS\_FILM\_SCAN\_MODE property

| Scan type                  | Definition                                         |
|----------------------------|----------------------------------------------------|
| WIA\_FILM\_COLOR\_SLIDE    | The scan will be a color scan.                     |
| WIA\_FILM\_COLOR\_NEGATIVE | The scan will be a color scan of a negative.       |
| WIA\_FILM\_BW\_NEGATIVE    | The scan will be black and white (grayscale) scan. |

 

This property is required for the root item in the WIA item tree of film scanners and transparency adapters.

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
<td><p>Available in Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_FILM_SCAN_MODE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




