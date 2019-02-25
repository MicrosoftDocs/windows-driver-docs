---
title: Accelerometer object
description: The sample driver treats the accelerometer as an object that’s represented by the CAccelerometerDevice class.
ms.assetid: D8E227E1-FFB5-4F4B-A981-6BD05C8FFAF2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accelerometer object


| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |
| SensorDdi.cpp           | CSensorDdi           |

 

The sample driver treats the accelerometer as an object that’s represented by the CAccelerometerDevice class. This object is declared in the header file AccelerometerDevice.h; and, is defined in AccelerometerDevice.cpp. If you were to extend this driver to support another sensor, in addition to the ADXL345, you'll create a similarly named header and source file that corresponded to your new device (for example, CompassDevice.h and CompassDevice.cpp). If your driver supported a single sensor, replace the existing header and source files.

The accelerometer object supports the methods that:

-   Initialize the accelerometer
    -   Configure the hardware
    -   Connect the data-notification interrupt
    -   Write data to the device's register interface
    -   Read data from the device’s register interface
    -   Support user-mode interrupts
    -   Retrieve the supported data fields
    -   Retrieve the supported events
    -   Retrieve the supported properties
    -   Set the report interval
    -   Set the device state
    -   Set the default property values

## Initialization methods

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |

 

The object supports these methods:

| Method                                      | Description                                                                                                                                                                                                                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CAccelerometerDevice::InitializeDevice**  | Retrieves the device configuration settings from ACPI, and then, retrieves the resource-hub connection IDs. This method is invoked by the **CSensorDdi::Initialize** method after the latter has initialized the sensor driver interface, the client manager, and the report manager. |
| **CAccelerometerDevice::ConfigureHardware** | Allocates the read and write buffers and sets the read and writer registers.                                                                                                                                                                                                          |
| **CAccelerometerDevice::ConnectInterrupt**  | Sreates a WUDF device interrupt. It does this by configuring a WUDF\_INTERRUPT\_CONFIG data structure and then invoking the **IWDFDevice3::CreateInterrupt** method.                                                                                                                  |

 

For the complete sequence of initialization methods, refer to the [Driver initialization](driver-initialization.md) section in this guide.

## Device-register read- and write-operations

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |

 

The accelerometer object supports both a read- and a write-operation. These operations let the driver get the current value of a given register, or, to write a new value to a register. The **CAccelerometerDevice::ReadRegister** corresponds to the read operation and the **CAccelerometerDevice::WriteRegister** corresponds to the write operation. These operations are invoked:

-   At driver initialization time when the **CAccelereometerDevice::ConfigureHardware** method is invoked to configure the device and place it in standby mode.
-   When the count of connected clients goes to zero and the **CAccelerometerDevice::SetDeviceStateStandby** method is invoked.
-   When the GPIO line is asserted by the ADXL345 and the **CAccelerometerDevice::OnInterruptIsr** method is invoked.

## Supporting user-mode interrupts

This section explains how the sample driver gets the data for the ADXL345.

The accelerometer object supports user-mode interrupts with the **CAccelerometerDevice::OnInterruptWorkItem** method. When the user-mode framework invokes this method, it in turn, invokes **CAccelerometerDevice::RequestData**. This method, in turn, invokes **CAccelerometerDevice::ReadRegister** to read the contents of register 0x32 through register 0x37 on the ADXL345. These six registers contain the current readings, in G-force, along the X-, Y-, and Z-axis.

| Register | Contents                              |
|----------|---------------------------------------|
| 0x32     | Low-order byte of the X-axis reading  |
| 0x33     | High-order byte of the X-axis reading |
| 0x34     | Low-order byte of the Y-axis reading  |
| 0x35     | High-order byte of the Y-axis reading |
| 0x36     | Low-order byte of the Z-axis reading  |
| 0x37     | High-order byte of the Z-axis reading |

 

