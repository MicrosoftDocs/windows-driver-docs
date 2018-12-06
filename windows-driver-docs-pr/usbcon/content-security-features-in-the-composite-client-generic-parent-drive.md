---
Description: Digital Rights Management (DRM) systems often make use of device serial numbers to ensure that legitimate customers have access to digitized intellectual property.
title: Content Security Features in Usbccgp.sys
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Content Security Features in Usbccgp.sys


Digital Rights Management (DRM) systems often make use of device serial numbers to ensure that legitimate customers have access to digitized intellectual property. If a USB device has a CSM-1 content security interface, a client driver can query for its serial number by sending an [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff560557) request to the generic parent driver.

## Related topics
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  



