---
title: WIA\_IPS\_LAMP\_AUTO\_OFF
description: The WIA\_IPS\_LAMP\_AUTO\_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.
ms.assetid: 82a3b5dc-0a70-4e2a-a863-6019b04cbbaf
keywords: ["WIA_IPS_LAMP_AUTO_OFF Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_LAMP_AUTO_OFF
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPS\_LAMP\_AUTO\_OFF


The WIA\_IPS\_LAMP\_AUTO\_OFF property contains the current configuration setting for automatically shutting off a scanner's lamp. The WIA minidriver creates and maintains this property.

Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_IPS\_LAMP\_AUTO\_OFF property enables the programmatic control of how long a lamp will be kept on when a scanner is not in use; this lamp could be a dedicated lamp (for a transparency adapter) or the main scanner lamp (for dedicated film scanners).

You should implement WIA\_IPS\_LAMP\_AUTO\_OFF only if the device supports an automatic lamp-off feature.

The valid values for WIA\_IPS\_LAMP\_AUTO\_OFF range from 0 through 4095 seconds.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_LAMP_AUTO_OFF%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




