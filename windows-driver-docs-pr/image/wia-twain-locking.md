---
title: WIA-TWAIN Locking
description: WIA-TWAIN Locking
ms.assetid: bf2dc7f5-f3a0-4c51-86e1-854d0704074a
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA-TWAIN Locking





For a TWAIN driver and a WIA driver that use different locking mechanisms, when the WIA driver accesses the device, the TWAIN driver should not be able to simultaneously access the device. This can lead to such problems as corrupted images and failed transfers.

TWAIN hardware often comes with vendor-supplied utility or application software to do diagnostics, transfer data, and send faxes. This vendor-supplied software might access the STI driver directly instead of through the WIA service. This is not recommended and can introduce locking issues. For example, If vendor-supplied application software accesses the device and locks it directly, then no WIA application will be able to use that device until the application releases the lock. If the application is a tool that monitors the device and appears in the notification area (previously known as the System Tray), it is not permitted to release the lock until another vendor-specific application privately asks it to.

So, when you use this vendor-supplied software, make sure you adhere to reliable locking and unlocking techniques. This ensures that when the WIA service polls the device or transfers data, it does not interrupt another transfer (for example, through TWAIN), and that the WIA service is itself not similarly interrupted. Make sure that only one system gets a specified event. That is, if you push the button on a scanner, the WIA service will not initiate the registered WIA application at the same time that the vendor-supplied software initiates its own application.

For additional information, see [Locking and Unlocking Best Practices](locking-and-unlocking-best-practices.md).

 

 




