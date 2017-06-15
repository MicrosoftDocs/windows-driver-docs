---
title: Calling PoStartNextPowerIrp from a Bus Driver
author: windows-driver-content
description: Calling PoStartNextPowerIrp from a Bus Driver
MS-HAID:
- 'PwrMgmt\_939e02f7-a71a-4e8f-a2f4-ba33e02eab10.xml'
- 'kernel.calling\_postartnextpowerirp\_from\_a\_bus\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4e23ebe1-c939-48e1-82bf-cdb4980a5a7b
keywords: ["bus drivers WDK power management", "power IRPs WDK kernel , PoStartNextPowerIrp", "PoStartNextPowerIrp"]
---

# Calling PoStartNextPowerIrp from a Bus Driver


## <a href="" id="ddk-calling-postartnextpowerirp-from-a-bus-driver-kg"></a>


Beginning with Windows Vista, calling [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) is not required and call to this routine performs no power management operation. However, in Windows Server 2003, Windows XP, and Windows 2000, a bus driver must call **PoStartNextPowerIrp** once for every [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699) or [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request that the driver receives.

A bus driver always calls this routine in its *DispatchPower* routine, before it calls the [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343) routine.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20PoStartNextPowerIrp%20from%20a%20Bus%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


