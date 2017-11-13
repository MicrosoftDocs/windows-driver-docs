---
title: WIA\_IPS\_PAGE\_SIZE
description: The WIA\_IPS\_PAGE\_SIZE property contains the size of the page that is currently selected to be scanned.
MS-HAID:
- 'WIA\_PropTable\_f66008ea-cd93-4b34-a27c-b46128126ddd.xml'
- 'image.wia\_ips\_page\_size'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: dcfad67e-31d5-41b8-b471-532626f571af
keywords: ["WIA_IPS_PAGE_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PAGE_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_PAGE\_SIZE


The WIA\_IPS\_PAGE\_SIZE property contains the size of the page that is currently selected to be scanned.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

To select the dimensions of the page to scan, an application sets the WIA\_IPS\_PAGE\_SIZE property. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with WIA\_IPS\_PAGE\_SIZE.

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
<td><p>WIA_PAGE_A4</p></td>
<td><p>8267 × 11692 (PORTRAIT orientation).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PAGE_AUTO</p></td>
<td><p>Used to configure automatic page size detection.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PAGE_CUSTOM</p></td>
<td><p>Defined by the values of the [<strong>WIA_IPS_PAGE_HEIGHT</strong>](wia-ips-page-height.md) and [<strong>WIA_IPS_PAGE_WIDTH</strong>](wia-ips-page-width.md) properties.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PAGE_CUSTOM_BASE</p></td>
<td><p>Defined by the values of the WIA_IPS_PAGE_HEIGHT and WIA_IPS_PAGE_WIDTH properties. This value is used to define custom page sizes, instead of the single page that the WIA_PAGE_CUSTOM value enables.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PAGE_LETTER</p></td>
<td><p>8500 × 11000 (PORTRAIT orientation).</p></td>
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
<td><p>Version</p></td>
<td><p>Available in Windows Vista and later operating systems. For Windows XP, use the WIA_DPS_PAGE_SIZE property instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017)

[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md)

[**WIA\_IPS\_PAGE\_HEIGHT**](wia-ips-page-height.md)

[**WIA\_IPS\_PAGE\_WIDTH**](wia-ips-page-width.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PAGE_SIZE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





