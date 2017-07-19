---
title: Connect to hardware
author: windows-driver-content
description: This topic shows you how the sensor driver determines the assigned hardware resources and connects to the I2C driver controller.
ms.assetid: 88D9162B-2B99-4608-B31A-48B1810747A9
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Connect to hardware


This topic shows you how the sensor driver determines the assigned hardware resources, then connects to the I2C driver controller so that it can connect to the ADXL345 hardware.

The following sections will use code snippets from the sample driver that was developed for the ADXL345 accelerometer, as a test case for showing how to make your sensor driver connect to hardware. If you haven't already done so, navigate to the [ADXL345Acc sample](https://github.com/Microsoft/Windows-driver-samples/tree/1fbea08887e10e087c3f6bb0be8968e29e20cc84/sensors/ADXL345Acc) on GitHub, so that you can follow along with the explanations.

These code snippets highlight some of the important sections of the sensor driver files. But you must review all the driver files in their entirety, to get a good understanding of how the driver works, and to be able to figure out how to customize these files for your sensor.

## Prepare hardware resources


1. Click the *device.cpp* file to open it, then find the **OnPrepareHardware** function. Within that function, find the following code:
```ManagedCPlusPlus
// Create WDFOBJECT for the sensor
    WDF_OBJECT_ATTRIBUTES sensorAttributes;
    WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(&amp;sensorAttributes, ADXL345AccDevice);
```

The preceding code creates a sensor object and assigns the appropriate device context to it.

2. Find the following code:
```ManagedCPlusPlus
// Register sensor instance with clx
    SENSOROBJECT SensorInstance = NULL;
    NTSTATUS Status = SensorsCxSensorCreate(Device, &amp;sensorAttributes, &amp;SensorInstance);
```

The preceding code registers the sensor instance with the sensor class extension. A sensor instance is created instead of a device instance, to allow for the scenario where you have multiple sensors within the same chip.

3. Find the following code:
```ManagedCPlusPlus
// Initialize sensor instance with clx
    SENSOR_CONFIG SensorConfig;
    SENSOR_CONFIG_INIT(&amp;SensorConfig);
    SensorConfig.pEnumerationList = pAccDevice->m_pEnumerationProperties;
    Status = SensorsCxSensorInitialize(SensorInstance, &amp;SensorConfig);
```

The preceding code uses the sensor class extension to initialize the sensor instance.

4. Find the following code:
```ManagedCPlusPlus
Status = pAccDevice->ConfigureIoTarget(ResourcesRaw, ResourcesTranslated);
```

The preceding code configures an I/O target object for the sensor driver. An I/O target object enables the sensor driver to communicate with other drivers.

## Configure the device with default settings


Remember that D0 is the active state of the device. To put the device into D0 requires setting up this configuration in the registers of the device itself, and you will communicate with the device over I2C. You must hold the lock for this resource before performing a write or read.

Within the *device.cpp* file, find the **OnD0Entry** function and notice that it calls **PowerOn**, using the ADXL345 context to do the work of powering on the device. Within the **PowerOn** function, find the following code:
1.
```ManagedCPlusPlus
WdfWaitLockAcquire(m_I2CWaitLock, NULL);
```

The preceding code is used to acquire a lock for the I2C bus.

2. Find the following code:
```ManagedCPlusPlus
// Write the default device configuration to the device
   For (DWORD i = 0; i < ARRAYSIZE(g_ConfigurationSettings); i++)
   {
       REGISTER_SETTING setting = g_ConfigurationSettings[i];
       Status = I2CSensorWriteRegister(m_I2CIoTarget, setting.Register, &amp;setting.Value, sizeof(setting.Value));
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
```ManagedCPlusPlus
// Release the I2C bus lock
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);
        
   InitPropVariantFromUInt32(SensorState_Idle, &amp;(m_pSensorProperties->List[SENSOR_PROPERTY_STATE].Value));
   m_PoweredOn = true;
```

After the device is successfully configured, WdfWaitLockRelease is used to release the lock for the I2C bus.

4. Close the *device.cpp* file.
## Start the device activity


1. Click the *client.cpp* file to open it, and find the **OnStart** function.
2. Review the following code, which is used to acquire a lock on the sensor device:
```ManagedCPlusPlus
WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
```

3. Find the following code:
```ManagedCPlusPlus
// Set accelerometer to measurement mode
   REGISTER_SETTING RegisterSetting = { ADXL345_POWER_CTL, ADXL345_POWER_CTL_MEASURE };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &amp;RegisterSetting.Value, sizeof(RegisterSetting.Value));
```

In the preceding code, the I2C connection is used to set the accelerometer to *measure mode* to make it ready for reading sensor values. See the *adxl345.h* header file for the definitions of ADXL345\_POWER\_CTL, ADXL345\_POWER\_CTL\_MEASURE and some other constants used in the sample sensor driver.

4. Find the following code:
```ManagedCPlusPlus
// Enable interrupts
   RegisterSetting = { ADXL345_INT_ENABLE, ADXL345_INT_ACTIVITY };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &amp;RegisterSetting.Value, sizeof(RegisterSetting.Value));
   WdfWaitLockRelease(pAccDevice->m_I2CWaitLock);
```

The *RegisterSetting* parameter enables interrupts for the sensor. WdfWaitLockRelease is used to release the lock on the I2C bus.

## Stop the device activity and set device to standby


1. Within the *client.cpp* file, find the following code in the **OnStop** function:
```ManagedCPlusPlus
// Disable interrupts   
   REGISTER_SETTING RegisterSetting = { ADXL345_INT_ENABLE, 0 };
   WdfWaitLockAcquire(pAccDevice->m_I2CWaitLock, NULL);
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &amp;RegisterSetting.Value, sizeof(RegisterSetting.Value));
```

In the preceding code, the *RegisterSetting* parameter captures a register address and configuration code. In this case RegisterSetting.Register is the address of an interrupt enable register, while RegisterSetting.Value configures the register to stop the device from issuing interrupts.

2. Find the following code, which clears any unprocessed interrupts that might still be pending from the device:
```ManagedCPlusPlus
// Clear any stale interrupts
   RegisterSetting = { ADXL345_INT_SOURCE, 0 };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &amp;RegisterSetting.Value, sizeof(RegisterSetting.Value));
```

3. Find the following code, which sets the device to standby mode. This setting stops the device activity:
```ManagedCPlusPlus
// Set accelerometer to standby
   RegisterSetting = { ADXL345_POWER_CTL, ADXL345_POWER_CTL_STANDBY };
   Status = I2CSensorWriteRegister(pAccDevice->m_I2CIoTarget, RegisterSetting.Register, &amp;RegisterSetting.Value, sizeof(RegisterSetting.Value));
```

## Disconnect hardware resources


Note that the framework uses the **OnReleaseHardware** function to disconnect the hardware resources in response to an I/O request packet (IRP), to stop or remove the device.

1. Within the *client.cpp* file, in the **DeInit** function (called by **OnReleaseHardware** in the *device.cpp* file) find the following code:
```ManagedCPlusPlus
// Delete lock
   WdfObjectDelete(m_I2CWaitLock);
   m_I2CWaitLock = NULL;
```

The preceding code is used to delete the wait lock on the device object.

2. Find the following code, which is used to delete the sensor instance:
```ManagedCPlusPlus
// Delete sensor instance
   WdfObjectDelete(m_SensorInstance);
```

3. Close the *client.cpp* file.
 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Connect%20to%20hardware%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


