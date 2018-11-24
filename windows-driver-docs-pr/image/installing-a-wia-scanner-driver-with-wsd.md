---
title: Installing a WIA Scanner Driver with WSD
description: Installing a WIA Scanner Driver with WSD
ms.assetid: 7dc125cb-0f20-4d3d-8124-df556a9644d7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a WIA Scanner Driver with WSD


To install a WIA scanner driver with WSD, you should use the *WSDScan.sys* kernel-mode driver, which is provided as part of Windows Vista. During IRP\_MN\_START\_DEVICE, *WSDScan.sys* reads the PKEY\_PNPX\_ID device property and saves it to the registry. The device property is written to a device key that is created in the registry for the imaging device that is being installed and to the **CreateFileName** WIA registry value (which is described in [INF Files for WIA Devices](inf-files-for-wia-devices.md)). This value is returned by the WIA service to the WIA minidriver when the [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) call is made during the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method.

A WIA minidriver for a web service scanner that is using *WSDScan.sys* has its **CreateFileName** value initialized when the device is installed. To initialize this value, the INF file for the WIA minidriver must reference **STI.WSDSection** and **STI.WSDSection.Services** from the *Sti.inf* file in the **Install** and **Services** sections of the minidriver INF file, as shown in [Sample INF File for a Web Services Scanner](sample-inf-file-for-a-web-services-scanner.md).

 

 




