---
title: Page Orientation
description: Page Orientation
ms.assetid: fb28863a-920a-4b26-a652-fb255622824f
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Page Orientation


The WIA minidriver must ensure that the WIA\_IPS\_ORIENTATION property agrees with the current selection area. If an application changes the value of WIA\_IPS\_ORIENTATION to one that is invalid for the currently selected page size, the minidriver should change the value of WIA\_IPS\_PAGE\_SIZE to a page size that the new orientation value supports.

Note that if [**WIA\_IPS\_ORIENTATION**](https://msdn.microsoft.com/library/windows/hardware/ff552625) is set to LANSCAPE, the extent settings will be "flipped." For example, if an application sets WIA\_IPS\_PAGE\_SIZE to WIA\_PAGE\_A4, the minidriver should set [**WIA\_IPS\_PAGE\_WIDTH**](https://msdn.microsoft.com/library/windows/hardware/ff552636) to 11692 and [**WIA\_IPS\_PAGE\_HEIGHT**](https://msdn.microsoft.com/library/windows/hardware/ff552632) to 8267. (The minidriver should also set [**WIA\_IPS\_XEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552661) and [**WIA\_IPS\_YEXTENT**](https://msdn.microsoft.com/library/windows/hardware/ff552669) accordingly.) Note that if WIA\_IPS\_PAGE\_SIZE is set to WIA\_PAGE\_CUSTOM, the orientation setting is not used to determine the extent dimensions of the page to be scanned.

 

 




