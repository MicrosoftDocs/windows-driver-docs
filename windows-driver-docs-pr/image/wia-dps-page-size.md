---
title: WIA_DPS_PAGE_SIZE
description: The WIA_DPS_PAGE_SIZE property contains the size of the page that is currently selected to be scanned.
keywords: ["WIA_DPS_PAGE_SIZE Imaging Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- WIA_DPS_PAGE_SIZE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 09/30/2021
---

# WIA_DPS_PAGE_SIZE

The WIA_DPS_PAGE_SIZE property contains the size of the page that is currently selected to be scanned.

Property Type: VT_I4

Valid Values: WIA_PROP_LIST

Access Rights: Read/write

## Remarks

To select the dimensions of the page to scan, an application sets WIA_DPS_PAGE_SIZE. The WIA minidriver creates and maintains this property.

The following table describes the constants that are valid with [**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md).

| Value | Definition |
|--|--|
| WIA_PAGE_A4 | The page size is 8267 × 11692 (PORTRAIT orientation). |
| WIA_PAGE_CUSTOM | The page size is defined by the values of the [**WIA_DPS_PAGE_HEIGHT**](wia-dps-page-height.md) and [**WIA_DPS_PAGE_WIDTH**](wia-dps-page-width.md) properties. |
| WIA_PAGE_LETTER | The page size is 8500 × 11000 (PORTRAIT orientation). |

The value of the [**WIA_IPS_ORIENTATION**](wia-ips-orientation.md) property determines the orientation of the currently selected page. The WIA_DPS_PAGE_WIDTH and WIA_DPS_PAGE_HEIGHT properties report the page's dimensions, in thousandths of an inch (.001). These properties must have values that are equivalent to the [**WIA_IPS_XEXTENT**](wia-ips-xextent.md) and [**WIA_IPS_YEXTENT**](wia-ips-yextent.md) properties, which contain the page's dimensions, in pixels.

WIA_PROP_LIST-typed values should depend on valid settings of the WIA_IPS_ORIENTATION property. If a device cannot scan landscape-oriented documents with a WIA_PAGE_A4 setting, WIA_PAGE_A4 should not appear in the list of valid values for the WIA_DPS_PAGE_SIZE property when WIA_IPS_ORIENTATION is set to LANDSCAPE.

If an application sets WIA_DPS_PAGE_SIZE to any value other than WIA_PAGE_CUSTOM, the minidriver should adjust the values of WIA_DPS_PAGE_WIDTH and WIA_DPS_PAGE_HEIGHT to the page's dimensions, in thousandths of an inch (.001). The minidriver should also adjust the values of WIA_IPS_XEXTENT and WIA_IPS_YEXTENT to the page's dimensions, in pixels.

If an extent setting (WIA_IPS_XEXTENT or WIA_IPS_YEXTENT) is changed to a value that does *not* match the current page-size setting, the minidriver should change the value of the WIA_DPS_PAGE_SIZE property to WIA_PAGE_CUSTOM. The minidriver should also modify WIA_DPS_PAGE_WIDTH or WIA_DPS_PAGE_HEIGHT in accordance with the new extent setting.

If WIA_IPS_ORIENTATION is set to LANDSCAPE, the extent settings will be "flipped." For example, if an application sets WIA_DPS_PAGE_SIZE to WIA_PAGE_A4, the minidriver should set WIA_DPS_PAGE_WIDTH to 11692 and WIA_DPS_PAGE_HEIGHT to 8267. (The minidriver should also set WIA_IPS_XEXTENT and WIA_IPS_YEXTENT accordingly.) Note that if WIA_DPS_PAGE_SIZE is set to WIA_PAGE_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.

The minidriver must ensure that the WIA_IPS_ORIENTATION property agrees with the current selection area. If an application changes the value of WIA_IPS_ORIENTATION to one that is invalid for the currently selected page size, the minidriver should change the value of WIA_DPS_PAGE_SIZE to a page size that is supported by the new orientation value.

If an application sets the WIA_DPS_PAGE_SIZE property to WIA_PAGE_CUSTOM, the current selection area is not affected. The WIA minidriver should obtain the current image layout, starting from the current settings of the [**WIA_IPS_XPOS**](wia-ips-xpos.md) and [**WIA_IPS_YPOS**](wia-ips-ypos.md) properties. If the page-size setting results in a selection area that is outside the scanner's bed, the minidriver must automatically adjust the values of the WIA_IPS_XPOS and WIA_IPS_YPOS properties to valid settings. If the WIA_DPS_PAGE_SIZE and WIA_IPS_ORIENTATION properties are set at the same time and they are invalid when they are applied in combination, the minidriver should fail the application's settings by returning an error in the [**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties) method.

The following four code examples show the following WIA_DPS_PAGE_SIZE scenarios:

1. The driver reports the settings.

1. An application sets the WIA_DPS_PAGE_SIZE property to WIA_PAGE_LETTER.

1. An application sets the [**WIA_IPS_ORIENTATION**](wia-ips-orientation.md) property to LANDSCAPE.

1. An application changes the [**WIA_IPS_XEXTENT**](wia-ips-xextent.md) property to a smaller value.

### Example 1: The minidriver reports the settings

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

### Example 2: An application sets the WIA_DPS_PAGE_SIZE property to WIA_PAGE_LETTER

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

### Example 3: An application sets the WIA_IPS_ORIENTATION property to LANDSCAPE

The physical bed must be able to acquire a page that was originally in landscape orientation.

WIA_DPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_DPS_PAGE_HEIGHT = 11000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION  = LANDSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1100
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

### Example 4: An application changes the WIA_IPS_XEXTENT property to a smaller value

In the following code example, an application changes the WIA_IPS_XEXTENT property to 1000. The minidriver should assume that the new value for WIA_IPS_XEXTENT is no longer valid for the WIA_DPS_PAGE_SIZE property and should thus change WIA_DPS_PAGE_SIZE to WIA_PAGE_CUSTOM. The minidriver must also adjust [**WIA_DPS_PAGE_WIDTH**](wia-dps-page-width.md).

WIA_DPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_DPS_PAGE_HEIGHT = 10000
WIA_DPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION  = LANDSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1000
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

## Requirements

**Version:** Obsolete, use the WIA_IPS_PAGE_SIZE property instead.

**Header:** wiadef.h (include Wiadef.h)

## See also

[**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties)

[**WIA_DPS_PAGE_HEIGHT**](wia-dps-page-height.md)

[**WIA_DPS_PAGE_SIZE**](wia-dps-page-size.md)

[**WIA_DPS_PAGE_WIDTH**](wia-dps-page-width.md)

[**WIA_IPS_ORIENTATION**](wia-ips-orientation.md)

[**WIA_IPS_PAGE_SIZE**](wia-ips-page-size.md)

[**WIA_IPS_XEXTENT**](wia-ips-xextent.md)

[**WIA_IPS_XPOS**](wia-ips-xpos.md)

[**WIA_IPS_YEXTENT**](wia-ips-yextent.md)

[**WIA_IPS_YPOS**](wia-ips-ypos.md)
