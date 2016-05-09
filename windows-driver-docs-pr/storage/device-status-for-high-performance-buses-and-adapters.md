---
title: Device Status for High-Performance Buses and Adapters
author: windows-driver-content
description: Device Status for High-Performance Buses and Adapters
ms.assetid: 7a6b8048-d9aa-4169-aac5-150dc805f61b
keywords: ["Storport drivers WDK , errors", "errors WDK Storport"]
---

# Device Status for High-Performance Buses and Adapters


## <span id="ddk_device_status_for_high_performance_buses_and_adapters_kg"></span><span id="DDK_DEVICE_STATUS_FOR_HIGH_PERFORMANCE_BUSES_AND_ADAPTERS_KG"></span>


The Storport driver has been designed to report some transport-specific errors and conditions that the SCSI Port driver does not report. For example, Storport reports error conditions that occur on a fibre channel, such as "link-down" errors, where the connection between a fibre channel host bus adapter (HBA) is lost or the fibre channel HBA ceases to transmit signals. Storport supports fibre channel's extended link service and is capable of reporting registered state change notifications (RSCNs) and errors associated with fibre channel's loop initialization protocol (LIP).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Device%20Status%20for%20High-Performance%20Buses%20and%20Adapters%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


