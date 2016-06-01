---
Description: 'SPI test modules that are included in the MITT software package can be used to test data transfers for a SPI controller on the system under test and its driver. The MITT board acts as a client device connected to the SPI bus.'
MS-HAID: 'SPB.spi\_tests\_in\_mitt'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
title: SPI tests in MITT
author: windows-driver-content
---

# SPI tests in MITT


**Last updated**

-   January, 2015

**Applies to:**

-   Windows 8.1

SPI test modules that are included in the MITT software package can be used to test data transfers for a SPI controller on the system under test and its driver. The MITT board acts as a client device connected to the SPI bus.

## Before you begin...


-   Get a MITT board and a SPI or UART adapter board. See [Buy hardware for using MITT](buses.multi_interface_test_tool__mitt__).
-   [Download the MITT software package](buses.mitt_software_package). Install it on the system under test.
-   Install MITT firmware on the MITT board. See [Get started with MITT](buses.get_started_with_mitt___).

## Hardware setup


![spi mitt test](images/spi.jpg)

| Bus interface | Pin-out                                      | ACPI and schematics | Connection solution                  |
|---------------|----------------------------------------------|---------------------|--------------------------------------|
| SPI           | All lines needed (SCLK, MISO, MOSI, SS, GND) | ACPI table          | Simple block header (on debug board) |

 

1.  Connect the SPI adapter to **JC1** on the MITT board.
2.  Use the jumper on the SPI adapter board to select the correct SPI voltage. The jumper can be used to select between 3.3V and 1.8V.
3.  Connect SCLK, MOSI, MISO, SS, and GND to the system under test.

    ![spi wiring](images/spiwiring.png)

4.  On the MITT board, set switch **SW1** to the high position. This position enables the default mode for SPI when the MITT is powered. You can directly connect the board (without the SPI adapter board) if the signal is at 3.3V.

    ![spi power](images/spi-power.png)

## <a href="" id="test-driver-and-acpi-configuration--"></a>Test driver and ACPI configuration


Perform these steps on the system under test that has the I²C controller:

1.  Install WITTTest driver included in the MITT software package by running this command:

    **pnputil –a witttest.inf**

    ![intall witt driver for the mitt board](images/mitt-install-witt.png)

    **Note**  PnpUtil.exe is included in %SystemRoot%\\System32.

     

2.  Modify the system ACPI and include this ASL table. You can use the [Microsoft ASL compiler](p_oembringup.microsoft_asl_compiler).

    **Note**  Change "\\\\\_SB\_.SPI1" to ACPI entry name for the SPI controller to test as shown here. It defines three test targets with SPI frequency at 1Mhz, 5Mhz, and 20Mhz.

     

    ``` syntax
    Device(TP1) {
        Name (_HID, "SPT0001") 
        Name (_CID, "WITTTest") 
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
              SpiSerialBus (0x0000, PolarityLow, FourWireMode, 0x08,ControllerInitiated, 0x000F4240, ClockPolarityLow,ClockPhaseFirst, "\\_SB.SPI1", 0x00, ResourceConsumer, , )
          })
          Return(RBUF)
        }
    }
    Device(TP2) {
        Name (_HID, "SPT0002") 
        Name (_CID, "WITTTest") 
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
              SpiSerialBus (0x0000, PolarityLow, FourWireMode, 0x08,ControllerInitiated, 0x004c4b40, ClockPolarityLow,ClockPhaseFirst, "\\_SB.SPI1", 0x00, ResourceConsumer, , )
          })
          Return(RBUF)
        }
    }
    Device(TP3) {
        Name (_HID, "SPT0003") 
        Name (_CID, "WITTTest") 
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
              SpiSerialBus (0x0000, PolarityLow, FourWireMode, 0x08,ControllerInitiated, 0x01312d00, ClockPolarityLow,ClockPhaseFirst, "\\_SB.SPI1", 0x00, ResourceConsumer, , )
          })
          Return(RBUF)
        }
    }

    ```

## <a href="" id="spi-automation-tests--"></a>SPI automation tests


1.  Create a folder on the system under test.
2.  Copy the TAEF binaries to the folder and then add it to your PATH environment variable. The required TAEF binaries are in %ProgramFiles(x86)%\\Windows Kits\\8.1\\Testing\\Runtimes\\TAEF .
3.  Copy Muttutil.dll and Mittspitest.dll from the MITT software package to the folder.
4.  View all MITT SPI tests by using the **/list** option:

You are now ready to run SPI tests. You can run a single test, all tests at once, or run tests manually.

-   Run a single test by using the **/name:*&lt;test name&gt;*** option. This command runs the BasicIORead test:
-   Run all tests by using this command:
-   Run tests manually by using SPBCmd.exe tool included in the MITT software package.

## SPI adapter schematic


![spi schematic](images/spi-schematic.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5BSPB\buses%5D:%20SPI%20tests%20in%20MITT%20%20RELEASE:%20%286/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")


