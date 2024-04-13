---
description: The User Mode Driver Framework (UMDF) requires that drivers support the IPnpCallback interface for Plug and Play (PnP) operations and the IPnpCallbackSelfManagedIo interface for power-management operations.
title: Supporting Plug and Play (PnP) and Power Management
ms.date: 03/03/2023
---

# Supporting Plug and Play (PnP) and Power Management


The User Mode Driver Framework (UMDF) requires that drivers support the [**IPnpCallback**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallback) interface for Plug and Play (PnP) operations and the [**IPnpCallbackSelfManagedIo**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackselfmanagedio) interface for power-management operations.

The first interface, **IPnpCallback** supports the methods invoked when a user plugs-in, or unplugs, their device. The second interface, **IPnpCallbackSelfManagedIo** supports the methods invoked when a device enters low-power state, or, returns to its working state.

Because all but one of the WPD samples emulate hardware, the methods for these interfaces perform no meaningful work and return immediately.

The one exception is the WpdBasicHardwareDriver sample. Because this driver supports actual hardware, it contains working code for two methods in the **IPnpCallback** interface. The two methods supported by this sample are [**IPnpCallback::OnD0Entry**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0entry) and [**IPnpCallback::OnD0Exit**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0exit). The first method retrieves a pointer to the I/O Target that the sample driver uses to forward I/O requests to the kernel-mode RS232 driver. After retrieving this pointer, the **IPnpCallback::OnDOEntry** method starts the I/O target. The second method, **IPnpCallback::OnD0Exit** retrieves a pointer to the I/O Target and then stops it.

If your driver supports hardware, you'll want to add support for one, or both, of these interfaces. For a complete description of PnP and Power-Management in user-mode device drivers, see [PnP and Power Management Scenarios in UMDF](../wdf/pnp-and-power-management-scenarios-in-umdf.md).

## <span id="related_topics"></span>Related topics


[**IPnpCallback**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallback)

[**IPnpCallback::OnD0Entry**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0entry)

[**IPnpCallback::OnD0Exit**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallback-ond0exit)

[**IPnpCallbackSelfManagedIo**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackselfmanagedio)

[PnP and Power Management Scenarios in UMDF](../wdf/pnp-and-power-management-scenarios-in-umdf.md)

 

