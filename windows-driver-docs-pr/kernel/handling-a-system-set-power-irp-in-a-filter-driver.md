---
title: Handling a System Set-Power IRP in a Filter Driver
author: windows-driver-content
description: Handling a System Set-Power IRP in a Filter Driver
ms.assetid: a6e364fc-f173-47ce-b36b-84f802cefcc3
keywords: ["set-power IRPs WDK power management", "filter drivers WDK power management"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Handling a System Set-Power IRP in a Filter Driver


## <a href="" id="ddk-handling-a-system-set-power-irp-in-a-filter-driver-kg"></a>


All filter drivers and any function driver that does not own power policy for its device stack should simply pass the system set-power IRP to the next-lower driver, in the following steps:

1.  Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, beginning with Windows Vista, the driver should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP and return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should first call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), call **IoCompleteRequest** to complete the IRP, and then return the failure status.

2.  Call **PoStartNextPowerIrp** to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

3.  Set the IRP stack location ([**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) or [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387)). The driver can set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine in the IRP, but doing so is rarely necessary.

4.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP to the next-lower driver.

5.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560). However, if the driver set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for the IRP, make this call from the *IoCompletion* routine instead.

6.  Return STATUS\_PENDING from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20System%20Set-Power%20IRP%20in%20a%20Filter%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


