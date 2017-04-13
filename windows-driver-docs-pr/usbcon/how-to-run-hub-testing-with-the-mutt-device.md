---
Description: The goal of hub testing is to generate a complete set of possible traffic patterns from devices. You can test disconnect scenarios by adding an upstream SuperMUTT pack.
MS-HAID: buses.how\_to\_run\_hub\_testing\_with\_the\_mutt\_device
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: USB hub testing with MUTT devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20USB%20hub%20testing%20with%20MUTT%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




