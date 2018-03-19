---
title: About ISensorClassExtension
author: windows-driver-content
description: About ISensorClassExtension
ms.assetid: 1f55f28a-796a-40e5-9995-e6a28761b9a4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# About ISensorClassExtension


A sensor driver uses ISensorClassExtension to initialize and unitialize the sensor class extension, raise events, process WPD input/output control codes (IOCTLs), and correctly close UMDF file handles.

### Methods to Manage Object Lifetime

To initialize the class extension, a PnP-based hardware sensor driver calls [**ISensorClassExtension::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff545514) when it is called by UMDF in [**IPnpCallbackHardware::OnPrepareHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556766). This step provides the class extension object with pointers to the driver's main class and to the class that implements the callback interface to handle events that are raised by the class extension object. When the driver is called by UMDF in [**IPnpCallbackHardware::OnReleaseHardware**](https://msdn.microsoft.com/library/windows/hardware/ff556768), it should call [**ISensorClassExtension::Uninitialize**](https://msdn.microsoft.com/library/windows/hardware/ff545547) and then release the class extension object. Note that some types of sensors may need to initialize and uninitialize the class extension at different times.

### Methods to Raise Events

The driver can raise various kinds of sensor events (usually that contain sensor data) by calling [**ISensorClassExtension::PostEvent**](https://msdn.microsoft.com/library/windows/hardware/ff545519) and state-information events by calling [**ISensorClassExtension::PostStateChange**](https://msdn.microsoft.com/library/windows/hardware/ff545523). For more information about how events work in sensor drivers, see [About Sensor Driver Events](about-sensor-driver-events.md).

### Methods to Manage IOCTLs and Handles

Sensor drivers forward two kinds of UMDF calls to the class extension:

-   Requests to process I/O control codes that are received through [**IQueueCallbackDeviceIoControl::OnDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff556854). To forward an I/O request to the class extension for processing, the driver must call [**ISensorClassExtension::ProcessIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff545536).

-   Notifications about clients closing file handles that are received through [**IFileCallbackCleanup::OnCleanupFile**](https://msdn.microsoft.com/library/windows/hardware/ff554905). To forward an I/O request cancellation, the driver must call [**ISensorClassExtension::CleanupFile**](https://msdn.microsoft.com/library/windows/hardware/ff545512).

 

 




