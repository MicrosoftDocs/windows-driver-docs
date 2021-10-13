---
title: PnP and Power Management Interfaces
description: PnP and Power Management Interfaces
keywords:
- Plug and Play WDK UMDF , power management interfaces
- PnP WDK UMDF , power management interfaces
- power management WDK UMDF , interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnP and Power Management Interfaces


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method to notify the UMDF driver of the arrival and passes the [**IWDFDriver**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdriver) and [**IWDFDeviceInitialize**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize) interfaces in the call. The driver calls the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method to create a framework device object for the device.

When drivers create a framework device object, they can register the following interfaces so that the framework notifies the driver—by calling the methods associated with the interfaces—when Plug and Play (PnP) and power management (PM) events occur.

[**IPnpCallback**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallback)

[**IPnpCallbackSelfManagedIo**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackselfmanagedio)

[**IPnpCallbackHardware**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardware)

[**IPowerPolicyCallbackWakeFromS0**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefroms0)

[**IPowerPolicyCallbackWakeFromSx**](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipowerpolicycallbackwakefromsx)

 

