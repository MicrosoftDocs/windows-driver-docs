---
Description: Digital Rights Management (DRM) systems often make use of device serial numbers to ensure that legitimate customers have access to digitized intellectual property.
title: Content Security Features in Usbccgp.sys
---

# Content Security Features in Usbccgp.sys


Digital Rights Management (DRM) systems often make use of device serial numbers to ensure that legitimate customers have access to digitized intellectual property. If a USB device has a CSM-1 content security interface, a client driver can query for its serial number by sending an [**IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER**](https://msdn.microsoft.com/library/windows/hardware/ff560557) request to the generic parent driver.

## Related topics
[USB Generic Parent Driver (Usbccgp.sys)](usb-common-class-generic-parent-driver.md)  
[Microsoft-provided USB drivers](system-supplied-usb-drivers.md)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Content%20Security%20Features%20in%20Usbccgp.sys%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


