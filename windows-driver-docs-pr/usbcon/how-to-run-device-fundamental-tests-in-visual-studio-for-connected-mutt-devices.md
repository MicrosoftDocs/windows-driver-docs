---
title: Run System Power Device Fundamental Tests in Visual Studio for MUTT Devices
description: Describes the device fundamental tests that you must run for MUTT devices that are attached to available ports.
ms.date: 01/16/2024
---

# How to run system power device fundamental (devfund) tests in Visual Studio for MUTT devices

Describes the device fundamental tests that you must run for MUTT devices that are attached to available ports, to perform stress and transfer tests and system power tests.

These tests perform simple device transfers at the same time that they perform system power events. Devfund tests can only be run on Windows 8 and later. You cannot [run stress and transfer tests](how-to-run-stress-and-transfer-and-super-mutt-performance-tests-for-mutt-devices.md) and the system power tests simultaneously. Perform those tests on separate systems. However, you can switch between stress transfer and system power tests. To do so, complete the first set of tests, reboot the machine, and then follow the instructions of the next test.

## How to run device fundamental (devfund) tests in Visual Studio for connected MUTT devices

The devfund tests are a collection of tests that are used for testing the drivers and hardware. These tests are included with the WDK for Windows. You can run the WDK add-in to Microsoft Visual Studio Professional, and run these tests from your development environment.

### Prerequisites

Before you start running devfund tests, make sure that you meet the following requirements:

- To run these tests, you will need at least two computers: host and test. Configure the host and test computers for testing and debugging.

  - You must install Microsoft Visual Studio Professional and the Windows Driver Kit (WDK).
  - The test computer must be running the latest version of Windows.

    You can download Visual Studio and WDK from [Downloads for Windows Hardware Development](https://developer.microsoft.com/windows/hardware/).

    For instructions about configuration, see [Configuring a Computer for Driver Deployment, Testing, and Debugging](/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1).

- Before you connect the host computer to the test computer, you must enable the File and Print Sharing and Network Discovery on the test computer. You can enable those options either in Control Panel or by using the following command in an elevated Command Prompt:

    `netsh.exe advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes`

- Set up and configure the MUTT device and install the firmware. For more information, see [How to prepare the test system](mutt-testing-options.md).
- Provision the test computer. For instructions, see [Configuring a Computer for Driver Deployment, Testing, and Debugging](/windows-hardware/drivers/gettingstarted/provision-a-target-computer-wdk-8-1).

### Scheduling tests

1. Select tests to run on the test computer. For instructions, see **Step 2: Select the tests to run on the test computer** in [How to test a driver at runtime using Visual Studio](/windows-hardware/drivers/develop/testing-a-driver-at-runtime).

1. Set the following runtime parameters as shown in the following image.

    - DQ: Class='USBTest'
    - TestCycles: 100

    ![visual studio test group.](images/fig11-vs-testgroup.png)

1. Configure the test parameters. For information about configuration, see **Step 3: Configure test parameters** in [How to test a driver at runtime using Visual Studio](https://go.microsoft.com/fwlink/p/?linkid=290770).

1. Run the Tests. For information about tests to run, see **Step 5: Run the tests on the test computer** in [How to test a driver at runtime using Visual Studio](https://go.microsoft.com/fwlink/p/?linkid=290770).

### Recommended tests to schedule with the connected MUTT device

- Sleep with IO Before and After
- Sleep with IO during (Basic)
- PNP (disable and enable ) with IO Before and After

For more information about the tests in the preceding list, see **About the Device Fundamental Tests** in [How to select and configure the Device Fundamental tests](https://go.microsoft.com/fwlink/p/?linkid=316387).

## Related topics

- [USB](../index.yml)
- [Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)
