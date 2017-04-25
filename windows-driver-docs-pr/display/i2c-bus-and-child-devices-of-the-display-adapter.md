---
title: I2C Bus and Child Devices of the Display Adapter
description: I2C Bus and Child Devices of the Display Adapter
ms.assetid: bfa81f2d-dc35-4430-9117-4706a446058c
keywords:
- video miniport drivers WDK Windows 2000 , I2C
- I2C WDK video miniport
- child devices WDK video miniport
- I2CRead
- I2CWrite
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# I2C Bus and Child Devices of the Display Adapter


## <span id="ddk_i2c_bus_and_child_devices_of_the_display_adapter_gg"></span><span id="DDK_I2C_BUS_AND_CHILD_DEVICES_OF_THE_DISPLAY_ADAPTER_GG"></span>


Display adapters typically communicate with child devices over the I²C bus. For example, a monitor is a child device of the display adapter, and the display adapter can read a monitor's capability information over the I2C bus, which is built into all standard monitor cables.

The I²C bus has only two wires: the serial clock line and the serial data line. Data is read from and written to the lines one bit at a time. Reading and writing data bits to the I²C lines on the display adapter is hardware dependent, so the vendor-supplied video miniport driver must provide the functions that instruct the display adapter to read and write the individual bits.

The following functions, implemented by the video miniport driver, read and write individual data bits to the I²C serial clock and data lines:

[*ReadClockLine*](https://msdn.microsoft.com/library/windows/hardware/ff569230)

[*WriteClockLine*](https://msdn.microsoft.com/library/windows/hardware/ff570607)

[*ReadDataLine*](https://msdn.microsoft.com/library/windows/hardware/ff569231)

[*WriteDataLine*](https://msdn.microsoft.com/library/windows/hardware/ff570609)

The I²C specification defines a protocol for initiating I²C communication, reading and writing bytes over the I²C data line and terminating I²C communication. The system-supplied video port driver provides the following functions that implement that protocol.

[**I2CStart**](https://msdn.microsoft.com/library/windows/hardware/ff567375)

[**I2CRead**](https://msdn.microsoft.com/library/windows/hardware/ff567372)

[**I2CWrite**](https://msdn.microsoft.com/library/windows/hardware/ff567378)

[**I2CStop**](https://msdn.microsoft.com/library/windows/hardware/ff567376)

Each of the functions (implemented by the video port driver) in the preceding list requires assistance from the video miniport driver. For example, the **I2CRead** function reads a sequence of bytes over the I²C data line, but reading each byte requires reading eight individual bits, a task that only the video miniport driver can do. The **I2CRead** function can obtain assistance from the video miniport driver because it receives pointers (in an *I2CCallbacks* structure) to the four I²C functions implemented by the video miniport driver (*ReadClockLine*, *WriteClockLine*, *ReadDataLine*, and *WriteDataLine*). Similarly, **I2CStart**, **I2CRead**, and **I2CWrite** each receive an *I2CCallbacks* structure that contains pointers to all four of the video miniport driver's I²C functions.

The *HwVidGetChildDescriptor* function, implemented by the video miniport driver, is responsible for reading the Enhanced Display Identification Data (EDID) structure from a particular monitor and returning the EDID to the video port driver. *HwVidGetChildDescriptor* can get assistance from the video port driver by calling [**VideoPortDDCMonitorHelper**](https://msdn.microsoft.com/library/windows/hardware/ff570290), which uses the I²C bus to read a monitor's EDID according to the Display Data Channel (DDC) standard. However, when **VideoPortDDCMonitorHelper** needs to read and write individual bits to the I²C clock and data lines, it must call back into the video miniport driver for assistance. Therefore, *HwVidChildDescriptor* passes an *I2CCallbacks* structure (which contains pointers to *ReadClockLine*, *WriteClockLine*, *ReadDataLine*, and *WriteDataLine*) to **VideoPortDDCMonitorHelper**.

For more information about the I²C functions implemented by the video miniport driver and video port driver, see the following topics:

[I2C Functions](https://msdn.microsoft.com/library/windows/hardware/ff567383)

[I2C Functions Implemented by the Video Port Driver](https://msdn.microsoft.com/library/windows/hardware/ff567384)

For an overview of all video miniport driver functions and how those functions are registered, see [Video Miniport Driver Functions](https://msdn.microsoft.com/library/windows/hardware/ff570512).

For details on the I²C bus, see the I²C Bus Specification published by Philips Semiconductors.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20I2C%20Bus%20and%20Child%20Devices%20of%20the%20Display%20Adapter%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




