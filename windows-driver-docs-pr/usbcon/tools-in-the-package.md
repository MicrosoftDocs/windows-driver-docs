---
Description: The goal of device testing is to test device usage against various hub scenarios and systems power states.
title: USB device testing with MUTT devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB device testing with MUTT devices


The goal of device testing is to test device usage against various hub scenarios and systems power states. The MUTT Pack and SuperMUTT Pack devices can provide a way to expose the device to connect/disconnect scenarios across different hub and system power state scenarios. Test the device when it is attached to a USB 2.0 and 3.0 hubs in the MUTT Pack and SuperMUTT Pack devices, respectively.

## USB device testing prerequisites


Before you run the MUTT test commands at an elevated command prompt, make sure you meet the following requirements:

-   The test system must be running the latest version of Windows 8.
-   Set up and configure the MUTT device and install the firmware. For more information, see [How to prepare the test system to run MUTT test tools](mutt-testing-options.md).

## Suggested device tests


-   USB IF electrical tests. All of our tests are protocol and state focused. See [USB-IF Compliance Program](http://www.usb.org/developers/compliance/) for more information on electrical tests.
-   Device Fundamental test. For more information, see [How to run devfund tests in Visual Studio for MUTT devices](how-to-run-device-fundamental-tests-in-visual-studio-for-connected-mutt-devices.md).
-   Controller Windows Hardware Certification Kit tests. For more information, see [USB-IF Certification Validation Test (Controller)](http://go.microsoft.com/fwlink/p/?linkid=316509).
-   Manual test cases for host controllers, as found in Windows Test Guidance document in the section.

## Topologies for testing USB devices


Consider the following configurations for USB devices under test:

-   The test device is downstream of SuperMUTT Pack.

    ![device is downstream of supermutt pack](images/fig13-topology-downstream-supermuttpack.png)

-   The test device is downstream of MUTT Pack.

    ![device is downstream from mutt pack](images/fig14-topology-downstream-muttpack.png)

## Related topics
[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  



