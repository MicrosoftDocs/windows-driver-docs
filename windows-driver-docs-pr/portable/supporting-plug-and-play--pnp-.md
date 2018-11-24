---
Description: The User Mode Driver Framework (UMDF) requires that drivers support the IPnpCallback interface for Plug and Play (PnP) operations and the IPnpCallbackSelfManagedIo interface for power-management operations.
title: Supporting Plug and Play (PnP) and Power Management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Plug and Play (PnP) and Power Management


The User Mode Driver Framework (UMDF) requires that drivers support the [**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762) interface for Plug and Play (PnP) operations and the [**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776) interface for power-management operations.

The first interface, **IPnpCallback** supports the methods invoked when a user plugs-in, or unplugs, their device. The second interface, **IPnpCallbackSelfManagedIo** supports the methods invoked when a device enters low-power state, or, returns to its working state.

Because all but one of the WPD samples emulate hardware, the methods for these interfaces perform no meaningful work and return immediately.

The one exception is the WpdBasicHardwareDriver sample. Because this driver supports actual hardware, it contains working code for two methods in the **IPnpCallback** interface. The two methods supported by this sample are [**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799) and [**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803). The first method retrieves a pointer to the I/O Target that the sample driver uses to forward I/O requests to the kernel-mode RS232 driver. After retrieving this pointer, the **IPnpCallback::OnDOEntry** method starts the I/O target. The second method, **IPnpCallback::OnD0Exit** retrieves a pointer to the I/O Target and then stops it.

If your driver supports hardware, you'll want to add support for one, or both, of these interfaces. For a complete description of PnP and Power-Management in user-mode device drivers, see [PnP and Power Management Scenarios in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff560452).

## <span id="related_topics"></span>Related topics


[**IPnpCallback**](https://msdn.microsoft.com/library/windows/hardware/ff556762)

[**IPnpCallback::OnD0Entry**](https://msdn.microsoft.com/library/windows/hardware/ff556799)

[**IPnpCallback::OnD0Exit**](https://msdn.microsoft.com/library/windows/hardware/ff556803)

[**IPnpCallbackSelfManagedIo**](https://msdn.microsoft.com/library/windows/hardware/ff556776)

[PnP and Power Management Scenarios in UMDF](https://msdn.microsoft.com/library/windows/hardware/ff560452)

 

 





