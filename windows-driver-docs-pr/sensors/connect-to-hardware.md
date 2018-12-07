---
title: Connect to hardware
description: This topic shows you how the sensor driver determines the assigned hardware resources and connects to the I2C driver controller.
ms.assetid: 88D9162B-2B99-4608-B31A-48B1810747A9
ms.date: 07/20/2018
ms.localizationpriority: medium
---

# Connect to hardware


This topic shows you how the sensor driver determines the assigned hardware resources, then connects to the I2C driver controller so that it can connect to the ADXL345 hardware.

The following sections will use code snippets from the sample driver that was developed for the ADXL345 accelerometer, as a test case for showing how to make your sensor driver connect to hardware. If you haven't already done so, navigate to the [ADXL345Acc sample](https://github.com/Microsoft/Windows-driver-samples/tree/1fbea08887e10e087c3f6bb0be8968e29e20cc84/sensors/ADXL345Acc) on GitHub, so that you can follow along with the explanations.

These code snippets highlight some of the important sections of the sensor driver files. But you must review all the driver files in their entirety, to get a good understanding of how the driver works, and to be able to figure out how to customize these files for your sensor.

## Prepare hardware resources


1. Click the *device.cpp* file to open it, then find the **OnPrepareHardware** function. Within that function, find the following code:
   ```cpp
   // Create WDFOBJECT for the sensor
    WDF_OBJECT_ATTRIBUTES sensorAttributes;
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&sensorAttributes, ADXL345AccDevice);
   ```

The preceding code creates a sensor object and assigns the appropriate device context to it.

2. Find the following code:
   ```cpp
   // Register sensor instance with clx
    SENSOROBJECT SensorInstance = NULL;
    NTSTATUS Status = SensorsCxSensorCreate(Device, &sensorAttributes, &SensorInstance);
   ```

The preceding code registers the sensor instance with the sensor class extension. A sensor instance is created instead of a device instance, to allow for the scenario where you have multiple sensors within the same chip.

3. Find the following code:
   ```cpp
   // Initialize sensor instance with clx
    SENSOR_CONFIG SensorConfig;
    SENSOR_CONFIG_INIT(&SensorConfig);
    SensorConfig.pEnumerationList = pAccDevice->m_pEnumerationProperties;
    Status = SensorsCxSensorInitialize(SensorInstance, &SensorConfig);
   ```

The preceding code uses the sensor class extension to initialize the sensor instance.

4. Find the following code:
   ```cpp
   Status = pAccDevice->ConfigureIoTarget(ResourcesRaw, ResourcesTranslated);
   ```

The preceding code configures an I/O target object for the sensor driver. An I/O target object enables the sensor driver to communicate with other drivers.

## Configure the device with default settings


Remember that D0 is the active state of the device. To put the device into D0 requires setting up this configuration in the registers of the device itself, and you will communicate with the device over I2C. You must hold the lock for this resource before performing a write or read.

Within the *device.cpp* file, find the **OnD0Entry** function and notice that it calls **PowerOn**, using the ADXL345 context to do the work of powering on the device. Within the **PowerOn** function, find the following code:
1.
```cpp
WdfWaitLockAcquire(m_I2CWaitLock, NULL);
```

The preceding code is used to acquire a lock for the I2C bus.

2. Find the following code:
   ```cpp
   // Write the default device configuration to the device
   For (DWORD i = 0; i < ARRAYSIZE(g_ConfigurationSettings); i++)
   {
       REGISTER_SETTING setting = g_ConfigurationSettings[i];
       Status = I2CSensorWriteRegister(m_I2CIoTarget, setting.Register, &setting.Value, sizeof(setting.Value));
       if (!NT_SUCCESS(Status))
       {
           TraceError("ACC %!FUNC! I2CSensorReadRegister from 0x%02x failed! %!STATUS!", setting.Register, Status);
           WdfWaitLockRelease(m_I2CWaitLock);
           return Status

       }
    }
   ```

The For-loop is used to write the default configuration settings to the device registers.

3. Find the following code:
   ```cpp
   // Release the I2C bus lock
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);

   InitPropVariantFromUInt32(SensorState_Idle, &(m_pSensorProperties->List[SENSOR_PROPERTY_STATE].Value));
   m_PoweredOn = true;
   ```

After the device is successfully configured, WdfWaitLockRelease is used to release the lock for the I2C bus.

4. Close the *device.cpp* file.
   ## Start the device activity


5. Click the *client.cpp* file to open it, and find the **OnStart** function.
6. Review the following code, which is used to acquire a lock on the sensor device:
   ```cpp
   WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
   ```

7. Find the following code:
   ```cpp
   // Set accelerometer to measurement mode
   REGISTER_SETTING RegisterSetting = { ADXL345_POWER_CTL, ADXL345_POWER_CTL_MEASURE };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &RegisterSetting.Value, sizeof(RegisterSetting.Value));
   ```

In the preceding code, the I2C connection is used to set the accelerometer to *measure mode* to make it ready for reading sensor values. See the *adxl345.h* header file for the definitions of ADXL345\_POWER\_CTL, ADXL345\_POWER\_CTL\_MEASURE and some other constants used in the sample sensor driver.

4. Find the following code:
   ```cpp
   // Enable interrupts
   RegisterSetting = { ADXL345_INT_ENABLE, ADXL345_INT_ACTIVITY };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &RegisterSetting.Value, sizeof(RegisterSetting.Value));
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);
   ```

The *RegisterSetting* parameter enables interrupts for the sensor. WdfWaitLockRelease is used to release the lock on the I2C bus.

## Stop the device activity and set device to standby


1. Within the *client.cpp* file, find the following code in the **OnStop** function:
   ```cpp
   // Disable interrupts
   REGISTER_SETTING RegisterSetting = { ADXL345_INT_ENABLE, 0 };
   WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &RegisterSetting.Value, sizeof(RegisterSetting.Value));
   ```

In the preceding code, the *RegisterSetting* parameter captures a register address and configuration code. In this case RegisterSetting.Register is the address of an interrupt enable register, while RegisterSetting.Value configures the register to stop the device from issuing interrupts.

2. Find the following code, which clears any unprocessed interrupts that might still be pending from the device:
   ```cpp
   // Clear any stale interrupts
   RegisterSetting = { ADXL345_INT_SOURCE, 0 };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &RegisterSetting.Value, sizeof(RegisterSetting.Value));
   ```

3. Find the following code, which sets the device to standby mode. This setting stops the device activity:
   ```cpp
   // Set accelerometer to standby
   RegisterSetting = { ADXL345_POWER_CTL, ADXL345_POWER_CTL_STANDBY };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &RegisterSetting.Value, sizeof(RegisterSetting.Value));
   ```

## Disconnect hardware resources


Note that the framework uses the **OnReleaseHardware** function to disconnect the hardware resources in response to an I/O request packet (IRP), to stop or remove the device.

1. Within the *client.cpp* file, in the **DeInit** function (called by **OnReleaseHardware** in the *device.cpp* file) find the following code:
   ```cpp
   // Delete lock
   WdfObjectDelete(m_I2CWaitLock);
   m_I2CWaitLock = NULL;
   ```

The preceding code is used to delete the wait lock on the device object.

2. Find the following code, which is used to delete the sensor instance:
   ```cpp
   // Delete sensor instance
   WdfObjectDelete(m_SensorInstance);
   ```

3. Close the *client.cpp* file.







