---
Description: Read how to run stress and transfer and Super MUTT performance tests.Stress and transfer tests are geared towards saturating the bus protocol and the host controller software.
MS-HAID: buses.how\_to\_run\_stress\_and\_transfer\_and\_super\_mutt\_performance\_tests\_for\_mutt\_devices
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: How to run stress and transfer performance tests for MUTT devices
---

# How to run stress and transfer performance tests for MUTT devices


Read how to run stress and transfer and Super MUTT performance tests.

Stress and transfer tests are geared towards saturating the bus protocol and the host controller software. These tests perform several simultaneous I/O transfers and cancellations to the MUTT device. The MUTT firmware is programmed to fail transfers during these tests. These failures emulate error conditions that the controller or USB driver stack are exposed to under stressful USB conditions.

## How to run stress and transfer tests


1.  Open an elevated command window on the test system that has MUTT devices attached to available ports.
2.  Navigate to the test folder, such as **C:\\usbTest**.
3.  The transfer and stress tests run via the same script back to back. To run them, run the script runtest.bat:

    **C:\\usbTest\\runtest.bat**

The .bat files as written will run the tests indefinitely. The tests should run for at least 30 minutes. For more exhaustive testing, consider running these tests for eight hours. The batch file contains comments for additional tuning that can be done.

To exit all tests, press **Ctrl-C** in the command window. If the system does not generate a bugcheck during the run and exits cleanly from the command window, the test run is considered to be successful (or a positive run). If the tool does not exit cleanly, then it indicates that transfers are not completing and must be investigated.

## <a href="" id="supermutt-perf"></a>How to run SuperMUTT performance tests


1.  Open an elevated command window on the test system that has a SuperMUTT attached to an xHCI controller.
2.  Navigate to the test folder, such as **C:\\usbTest**.
3.  Run the script that is named **FX3Perf.bat** to start a test run.

## Related topics


[USB](https://msdn.microsoft.com/library/windows/hardware/ff538930)

[Microsoft USB Test Tool (MUTT) devices](microsoft-usb-test-tool--mutt--devices.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Busbcon\buses%5D:%20How%20to%20run%20stress%20and%20transfer%20performance%20tests%20for%20MUTT%20devices%20%20RELEASE:%20%281/26/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




