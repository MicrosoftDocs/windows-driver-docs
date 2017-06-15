---
title: Handling a System Query-Power IRP in a Bus Driver
author: windows-driver-content
description: Handling a System Query-Power IRP in a Bus Driver
MS-HAID:
- 'PwrMgmt\_961ebd28-baaf-43ce-9766-41ecfc7f6af6.xml'
- 'kernel.handling\_a\_system\_query\_power\_irp\_in\_a\_bus\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: d42c268e-d57d-41a6-8e61-67c651082106
keywords: ["query-power IRPs WDK power management", "bus drivers WDK power management"]
---

# Handling a System Query-Power IRP in a Bus Driver


## <a href="" id="ddk-handling-a-system-query-power-irp-in-a-bus-driver-kg"></a>


When a system query-power request reaches a bus driver (that is not the power policy owner for a device), the driver ensures that it can support a device power state that corresponds to the queried system power state and, if wake-up is enabled, that the queried system power state would not prevent its device from waking the system.

In Windows 7 and Windows Vista, the bus driver sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS if the driver can change to the specified power state or sets a failure status if the driver cannot.

In Windows Server 2003, Windows XP, and Windows 2000, the bus driver first calls [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) and then sets **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS if the driver can change to the specified power state or sets a failure status if the driver cannot.

After the bus driver completes the IRP, the power manager calls [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines set by other drivers as they passed the IRP down the stack.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20System%20Query-Power%20IRP%20in%20a%20Bus%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


