---
title: Defining the accelerometer object
description: The sample driver treats the accelerometer as an object.
ms.assetid: EA30C9E6-3DA1-44C8-89DA-6FA21BE3B226
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Defining the accelerometer object


The sample driver treats the accelerometer as an object.

## Defining the accelerometer object


This object is declared in the header file AccelerometerDevice.h; and, it's defined in the source file AccelerometerDevice.cpp. If you were to extend this driver to support additional sensors, you would create similar header and source files that corresponded to these additional devices. (If your driver supported a single sensor, you would replace this header and source with files corresponding to your device and its capabilities and requirements.)

The accelerometer object supports the methods that:

-   Initialize the sensor object
-   Configure the hardware
-   Connect the data notification interrupt
-   Set the report interval
-   Set the device state
-   Write data to the device's register interface

### Initializing the sensor object

The object supports an **Initialize** method that retrieves the device configuration settings from ACPI, and then, retrieves the resource-hub connection IDs.

### Configuring the hardware

The object supports a **ConfigureHardware** method which allocates the read and write buffers and sets the read and writer registers.

### Configuring the data-notification interrupt

The object supports a **ConnectInterrupt** method that creates a WUDF device interrupt. It does this by configuring a **WUDF\_INTERRUPT\_CONFIG** data structure and then invoking the **IWDFDevice3::CreateInterrupt** method.

### Supporting the report interval

The sensor platform supports the notion of a report interval and allows applications to set this interval to values within a defined range. A Windows app can set the interval for an Accelerometer by invoking the **Accelerometer.ReportInterval** property. When an app invokes this property, the driver's **SetReportInterval** method is called to pass the requested interval to the device's firmware.

The primary component responsible for the report interval is the client manager. The supporting code is found in the module ClientManager.cpp. The client manager maintains a list of connected clients, their subscription state, desired report interval, and desired change sensitivities. Whenever any of these change, the client manager computes the data update mode and lowest report interval and change sensitivity values. For more information about the report interval and change sensitivity, see the [Filtering data](filtering-data.md) topic.

The minimum and default report intervals for the ADXL345 are defined in the file Adxl345.h. The sample driver limits the minimum report interval to 10 milliseconds and the default interval to 100 milliseconds.

### Supporting the device state

The sample device supports three modes:

-   Measurement mode with eventing
-   Measurement mode without eventing
-   Standby mode

Measurement mode is the mode that results in data collection; standby mode (as the name implies) results in no data being returned by the device. When measurement mode with eventing is set, the driver allows apps to register to receive notifications each time data arrives from the device. When measurement mode without eventing is set, apps must poll the device for the most recent data.

There are three methods in the source file that correspond to each of the three modes: **SetDeviceStateEventing**, **SetDeviceStatePolling**, and **SetDeviceStateStandby**. These methods are invoked from within **SetDataUpdateMode**.

### Writing data to the device's register interface

The ADXL345 is controlled by writing values to its registers. For example, the driver enables interrupts by setting the appropriate bit in the **INT\_ENABLE** register. And, a specific interrupt pin is chosen when the driver writes a value to the **INT\_MAP** register.

The driver supports a **WriteRegister** method that it invokes internally when writing data to the sensor registers. The first argument to this method specifies which register is being written to, the second arguments points to the data buffer and the third argument specifies the size of the buffer.

The complete register map for the accelerometer is found within table 16 of the device's data sheet. The sample driver supports a subset of the values found in the register map. These supported values are found within the Adxl345.h header file:

```cpp
//
// Register interface
//

#define ADXL345_DEVID                       0x00
#define ADXL345_THRESH_TAP                  0x1D
#define ADXL345_OFFSET_X                    0x1E
#define ADXL345_OFFSET_Y                    0x1F
#define ADXL345_OFFSET_Z                    0x20
#define ADXL345_DURATION_TAP                0x21
#define ADXL345_LATENT_TAP                  0x22
#define ADXL345_WINDOW_TAP                  0x23
#define ADXL345_THRESH_ACT                  0x24
#define ADXL345_THRESH_INACT                0x25
#define ADXL345_TIME_INACT                  0x26
#define ADXL345_ACT_INACT_CTL               0x27
#define ADXL345_THRESH_FF                   0x28
#define ADXL345_TIME_FF                     0x29
#define ADXL345_TAP_AXES                    0x2A
#define ADXL345_ACT_TAP_STATUS              0x2B
#define ADXL345_BW_RATE                     0x2C
#define ADXL345_POWER_CTL                   0x2D
#define ADXL345_INT_ENABLE                  0x2E
#define ADXL345_INT_MAP                     0x2F
#define ADXL345_INT_SOURCE                  0x30
#define ADXL345_DATA_FORMAT                 0x31
#define ADXL345_DATA_X0                     0x32
#define ADXL345_DATA_X1                     0x33
#define ADXL345_DATA_Y0                     0x34
#define ADXL345_DATA_Y1                     0x35
#define ADXL345_DATA_Z0                     0x36
#define ADXL345_DATA_Z1                     0x37
#define ADXL345_FIFO_CTL                    0x38
#define ADXL345_FIFO_STATUS                 0x39
```

## Related topics
[SpbAccelerometer driver sample](spbaccelerometer-driver-sample.md)



