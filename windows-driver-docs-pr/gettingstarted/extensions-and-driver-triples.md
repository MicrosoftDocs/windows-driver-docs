---
title: KMDF extensions and driver triples
description: In this topic, we discuss class-based extensions to the Kernel Mode Driver Framework (KMDF). Before you read this topic, you should understand the ideas presented in Minidrivers and driver pairs and KMDF as a Generic Driver Pair Model.
ms.assetid: 49207485-AFDF-4E84-B39C-A14FC7E2CF60
---

# KMDF extensions and driver triples


In this topic, we discuss class-based extensions to the Kernel Mode Driver Framework (KMDF). Before you read this topic, you should understand the ideas presented in [Minidrivers and driver pairs](minidrivers-and-driver-pairs.md) and [KMDF as a Generic Driver Pair Model](kmdf-as-a-generic-pair-model.md).

For some device classes, Microsoft provides KMDF extensions that further reduce the amount of processing that must be performed by KMDF drivers. A driver that uses a class-based KMDF extension has these three pieces, which we call a *driver triple*.

-   The Framework, which handles tasks common to most all drivers
-   The class-based framework extension, which handles tasks that are specific to a particular class of devices
-   The KMDF driver, which handles tasks that are specific to a particular device.

The three drivers in a driver triple (KMDF driver, device-class KMDF extension, Framework) combine to form a single WDM driver.

An example of a device-class KMDF extension is SpbCx.sys, which is the KMDF extension for the Simple Peripheral Bus (SPB) device class. The SPB class includes synchronous serial buses such as I2C and SPI. A driver triple for an I2C bus controller would look like this:

-   The Framework handles general tasks that are common to most all drivers.
-   SpbCx.sys handles tasks that are specific to the SPB bus class. These are tasks that are common to all SPB busses.
-   The KMDF driver handles tasks that are specific to an I2C bus. Let's call this driver MyI2CBusDriver.sys.

![kmdf driver triple extension](images/kmdfdrivertriple.png)

The three drivers in the driver triple (MyI2CBusDriver.sys, SpbCx.sys, Wdf01000.sys) combine to form a single WDM driver that serves as the function driver for the I2C bus controller. Wdf01000.sys (the Framework) owns the dispatch table for this driver, so when someone sends an IRP to the driver triple, it goes to the wdf01000.sys. If the wdf01000.sys can handle the IRP by itself, SpbCx.sys and MyI2CBusDriver.sys are not involved. If wdf01000.sys cannot handle the IRP by itself, it gets help by calling an event handler in SbpCx.sys.

Here are some examples of event handlers that might be implemented by MyI2CBusDriver.sys:

-   EvtSpbControllerLock
-   EvtSpbIoRead
-   EvtSpbIoSequence

Here are some examples of event handlers that are implemented by SpbCx.sys

-   EvtIoRead

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[wdkgetstart\wdkgetstart]:%20KMDF%20extensions%20and%20driver%20triples%20%20RELEASE:%20%281/20/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




