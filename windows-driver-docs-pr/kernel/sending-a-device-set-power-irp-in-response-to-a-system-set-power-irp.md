---
title: Sending a Device Set-Power IRP in Response to a System Set-Power IRP
author: windows-driver-content
description: Sending a Device Set-Power IRP in Response to a System Set-Power IRP
MS-HAID:
- 'PwrMgmt\_22667c7e-69af-47eb-9ea0-ce08e795c774.xml'
- 'kernel.sending\_a\_device\_set\_power\_irp\_in\_response\_to\_a\_system\_set\_power\_irp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b2029292-d770-4095-8bd7-9358b282216c
keywords: ["sending set-power IRPs", "set-power IRPs WDK power management"]
---

# Sending a Device Set-Power IRP in Response to a System Set-Power IRP


## <a href="" id="ddk-sending-a-device-set-power-irp-in-response-to-a-system-set-power-i"></a>


The device power policy owner should take the following steps to respond to a system set-power IRP:

1.  Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204), passing the current IRP as the *Tag* parameter, to ensure that the driver does not receive a Plug and Play [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, starting with Windows Vista, the driver should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the request and then return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should first call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), call **IoCompleteRequest** to complete the IRP, and then return the failure status.

2.  Set up the IRP stack location for the next-lower driver by calling [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387).

3.  Set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine in the system set-power IRP.

4.  Call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) to mark the system set-power IRP as pending.

5.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (starting with Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the system set-power IRP to the next-lower driver.

6.  Return STATUS\_PENDING from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

In the *IoCompletion* routine (see Step 3 in the preceding list), the device power policy owner sends a device set-power IRP as follows:

1.  Inspect the system set-power IRP to get the requested system power state. Choose an appropriate device power state for that system power state. For further information, see [Determining the Correct Device Power State](determining-the-correct-device-power-state.md).

2.  Call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) for the device power state determined in Step 1. The power policy owner must send the device set-power request even if the device is already in that state.

3.  Specify a power-completion callback routine (*CompletionFunction*) in the call to **PoRequestPowerIrp** and pass the system set-power IRP in the *Context* buffer.

4.  Return STATUS\_MORE\_PROCESSING\_REQUIRED from the *IoCompletion* routine, so that the driver can finish processing the system set-power IRP in the power-completion callback routine.

Remember that the device power policy owner not only sends the device set-power IRP but also must handle this IRP as it travels through the device stack. Consequently, a device power policy owner might have not only a power-completion callback routine associated with the device set-power IRP and an *IoCompletion* routine for the system set-power IRP, but also an *IoCompletion* routine for the device set-power IRP. For further information, see [Handling IRP\_MN\_SET\_POWER for Device Power States](handling-irp-mn-set-power-for-device-power-states.md).

After the I/O manager calls all the *IoCompletion* routines that were set as the device set-power IRP traveled down the device stack, the I/O manager calls the power-completion callback routine. By this time, all drivers in the stack have completed the device set-power IRP and the device power transition is complete.

The power-completion callback routine must do the following:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Complete the system set-power IRP ([**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)) with the status returned for the device set-power IRP.

3.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to free the previously acquired lock.

4.  Return the status with which the set-power IRPs completed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sending%20a%20Device%20Set-Power%20IRP%20in%20Response%20to%20a%20System%20Set-Power%20IRP%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


