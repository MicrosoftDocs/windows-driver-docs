---
title: Creating a sensor driver
author: windows-driver-content
description: Creating a sensor driver
ms.assetid: 7a1cea3c-d542-47e9-90f9-18bae4969b9f
---

# Creating a sensor driver


If your sensor uses HID we recommend that rather than creating a driver, you use the inbox HID class driver. If your sensor uses a transport other than HID, you should start with either the [Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273) or the SpbAccelerometer sample.

These samples provide basic working implementations for the classes and COM interfaces required by a sensor driver. The following procedure shows the steps that you should follow to create a driver from the samples:

1.  Follow the instructions that are provided in the [Creating a Persistent Unique Identifier](creating-a-persistent-unique-identifier.md) topic to make sure that your driver is unique. When you work with the sample driver source, always provide new **GUID**s and other identifiers.

2.  Add a class to handle communication with your device hardware, or with the software data provider if your sensor is a logical sensor.

3.  Add support for events, as needed. You have to write code to create a thread to raise events at a particular time interval. You also have to update the implementation for [**ISensorDriver::OnGetSupportedEvents**](https://msdn.microsoft.com/library/windows/hardware/ff545623) in SensorDdi.cpp to report the list of events that the driver can raise.

4.  Remove any code that is not needed.

### Building the Driver

To build your driver, follow these steps:

1.  Start Microsoft Visual Studio 2012.
2.  Select the build configuration (for example, Debug) and the architecture (for example, Win32).
3.  Open your driver's solution or project file.
4.  Choose Build/Build Solution.

### Installing the Sensors Geolocation Driver Sample for Testing

To install your driver for testing, follow these steps:

1.  Make sure that your driver builds without errors.

2.  Copy the DLL and INF files for your driver to a separate folder.

3.  Locate the two co-installer DLL files (either checked or free) from the redist/wdf/*processor\_type* folder where you installed the WDK. Copy these files to the folder that you created in step 3. For example, if you installed the WDK on your drive C, you might copy WUDFUpdate\_01009.dll from C:\\WinDDK\\*build\#*\\redist\\wdf\\x86.

4.  Run Devcon.exe. You can find this program in the tools\\devcon folder where you installed the WDK. For example, for a sensor named WDKExample, you type:

    **devcon.exe install WDKExample.inf "Sensors\\WDKExample"**

    **Note**  Do not use Devcon.exe to install released drivers. This recommendation is for testing only.

     

If your driver cannot be installed, it is likely that one of the methods in step 2 returned an error code. To debug this problem, you must attach a debugger during installation. For information about how to debug UMDF drivers during loading, see [Determining Why the UMDF Driver Fails to Load or the UMDF Device Fails to Start](https://msdn.microsoft.com/library/windows/hardware/ff554611).

You should also verify that the class ID that you provided in the INF file matches the **GUID** that you used in the IDL file for the driver's coclass.

### Uninstalling the Driver

You may have to uninstall the driver during testing, for example when you want to update the driver installation after you make a change to the code. To uninstall the driver, follow these steps:

1.  Open **Device Manager**. For example, click **Start**, then in the **Start Search** box, type the following.

    ``` syntax
    Device Manager
    ```

    After that, press CTRL + ENTER.

2.  Expand the Sensors node.

3.  Right-click the name of your driver, and then click **Uninstall**.

4.  Select **Delete the driver software for this device**.

5.  Click **OK**.

## Related topics
[The Sensors Geolocation Driver Sample](https://msdn.microsoft.com/library/windows/hardware/hh768273)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Creating%20a%20sensor%20driver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


