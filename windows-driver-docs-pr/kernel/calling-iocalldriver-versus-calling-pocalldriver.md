---
title: Calling IoCallDriver versus Calling PoCallDriver
author: windows-driver-content
description: Calling IoCallDriver versus Calling PoCallDriver
MS-HAID:
- 'PwrMgmt\_aaeef4d9-83d8-4ed5-9044-b406d7abb838.xml'
- 'kernel.calling\_iocalldriver\_versus\_calling\_pocalldriver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a47e2310-e89b-4552-bbe3-d4984ae8b564
keywords: ["PoCallDriver", "active power IRPs WDK kernel", "power IRPs WDK kernel , IoCallDriver versus PoCallDriver"]
---

# Calling IoCallDriver versus Calling PoCallDriver


## <a href="" id="ddk-using-pocalldriver-kg"></a>


Beginning with Windows Vista, a driver should call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) instead of [**PoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff559654), to pass power IRPs to the next-lower driver. In Windows Server 2003, Windows XP, and Windows 2000, a driver must call **PoCallDriver**, not **IoCallDriver**, to pass power IRPs to the next-lower driver. Note, however, that drivers that use the same code to run both in Windows Vista and in earlier Windows versions, must call **PoCallDriver**, not **IoCallDriver**.

Beginning with Windows Vista, [**PoRequestPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559734) and **IoCallDriver** ensure that the power manager properly synchronizes power IRPs throughout the system. In Windows Server 2003, Windows XP, and Windows 2000, **PoRequestPowerIrp**, **PoCallDriver**, and [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776), ensure that the power manager properly synchronizes power IRPs throughout the system.

The system limits the number of active power IRPs as follows:

-   No more than one system power IRP ([**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744), [**IRP\_MN\_QUERY\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551699)) can be active for each physical device object ([PDO](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) at any given time.

-   No more than one device set-power IRP (**IRP\_MN\_SET\_POWER)** can be active for each PDO at any given time.

-   No more than one device power IRP that requires an inrush of power can be active anywhere in the system at any given time.

To ensure that two inrush devices do not attempt to power up simultaneously, the power manager keeps track of active inrush power IRPs across the whole system and allows only one to be active at a time. An additional inrush IRP cannot start until the active inrush IRP has completed.

Because of these restrictions on inrush IRPs, a device power IRP might block while an inrush IRP for another device completes. Driver writers should be aware of this behavior while debugging.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Calling%20IoCallDriver%20versus%20Calling%20PoCallDriver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


