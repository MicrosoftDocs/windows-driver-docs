---
title: About ISensorClassExtension
description: About ISensorClassExtension
MS-HAID:
- 'Sensor\_DG\_Overview\_02c75653-460f-4a62-af75-fd070b5f3acd.xml'
- 'sensors.about\_isensorclassextension'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 1f55f28a-796a-40e5-9995-e6a28761b9a4
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20About%20ISensorClassExtension%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




