---
title: Handling a System Query-Power IRP in a Filter or Function Driver
description: Handling a System Query-Power IRP in a Filter or Function Driver
ms.assetid: 81d921d5-6db8-4858-b86e-1484781faba5
keywords: ["query-power IRPs WDK power management", "filter drivers WDK power management", "function drivers WDK power management"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Handling a System Query-Power IRP in a Filter or Function Driver





A filter or function driver (that is not the power policy owner for a device) should pass a system query-power IRP to the next-lower driver, in the following steps:

1.  Call [**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204), passing the current IRP, to ensure that the driver does not receive a PnP [**IRP\_MN\_REMOVE\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551738) request while handling the power IRP.

    If **IoAcquireRemoveLock** returns a failure status, the driver should not continue processing the IRP. Instead, beginning with Windows Vista, the driver should call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) to complete the IRP and return the failure status. In Windows Server 2003, Windows XP, and Windows 2000, the driver should call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), call **IoCompleteRequest** to complete the IRP, and return the failure status.

2.  Determine whether it should fail the query. For guidelines, see [Failing a System Query-Power IRP in a Filter or Function Driver](failing-a-system-query-power-irp-in-a-filter-or-function-driver.md) and complete processing as described in that section.

3.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776). (Windows Server 2003, Windows XP, and Windows 2000 only)

4.  Set the IRP stack location ([**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) or [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387)). The driver can set an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine in the IRP, but doing so is rarely necessary.

5.  Call **IoCallDriver** (in Windows 7 and Windows Vista) or [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654) (in Windows Server 2003, Windows XP, and Windows 2000) to pass the IRP to the next-lower driver.

6.  Call [**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560). However, if the driver set an *IoCompletion* routine for the IRP, make this call from the *IoCompletion* routine instead.

7.  Return STATUS\_PENDING from its [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routine.

 

 




