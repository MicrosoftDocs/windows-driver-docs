---
Description: Selective suspend is disabled for upgrade versions of Microsoft Windows XP. It is enabled for clean installations of Windows XP, Windows Vista, and later versions of Windows.
title: Enabling Selective Suspend
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Enabling Selective Suspend


Selective suspend is disabled for upgrade versions of Microsoft Windows XP. It is enabled for clean installations of Windows XP, Windows Vista, and later versions of Windows.

To enable selective suspend support for a given root hub and its child devices, select the checkbox on the **Power Management** tab for the USB root hub in **Device Manager**.

Alternatively, you can enable or disable selective suspend by setting the value of **HcDisableSelectiveSuspend** under the software key of the USB port driver. A value of 1 disables selective suspend. A value of 0 enables selective suspend.

For instance, the following lines in Usbport.inf disable selective suspend for a Hydra OHCI controller:

```cpp
[OHCI_NOSS.AddReg.NT]
HKR,,"HcDisableSelectiveSuspend",0x00010001,1
```

Client drivers should not try to determine whether selective suspend is enabled before sending idle requests. They should submit idle requests whenever the device is idle. If the idle request fails the client driver should reset the idle timer and retry.

## Related topics


[USB Selective Suspend](usb-selective-suspend.md)

[USB Power Management](usb-power-management.md)

 

 





