---
title: Page Size and Orientation
author: windows-driver-content
description: Page Size and Orientation
ms.assetid: f744a00c-8614-4488-9a29-d193a0c4268f
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Page%20Size%20and%20Orientation%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


