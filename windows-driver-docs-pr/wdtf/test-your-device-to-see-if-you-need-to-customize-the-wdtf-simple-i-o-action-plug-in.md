---
title: How to determine if a custom WDTF Simple I/O Action Plug-in is required for your device
author: windows-driver-content
description: If you have configured a remote computer for testing using Visual Studio, you can run a utility test that displays all the devices that have WDTF Simple I/O plug-ins.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 7AD2F8DD-8428-4C30-A3B0-B6678986DCCD
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdtf\dtf%5D:%20How%20to%20determine%20if%20a%20custom%20%20WDTF%20Simple%20I/O%20Action%20Plug-in%20is%20required%20for%20your%20device%20%20RELEASE:%20%289/13/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


