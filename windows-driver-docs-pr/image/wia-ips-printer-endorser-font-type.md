---
title: WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE
description: The WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE property configures the font type that is used by the printer/endorser device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: DBA20346-36F8-4D9A-A9F2-F97F8955CDF8
keywords: ["WIA_IPS_PRINTER_ENDORSER_FONT_TYPE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PRINTER_ENDORSER_FONT_TYPE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE


The **WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE** property configures the font type that is used by the printer/endorser device. This property is initialized and maintained by the WIA mini-driver. This feature is available with Windows 8 and later versions of Windows.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read-Write

Remarks
-------

The accepted values for the **WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE** property are shown in the following table.

| Value                                        | Description                       |
|----------------------------------------------|-----------------------------------|
| WIA\_PRINT\_FONT\_NORMAL                     | Normal font.                      |
| WIA\_PRINT\_FONT\_BOLD                       | Bold font.                        |
| WIA\_PRINT\_FONT\_EXTRA\_BOLD                | Extra bold font.                  |
| WIA\_PRINT\_FONT\_ITALIC\_BOLD               | Italic, bold font.                |
| WIA\_PRINT\_FONT\_ITALIC\_EXTRA\_BOLD        | Italic, extra bold font.          |
| WIA\_PRINT\_FONT\_ITALIC                     | Italic font.                      |
| WIA\_PRINT\_FONT\_SMALL                      | Small font.                       |
| WIA\_PRINT\_FONT\_SMALL\_BOLD                | Small bold font.                  |
| WIA\_PRINT\_FONT\_SMALL\_EXTRA\_BOLD         | Small extra bold font.            |
| WIA\_PRINT\_FONT\_SMALL\_ITALIC\_BOLD        | Small italic and bold font.       |
| WIA\_PRINT\_FONT\_SMALL\_ITALIC\_EXTRA\_BOLD | Small italic and extra bold font. |
| WIA\_PRINT\_FONT\_SMALL\_ITALIC              | Small italic font.                |
| WIA\_PRINT\_FONT\_LARGE                      | Large font.                       |
| WIA\_PRINT\_FONT\_LARGE\_BOLD                | Large bold font.                  |
| WIA\_PRINT\_FONT\_LARGE\_EXTRA\_BOLD         | Large extra bold font.            |
| WIA\_PRINT\_FONT\_LARGE\_ITALIC\_BOLD        | Large italic and bold font.       |
| WIA\_PRINT\_FONT\_LARGE\_ITALIC\_EXTRA\_BOLD | Large italic and extra bold font. |
| WIA\_PRINT\_FONT\_LARGE\_ITALIC              | Large italic font.                |

 

The **WIA\_IPS\_PRINTER\_ENDORSER\_FONT\_TYPE** property is optional for the Imprinter/Endorser items. When this is not supported, the printer/endorser device does not support font configuration.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PRINTER_ENDORSER_FONT_TYPE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




