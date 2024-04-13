---
title: Install a WIA Scanner Driver with WSD
description: Provides information about installing a WIA scanner driver with the *WSDScan.sys* kernel-mode driver.
ms.date: 12/14/2023
---

# Install a WIA scanner driver with WSD

To install a WIA scanner driver with WSD, you should use the *WSDScan.sys* kernel-mode driver. During **IRP_MN_START_DEVICE**, *WSDScan.sys* reads the **PKEY_PNPX_ID** device property and saves it to the registry.

 The device property is written to a device key that is created in the registry for the imaging device that is being installed and to the **CreateFileName** WIA registry value (which is described in [INF Files for WIA Devices](inf-files-for-wia-devices.md)).

This value is returned by the WIA service to the WIA minidriver when the [**IStiDeviceControl::GetMyDevicePortName**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istidevicecontrol-getmydeviceportname) call is made during the [**IStiUSD::Initialize**](/windows-hardware/drivers/ddi/stiusd/nf-stiusd-istiusd-initialize) method.

A WIA minidriver for a web service scanner that is using *WSDScan.sys* has its **CreateFileName** value initialized when the device is installed. To initialize this value, the INF file for the WIA minidriver must reference **STI.WSDSection** and **STI.WSDSection.Services** from the *Sti.inf* file in the **Install** and **Services** sections of the minidriver INF file, as shown in [Sample INF File for a Web Services Scanner](sample-inf-file-for-a-web-services-scanner.md).
