---
title: CM_PROB_FAILED_ADD
description: CM_PROB_FAILED_ADD
ms.assetid: 3004f9fa-4afb-47a9-8aa1-95086eb4f38d
keywords: ["CM_PROB_FAILED_ADD"]
---

# CM_PROB_FAILED_ADD


## <a href="" id="ddk-cm-prob-failed-add-dg"></a>


A driver's attempt to add a device failed.

### Error Code

31

### Display Message (Windows 2000 and later versions of Windows)

"This device is not working properly because Windows cannot load the drivers required for this device. (Code 31)"

### Recommended Resolution (Windows 2000 and later versions of Windows)

Update the device driver.

Starting with Windows XP, this problem can only occur if the driver's [AddDevice routine](https://msdn.microsoft.com/library/windows/hardware/ff566398) fails.

For Windows 2000, this problem can occur in any of the following cases:

-   The service key is corrupted.

-   The driver's image could not be loaded from the disk.

-   The driver's [DriverEntry routine](https://msdn.microsoft.com/library/windows/hardware/ff566402) failed.

-   The driver could not unload because of a leaked reference.

-   The driver is a legacy driver that did not create device objects.

-   The driver's *AddDevice* routine failed.

To update a device driver, follow these steps:

1.  [Open Device Manager](using-device-manager.md).

2.  Right-click the icon that represents the device in the Device Manager window.

3.  On the menu that appears, click **Update Driver** to start the Hardware Update wizard.

 

 





