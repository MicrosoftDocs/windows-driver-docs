---
Description: Selective suspend is disabled for upgrade versions of Microsoft Windows XP. It is enabled for clean installations of Windows XP, Windows Vista, and later versions of Windows.
title: Enabling Selective Suspend
author: windows-driver-content
---

# Enabling Selective Suspend


Selective suspend is disabled for upgrade versions of Microsoft Windows XP. It is enabled for clean installations of Windows XP, Windows Vista, and later versions of Windows.

To enable selective suspend support for a given root hub and its child devices, select the checkbox on the **Power Management** tab for the USB root hub in **Device Manager**.

Alternatively, you can enable or disable selective suspend by setting the value of **HcDisableSelectiveSuspend** under the software key of the USB port driver. A value of 1 disables selective suspend. A value of 0 enables selective suspend.

For instance, the following lines in Usbport.inf disable selective suspend for a Hydra OHCI controller:

```
[OHCI_NOSS.AddReg.NT]
HKR,,"HcDisableSelectiveSuspend",0x00010001,1
```

Client drivers should not try to determine whether selective suspend is enabled before sending idle requests. They should submit idle requests whenever the device is idle. If the idle request fails the client driver should reset the idle timer and retry.

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20Enabling%20Selective%20Suspend%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




