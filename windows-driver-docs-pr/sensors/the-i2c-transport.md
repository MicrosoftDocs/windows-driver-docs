---
title: I2C transport
description: I2C transport
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: A483FAA6-9FA6-4C91-B8D4-021DDBB9B869
---

# I2C transport


| Module                  | Class/Interface      |
|-------------------------|----------------------|
| AccelerometerDevice.cpp | CAccelerometerDevice |
| Adxl345.h               | N/A                  |

 

The I²C (Inter-IC) transport is a two-wire serial transport that was introduced by the Phillips Corporation for their consumer products. Sensors are one category of device that support this transport. Examples include:

-   ADXL345 accelerometer
-   HMC5883L compass
-   MS5611-01BA03 barometric pressure sensor
-   TMP100 temperature sensor

The two wires on the I2C bus correspond to a clock-line (SCL) and a serial data-line (SDA). For more information about the I2C transport, see to the I2C Bus Specification.

Sensors that support the I2C transport often support a set of registers. The master uses these registers to configure and control the slave device. For the ADXL345, the registers correspond to specific device properties, capabilities, or functionality. Some of the registers are read only; others are read/write. For example, register 0x2D (POWER\_CTL) lets the master set an auto-sleep mode on the sensor—this mode sets the device to a low power state after a certain period of inactivity. (For more information about the ADXL345s registers and commands see to the manufacturer's datasheet.)

The sample driver has a method that writes values to a given register (**CAcclelerometerDevice::WriteRegister**) and one that reads values from a register (**CAccelerometerDevicce::ReadRegister**). They take arguments that identify the register being written to (or read from), a pointer to the data being written or read, and a buffer length for the data buffer.

For example, the following sequence of **WriteRegister** and **ReadRegister** calls takes place during driver and device initialization. The driver invokes **WriteRegister** to configure the sensor. If the operation succeeds, **ReadRegister** returns contents that reflect the previously written values.

Method
Register
Data
Purpose
**CAccelerometerDevice::WriteRegister**
0x2d
'\\0' (0x00)
Reset the sensor’s power-control register and place the device in standby mode.
**CAccelerometerDevice::ReadRegister**
0x2d
'\\0' (0x00)
The device has been placed in standby mode.
**CAccelerometerDevice::WriteRegister**
0x31
'\\v' (0x0b)
Set the device in full-resolution mode with a range along each axis of +/- 16G.
**CAccelerometerDevice::ReadRegister**
0x31
'\\v' (0x0b)
Full-resolution has been set with maximum range (+/- 16G).
. . .
. . .
. . .
 

The complete register map for the accelerometer is in Table 16 of the device's data sheet. The sample driver supports a subset of these registers. These supported values are found within the Adxl345.h header file:

```ManagedCPlusPlus
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20I2C%20transport%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




