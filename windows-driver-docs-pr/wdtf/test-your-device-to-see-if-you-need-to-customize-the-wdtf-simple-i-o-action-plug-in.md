---
title: Test presence or need for custom WDTF simple I/O action plug-ins
description: If you have configured a remote computer for testing using Visual Studio, you can run a utility test that displays all the devices that have WDTF Simple I/O plug-ins.
ms.assetid: 7AD2F8DD-8428-4C30-A3B0-B6678986DCCD
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to determine if a custom WDTF Simple I/O Action Plug-in is required for your device


If you have configured a remote computer for testing using Visual Studio, you can run a utility test that displays all the devices that have WDTF Simple I/O plug-ins. The test also returns a list of devices on the test computer that do not have WDTF Simple I/O support. If your device is not supported, you can create one in Visual Studio using the **WDTF Simple I/O Action Plug-in** template, see [How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](to-customize-i-o-for-your-device-using-the-wdtf-simple-i-o-action-plug-in.md).

### Prerequisites

-   Device under test is installed on the test computer.
-   Driver Package that is test signed and installed on the test computer. To verify that your driver is correctly installed, see How to test driver package.
-   Test computers that are configured and provisioned for deployment. See [test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime)

Instructions
------------

### Test your device to see if you need to customize the WDTF Simple I/O Action Plug-in

The WDK provides a utility test you can run to determine whether there is a WDTF Simple I/O plug-in for your device type.

1.  Open the **Driver Test Group Explorer**. From the Driver menu, click **Driver &gt; Test &gt; Driver Test Group Explorer**.
2.  Create a new test group.
3.  In the Driver Test Group window, click **Add/Remove Tests**.
4.  In the **Add or Remove Tests** dialog box, select **All Tests\\Utilities** from the **Device Test Categories** list, and add the test **Display devices that have WDTF Simple I/O plug-ins**. Click **OK**. Save the test group.
5.  Run the test group that includes the utility test **Display devices that have WDTF Simple I/O plug-ins**.
6.  Open the TestTextlog for the test and verify that your device is reported as a device that has a WDTF Simple I/O plug-in. If your device is listed, you do not need to create a Simple I/O plug-in for your device. You can run the Device Fundamental tests and the correct plug-in for your device type will automatically be selected. For information about the provided tests, see [How to select and configure the Device Fundamental tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

    If there is no I/O plug-in for your device, you need to create one by customizing the provided WDTF Simple I/O Action Plug-in template.

**Example test text log**

``` syntax
WDTF_TEST                 : INFO  : 
WDTF_TEST                 : INFO  :  Devices that we do NOT have a simple I/O Plug-in for
WDTF_TEST                 : INFO  : 
WDTF_TEST                 : INFO  :      Intel(R) ICH10 Family USB Universal Host Controller - 3A68 PCI\VEN_8086&DEV_3A68&SUBSYS_3035103C&REV_02\3&33FD14CA&0&D1 
WDTF_TEST                 : INFO  :      Generic Non-PnP Monitor DISPLAY\DEFAULT_MONITOR\5&1934D7DD&0&UID259 

....

WDTF_TEST                 : INFO  :  Devices that we have a simple I/O Plug-in for
WDTF_TEST                 : INFO  : 
WDTF_TEST                 : INFO  :      Generic volume (I:) STORAGE\VOLUME\{A6EA1A2E-87E6-11E1-9834-806E6F6E6963}#0000006F7FD00000
WDTF_TEST                 : INFO  :      Generic volume (G:) STORAGE\VOLUME\_??_USBSTOR#DISK&VEN_GENERIC&PROD_STORAGE_DEVICE&REV_9744#000000000010&2#{53F56307-B6BF-11D0-94F2-00A0C91EFB8B} 

..... 

```

## Related topics
[How to customize I/O for your device using the WDTF Simple I/O Action Plug-in](to-customize-i-o-for-your-device-using-the-wdtf-simple-i-o-action-plug-in.md)  
[Provided WDTF Simple I/O plug-ins](provided-wdtf-simpleio-plug-ins.md)  



