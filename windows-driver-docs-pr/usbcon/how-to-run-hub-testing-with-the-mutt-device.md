---
Description: The goal of hub testing is to generate a complete set of possible traffic patterns from devices. You can test disconnect scenarios by adding an upstream SuperMUTT pack.
title: USB hub testing with MUTT devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB hub testing with MUTT devices


The goal of hub testing is to generate a complete set of possible traffic patterns from devices. You can test disconnect scenarios by adding an upstream SuperMUTT pack.

## Hub testing prerequisites


Before you run the MUTT test commands at an elevated command prompt, make sure you meet the following requirements:

-   The test system must be running the latest version of Windows 8.
-   Set up and configure the MUTT device and install the firmware. For more information, see [How to prepare the test system to run MUTT test tools](mutt-testing-options.md).

## Recommended hub tests


-   USB IF electrical tests. All of our tests are protocol and state focused. See [USB-IF Compliance Program](http://www.usb.org/developers/compliance/) for more information on electrical tests.
-   MUTT stress and transfer tests included in the MUTT software package with MUTT devices connected in the suggested configurations for USB controllers. **RunTest.bat** runs both the stress and transfer tests. See [How to run stress and transfer performance tests for MUTT devices](how-to-run-stress-and-transfer-and-super-mutt-performance-tests-for-mutt-devices.md).
-   Device Fundamental test. For more information, see [How to run devfund tests in Visual Studio for MUTT devices](how-to-run-device-fundamental-tests-in-visual-studio-for-connected-mutt-devices.md).
-   Controller Windows Hardware Certification Kit tests. For more information, see [USB-IF Certification Validation Test (Controller)](http://go.microsoft.com/fwlink/p/?linkid=316509).
-   Manual test cases for host controllers, as found in Windows Test Guidance document in the section.

## Recommended topologies for hub testing with MUTT devices


-   Attach MUTT devices to each available downstream port.
-   Attach SuperMUTTs to half of the available ports. Attach MUTT devices to the remaining ports.
-   Attach a SuperMutt Pack upstream of the hub under test and downstream ports have equal number of SuperMUTT and MUTT devices as shown in the following figure:

    ![test connect/disconnect](images/fig14-topology-connect-disconnect.png)

## Related topics
[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)  
[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)  



