---
title: The Filter Driver's Control Device Object
author: windows-driver-content
description: The Filter Driver's Control Device Object
ms.assetid: ac49b5d0-110d-4e47-814b-05f59791de41
keywords: ["control device objects WDK file system", "CDOs WDK file system"]
---

# The Filter Driver's Control Device Object


## <span id="ddk_the_filter_drivers_control_device_object_if"></span><span id="DDK_THE_FILTER_DRIVERS_CONTROL_DEVICE_OBJECT_IF"></span>


Unlike a file system, which is required to create and use a named control device object (CDO), a file system filter driver is not required to have a CDO. If it does, this CDO, which can optionally be named, represents the filter driver to the system. Its role is to receive I/O requests from a user-mode application (or, less commonly, another kernel-mode driver), and to act on them appropriately.

Most file system filter drivers create and use a CDO. However, support for I/O requests on the CDO is optional. To provide this support, when the filter driver calls [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create the CDO, it must supply a device name for the object. The user-mode application can then obtain a handle to the named CDO by calling [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858), supplying the user-mode version of the device name.

For example, consider a hypothetical "MyLegacyFilter" kernel-mode driver. This driver can create a CDO with the name:

```
\Device\MyLegacyFilter
```

and calls [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) to link this name to an equivalent user-mode-visible name. This is done so that MyLegacyFilter's user-mode application can open a handle to the kernel-mode driver's CDO by supplying the name:

```
\\.\MyLegacyFilter
```

when it calls [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858).

### <span id="types_of_i_o_requests_that_are_sent_to_the_filter_driver_s_control_dev"></span><span id="TYPES_OF_I_O_REQUESTS_THAT_ARE_SENT_TO_THE_FILTER_DRIVER_S_CONTROL_DEV"></span>Types of I/O Requests That Are Sent to the Filter Driver's Control Device Object

File system filter drivers are not required to support any I/O operations on the control device object (CDO). However, most filters permit the following types of I/O requests to be sent to the filter's CDO:

-   [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff548630) (to open a handle to the target device object, and give that handle to a user application)

-   [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff548608) (to close a user-mode application's handle to the target device object)

-   [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff548621) (to close the last remaining open handle to the target device object)

-   [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548649), [**IRP\_MJ\_FILE\_SYSTEM\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff548670), or **FastIoDeviceControl** (to send private IOCTLs or FSCTLs to the filter driver)

Note that, unlike all other device objects that a file system filter driver creates, the CDO is not attached to a driver stack. No device objects are attached above or below the filter driver's CDO. Thus, for any I/O request it receives, the CDO can safely assume that it is the sole intended recipient. This is not true for filter device objects or file system CDOs. Accordingly, the CDO must eventually complete every IRP it receives. For fast I/O requests, it must return **TRUE** or **FALSE**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20The%20Filter%20Driver's%20Control%20Device%20Object%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


