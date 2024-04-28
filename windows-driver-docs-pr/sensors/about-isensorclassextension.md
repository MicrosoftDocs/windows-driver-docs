---
title: About ISensorClassExtension
description: About ISensorClassExtension
ms.date: 07/20/2018
---

# About ISensorClassExtension


A sensor driver uses ISensorClassExtension to initialize and uninitialize the sensor class extension, raise events, process WPD input/output control codes (IOCTLs), and correctly close UMDF file handles.

## Methods to Manage Object Lifetime

To initialize the class extension, a PnP-based hardware sensor driver calls [**ISensorClassExtension::Initialize**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-initialize) when it is called by UMDF in [**IPnpCallbackHardware::OnPrepareHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onpreparehardware). This step provides the class extension object with pointers to the driver's main class and to the class that implements the callback interface to handle events that are raised by the class extension object. When the driver is called by UMDF in [**IPnpCallbackHardware::OnReleaseHardware**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ipnpcallbackhardware-onreleasehardware), it should call [**ISensorClassExtension::Uninitialize**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-uninitialize) and then release the class extension object. Note that some types of sensors may need to initialize and uninitialize the class extension at different times.

## Methods to Raise Events

The driver can raise various kinds of sensor events (usually that contain sensor data) by calling [**ISensorClassExtension::PostEvent**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-postevent) and state-information events by calling [**ISensorClassExtension::PostStateChange**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-poststatechange). For more information about how events work in sensor drivers, see [About Sensor Driver Events](about-sensor-driver-events.md).

## Methods to Manage IOCTLs and Handles

Sensor drivers forward two kinds of UMDF calls to the class extension:

-   Requests to process I/O control codes that are received through [**IQueueCallbackDeviceIoControl::OnDeviceIoControl**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iqueuecallbackdeviceiocontrol-ondeviceiocontrol). To forward an I/O request to the class extension for processing, the driver must call [**ISensorClassExtension::ProcessIoControl**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-processiocontrol).

-   Notifications about clients closing file handles that are received through [**IFileCallbackCleanup::OnCleanupFile**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-ifilecallbackcleanup-oncleanupfile). To forward an I/O request cancellation, the driver must call [**ISensorClassExtension::CleanupFile**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensorclassextension-cleanupfile).

 

