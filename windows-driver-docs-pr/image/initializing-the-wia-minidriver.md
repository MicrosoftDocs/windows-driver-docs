---
title: Initializing the WIA Minidriver
description: Initializing the WIA Minidriver
ms.date: 04/20/2017
---

# Initializing the WIA Minidriver





The first step in implementing the [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv) is to initialize the minidriver and create a hierarchical tree of driver items. To do this, the WIA service calls the [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) method each time a client application intends to use the device. If two or more applications are simultaneously using the device, the WIA service calls this method for each application. In this method, the minidriver typically does the following:

1.  Initializes parameters passed in from the WIA service.

2.  Saves the STI device interface pointed to by *pStiDevice.* This is done so that the [**IStiDevice::LockDevice**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-lockdevice) and [**IStiDevice::UnLockDevice**](/windows-hardware/drivers/ddi/sti/nf-sti-istidevice-unlockdevice) methods can be used to lock or unlock the WIA device.

3.  Caches *bstrDeviceID* and *bstrRootFullItemName* in member variables so that they can be used by other methods.

4.  Opens a handle to the device. (This step is recommended for nonshared ports such as USB, SCSI, and 1394.)

5.  Builds the item tree, as described in [Creating the WIA Driver Item Tree](creating-the-wia-driver-item-tree.md).

The **IWiaMiniDrv::drvInitializeWia** method also can be used to create and initialize dynamic arrays and structures that the driver uses. For example, an array of commands and events the driver supports can be created for later use by the [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) method.

**Note**   The [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) method might be called before **IWiaMiniDrv::drvInitializeWia** is called. This can happen when the WIA service needs to query for event information before an application exists to use the device. The **IWiaMiniDrv::drvInitializeWia** method is called only when an application signals its intent to use the device.

 

### Keeping Track of Application Connections

As stated previously, when an application intends to communicate with a WIA device, the WIA service calls the appropriate driver's [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) method. When the application is finished with the device and releases all WIA references to it, the WIA service calls the appropriate driver's [**IWiaMiniDrv::drvUnInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvuninitializewia) method. Note that WIA supports multiple, simultaneous application connections. This means that two or more applications can request a WIA interface associated with the same device. It does not mean, though, that the driver must handle simultaneous requests; the WIA service ensures that only one request is sent to the driver at a time. However, the WIA service can call the **IWiaMiniDrv::drvInitializeWia** method multiple times before it calls the **IWiaMiniDrv::drvUnInitializeWia** method.

Why is this information useful? Often there are resources that drivers might need when applications are using them, such as the WIA driver item tree, image filtering libraries, and others. Because these resources can take up a large amount of memory, it is best to unload them when they are not needed.

**Note**   The **IWiaMiniDrv::drvInitializeWia** and **IWiaMiniDrv::drvUnInitializeWia** methods are used to inform drivers of application connections only. The WIA service can call other driver methods without first calling **IWiaMiniDrv::drvInitializeWia**, which means that the WIA service does not necessarily call **IWiaMiniDrv::drvUnInitializeWia** when it is done. The methods called are informational methods that do not require WIA items, such as [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) and [**IWiaMiniDrv::drvGetWiaFormatInfo**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo).

 

This section contains the following topics:

[Calling Order for Minidriver Functions](calling-order-for-minidriver-functions.md)

[Loading and Unloading a WIA Minidriver](loading-and-unloading-a-wia-minidriver.md)

[Connecting and Disconnecting a WIA Application](connecting-and-disconnecting-a-wia-application.md)

[Reporting WIA Minidriver Status](reporting-wia-minidriver-status.md)

 

