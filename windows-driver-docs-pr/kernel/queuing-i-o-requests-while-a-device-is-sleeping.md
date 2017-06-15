---
title: Queuing I/O Requests While a Device Is Sleeping
author: windows-driver-content
description: Queuing I/O Requests While a Device Is Sleeping
MS-HAID:
- 'PwrMgmt\_edf2fbaa-3bad-4fb1-9d3f-c212621d28f1.xml'
- 'kernel.queuing\_i\_o\_requests\_while\_a\_device\_is\_sleeping'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 8cc0cea0-e5be-4705-ad4d-13a44d536469
keywords: ["I/O WDK power management", "queuing I/O requests", "sleep power management WDK kernel", "asleep devices WDK power management", "queuing IRPs", "power IRPs WDK kernel , queuing I/O requests", "working state returns WDK power management"]
---

# Queuing I/O Requests While a Device Is Sleeping


## <a href="" id="ddk-queuing-i-o-requests-while-a-device-is-sleeping-kg"></a>


While a device is asleep, its drivers should queue any I/O requests directed to the device. The [**IoAllocateWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff548276), [**IoQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549466), and [**IoFreeWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549133) support routines provide one way of queuing IRPs for delayed processing. For an example, see the queuing mechanism described for PnP drivers in [Holding Incoming IRPs When A Device Is Paused](holding-incoming-irps-when-a-device-is-paused.md).

A driver can access its device only when the device is in the Working (D0) state. A driver cannot touch any device registers when the device is in a sleep state; the device must first be returned to the Working state.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Queuing%20I/O%20Requests%20While%20a%20Device%20Is%20Sleeping%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


