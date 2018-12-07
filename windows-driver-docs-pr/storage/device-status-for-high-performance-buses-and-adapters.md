---
title: Device Status for High-Performance Buses and Adapters
description: Device Status for High-Performance Buses and Adapters
ms.assetid: 7a6b8048-d9aa-4169-aac5-150dc805f61b
keywords:
- Storport drivers WDK , errors
- errors WDK Storport
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Device Status for High-Performance Buses and Adapters


## <span id="ddk_device_status_for_high_performance_buses_and_adapters_kg"></span><span id="DDK_DEVICE_STATUS_FOR_HIGH_PERFORMANCE_BUSES_AND_ADAPTERS_KG"></span>


The Storport driver has been designed to report some transport-specific errors and conditions that the SCSI Port driver does not report. For example, Storport reports error conditions that occur on a fibre channel, such as "link-down" errors, where the connection between a fibre channel host bus adapter (HBA) is lost or the fibre channel HBA ceases to transmit signals. Storport supports fibre channel's extended link service and is capable of reporting registered state change notifications (RSCNs) and errors associated with fibre channel's loop initialization protocol (LIP).

 

 




