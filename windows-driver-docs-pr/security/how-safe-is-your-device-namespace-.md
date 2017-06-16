---
title: How safe is your device namespace
description: The I/O Manager can protect your device's namespace from unprivileged access if you set the FILE\_DEVICE\_SECURE\_OPEN device characteristic.
ms.assetid: 1E1A77C3-C9F7-4668-B73A-BC5770D907EE
---

# How safe is your device namespace?


**Last updated:**

-   May 27, 2007

The I/O Manager can protect your device's namespace from unprivileged access if you set the FILE\_DEVICE\_SECURE\_OPEN device characteristic.

The I/O Manager can protect your device's namespace from unprivileged access if you allow it to. Setting the FILE\_DEVICE\_SECURE\_OPEN device characteristic directs the I/O Manager to apply the security descriptor of the device object to all open requests, including file-open requests into the device's namespace. Essentially, the I/O Manager performs access checks and fails requests that don't have the privileges you established for the device object. FILE\_DEVICE\_SECURE\_OPEN is supported on Microsoft Windows NT 4.0 SP5 and later versions of Windows.

A client usually opens a driver's named device objects ("\\Device\\MyDevice") in order to access the device. However, a client can also attempt to open files on a device by appending a file path to the device object name ("\\Device\\MyDevice\\Some\\Arbitrary\\Path\\To\\A\\File"). When this happens, the file object has a FileName equal to the trailing portion of the name ("\\Some\\Arbitrary\\Path\\To\\A\\File"). Unless the device driver watches for this case and either fails the create request or applies a security check, this can create a security hole in the system, because an unprivileged user could bypass security and obtain handles with read and write access simply by opening a file in the device's namespace.

Your driver is always responsible for managing its namespace, and using FILE\_DEVICE\_SECURE\_OPEN makes that easier by having the I/O Manager perform security checks for your driver. Setting FILE\_DEVICE\_SECURE\_OPEN closes potential security holes because the security descriptor for the device is applied to all open attempts, including those with trailing names, no matter how deep into the namespace they go. (To be absolutely sure of preventing a caller from opening files, make sure that **IrpSp-&gt;FileObject-&gt;FileName.Length** is 0 in every create IRP your driver receives).

## <span id="What_should_you_do__"></span><span id="what_should_you_do__"></span><span id="WHAT_SHOULD_YOU_DO__"></span>What should you do?


Almost all drivers that create device objects should set FILE\_DEVICE\_SECURE\_OPEN when the device object is created. The only drivers that shouldn't are those that implement their own security checking, such as file systems.

-   Set FILE\_DEVICE\_SECURE\_OPEN when calling [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) or [**IoCreateDeviceSecure**](https://msdn.microsoft.com/library/windows/hardware/ff548407) to create a device object.
-   For Plug and Play drivers for Microsoft Windows 2000 and later, use the INF file to assign FILE\_DEVICE\_SECURE\_OPEN to the DeviceCharacteristics value name in the registry.
-   If your driver cannot use FILE\_DEVICE\_SECURE\_OPEN for some reason, perform your own access checks or reject I/O requests from unprivileged callers.
-   If your driver does not support opening files or supports exclusive opens, fail any IRP\_MJ\_CREATE requests that specify an **IrpSp-&gt;FileObject-&gt;FileName** parameter with a nonzero length.

## <span id="related_topics"></span>Related topics


[Kernel-Mode Drivers: Fixing Common Driver Reliability Issues](http://download.microsoft.com/download/5/7/7/577a5684-8a83-43ae-9272-ff260a9c20e2/drvqa.doc)

[Controlling Device Namespace Access](https://msdn.microsoft.com/library/windows/hardware/ff542068)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[hw_design\hw_design]:%20How%20safe%20is%20your%20device%20namespace?%20%20RELEASE:%20%286/16/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





