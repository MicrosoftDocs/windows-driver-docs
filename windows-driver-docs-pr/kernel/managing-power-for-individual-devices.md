---
title: Managing Power for Individual Devices
author: windows-driver-content
description: Managing Power for Individual Devices
MS-HAID:
- 'PwrMgmt\_d2931041-848b-4465-8123-34a0754ad3db.xml'
- 'kernel.managing\_power\_for\_individual\_devices'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 95c7e900-5d51-4eb7-8780-1c40befa3599
keywords: ["power management WDK kernel , device management", "device power management WDK kernel", "system power states WDK kernel", "conserving power WDK kernel", "change power states WDK kernel", "IRPs WDK power management", "I/O request packets WDK power management"]
---

# Managing Power for Individual Devices


## <a href="" id="ddk-managing-power-for-individual-devices-kg"></a>


Drivers manage power for their devices by responding to [system power state](system-power-states.md) changes, detecting and shutting down idle devices, and powering up devices when they are needed.

This section covers the following topics related to device power management:

[Device Power States](device-power-states.md)

[Detecting an Idle Device](detecting-an-idle-device.md)

[Managing Device Power Policy](managing-device-power-policy.md)

[Handling IRP\_MN\_SET\_POWER for Device Power States](handling-irp-mn-set-power-for-device-power-states.md)

[Handling IRP\_MN\_QUERY\_POWER for Device Power States](handling-irp-mn-query-power-for-device-power-states.md)

[Sending IRP\_MN\_QUERY\_POWER or IRP\_MN\_SET\_POWER for Device Power States](sending-irp-mn-query-power-or-irp-mn-set-power-for-device-power-states.md)

[Detecting an Idle Device](detecting-an-idle-device.md)

[Supporting D3cold in a Driver](supporting-d3cold-in-a-driver.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Managing%20Power%20for%20Individual%20Devices%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