The code in the **CAccelerometerDevice::RequestData** method packages the register contents for each axis into a variable of type SHORT (xRaw, yRaw, and zRaw) and then applies a scale factor of .00390625. (The scale factor is a result of dividing the range of acceleration values, 32 in this case (because +/- 16G is supported), by the number that can be represented in 13 bits (2^13)--which is the selected resolution.

```cpp
// Get the data values as doubles
SHORT xRaw, yRaw, zRaw;
DOUBLE xAccel, yAccel, zAccel;
const DOUBLE scaleFactor = 1/256.0F;

xRaw = (SHORT)((m_pDataBuffer[1] << 8) | m_pDataBuffer[0]);
yRaw = (SHORT)((m_pDataBuffer[3] << 8) | m_pDataBuffer[2]);
zRaw = (SHORT)((m_pDataBuffer[5] << 8) | m_pDataBuffer[4]);

xAccel = (DOUBLE)xRaw * scaleFactor;
yAccel = (DOUBLE)yRaw * scaleFactor;
zAccel = (DOUBLE)zRaw * scaleFactor;
```

After the driver computes the values, it packages each one into a **PROPVARIANT** structure and invokes the **CAccelerometerDevice::AddDataField** method to update the value for each axis.

Note that the supported acceleration range (+/- 16G) and the resolution were set using register 0x31 in the ADXL345. This occurs in the *g\_ConfigurationSettings* array found at the beginning of AccelerometerDevice.cpp:

```cpp
// +-16g, 13-bit resolution
{ ADXL345_DATA_FORMAT,
   ADXL345_DATA_FORMAT_FULL_RES |
   ADXL345_DATA_FORMAT_JUSTIFY_RIGHT |
   ADXL345_DATA_FORMAT_RANGE_16G },
```

## Supporting the report interval

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |

 

The sensor platform supports report intervals and lets applications set them to values within a defined range. The minimum and default report intervals for the sample driver are defined in the file Adxl345.h.

```cpp
const ULONG ACCELEROMETER_MIN_REPORT_INTERVAL              = 10;
const ULONG DEFAULT_ACCELEROMETER_CURRENT_REPORT_INTERVAL  = 100;
```

The sample driver limits the minimum report interval to 10 milliseconds and the default interval to 100 milliseconds.

A sensor driver uses the report interval to determine when to raise event notifications. If the change-sensitivity has not been exceeded, the driver waits for the current interval and then raises a data event to give connected apps the current data reading. (If the change sensitivity has been exceeded, this overrides the report interval and the driver will immediately raise a data event.)

A Windows app can set the interval for an accelerometer by invoking the **Accelerometer.ReportInterval** property. When an app invokes this property, the driver's **CAccelerometerDevice::SetReportInterval** method is called to pass the requested interval to the device's firmware.

Setting the report interval translates into three consecutive write operations to the ADXL registers. The first write operation disables interrupts while we modify the data rate on the device:

```cpp
// Disable interrupts while data rate is modified
pWriteBuffer[0] = 0;
hr = WriteRegister(ADXL345_INT_ENABLE, pWriteBuffer, 1);
The second write operation updates the new data rate:

// Update the data rate.
pWriteBuffer[0] = newDataRate.RateCode;
hr = WriteRegister(ADXL345_BW_RATE, pWriteBuffer, 1);

The third write operation re-enables interrupts:

// Reenable interrupts
pWriteBuffer[0] = ADXL345_INT_ACTIVITY;
hr = WriteRegister(ADXL345_INT_ENABLE, pWriteBuffer, 1);
```

## Supporting the device mode

| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |

 

The sample device supports three device modes:

-   Measurement mode with eventing
-   Measurement mode without eventing
-   Standby mode

Measurement mode results in data collection; standby mode results in no data being returned by the device. When measurement mode with eventing is set, the driver lets apps register to receive notifications when data arrives from the device. When measurement mode without eventing is set, apps must poll the device for the most recent data.

Three methods in the source file correspond to each of the three modes: **SetDeviceStateEventing, SetDeviceStatePolling**, and **SetDeviceStateStandby**. They are invoked from within **SetDataUpdateMode**.

## Measurement mode without eventing

When measurement mode without eventing is set, Windows apps get the most recent sensor reading by invoking **Accelerometer.GetCurrentReading**.

The driver sets this mode during initialization and, when returning from standby mode. It uses two write operations. The first operation disables interrupts:

```cpp
pBuffer[0] = 0;
hr = WriteRegister(ADXL345_INT_ENABLE, pBuffer, 1);
```

The second operation places the device in measurement mode:

```cpp
pBuffer[0] = ADXL345_POWER_CTL_MEASURE;
hr = WriteRegister(ADXL345_POWER_CTL, pBuffer, 1);
```

## Measurement mode with eventing

When measurement mode with eventing is set, Windows apps can receive data updates from the driver by registering an event handler for the **Accelerometer.ReadingChanged** event.

The driver sets this mode during initialization (and, when it’s returning from standby mode). The driver sets this mode with two write operations. The first operation ensures that the device is placed in measurement mode:

```cpp
pBuffer[0] = ADXL345_POWER_CTL_MEASURE;
hr = WriteRegister(ADXL345_POWER_CTL, pBuffer, 1);
```

And, the second operation enables the activity-detection interrupt:

```cpp
 pBuffer[0] = ADXL345_INT_ACTIVITY;
 hr = WriteRegister(ADXL345_INT_ENABLE, pBuffer, 1);
```

## Supporting standby mode

The driver sets this mode when the client subscription count goes to 0. It uses two write operations and a read operation. The first write operation ensures interrupts are disabled:

```cpp
pBuffer[0] = 0;
hr = WriteRegister(ADXL345_INT_ENABLE, pBuffer, 1);
```

Next, a read operation to clear any outstanding interrupts:

```cpp
hr = ReadRegister(ADXL345_INT_SOURCE, pBuffer, 1, 0);
```

Then, a second write operation places the device in standby mode:

```cpp
pBuffer[0] = ADXL345_POWER_CTL_STANDBY;
hr = WriteRegister(ADXL345_POWER_CTL, pBuffer, 1);
```

 

 




