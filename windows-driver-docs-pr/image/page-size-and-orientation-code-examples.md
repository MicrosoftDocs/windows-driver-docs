---
title: Page Size and Orientation Code Examples
author: windows-driver-content
description: Page Size and Orientation Code Examples
ms.assetid: 28425df2-131b-4fbc-ae44-043be2fb4813
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Page Size and Orientation Code Examples


These code examples show the following WIA\_IPS\_PAGE\_SIZE scenarios:

1.  The minidriver reports the settings.

2.  An application sets the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER.

3.  An application sets the [**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625) property to LANSCAPE.

4.  An application changes the [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) property to a smaller value.

### Example 1: The minidriver reports the settings

In the following code example, the minidriver sets a custom selection area before an application sets any WIA properties. In this case, the selection area represents the entire flatbed.

```
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
```

### <a href="" id="example-2--an-application-sets-the-wia-ips-page-size-property-to-wia-p"></a>Example 2: An application sets the WIA\_IPS\_PAGE\_SIZE property to WIA\_PAGE\_LETTER

In the following code example, the minidriver changes the page size from custom values to a standard letter size of 8500 × 11000 pixels.

```
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
```

### <a href="" id="example-3--an-application-sets-the-wia-ips-orientation--property-to-la"></a>Example 3: An application sets the WIA\_IPS\_ORIENTATION property to LANSCAPE

In the following code example, the minidriver changes the page orientation from portrait to landscape. The physical bed must be able to acquire a page that was originally in landscape orientation.

```
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
```

### <a href="" id="example-4--an-application-changes-the-wia-ips-xextent-property-to-a-sm"></a>Example 4: An application changes the WIA\_IPS\_XEXTENT property to a smaller value

In the following code example, an application changes the [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) property to 1000. The minidriver should assume that the new value that is contained in WIA\_IPS\_XEXTENT is no longer valid for the WIA\_IPS\_PAGE\_SIZE property and should thus change WIA\_IPS\_PAGE\_SIZE to WIA\_PAGE\_CUSTOM. The minidriver must also adjust [**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636).

```
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
```

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Page%20Size%20and%20Orientation%20Code%20Examples%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


