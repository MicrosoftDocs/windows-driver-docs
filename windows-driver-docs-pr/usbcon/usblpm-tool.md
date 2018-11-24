---
Description: The USBLPM tool monitors the U0/U1/U2/U3 power states of USB 3.0 ports. 
title: USBLPM
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USBLPM


The USBLPM tool monitors the U0/U1/U2/U3 power states of USB 3.0 ports. It can also be used to verify that transitions between U0/U1/U2 occur correctly. In addition, the tool can enable or disable U1 and/or U2 states on all devices in the system.

The tool is included in the [MUTT Software Package](https://msdn.microsoft.com/windows/hardware/jj590752).

## USBLPM


USBLPM is for Windows 8 only and works with the Microsoft USB 3.0 driver stack. The tool does not run as part of the batch files and scripts in this package. The tool is intended for controller, hub, and device companies to monitor the new USB 3.0 power states.

USBLPM runs in **Monitoring**, **Testing**, or **Configuring** mode.

![usb lpm tool](images/fig10-usb-lpm-tool.png)

### Monitoring

This is the default mode when the tool is run without any parameters. In this mode, the tool periodically queries each level of USB 3.0 devices and displays the current U state of the port. By default, the tool runs the query every 500 milliseconds.

In monitoring mode, the period can be changed by this command-line option:

**usblpm /PollingInterval** &lt;*time in milliseconds*&gt;

Where the time value is an integer from 1 through 100000. The **/PollingInterval** option is optional. In general, you should not change the time period.

### Testing

**To test a device or a hub:**

1.  Start the tool.
2.  Change the mode from Monitoring to Testing.
3.  Select the test device.
4.  Click **Start** to start a test run.

The test completes within 10 seconds and the results are displayed to the user.

The test tries different combinations of U0/U1/U2 states and ensures that the test device re-enters U0 successfully. That is done by sending a control transfer which queries the BOS descriptor.

To test a hub, remove all devices attached to it and run the test. Then, attach one or more devices and rerun the test. However, if one of the downstream devices does not correctly support U1/U2, the hub test fails. Therefore, before running the test on the hub, we recommend that you first run the test on devices that are downstream of the hub to ensure that they pass the test.

**Note**  Do not change the device topology while running the test. The behavior of the tool is undefined if the configuration is changed dynamically.

 

### Configuring U1/U2 states

You can use USBLPM to enable or disable U1 and U2 states for all USB devices on the system by running the following command:

**usblpm /enable|/disable U1|U2**

For example, this command disables U2:

**usblpm /disable U2**

In the Configuring mode, the tool does not display any window. The enabling or disabling will persist after the tool has been run.

### Known issues with USBLPM

Before you test selective suspend for a SuperSpeed hub, you should perform the following steps to disable selective suspend.

1.  In Device Manager, right-click on the **SuperSpeed hub** and select **Properties**.
2.  Click the **Power Management** tab.
3.  Uncheck **Allow the computer to turn off this device to save power**.

After you have finished testing with USBLPM, enable selective suspend for the hub by checking **Allow the computer to turn off this device to save power to re-enable selective suspend**.

**Note**  USBLPM currently does not test USB 2.1 LPM.

 

## Related topics
[USB test tools](usb-test-tools.md)  
[Tools in the MUTT software package](mutt-software-package.md)  



