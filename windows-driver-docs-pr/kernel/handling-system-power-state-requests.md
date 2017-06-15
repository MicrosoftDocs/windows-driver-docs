---
title: Handling System Power State Requests
author: windows-driver-content
description: Handling System Power State Requests
MS-HAID:
- 'PwrMgmt\_83420295-5798-4ec7-8e21-69c339bfd8a2.xml'
- 'kernel.handling\_system\_power\_state\_requests'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: c4547b72-107e-4335-a7bd-081376962da0
keywords: ["power states WDK kernel", "power management WDK kernel , power state requests", "system power states WDK kernel , power state requests", "requests WDK power management", "IRPs WDK power management", "I/O request packets WDK power management", "power requests WDK kernel"]
---

# Handling System Power State Requests


## <a href="" id="ddk-handling-system-power-state-requests-kg"></a>


All drivers must be able to respond to system power state requests if the system is to sleep, hibernate, and wake successfully. A driver for a device changes the [device power state](device-power-states.md) for the device in response to system power state requests.

If any driver does not support system power management, individual devices can sleep and wake, but the power manager cannot put the system as a whole into a sleeping state.

The following topics cover details of handling system power state requests:

[System Power States](system-power-states.md)

[System Power Policy](system-power-policy.md)

[Preventing System Power State Changes](preventing-system-power-state-changes.md)

[Handling IRP\_MN\_QUERY\_POWER for System Power States](handling-irp-mn-query-power-for-system-power-states.md)

[Handling IRP\_MN\_SET\_POWER for System Power States](handling-irp-mn-set-power-for-system-power-states.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Handling%20System%20Power%20State%20Requests%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


