---
title: Make the driver loadable
description: To make a driver loadable, you must add a function that will register the required driver callback routines (DriverEntry), a function that will attach the driver to a device stack (DeviceAdd), and a function that will unload the driver when it's no longer needed (DriverUnload).
ms.assetid: 6BEB7CBC-0179-41B3-BD3D-126290940768
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Make the driver loadable


To make a driver loadable, you must add a function that will register the required driver callback routines (**DriverEntry**), a function that will attach the driver to a device stack (**DeviceAdd**), and a function that will unload the driver when it's no longer needed (**DriverUnload**).

The following sections will use code snippets from the sample driver that was developed for the ADXL345 accelerometer, as a test case for showing how to make your sensor driver loadable. If you haven't already done so, navigate to the [ADXL345Acc sample](https://github.com/Microsoft/Windows-driver-samples/tree/1fbea08887e10e087c3f6bb0be8968e29e20cc84/sensors/ADXL345Acc) on GitHub, so that you can follow along with the explanations.

These code snippets highlight some of the important sections of the sensor driver files. But you must review all the driver files in their entirety, to get a good understanding of how the driver works, and to be able to figure out how to customize these files for your sensor.

## Register the driver - DriverEntry


1. Click to open the *driver.cpp* file, then find the code block that starts with NTSTATUS DriverEntry. The **DriverEntry** function registers the sensor driver by configuring and initializing the DriverObject. This function also initializes logging by using WPP tracing.
2. Within **DriverEntry**, find the following code:
   ```cpp
   WPP_INIT_TRACING(DriverObject, NULL);
   ```

This code configures logging for the driver.

3. Find the WDF\_DRIVER\_CONFIG\_INIT statement. The WDF\_DRIVER\_CONFIG\_INIT function is called to set the **DeviceAdd** callback.
   ```cpp
   WDF_DRIVER_CONFIG_INIT(&DriverConfig, ADXL345AccDevice::OnDeviceAdd);
   ```

4. Find the code block that starts with NTSTATUS Status = WdfDriverCreate.
   ```cpp
   NTSTATUS Status = WdfDriverCreate(DriverObject, RegistryPath, WDF_NO_OBJECT_ATTRIBUTES, &DriverConfig, WDF_NO_HANDLE);
   ```

The WdfDriverCreate function is used to initialize the driver object.

5. Close the *driver.cpp* file.
   ## Set up the device object - DeviceAdd


6. Click to open the *device.cpp* file, then find the **OnDeviceAdd** function. This function attaches the driver to a device stack, and allocates a per-device context structure to the device. **OnDeviceAdd** is typically invoked during the second call that is made into the driver. As you develop the driver you may also include code to handle PnP, Power management, and I/O.
7. Find the following code:
   ```cpp
   // Create WDFOBJECT for the sensor
   WDF_OBJECT_ATTRIBUTES attributes;
   WDF_OBJECT_ATTRIBUTES_INIT_CONTEXT_TYPE(WDFDRIVER Driver, &attributes, ADXL345AccDevice);
   ```

This code sets up a context structure of type ADXL345AccDevice for the device object.

3. Find the following code:
   ```cpp
   // Call the framework to create the device
   NTSTATUS Status = WdfDeviceCreate(&pAccDeviceInit, &FdoAttributes, &Device);
   ```

This function is used to create a WDFDEVICE object. WDF creates the device object, and then allocates an ADXL345 accelerometer context to it.

4. Close the *device.cpp* file.
   ## Unload the driver - DriverUnload


5. Click to open the *driver.cpp* file, and find the **OnDriverUnload** function. This function is used to perform cleanup after the IO manager unloads the driver from memory.
6. Find the following code:
   ```cpp
   WPP_CLEANUP(WdfDriverWdmGetDriverObject(Driver));
   ```

This code turns off WPP diagnostic tracing.

 

 




