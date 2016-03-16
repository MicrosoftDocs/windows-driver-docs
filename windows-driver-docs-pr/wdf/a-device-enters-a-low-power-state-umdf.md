---
title: A Device Enters a Low Power State
description: A Device Enters a Low Power State
ms.assetid: c3697272-75ec-4de5-b123-3d1c68d2044e
keywords: ["power management scenarios WDK UMDF entering a low power state", "low power state scenario WDK UMDF"]
---

# A Device Enters a Low-Power State


\[This topic applies to UMDF 1.*x*.\]

A device leaves its working (D0) state and enters a low-power state if one of the following occurs:

-   The device is idle (that is, not being accessed) and is capable of entering a low-power idle state while the system remains in its working (S0) state.

-   The system's power state has changed from its working (S0) state to a low-power state. (Drivers can call [**IWDFDevice2::GetSystemPowerAction**](https://msdn.microsoft.com/library/windows/hardware/ff556936) to determine the reason for the change in the system's power state.)

For each UMDF-based function and filter driver that supports the device, the framework does the following, in sequence, one driver at a time, starting with the driver that is highest in the driver stack:

1.  If the driver is using self-managed I/O, the framework calls the driver's [**IPnpCallbackSelfManagedIo::OnSelfManagedIoSuspend**](https://msdn.microsoft.com/library/windows/hardware/ff556790) callback function.

2.  The framework stops all of the device's power-managed I/O queues and calls their [**IPnpCallbackSelfManagedIo::OnSelfManagedIoStop**](https://msdn.microsoft.com/library/windows/hardware/ff556787) callback functions (if they exist).

3.  If the driver is the device's power policy owner, the framework calls its [**IPowerPolicyCallbackWakeFromS0::OnArmWakeFromS0**](https://msdn.microsoft.com/library/windows/hardware/ff556817) or [**IPowerPolicyCallbackWakeFromSx::OnArmWakeFromSx**](https://msdn.microsoft.com/library/windows/hardware/ff556826) callback function.

4.  The framework calls the driver's [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803) callback function (if it exists).

To see a diagram that shows these steps, see the orderly removal figure in [A User Unplugs a Device](a-user-unplugs-a-device.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20A%20Device%20Enters%20a%20Low-Power%20State%20%20RELEASE:%20%283/16/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




