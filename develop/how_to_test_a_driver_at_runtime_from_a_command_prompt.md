How to test a driver at runtime from a Command Prompt
======================================================================================================================================

The WDK provides device testing components that enable you to test a driver on a test computer on your network. You can use these components outside of Visual Studio by copying and installing the necessary files. You can use these components to run the same collection of device driver tests that are available in Visual Studio to test the features and functions of your driver.

Starting in WDK 8.1, you can copy and run the HCK Test Suites on test computers using command scripts. See [How to run the HCK Test Suites in WDK 8.1](run_the_hck_test_suites_in_the_wdk.md).

### <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites

-   Install Visual Studio and the WDK on the computer you use for development.
-   From Visual Studio, you can configure and provision computers for testing. When you configure the test computer, the WDK driver test framework automatically enables the test computer for remote debugging and transfers the necessary test binaries and support files. If you have not already done so, follow the instructions in [Provision a computer for driver deployment and testing (WDK 8.1)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn745909)
-   Although it is not recommended, you can also install the necessary test components manually. Follow the instructions to install the [Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439725) and WDTF on the test computer. See [Manually installing and uninstalling TAEF on a test computer](https://msdn.microsoft.com/En-US/Library/Windows/Hardware/hh439627#manual_install_taef) and [Manually installing WDTF on a test computer](https://msdn.microsoft.com/En-US/Library/Windows/Hardware/hh831856#manual_install_wdtf).

Instructions
------------

### <span id="Copy_the_tests_to_the_test_computer"></span><span id="copy_the_tests_to_the_test_computer"></span><span id="COPY_THE_TESTS_TO_THE_TEST_COMPUTER"></span>Step 1: Copy the tests to the test computer

-   Copy the [Device Fundamentals Tests](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673011) from the computer you use for development. Copy the folder %ProgramFiles%\\Windows Kits\\8.0\\Testing\\Tests\\Device Fundamentals to the test computer.

### <span id="Run_the_tests"></span><span id="run_the_tests"></span><span id="RUN_THE_TESTS"></span>Step 2: Run the tests

The TAEF command to run the tests uses the following syntax:

``` syntax
Te.exe [/name:<Test Method>] [<Test Name>.dll | <Test Name.wsc> ]  [/rebootStateFile=<file> ] [/enablewttlogging]  [/P:"DQ= <>" ]  
```

Remarks
-------

You must specify the test binary (.dll) or script (.wsc) file. The test method (**/name:***&lt;test method&gt;*) is optional. For the test names and test methods, see the [Device Fundamentals Tests](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673011). For information about specifying test parameters, see [Device Fundamentals Test Parameters](how_to_select_and_configure_the_device_fundamental_tests.md) and [Te.exe Command Options](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439743) .

For example, to run all PnP tests in the Devfund\_PnPDTest.dll on a device with a specific device ID.

``` syntax
Te.exe  Devfund_PnPDTest.dll /P:"DQ=DeviceID='USB\ROOT_HUB\4&1CD5D022&0'"
```

For example, to run PnP Surprise Remove test on a device with a specific device ID.

``` syntax
Te.exe /name:"*PNPSurpriseRemoveAndRestartDevice" Devfund_PnPDTest.dll /P:"DQ=DeviceID='USB\ROOT_HUB\4&1CD5D022&0'"
```

<span id="related_topics"></span>Related topics
-----------------------------------------------

* [Device Fundamentals Tests](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/JJ673011)
* [Device Fundamentals Test Parameters](how_to_select_and_configure_the_device_fundamental_tests.md)
* [How to run the HCK Test Suites in WDK 8.1](run_the_hck_test_suites_in_the_wdk.md)
* [Test Authoring and Execution Framework (TAEF)](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439725)
* [Te.exe Command Options](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439743)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[VsDriver\vsdriver]:%20How%20to%20test%20a%20driver%20at%20runtime%20from%20a%20Command%20Prompt%20%20RELEASE:%20%289/30/2015%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default. "Send comments about this topic to Microsoft")


