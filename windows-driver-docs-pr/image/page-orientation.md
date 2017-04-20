---
title: Page Orientation
author: windows-driver-content
description: Page Orientation
ms.assetid: fb28863a-920a-4b26-a652-fb255622824f
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Page Orientation


The WIA minidriver must ensure that the WIA\_IPS\_ORIENTATION property agrees with the current selection area. If an application changes the value of WIA\_IPS\_ORIENTATION to one that is invalid for the currently selected page size, the minidriver should change the value of WIA\_IPS\_PAGE\_SIZE to a page size that the new orientation value supports.

Note that if [**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625) is set to LANSCAPE, the extent settings will be "flipped." For example, if an application sets WIA\_IPS\_PAGE\_SIZE to WIA\_PAGE\_A4, the minidriver should set [**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636) to 11692 and [**WIA\_IPS\_PAGE\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552632) to 8267. (The minidriver should also set [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) and [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669) accordingly.) Note that if WIA\_IPS\_PAGE\_SIZE is set to WIA\_PAGE\_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Page%20Orientation%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


