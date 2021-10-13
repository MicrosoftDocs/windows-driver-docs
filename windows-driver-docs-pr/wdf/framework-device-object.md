---
title: Framework Device Object
description: Framework Device Object
keywords:
- UMDF objects WDK , device objects
- framework objects WDK UMDF , device objects
- device objects WDK UMDF
- IWDFDevice
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Framework Device Object


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework device object is exposed to drivers by the [IWDFDevice](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdevice) interface. The framework device object is the framework representation of the device on the system. Each device object has a parent driver object.

When a new device arrives in the system, the framework calls the [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method to notify the driver of the arrival and passes the [IWDFDriver](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdriver) and [IWDFDeviceInitialize](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize) interfaces in the call. The driver can call methods of the IWDFDeviceInitialize interface to initialize the new device. For example, the driver calls the [**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore) method to query for the device information that is provided as part of device installation. The driver can then call the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method to configure and create the device object.

When drivers create a framework device object, they can register their [IPnpCallback](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallback), [IPnpCallbackSelfManagedIo](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackselfmanagedio), [IPnpCallbackHardware](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ipnpcallbackhardware), [IFileCallbackCleanup](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ifilecallbackcleanup), and [IFileCallbackClose](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-ifilecallbackclose) interfaces. The framework then notifies the driver when file cleanup and close and Plug and Play (PnP) and power management (PM) events occur. For more information about supporting PnP and PM, see [PnP and Power Management in UMDF-based Drivers](pnp-and-power-management-in-umdf-drivers.md).

 

