---
title: Test your universal sensor driver
description: This topic provides suggestions for how to test your universal sensor driver.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 46F50544-B130-4690-8047-6FBB6DD4749F
---

# Test your universal sensor driver


This topic provides suggestions for how to test your universal sensor driver.

## Sensor driver-specific testing


After you successfully [connect your sensor to the Sharks Cove board](connect-your-sensor-to-the-sharks-cove-board.md), and you [write and deploy your universal sensor driver](write-and-deploy-your-universal-sensor-driver.md), you can use the following tool for testing/debugging the universal sensor driver.

-   **The SensorInfo App**

    If you want to use a Universal Windows Platform (UWP) app test sensor driver, then you can use the [SensorInfo app](http://apps.microsoft.com/windows/app/95015d9e-2116-44b8-9d3c-15c7b8753086?ocid=Apps_Search_WOL_en-us_search-main_search-results-from_search-sensorinfo_image_sensorinfo). This app will automatically detect any sensors that are attached to (or embedded in) your platform, and then invoke the associated drivers. The app will then display the information that it reads from the sensors, and display the information as moving waveforms.

-   **The sensor diagnostic tool**

    **Note**  The Sensor Diagnostic Tool is now deprecated for Windows 10. Please use the SensorInfo App from the Windows Store, for all sensor testing and diagnostics.

     

    If you simply want to monitor data retrieval, event handling, report intervals etc., then install this tool on Sharks Cove to monitor these sensor values. The sensor diagnostic tool ships with the Windows driver kit (WDK) and can be found in the following folder: *&lt;Kit root&gt;\\Tools\\&lt;architecture&gt;\\sensordiagnostictool.exe*.

    For example, if your driver development computer is an x64-based machine, and you installed the WDK to the default location, then you will find the sensor diagnostic tool in the following folder:

    *C:\\Program Files (x86)\\Windows Kits\\10\\Tools\\x64\\sensordiagnostictool.exe*

## General driver testing


If you want to find out about testing drivers in general, see the following resources.

-   **Visual Studio Kernel-Mode Debugging, using Serial over USB**
    Use this test/debug option, if you want the help of Visual Studio in setting up the debugging session for your sensor and its universal sensor driver. For more information, see [Setting Up Kernel-Mode Debugging using Serial over USB in Visual Studio](http://msdn.microsoft.com/library/windows/hardware/dn745913.aspx).
-   **Manually set up Kernel-Mode Debugging, using Serial over USB**
    If you want to test/debug your universal sensor driver, but don't want to use Visual Studio for doing the setup, you can use this option. For instructions on how to do this, see [Setting Up Kernel-Mode Debugging using Serial over USB Manually](http://msdn.microsoft.com/library/windows/hardware/dn745914.aspx).
-   **WDK driver testing interface**
    You can use the Windows driver kit (WDK) driver testing interface via Microsoft Visual Studio, to test drivers. For information about how to do this, see [Testing a Driver](http://msdn.microsoft.com/library/windows/hardware/ff554820.aspx).

For information about how to monitor the operation of trace providers, see [Collecting and decoding WPP logs](collecting-and-decoding-wpp-logs.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bsensors\sensors%5D:%20Test%20your%20universal%20sensor%20driver%20%20RELEASE:%20%281/12/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




