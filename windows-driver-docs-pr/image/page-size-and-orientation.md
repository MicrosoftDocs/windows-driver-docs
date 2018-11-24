---
title: Page Size and Orientation
description: Page Size and Orientation
ms.assetid: f744a00c-8614-4488-9a29-d193a0c4268f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Page Size and Orientation


Scanner settings for page size and orientation are interrelated. Both determine the size of a page that will be scanned.

For example, the page size and extent values used by WIA\_PROP\_LIST depend on valid settings of the WIA\_IPS\_ORIENTATION property. Therefore, if a device cannot scan landscape-oriented documents with a WIA\_PAGE\_A4 setting, WIA\_PAGE\_A4 should not appear in the list of valid values for the WIA\_IPS\_PAGE\_SIZE property when WIA\_IPS\_ORIENTATION is set to LANSCAPE.

The value of the [**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625) property determines the orientation of the currently selected page. The [**WIA\_IPS\_PAGE\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552632) and [**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636) properties report the page's dimensions, in thousandths of an inch (.001). These height and width properties must contain values that are equivalent to the values in [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) and [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669), which provide the page's dimensions in pixels.

For more information about working with page size and orientation, see the following topics:

[Supported Scanner Paper Sizes](supported-scanner-paper-sizes.md)

[Custom and Auto Page Sizes](custom-and-auto-page-sizes.md)

[Page Orientation](page-orientation.md)

[Scanner Page Size and Orientation Code Examples](page-size-and-orientation-code-examples.md)

 

 




