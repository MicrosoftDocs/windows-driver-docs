---
title: WIA\_DPS\_PAGE\_SIZE
description: The WIA\_DPS\_PAGE\_SIZE property contains the size of the page that is currently selected to be scanned.
ms.assetid: 16e32b83-26b8-4283-a937-9fbbe77b42b8
keywords: ["WIA_DPS_PAGE_SIZE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_PAGE_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_PAGE\_SIZE


The WIA\_DPS\_PAGE\_SIZE property contains the size of the page that is currently selected to be scanned.

## <span id="ddk_wia_dps_page_size_si"></span><span id="DDK_WIA_DPS_PAGE_SIZE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

To select the dimensions of the page to scan, an application sets WIA\_DPS\_PAGE\_SIZE. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with [**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md).

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
<td><p>The page size is 8267 × 11692 (PORTRAIT orientation).</p></td>
</tr>
<tr class="even">
<td><p>WIA_PAGE_CUSTOM</p></td>
<td><p>The page size is defined by the values of the <a href="wia-dps-page-height.md" data-raw-source="[&lt;strong&gt;WIA_DPS_PAGE_HEIGHT&lt;/strong&gt;](wia-dps-page-height.md)"><strong>WIA_DPS_PAGE_HEIGHT</strong></a> and <a href="wia-dps-page-width.md" data-raw-source="[&lt;strong&gt;WIA_DPS_PAGE_WIDTH&lt;/strong&gt;](wia-dps-page-width.md)"><strong>WIA_DPS_PAGE_WIDTH</strong></a> properties.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_PAGE_LETTER</p></td>
<td><p>The page size is 8500 × 11000 (PORTRAIT orientation).</p></td>
</tr>
</tbody>
</table>

 

The value of the [**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md) property determines the orientation of the currently selected page. The WIA\_DPS\_PAGE\_WIDTH and WIA\_DPS\_PAGE\_HEIGHT properties report the page's dimensions, in thousandths of an inch (.001). These properties must have values that are equivalent to the [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md) and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties, which contain the page's dimensions, in pixels.

WIA\_PROP\_LIST-typed values should depend on valid settings of the WIA\_IPS\_ORIENTATION property. If a device cannot scan landscape-oriented documents with a WIA\_PAGE\_A4 setting, WIA\_PAGE\_A4 should not appear in the list of valid values for the WIA\_DPS\_PAGE\_SIZE property when WIA\_IPS\_ORIENTATION is set to LANSCAPE.

If an application sets WIA\_DPS\_PAGE\_SIZE to any value other than WIA\_PAGE\_CUSTOM, the minidriver should adjust the values of WIA\_DPS\_PAGE\_WIDTH and WIA\_DPS\_PAGE\_HEIGHT to the page's dimensions, in thousandths of an inch (.001). The minidriver should also adjust the values of WIA\_IPS\_XEXTENT and WIA\_IPS\_YEXTENT to the page's dimensions, in pixels.

If an extent setting (WIA\_IPS\_XEXTENT or WIA\_IPS\_YEXTENT) is changed to a value that does *not* match the current page-size setting, the minidriver should change the value of the WIA\_DPS\_PAGE\_SIZE property to WIA\_PAGE\_CUSTOM. The minidriver should also modify WIA\_DPS\_PAGE\_WIDTH or WIA\_DPS\_PAGE\_HEIGHT in accordance with the new extent setting.

If WIA\_IPS\_ORIENTATION is set to LANSCAPE, the extent settings will be "flipped." For example, if an application sets WIA\_DPS\_PAGE\_SIZE to WIA\_PAGE\_A4, the minidriver should set WIA\_DPS\_PAGE\_WIDTH to 11692 and WIA\_DPS\_PAGE\_HEIGHT to 8267. (The minidriver should also set WIA\_IPS\_XEXTENT and WIA\_IPS\_YEXTENT accordingly.) Note that if WIA\_DPS\_PAGE\_SIZE is set to WIA\_PAGE\_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.

The minidriver must ensure that the WIA\_IPS\_ORIENTATION property agrees with the current selection area. If an application changes the value of WIA\_IPS\_ORIENTATION to one that is invalid for the currently selected page size, the minidriver should change the value of WIA\_DPS\_PAGE\_SIZE to a page size that is supported by the new orientation value.

If an application sets the WIA\_DPS\_PAGE\_SIZE property to WIA\_PAGE\_CUSTOM, the current selection area is not affected. The WIA minidriver should obtain the current image layout, starting from the current settings of the [**WIA\_IPS\_XPOS**](wia-ips-xpos.md) and [**WIA\_IPS\_YPOS**](wia-ips-ypos.md) properties. If the page-size setting results in a selection area that is outside the scanner's bed, the minidriver must automatically adjust the values of the WIA\_IPS\_XPOS and WIA\_IPS\_YPOS properties to valid settings. If the WIA\_DPS\_PAGE\_SIZE and WIA\_IPS\_ORIENTATION properties are set at the same time and they are invalid when they are applied in combination, the minidriver should fail the application's settings by returning an error in the [**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017) method.

The following four code examples show the following WIA\_DPS\_PAGE\_SIZE scenarios:

1.  The driver reports the settings.

2.  An application sets the WIA\_DPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER.

3.  An application sets the [**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md) property to LANSCAPE.

4.  An application changes the [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md) property to a smaller value.

**Example 1: The minidriver reports the settings**

In the following code example, the minidriver sets a custom selection area before an application sets any WIA properties. In this case, the selection area represents the entire flatbed.

WIA_DPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_DPS_PAGE_WIDTH = 11500
WIA_DPS_PAGE_HEIGHT = 14000
WIA_IPS_ORIENTATION  = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1150
WIA_IPS_YEXTENT = 1400
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

**Example 2: An application sets the WIA\_DPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER**

WIA_DPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_DPS_PAGE_WIDTH = 8500
WIA_DPS_PAGE_HEIGHT = 11000
WIA_IPS_ORIENTATION  = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 850
WIA_IPS_YEXTENT = 1100
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

**Example 3: An application sets the WIA\_IPS\_ORIENTATION property to LANSCAPE**

The physical bed must be able to acquire a page that was originally in landscape orientation.

WIA_DPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_DPS_PAGE_HEIGHT = 11000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION  = LANSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1100
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

**Example 4: An application changes the WIA\_IPS\_XEXTENT property to a smaller value**

In the following code example, an application changes the WIA\_IPS\_XEXTENT property to 1000. The minidriver should assume that the new value for WIA\_IPS\_XEXTENT is no longer valid for the WIA\_DPS\_PAGE\_SIZE property and should thus change WIA\_DPS\_PAGE\_SIZE to WIA\_PAGE\_CUSTOM. The minidriver must also adjust [**WIA\_DPS\_PAGE\_WIDTH**](wia-dps-page-width.md).

WIA_DPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_DPS_PAGE_HEIGHT = 10000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION  = LANSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1000
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

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
<td><p>Available for Microsoft Windows XP. For Windows Vista and later, use the identical WIA_IPS_PAGE_SIZE property.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also

[**IWiaMiniDrv::drvValidateItemProperties**](https://msdn.microsoft.com/library/windows/hardware/ff545017)

[**WIA\_DPS\_PAGE\_HEIGHT**](wia-dps-page-height.md)

[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_DPS\_PAGE\_WIDTH**](wia-dps-page-width.md)

[**WIA\_IPS\_ORIENTATION**](wia-ips-orientation.md)

[**WIA\_IPS\_PAGE\_SIZE**](wia-ips-page-size.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)
