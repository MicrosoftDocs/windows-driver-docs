---
title: Handling a System Set-Power IRP in a Bus Driver
author: windows-driver-content
description: Handling a System Set-Power IRP in a Bus Driver
MS-HAID:
- 'PwrMgmt\_4a00be48-e1ea-4167-92c4-08dc2b3e9dde.xml'
- 'kernel.handling\_a\_system\_set\_power\_irp\_in\_a\_bus\_driver'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: e88344bd-4223-4cd5-9428-201d46c6dbb4
keywords: ["set-power IRPs WDK power management", "bus drivers WDK power management"]
---

# Handling a System Set-Power IRP in a Bus Driver


## <a href="" id="ddk-handling-a-system-set-power-irp-in-a-bus-driver-kg"></a>


When a bus driver receives a system set-power IRP, it must take the following steps:

1.  Call [**PoStartNextPowerIrp**](https://msdn.microsoft.com/library/windows/hardware/ff559776) to start the next power IRP. (Windows Server 2003, Windows XP, and Windows 2000 only.)

2.  Set **Irp-&gt;IoStatus.Status** to STATUS\_SUCCESS. The driver cannot fail a system set-power IRP.

3.  Call [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), specifying IO\_NO\_INCREMENT, to complete the IRP.

The bus driver does not change device power settings until it receives a power IRP that requests a device power state.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20a%20System%20Set-Power%20IRP%20in%20a%20Bus%20Driver%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


