---
title: Calling PoStartNextPowerIrp
author: windows-driver-content
description: Calling PoStartNextPowerIrp
MS-HAID:
- 'PwrMgmt\_a8333353-d54a-44bc-9ea6-55d2e385e7f5.xml'
- 'kernel.calling\_postartnextpowerirp'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8b3fb578-2ac2-4a04-ac99-1cfd51b07b01
keywords: ["power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
---

# Calling PoStartNextPowerIrp


## <a href="" id="ddk-calling-postartnextpowerirp-kg"></a>


Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) is not required and a call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, after a driver processes a query-power IRP or a set-power IRP, the driver must call **PoStartNextPowerIrp** to notify the power manager that it is ready to receive another power IRP. Drivers must call **PoStartNextPowerIrp** while the IRP stack location points to the current driver and before calling [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654).

A driver must call this routine once for each [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) or [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request that it receives. Drivers do not need to call **PoStartNextPowerIrp** when handling [**IRP\_MN\_WAIT\_WAKE**](https://msdn.microsoft.com/library/windows/hardware/ff551766) or [**IRP\_MN\_POWER\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/ff551644) requests.

When a driver calls **PoStartNextPowerIrp**, the current IRP stack location must point to the current driver. As a general rule, this call is best made from an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine. **PoStartNextPowerIrp** must be called before [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355), and **PoCallDriver**. Calling the routines in the other order might cause a system deadlock.

Even if a driver fails the IRP, it must nevertheless call **PoStartNextPowerIrp** to inform the power manager that it is ready to handle another power IRP.

The following sections clarify when each type of driver should call this routine:

[Calling PoStartNextPowerIrp from a Filter Driver](calling-postartnextpowerirp-from-a-filter-driver.md)

[Calling PoStartNextPowerIrp from a Device Power Policy Owner](calling-postartnextpowerirp-from-a-device-power-policy-owner.md)

[Calling PoStartNextPowerIrp from a Bus Driver](calling-postartnextpowerirp-from-a-bus-driver.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20PoStartNextPowerIrp%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


