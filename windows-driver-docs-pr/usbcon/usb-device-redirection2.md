---
Description: This topic describes the routines that a third-party driver can call to replace the Microsoft-provided RPM driver.
title: USB Device Redirection
---

# USB Device Redirection


This topic describes the routines that a third-party driver can call to replace the Microsoft-provided RPM driver.

USB Device Redirection is controlled by the Redirection Policy Manager (RPM). RPM is a kernel-mode export driver that is available in Windows 7. By using RPM, third-party developers can load an alternate driver in place of the original USB device driver. RPM abstracts the redirection functionality that is provided by Microsoft. One of the clients for RPM is Windows Virtual PC, a client virtualization solution for Windows 7.

Whenever a client wants to redirect a particular USB device, RPM calls the USB stack to load its alternate driver for the corresponding device rather than load the actual driver. To load an alternate driver, the client needs to first register itself by calling the [**RPMRegisterAlternateDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537873) routine. This routine returns a handle that is used for all subsequent communication with RPM. RPM allows up to eight clients to be registered at any given time. Clients also provide the device identification string that matches the alternate driver's INF file as part of the call to the **RPMRegisterAlternateDriver** routine.

A client can get a list of devices for which the alternate driver can be loaded by calling the [**RPMGetAvailableDevices**](https://msdn.microsoft.com/library/windows/hardware/ff537863) routine. This routine returns all devices except for hubs and HID devices.

Clients can then load the alternate driver by calling the [**RPMLoadAlternateDriverForDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537867) routine and specifying the HubID and ConnectionIndex that is returned as part of the call to the [**RPMGetAvailableDevices**](https://msdn.microsoft.com/library/windows/hardware/ff537863) routine. This call redirects the USB device and loads the alternate driver.

After the client completes its task, it should call the [**RPMUnloadAlternateDriverForDevice**](https://msdn.microsoft.com/library/windows/hardware/ff537876) routine and then the [**RPMUnregisterAlternateDriver**](https://msdn.microsoft.com/library/windows/hardware/ff537880) routine.

## Related topics


[USB Driver Development Guide](usb-driver-development-guide.md)

[Group Policy Changes](group-policy-changes.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20Device%20Redirection%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




