---
title: Design Guidelines for Starting Devices
author: windows-driver-content
description: Design Guidelines for Starting Devices
ms.assetid: fbdde107-f3a5-4713-a4ac-1c9bafa3c634
---

# Design Guidelines for Starting Devices


## <a href="" id="ddk-design-guidelines-for-starting-devices-kr"></a>


-   The PnP manager fails create requests for the device until the [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) IRP completes, indicating that all the drivers for the device have performed their start operations.

-   Because a [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine runs in the context of a system thread at IRQL PASSIVE\_LEVEL, any memory allocated with [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) for use exclusively during initialization can be from paged pool as long as the driver does not control the device that holds a system page file. Such a memory allocation must be released with [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) before the *DispatchPnP* routine returns control.

-   A WDM device driver's ISR should be capable of determining whether it has been called with a spurious interrupt even during device startup. On return from the call to [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) in the code path that handles **IRP\_MN\_START\_DEVICE**, the ISR can be called immediately if interrupts are enabled on the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Design%20Guidelines%20for%20Starting%20Devices%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


