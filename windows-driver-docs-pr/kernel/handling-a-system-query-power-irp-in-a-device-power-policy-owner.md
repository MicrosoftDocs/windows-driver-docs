---
title: Handling a System Query-Power IRP in a Device Power Policy Owner
author: windows-driver-content
description: Handling a System Query-Power IRP in a Device Power Policy Owner
MS-HAID:
- 'PwrMgmt\_1cca1589-4985-4b2c-93ec-386c4ddee1f1.xml'
- 'kernel.handling\_a\_system\_query\_power\_irp\_in\_a\_device\_power\_policy\_owner'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 680e3be2-63d9-4d79-a7c0-422e852e9347
keywords: ["query-power IRPs WDK power management", "device power policy owners WDK kernel"]
---

# Handling a System Query-Power IRP in a Device Power Policy Owner


## <a href="" id="ddk-handling-a-system-query-power-irp-in-a-device-power-policy-owner-k"></a>


When a device power policy owner receives an [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) for a system power state, it responds by passing down the query and, in an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, sending an **IRP\_MN\_QUERY\_POWER** for a device power state. When all drivers in the stack have completed the device query, the device power policy owner completes the system query.

A device power policy owner should take the following steps in its [DispatchPower routine](dispatchpower-routines.md) to respond to a system query:

1.  Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, beginning with Windows Vista, the driver should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP and return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), call **IoCompleteRequest** to complete the IRP, and return the failure status.

2.  Ensure that the driver can support the queried system power state, as described in [Failing a System Query-Power IRP in a Filter or Function Driver](failing-a-system-query-power-irp-in-a-filter-or-function-driver.md). If not, complete the IRP with a failure status as described in that section.

    However, a driver must not fail a query for S4 (**PowerSystemHibernate**) if its device is enabled for wake-up but it cannot wake the system from the hibernate state. In this case, the power policy owner for the driver (which sent the [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766)) must cancel the wait/wake IRP and succeed the system query. For more information, see [Canceling a Wait/Wake IRP](canceling-a-wait-wake-irp.md).

3.  If the driver can support the queried system power state, call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422).

4.  Set up the IRP stack location for the next-lower driver by calling [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387).

5.  Set an *IoCompletion* routine in the system query power IRP.

6.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 2003, Windows XP, and Windows 2000), to pass the IRP to the next-lower driver.

7.  Return STATUS\_PENDING.

The [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine should do the following:

1.  Check **Irp-&gt;IoStatus.Status** to ensure that lower drivers have completed the IRP successfully. If a lower driver has specified a non-success NTSTATUS value, the *IoCompletion* routine should return the NTSTATUS value.

2.  If lower drivers have successfully completed the IRP, call [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) to send a device query-power IRP for a device power state that is valid for the queried system power state. If necessary, consult the DEVICE\_STATE array in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure to determine which device power states are valid for the queried system power state.

3.  Specify a callback routine (*CompletionFunction* parameter) in the call to **PoRequestPowerIrp** and pass the system IRP in the *Context* area.

4.  Return STATUS\_MORE\_PROCESSING\_REQUIRED so that the driver can finish processing the system query IRP in the callback routine.

After the IRP has been completed and all *IoCompletion* routines set during IRP processing have been run, the power manager, through the I/O manager, calls the power policy manager's callback routine (the *CompletionFunction* parameter to **PoRequestPowerIrp**). The callback routine, in turn, must do the following:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Complete the system query-power IRP (call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343)) with the status returned for the device query-power IRP.

3.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560) to free the previously acquired lock.

Remember that the device power policy owner not only sends the device query but also must handle it on its way down the device stack. For more information, see [Handling IRP\_MN\_QUERY\_POWER for Device Power States](handling-irp-mn-query-power-for-device-power-states.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20System%20Query-Power%20IRP%20in%20a%20Device%20Power%20Policy%20Owner%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


