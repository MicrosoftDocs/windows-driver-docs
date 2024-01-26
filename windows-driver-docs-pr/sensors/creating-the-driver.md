---
title: Creating a Sensor Driver
description: Creating a sensor driver
ms.date: 01/11/2024
---

# Creating a sensor driver

If your sensor uses HID we recommend that rather than creating a driver, you use the inbox HID class driver. If your sensor uses a transport other than HID, you should start with either the [Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md) or the SpbAccelerometer sample.

These samples provide basic working implementations for the classes and COM interfaces required by a sensor driver. The following procedure shows the steps that you should follow to create a driver from the samples:

1. Follow the instructions that are provided in the [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier.md) topic to make sure that your driver is unique. When you work with the sample driver source, always provide new **GUID**s and other identifiers.

1. Add a class to handle communication with your device hardware, or with the software data provider if your sensor is a logical sensor.

3. Add support for events, as needed. You have to write code to create a thread to raise events at a particular time interval. You also have to update the implementation for [**ISensorDriver::OnGetSupportedEvents**](/windows-hardware/drivers/ddi/sensorsclassextension/nf-sensorsclassextension-isensordriver-ongetsupportedevents) in SensorDdi.cpp to report the list of events that the driver can raise.

1. Remove any code that is not needed.

## Build the Driver

To build your driver, follow these steps:

1. Start Microsoft Visual Studio 2012.
1. Select the build configuration (for example, Debug) and the architecture (for example, Win32).
1. Open your driver's solution or project file.
1. Choose Build/Build Solution.

## Install the Sensors Geolocation Driver Sample for Testing

To install your driver for testing, follow these steps:

1. Make sure that your driver builds without errors.

1. Copy the DLL and INF files for your driver to a separate folder.

1. Locate the two co-installer DLL files (either checked or free) from the redist/wdf/*processor\_type* folder where you installed the WDK. Copy these files to the folder that you created in step 3. For example, if you installed the WDK on your drive C, you might copy WUDFUpdate\_01009.dll from C:\\WinDDK\\*build\#*\\redist\\wdf\\x86.

1. Run Devcon.exe. You can find this program in the tools\\devcon folder where you installed the WDK. For example, for a sensor named WDKExample, you type:

    **devcon.exe install WDKExample.inf "Sensors\\WDKExample"**

    **Note**  Do not use Devcon.exe to install released drivers. This recommendation is for testing only.

If your driver cannot be installed, it is likely that one of the methods in step 2 returned an error code. To debug this problem, you must attach a debugger during installation. For information about how to debug UMDF drivers during loading, see [Determining Why the UMDF Driver Fails to Load or the UMDF Device Fails to Start](../wdf/determining-why-the-umdf-driver-fails-to-load-or-the-umdf-device-fails.md).

You should also verify that the class ID that you provided in the INF file matches the **GUID** that you used in the IDL file for the driver's coclass.

## Uninstalling the Driver

You may have to uninstall the driver during testing, for example when you want to update the driver installation after you make a change to the code. To uninstall the driver, follow these steps:

1. Open **Device Manager**. For example, click **Start**, then in the **Start Search** box, type the following.

    ``` syntax
    Device Manager
    ```

    After that, press CTRL + ENTER.

1. Expand the Sensors node.

1. Right-click the name of your driver, and then click **Uninstall**.

1. Select **Delete the driver software for this device**.

1. Click **OK**.

## Related topics

- [The Sensors Geolocation Driver Sample](../gnss/sensors-geolocation-driver-sample.md)
