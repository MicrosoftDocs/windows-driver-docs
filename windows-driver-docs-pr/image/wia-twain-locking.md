---
title: WIA-TWAIN Locking
author: windows-driver-content
description: WIA-TWAIN Locking
ms.assetid: bf2dc7f5-f3a0-4c51-86e1-854d0704074a
---

# WIA-TWAIN Locking


## <a href="" id="ddk-wia-twain-locking-si"></a>


For a TWAIN driver and a WIA driver that use different locking mechanisms, when the WIA driver accesses the device, the TWAIN driver should not be able to simultaneously access the device. This can lead to such problems as corrupted images and failed transfers.

TWAIN hardware often comes with vendor-supplied utility or application software to do diagnostics, transfer data, and send faxes. This vendor-supplied software might access the STI driver directly instead of through the WIA service. This is not recommended and can introduce locking issues. For example, If vendor-supplied application software accesses the device and locks it directly, then no WIA application will be able to use that device until the application releases the lock. If the application is a tool that monitors the device and appears in the notification area (previously known as the System Tray), it is not permitted to release the lock until another vendor-specific application privately asks it to.

So, when you use this vendor-supplied software, make sure you adhere to reliable locking and unlocking techniques. This ensures that when the WIA service polls the device or transfers data, it does not interrupt another transfer (for example, through TWAIN), and that the WIA service is itself not similarly interrupted. Make sure that only one system gets a specified event. That is, if you push the button on a scanner, the WIA service will not initiate the registered WIA application at the same time that the vendor-supplied software initiates its own application.

For additional information, see [Locking and Unlocking Best Practices](locking-and-unlocking-best-practices.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA-TWAIN%20Locking%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


