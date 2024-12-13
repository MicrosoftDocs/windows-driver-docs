---
title: How to Run the HCK Test Suites in WDK 8.1
description: To make testing Windows drivers easier in the WDK, starting with WDK 8.1 you can now select HCK test suites to run on the test computers.
ms.date: 12/13/2024
---

# How to run the HCK Test Suites in WDK 8.1

To make testing Windows drivers easier in the WDK, starting with WDK 8.1 you can now select HCK test suites to run on the test computers. The [HCK test suites](#hck-test-suites) include the device fundamentals tests, and tests for graphics, imaging, wireless LAN, mobile broadband (CDMA and GSM), and WiFi Direct devices. These are the same tests that are used in the Windows Hardware Certification kit (Windows HCK). See [Windows Certification Program for Hardware](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) for information about the Windows HCK.

You can run the HCK test from a Command Prompt window or from Visual Studio. In addition, you can copy these tests to a new location—which might be another computer or a USB key drive—and run the tests from that location. Launching the tests automatically sets any local configuration needed to run the tests.

- [Run the HCK Test Suites on a test computer using Visual Studio](#run-the-hck-test-suites-on-a-test-computer-using-visual-studio)
- [Run the HCK Test Suites from a Command Prompt window](#run-the-hck-test-suites-from-a-command-prompt-window)

## Run the HCK Test Suites on a test computer using Visual Studio

If you have not already done so, follow the instructions in [Provision a computer for driver deployment and testing (WDK 8.1)](../gettingstarted/provision-a-target-computer-wdk-8-1.md). After you have configured a test computer, the name of the test computer appears in the toolbar. Be sure you have select the test computer that you have configured for device you are testing with the HCK Test Suite.

Prepare the test computer as needed, by installing the device and driver and any additional requirements for test topology (see the HCK test prerequisites for the device you are testing). In place of the HCK Studio and HCK controller, you run the tests using Visual Studio and WDK 8.1.

### To select an HCK Test Suite to run on a test computer

1. From the **Driver** menu, select **Test** and then select **Test Group Explorer**.
1. In the **Driver Test Group Explorer** window, select one of the [HCK Test Suites](#hck-test-suites). When you select a Test Suite, the Test Suite appears in the **Driver Test Group** window.
1. Be sure you have selected the test computer that you have configured for device you are testing with the HCK Test Suite.
1. To use the HCK test suites, you must also follow the configuration requirements for the device you are testing.
1. You can use the check boxes to select the tests that match the architecture of the intended test computer (x86, x64, Arm).
1. From the **Driver** menu, select **Test &gt; Run test**. By default, the Run test command runs all of the tests in the currently selected test group.

You can also copy one of the provided HCK Test Suites and export it, along with the necessary test support files so that you can run the test suite from a Command Prompt window.

### To export a Test Suite

1. In the **Test Group Explorer**, select and hold (or right-click) the HCK Test Suite you want to copy and select **Export Test Suite...** from the short-cut menu. (The command runs the **CopyMe.cmd** script).
1. Select a destination folder for the test suite. You can export the test suite to a network share or to a USB flash drive.
1. To run the HCK Test Suite, open a Command Prompt window on the test computer with elevated permissions. Navigate to the destination directory and run the **RunMe.cmd** script. For more information, see [Run the HCK Test Suite from a Command Prompt window](#run-the-hck-test-suite-from-a-command-prompt-window).

## Run the HCK Test Suites from a Command Prompt window

### Copy the HCK Test Suite

1. Open a Visual Studio Command Prompt window. Navigate to the %WindowsSdkDir%\\Testing\\Tests\\HCK Tests\\Basic directory. For example, C:\\Program Files (x86)\\Windows Kits\\8.1\\Testing\\Tests\\HCK Tests\\Basic
1. Run the **CopyMe.cmd** script and specify the name of test suite and destination directory. The script has the following command line syntax:

    ```syntax
    CopyMe.cmd testSuite destinationPath
    ```

    The *testSuite* is one of the following:

    - Device.Device Fundamentals
    - Device.Graphics
    - Device.Imaging
    - Device.Network.MobileBroadband.CDMA
    - Device.Network.MobileBroadband.GSM
    - Device.Network.WLAN

    The *destinationPath* can be any valid path, including UNC paths. For example, you can copy an HCK Test Suite to a USB flash drive, or to a share on a server.

    ```cmd
    C:\Program Files (x86)\Windows Kits\8.1\Testing\Tests\HCK Tests\Basic>CopyMe "De
    vice.Device Fundamentals" d:\temp\devfund
    Copying test target setup installers
    Copying TAEF and WDTF infrastructure
    Copying debuggers infrastructure
    Copying x86 tools
    Copying x64 tools
    Copying arm tools
    Copying test suite
    Copy complete!

    Run on any computer using an administrator command prompt in the same folder as
    the RunMe.cmd script.
    "RunMe.cmd <infFileName>"
    ```

### Run the HCK Test Suite from a Command Prompt window

> [!NOTE]
> If the test computer is running Windows 7, you need to download and install the [Microsoft .NET Framework 4.5](https://www.microsoft.com/download/details.aspx?id=30653) before you can run the HCK Test Suite.

1. On the test computer that you have configured for testing, open a Command Prompt window with elevated privileges (**Run as administrator**) and navigate to the directory where you copied the HCK Test Suite.

1. Run the **RunMe.cmd** script and specify the path and name of the INF file. The script has the following command line syntax:

    ```syntax
    RunMe.cmd infFileName
    ```

    For example:

    ```cmd
    RunMe.cmd myDriver.inf
    ```

    > [!NOTE]
    > The Device.Graphics test suite does not make use of an INF file, however, the **RunMe.cmd** script requires an INF file. You can provide the name of substitute INF file if necessary.

## HCK Test Suites

- [HCK Tests.Basic.Device.Device Fundamentals Test Suite](#hck-testsbasicdevicedevice-fundamentals-test-suite)
- [HCK Tests.Basic.Device.Graphics Test Suite](#hck-testsbasicdevicegraphics-test-suite)
- [HCK Tests.Basic.Device.Imaging Test Suite](#hck-testsbasicdeviceimaging-test-suite)
- [HCK Tests.Basic.Device.Network.MobileBroadband.CDMA Test Suite](#hck-testsbasicdevicenetworkmobilebroadbandcdma-test-suite)
- [HCK Tests.Basic.Device.Network.MobileBroadband.GSM Test Suite](#hck-testsbasicdevicenetworkmobilebroadbandgsm-test-suite)
- [HCK Tests.Basic.Device.Network.WLAN Test Suite](#hck-testsbasicdevicenetworkwlan-test-suite)

For information about specifying test parameters, see [Device Fundamentals Test Parameters](how-to-select-and-configure-the-device-fundamental-tests.md). If the device under test under test or one of its child devices is a WiFi adapter or a network device, you might need to set the *Wpa2PskAesSsid*, *Wpa2PskPassword*, or *WDTFREMOTESYSTEM* parameters.

### HCK Tests.Basic.Device.Device Fundamentals Test Suite

Use this test suite for general reliability testing of all device types. You must follow the hardware, software, and test requirements for the HCK tests as described in the [Device.Fundamentals Reliability Testing Prerequisites](/previous-versions/windows/hardware/hck/jj191690(v=vs.85)). In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Device Fundamentals Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Device.Fundamentals Reliability Testing Prerequisites](/previous-versions/windows/hardware/hck/jj191690(v=vs.85)) |
| **Test descriptions** | [DF - PNP (disable and enable) with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn260411(v=vs.85))<br>[DF - Sleep with IO Before and After (Basic)](/previous-versions/windows/hardware/hck/dn247481(v=vs.85)) |

### HCK Tests.Basic.Device.Graphics Test Suite

Use this test suite to test graphics adapters or chipsets. You must follow the hardware, software, and test requirements for the HCK tests as described in the [Graphic Adapter or Chipset Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998923(v=vs.85)). In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Graphics Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Graphic Adapter or Chipset Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998923(v=vs.85)) |
| **Test descriptions** | [Graphic Adapter or Chipset Tests](/previous-versions/windows/hardware/hck/hh998416(v=vs.85)) |

### HCK Tests.Basic.Device.Imaging Test Suite

Use this test suite to test printers. The test suite uses tests that are part of the HCK [Device.Imaging Testing](/previous-versions/windows/hardware/hck/jj123724(v=vs.85)). In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Imaging Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Printer Testing Prerequisites](/previous-versions/windows/hardware/hck/jj124568(v=vs.85)) |
| **Test descriptions** | [Printer Tests](/previous-versions/windows/hardware/hck/hh998007(v=vs.85)) |

### HCK Tests.Basic.Device.Network.MobileBroadband.CDMA Test Suite

Use this test suite to test Mobile Broadband CDMA devices. Follow the guidelines for setting up and configuring your device as described in the [Mobile Broadband Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998960(v=vs.85)). In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Network.MobileBroadband.CDMA Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Mobile Broadband Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998960(v=vs.85)) |
| **Test descriptions** | [CDMA Tests](/previous-versions/windows/hardware/hck/dn293733(v=vs.85)) |

### HCK Tests.Basic.Device.Network.MobileBroadband.GSM Test Suite

Use this test suite to test Mobile Broadband GSM devices. Follow the guidelines for setting up and configuring your device as described in the [Mobile Broadband Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998960(v=vs.85)). In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Network.MobileBroadband.GSM Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Mobile Broadband Testing Prerequisites](/previous-versions/windows/hardware/hck/hh998960(v=vs.85)) |
| **Test descriptions** | [GSM Tests](/previous-versions/windows/hardware/hck/dn247238(v=vs.85)) |

### HCK Tests.Basic.Device.Network.WLAN Test Suite

Use this test suite to test Wireless LAN (802.11) devices. Follow the guidelines for setting up and configuring your device as described in the [Wireless LAN (802.11) Testing Prerequisites](/previous-versions/windows/hardware/hck/jj123847(v=vs.85)) for the HCK. In place of the HCK Studio and HCK controller, you run the basic tests using Visual Studio and WDK 8.1.

| HCK Tests.Basic.Device.Network.WLAN Test Suite | &nbsp; |
|--|--|
| **Hardware, software, and test requirements** | [Wireless LAN (802.11) Testing Prerequisites](/previous-versions/windows/hardware/hck/jj123847(v=vs.85)) |
| **Test descriptions** | [WLAN L1 Tests](/previous-versions/windows/hardware/hck/dn247288(v=vs.85)) |

## Related topics

- [How to test a driver a runtime using Visual Studio](testing-a-driver-at-runtime.md)
- [How to select and configure the Device Fundamentals Tests](how-to-select-and-configure-the-device-fundamental-tests.md)
- [Deploying a Driver to a Test Computer](deploying-a-driver-to-a-test-computer.md)
- [Getting Started with Windows Debugging](../debugger/getting-started-with-windows-debugging.md)
- [Hardware Certification Program](/previous-versions/windows/hardware/hck/jj124227(v=vs.85))
- [Windows Hardware Certification Kit (HCK)](/windows-hardware/test/hlk/)
- [How to test a driver at runtime from a Command Prompt](how-to-test-a-driver-at-runtime-from-a-command-prompt.md)
