---
Description: How to run stress and transfer and Super MUTT performance tests.
title: How to run stress and transfer performance tests for MUTT devices
ms.date: 04/20/2017
ms.localizationpriority: medium
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



