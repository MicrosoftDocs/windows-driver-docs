---
title: Page Size and Orientation Code Examples
description: Page Size and Orientation Code Examples
ms.assetid: 28425df2-131b-4fbc-ae44-043be2fb4813
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Page Size and Orientation Code Examples

These code examples show the following WIA\_IPS\_PAGE\_SIZE scenarios:

1.  The minidriver reports the settings.

2.  An application sets the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER.

3.  An application sets the [**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625) property to LANSCAPE.

4.  An application changes the [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) property to a smaller value.

### Example 1: The minidriver reports the settings

In the following code example, the minidriver sets a custom selection area before an application sets any WIA properties. In this case, the selection area represents the entire flatbed.

WIA_IPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_IPS_PAGE_WIDTH = 11500
WIA_IPS_PAGE_HEIGHT = 14000
WIA_IPS_ORIENTATION = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1150
WIA_IPS_YEXTENT = 1400
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

### Example 2: An application sets the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER

In the following code example, the minidriver changes the page size from custom values to a standard letter size of 8500 × 11000 pixels.

WIA_IPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_PAGE_HEIGHT = 11000
WIA_IPS_ORIENTATION  = PORTRAIT
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 850
WIA_IPS_YEXTENT = 1100
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

### Example 3: An application sets the WIA\_IPS\_ORIENTATION property to LANSCAPE

In the following code example, the minidriver changes the page orientation from portrait to landscape. The physical bed must be able to acquire a page that was originally in landscape orientation.

WIA_IPS_PAGE_SIZE = WIA_PAGE_LETTER
WIA_IPS_PAGE_HEIGHT = 11000
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1100
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100

### Example 4: An application changes the WIA\_IPS\_XEXTENT property to a smaller value

In the following code example, an application changes the [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) property to 1000. The minidriver should assume that the new value that is contained in WIA\_IPS\_XEXTENT is no longer valid for the WIA\_IPS\_PAGE\_SIZE property and should thus change WIA\_IPS\_PAGE\_SIZE to WIA\_PAGE\_CUSTOM. The minidriver must also adjust [**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636).

WIA_IPS_PAGE_SIZE = WIA_PAGE_CUSTOM
WIA_IPS_PAGE_HEIGHT = 10000
WIA_IPS_PAGE_WIDTH = 8500
WIA_IPS_ORIENTATION = LANSCAPE
WIA_IPS_XPOS = 0
WIA_IPS_YPOS = 0
WIA_IPS_XEXTENT = 1000
WIA_IPS_YEXTENT = 850
WIA_IPS_XRES = 100
WIA_IPS_YRES = 100
