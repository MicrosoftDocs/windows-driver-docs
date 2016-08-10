---
title: Smart Card Driver Environment
description: Smart Card Driver Environment
ms.assetid: f1b369c6-84a0-4a0a-9e70-40dd3009c59e
keywords: ["smart card drivers WDK , environment"]
---

# Smart Card Driver Environment


## <span id="_ntovr_smart_card_driver_environment"></span><span id="_NTOVR_SMART_CARD_DRIVER_ENVIRONMENT"></span>


The following figure shows the standard environment for the smart card reader driver.

![diagram illustrating the standard environment for the smart card reader driver](images/memp1.png)

In addition, the figure shows the following components of the smart card environment:

-   Applications communicate with a smart card reader driver by means of the smart card resource manager. The reader driver resides in kernel space, and the smart card resource manager resides in user space.

-   The resource manager communicates with the reader driver by means of I/O controls that are dispatched using the [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=94613) system call. For information about how to use the [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=94613) system call, refer to the [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=94613) topic in the Microsoft Windows SDK.

    Likewise, smart card-aware applications can send instructions to a smart card reader driver by means of [DeviceIoControl](http://go.microsoft.com/fwlink/p/?linkid=94613), and the operating system will forward the indicated IOCTL to the reader driver. If the reader driver is a WDM driver, the operating system will forward the request by means of an I/O request packet (IRP).

-   Microsoft supplies one reader driver sample, *pscr.sys*, which is a driver for a PCMCIA smart card reader. The source code for this driver is available in the collection of WDK samples. For further information, see [PCMCIA Smart Card Driver](https://github.com/Microsoft/Windows-driver-samples/tree/master/smartcrd). Vendors of smart card reader devices must supply drivers that are designed to work with the system-supplied resource manager and smart card driver library.

-   Both native and vendor-supplied reader drivers must use the smart card driver library to perform many of their key operations, as explained in the section, [Smart Card Driver Library](smart-card-driver-library.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Smart%20Card%20Driver%20Environment%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




