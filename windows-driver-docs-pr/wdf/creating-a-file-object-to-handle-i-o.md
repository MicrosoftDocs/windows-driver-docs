---
title: Creating a File Object to Handle I/O
description: Creating a File Object to Handle I/O
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 3cd826fc-5c67-4ab4-800a-b5aa4bd5244f
keywords: ["file object to handle I/O WDK UMDF", "file object to handle I/O WDK UMDF creating", "I/O requests WDK UMDF file object", "User Mode Driver Framework WDK file object to handle I/O", "UMDF WDK file object to handle I/O", "user mode drivers WDK UMDF file object to handle I/O"]
---

# Creating a File Object to Handle I/O


When an application opens a file handle, the I/O manager creates a file object. The framework in turn creates a framework file object to represent the I/O manager's file object.

Unless the driver sets the **UmdfFileObjectPolicy** directive to **AllowNullAndUnknownFileObjects**, UMDF requires each I/O request to be associated with a file object. For more information about this directive, see [Specifying WDF Directives in INF Files](specifying-wdf-directives-in-inf-files.md).

If your UMDF driver sends I/O that is independent of the application to the next driver in the stack (for example, during device initialization or to get notification of device events), the driver must create its own file object to associate with the request.

The following sections describe the differences between driver-created file objects and application-created file objects, and how the driver creates and uses a file object.

-   [Driver-Created Versus Application-Created File Objects](driver-created-versus-application-created-file-objects.md)
-   [Creating and Using Driver-Created File Objects](creating-and-using-driver-created-file-objects.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Creating%20a%20File%20Object%20to%20Handle%20I/O%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




