---
title: Installing a WIA Scanner Driver with WSD
author: windows-driver-content
description: Installing a WIA Scanner Driver with WSD
MS-HAID:
- 'WIA\_wsd\_scan\_07ce4f98-9d85-4b88-8a22-a36230ab5af4.xml'
- 'image.installing\_a\_wia\_scanner\_driver\_with\_wsd'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7dc125cb-0f20-4d3d-8124-df556a9644d7
---

# Installing a WIA Scanner Driver with WSD


To install a WIA scanner driver with WSD, you should use the *WSDScan.sys* kernel-mode driver, which is provided as part of Windows Vista. During IRP\_MN\_START\_DEVICE, *WSDScan.sys* reads the PKEY\_PNPX\_ID device property and saves it to the registry. The device property is written to a device key that is created in the registry for the imaging device that is being installed and to the **CreateFileName** WIA registry value (which is described in [INF Files for WIA Devices](inf-files-for-wia-devices.md)). This value is returned by the WIA service to the WIA minidriver when the [**IStiDeviceControl::GetMyDevicePortName**](https://msdn.microsoft.com/library/windows/hardware/ff542944) call is made during the [**IStiUSD::Initialize**](https://msdn.microsoft.com/library/windows/hardware/ff543824) method.

A WIA minidriver for a web service scanner that is using *WSDScan.sys* has its **CreateFileName** value initialized when the device is installed. To initialize this value, the INF file for the WIA minidriver must reference **STI.WSDSection** and **STI.WSDSection.Services** from the *Sti.inf* file in the **Install** and **Services** sections of the minidriver INF file, as shown in [Sample INF File for a Web Services Scanner](sample-inf-file-for-a-web-services-scanner.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Installing%20a%20WIA%20Scanner%20Driver%20with%20WSD%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


