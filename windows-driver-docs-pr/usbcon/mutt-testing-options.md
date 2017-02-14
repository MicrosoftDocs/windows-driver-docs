---
Description: 'Before using MUTT devices, you must prepare the test system.'
MS-HAID: 'buses.mutt\_testing\_options'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: How to prepare the test system to run MUTT test tools
---

# How to prepare the test system to run MUTT test tools


Before using MUTT devices, you must prepare the test system.

## Prerequisites


The instructions in this document are based on the following assumptions:

-   You have an understanding of the Windows command shell. Installation of the test tools requires an elevated command window. For that window, you can open a Command Prompt window by using the **Run as administrator** option.
-   You are familiar with the tools that are included with the Windows Driver Kit (WDK).
-   You are familiar with kernel debugging tools.

**Note**  This setup applies to the MUTT, MUTTPack, SuperMUTT and SuperMUTT Pack. For more information about those devices, see [MUTT devices](microsoft-usb-test-tool--mutt--devices.md).

 

## Instructions


**To prepare a system to run MUTT test tools for USB hardware testing**

1.  Connect the test system to a kernel debugger.

    For more information, see [Download and Install Debugging Tools for Windows](http://go.microsoft.com/fwlink/p/?linkid=236405) and [Windows Debugging](http://go.microsoft.com/fwlink/p/?linkid=242503).

2.  Attach MUTT devices into each available port of the host controller or hub to test.

    You must attach the MUTT device to the test system before you run the installation scripts that are installed by the MUTT software package.

    For information about the recommended test configurations, see MUTT Topologies in this document.

3.  Open an elevated command window on the test system and navigate to the folder in which the test tools were copied.
4.  In the elevated command window, install the necessary MUTT driver **C:\\usbTest\\pnputil –i –a usbfx2.inf**

    If you want to test by using driver verifier then you can run **install.cmd** instead of the previous command. This will install the necessary drivers as well as configure driver verifier. Note that using **install.cmd** is optional.

5.  The following dialog box appears while installing the test drivers:

    ![windows security dialog](images/fig9-winsec.png)

    Check **Always trust software from “Microsoft Corporation”** to prevent the dialog box from appearing when the tests are running.

    The test system machine will reboot after **install.cmd** has completed installing.

6.  Switch the MUTT to the new driver **C:\\usbTest\\MuttUtil –UpdateDriver usbfx2.inf**
7.  Update the MUTT with the latest firmware **C:\\usbTest\\MuttUtil.exe -UpdateFirmware**
8.  If your test system is running Windows 8, we suggest that you perform a quick validation of your host controller before you start the tests.

    From an elevated Command Prompt window, run the following command to collect information about your host controller and hubs that are connected to the system: **C:\\usbTest\\xhciwmi -verify**.

    The tool displays information about the host controller in the command window. Information includes vendor ID, device ID, revision ID, and the firmware version. If known issues exist for the host controller under test, consider updating the firmware.

### Tracing and logging events in the USB driver stack

You can provide additional logs by capturing ETW traces by using the Logman tool. For information about how to read USB 2.0 ETW traces, see [ETW in the Windows 7 USB core stack](http://go.microsoft.com/fwlink/p/?linkid=266442).

## Related topics


[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)

[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20How%20to%20prepare%20the%20test%20system%20to%20run%20MUTT%20test%20tools%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




