---
Description: Describes the Device Fundamental tests that you must run for MUTT devices that are attached to available ports, to perform stress and transfer tests and system power tests.These tests perform simple device transfers at the same time that they perform system power events. Note that devfund tests can only be run on Windows 8. You cannot run stress and transfer tests and the system power tests simultaneously. Perform those tests on separate systems. However, you can switch between stress transfer and system power tests. To do so, complete the first set of tests, reboot the machine, and then follow the instructions of the next test.
MS-HAID: buses.how\_to\_run\_device\_fundamental\_tests\_in\_visual\_studio\_for\_connected\_mutt\_devices
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: How to run system power devfund tests in Visual Studio for MUTT devices
---

# How to run system power devfund tests in Visual Studio for MUTT devices


Describes the Device Fundamental tests that you must run for MUTT devices that are attached to available ports, to perform stress and transfer tests and system power tests.

These tests perform simple device transfers at the same time that they perform system power events. Note that devfund tests can only be run on Windows 8. You cannot [run stress and transfer tests](how-to-run-stress-and-transfer-and-super-mutt-performance-tests-for-mutt-devices.md) and the system power tests simultaneously. Perform those tests on separate systems. However, you can switch between stress transfer and system power tests. To do so, complete the first set of tests, reboot the machine, and then follow the instructions of the next test.

## How to run Device Fundamental (devfund) tests in Visual Studio for connected MUTT devices


The devfund tests are a collection of tests that are used for testing the drivers and hardware. These tests are included with the WDK for Windows 8. You can run the WDK add-in to Microsoft Visual Studio Professional 2012 RC, and run these tests from your development environment.

### Prerequisites

Before you start running devfund tests, make sure that you meet the following requirements:

-   To run these tests, you will need at least two computers: host and test. Configure the host and test computers for testing and debugging.

    -   You must install Microsoft Visual Studio Professional 2012 and the Windows Driver Kit (WDK) for Windows 8.
    -   The test computer must be running the latest version of Windows 8.

    You can download Visual Studio and WDK from [Downloads for Windows Hardware Development](http://go.microsoft.com/fwlink/p/?linkid=309780).

    For instructions about configuration, see [Configuring a Computer for Driver Deployment, Testing, and Debugging](http://go.microsoft.com/fwlink/p/?linkid=235504).

-   Before you connect the host computer to the test computer, you must enable the File and Print Sharing and Network Discovery on the test computer. You can enable those options either in Control Panel or by using the following command in an elevated Command Prompt:

    `netsh.exe advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes`

-   Set up and configure the MUTT device and install the firmware. For more information, see [How to prepare the test system](mutt-testing-options.md).
-   Provision the test computer. For instructions, see [Configuring a Computer for Driver Deployment, Testing, and Debugging](http://go.microsoft.com/fwlink/p/?linkid=235504).

### Scheduling tests

1.  Select tests to run on the test computer. For instructions, see **Step 2: Select the tests to run on the test computer** in [How to test a driver at runtime using Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=290770).
2.  Set the following runtime parameters as shown in the following image.

    -   DQ: Class=’USBTest’
    -   TestCycles: 100

    ![visual studio test group](images/fig11-vs-testgroup.png)

3.  Configure the test parameters. For information about configuration, see **Step 3: Configure test parameters** in [How to test a driver at runtime using Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=290770).
4.  Run the Tests. For information about tests to run, see **Step 5: Run the tests on the test computer** in [How to test a driver at runtime using Visual Studio](http://go.microsoft.com/fwlink/p/?linkid=290770).

### Recommended tests to schedule with the connected MUTT device

-   Sleep with IO Before and After
-   Sleep with IO during (Basic)
-   PNP (disable and enable ) with IO Before and After

For more information about the tests in the preceding list, see **About the Device Fundamental Tests** in [How to select and configure the Device Fundamental tests](http://go.microsoft.com/fwlink/p/?linkid=316387).

## Related topics


[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)

[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20How%20to%20run%20system%20power%20devfund%20tests%20in%20Visual%20Studio%20for%20MUTT%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




