---
title: Adding a Device
description: Adding a Device
keywords:
- User-Mode Driver Framework WDK , adding devices
- UMDF WDK , adding devices
- user-mode drivers WDK UMDF , adding devices
- installing devices WDK , UMDF
- adding devices WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Adding a Device


[!include[UMDF 1 Deprecation](../includes/umdf-1-deprecation.md)]

The framework adds a device object for each device loaded in the driver host process. To add the device, the framework calls the driver's [**IDriverEntry::OnDeviceAdd**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-idriverentry-ondeviceadd) method and passes the [IWDFDriver](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdriver) and [IWDFDeviceInitialize](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize) interfaces in the call. The supplied **IWDFDeviceInitialize** interface is only valid before the driver calls [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice). The driver can call the following methods of **IWDFDeviceInitialize** to perform the following operations:

-   The driver calls the [**IWDFDeviceInitialize::RetrieveDevicePropertyStore**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-retrievedevicepropertystore) method to retrieve the [IWDFNamedPropertyStore](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfnamedpropertystore) interface for the device property store. The driver can use **IWDFNamedPropertyStore** to retrieve and set properties for the device.

-   The driver calls the [**IWDFDeviceInitialize::SetLockingConstraint**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-setlockingconstraint) method to specify how its callback functions are called by the framework.

-   The driver calls the [**IWDFDeviceInitialize::SetFilter**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdeviceinitialize-setfilter) method to enable the device as a filter device.

After the driver uses [IWDFDeviceInitialize](/windows-hardware/drivers/ddi/wudfddi/nn-wudfddi-iwdfdeviceinitialize) to initialize the device, the driver passes a pointer to **IWDFDeviceInitialize** in a call to the [**IWDFDriver::CreateDevice**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdriver-createdevice) method to create a [UMDF device object](framework-device-object.md) for the device. After the framework device object is created, the driver makes calls to the [**IWDFDevice::CreateIoQueue**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createioqueue) method to create read and write I/O queues. In these **IWDFDevice::CreateIoQueue** calls, the driver must identify how it receives requests from the I/O queue. For more information, see [Configuring Dispatch Mode for an I/O Queue](configuring-dispatch-mode-for-an-i-o-queue.md).

 

