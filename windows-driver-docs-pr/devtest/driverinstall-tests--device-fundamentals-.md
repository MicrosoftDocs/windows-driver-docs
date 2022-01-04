---
title: Driver Install Tests (Device Fundamentals)
description: The Driver Install test category includes tests that uninstall and reinstall a driver several times to test install functionality.
ms.date: 04/20/2017
---

# Driver Install Tests (Device Fundamentals)

The Driver Install test category includes tests that uninstall and reinstall a driver several times to test install functionality. The tests initiate I/O testing against the driver and device after each reinstall. The tests are designed to improve the overall experience for end users who need to install and reinstall a device driver or a device.

## DriverInstall tests

### Reinstall with IO Before and After

This test uninstalls and reinstalls the drivers for selected devices, and runs I/O testing on devices.

**Test binary**: Devfund_Reinstall_With_IO_BeforeAndAfter.wsc

**Test method**: Reinstall_With_IO_Before_And_After

**Parameters**: [*DQ*] and [*IOPeriod*] For more information, see "Device Fundamentals Test Parameters" in [How to select and configure the Device Fundamentals tests](../develop/how-to-select-and-configure-the-device-fundamental-tests.md#device-fundamentals-test-parameters)

## About the ReInstall with I/O Before and After test

This test does the following:

1. Verifies that the test device and its descendants are not reporting any device problem codes.
2. Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
3. Reinstalls the original driver on the test device using [**IWDTFDriverSetupAction2::UpdateDriver**](/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-updatedriver) method.
4. Verifies that the test device and its descendants are not reporting any device problem codes.
5. Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
6. Reboots the system if step \#3 requires a reboot.
7. Installs NULL driver on the test device using [**IWDTFDriverSetupAction2::UnInstallDriverPermanently**](/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-uninstalldriverpermanently) method Reboots the system if a reboot is required.
8. Reinstalls the original driver on device under test using [**IWDTFDriverSetupAction2::UpdateDriver**](/windows-hardware/drivers/ddi/wdtfdriversetupdeviceaction/nf-wdtfdriversetupdeviceaction-iwdtfdriversetupaction2-updatedriver) method.
9. Verifies that the test device and its descendants are not reporting any device problem codes.
10. Tests I/O on the test device and its descendants using WDTF Simple I/O plugins. See [Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md) for more information.
11. Repeats step 1 - 10 several times.

### Debug installation failures using the Setup API logs

The Setup API logs (setupapi.app.log and setupapi.dev.log) contain useful information to debug driver installation failures logged by this test. The Setup API logs can be found under %windir%\\inf\\ directory on the test system.

To increase the verbosity and potential usefulness of these logs, set the following registry key to 0x2000FFFF before running the Reinstall test:

```command
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Setup\LogLevel
```

## Related topics

[How to How to test a driver at runtime using Visual Studio](/windows-hardware/drivers)

[How to select and configure the Device Fundamentals tests](/windows-hardware/drivers)

[Device Fundamentals Tests](device-fundamentals-tests.md)

[Device Fundamentals Test Parameters](/windows-hardware/drivers)

[Provided WDTF Simple I/O plug-ins](../wdtf/provided-wdtf-simpleio-plug-ins.md)

[How to test a driver at runtime from a Command Prompt](/windows-hardware/drivers)
