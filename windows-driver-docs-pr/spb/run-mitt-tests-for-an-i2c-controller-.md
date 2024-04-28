---
title: I2C Controller Tests in MITT
description: I2C test modules that are included in the MITT software package can be used to test data transfers for an I2C controller and its driver. The MITT board acts as a client device connected to the I2C bus.
ms.date: 01/12/2024
---

# I2C controller tests in MITT

I<sup>2</sup>C test modules that are included in the MITT software package can be used to test data transfers for an I<sup>2</sup>C controller and its driver. The MITT board acts as a client device connected to the I<sup>2</sup>C bus.

## Before you begin

- Get a MITT board and an I<sup>2</sup>C adapter board. See [Buy hardware for using MITT](./multi-interface-test-tool--mitt--.md).
- [Download the MITT software package](download-the-mitt-software-package.md). Install it on the system under test.
- Install MITT firmware on the MITT board. See [Get started with MITT](./get-started-with-mitt---.md).

## Hardware setup

:::image type="content" source="images/i2csetup.png" alt-text="Picture of the MITT I2C hardware setup.":::

| Bus interface | Pin-out | ACPI and schematics | Connection solution |
|---|---|---|---|
| I<sup>2</sup>C | All lines needed (SCL, SDA and GND) | ACPI table | Simple male block (on debug board) |

1. Connect the I<sup>2</sup>C adapter to **JB1** on the MITT board.

    :::image type="content" source="images/i2cheader.png" alt-text="Picture of the MITT I2C header.":::

2. Use the jumper on to the I<sup>2</sup>C header (above **JB1**) to select the correct I<sup>2</sup>C voltage between 3.3V and 1.8V. In this image, 1.8V is selected.
3. Connect SCL, SDA, and GND pins on the adapter board to the exposed SCL, SDA, and GND lines on the system under test.

    :::image type="content" source="images/i2c-power.png" alt-text="Picture of the I2C adapter.":::

4. Use the jumper on the I2C adapter board to select the correct I2C voltage between 3.3V and 1.8V. In this image, the 1.8V is selected.
5. On the MITT board, set switch **SW0** to the high position. This position enables the default mode for I<sup>2</sup>C when the MITT is powered.

    :::image type="content" source="images/sw0.png" alt-text="Picture of SW0 on the MITT board.":::

6. Use the **RESET** button to power cycle the MITT board. If the wire connections to the I<sup>2</sup>C controller are correct, **LD7** (SDA indicator) and **LD6** (SCL indicator) turn on. If either LED doesn't turn on, there's a wiring issue because either SDA or, SCL, or both are pulled low.

## Test driver and ACPI configuration

Perform these steps on the system under test that has the I<sup>2</sup>C controller:

1. Install WITTTest driver included in the MITT software package by running this command:

    `pnputil -a WittTest.inf`

    ```output
    Microsoft PnP Utility

    Processing inf :            WittTest.inf
    Driver package added successfully.
    Published name :            oem6.inf

    Total attempted:              1
    Number successfully imported: 1
    ```

    >[!NOTE]
    >[PnpUtil.exe](../devtest/pnputil.md) is included in %SystemRoot%\\System32.

2. Modify the system ACPI and include this ASL table. You can use the [Microsoft ASL compiler](../bringup/microsoft-asl-compiler.md).

    >[!NOTE]
    >Change "\\\\\_SB\_.I2C2" to ACPI entry name for the I<sup>2</sup>C controller to test.

    ```asl
    //TP1 100Khz Standard Target Device(TP1)
    Device(TP1) {
        Name (_HID, "STK0001")
        Name (_CID, "WITTTest")
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
            I2CSerialBus ( 0x11, ControllerInitiated, 100000,AddressingMode7Bit, "\\_SB_.I2C2",,, , )
          })
          Return(RBUF)
        }
    }
    
    //TP2 400Khz  Fast Target
    Device(TP2) {
        Name (_HID, "STK0002")
        Name (_CID, "WITTTest")
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
            I2CSerialBus ( 0x12, ControllerInitiated, 400000,AddressingMode7Bit, "\\_SB_.I2C2",,, , )
          })
          Return(RBUF)
        }
    }
    
    //TP3 1 Mhz  FastPlus Target
    Device(TP3) {
        Name (_HID, "STK0003")
        Name (_CID, "WITTTest")
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
            I2CSerialBus ( 0x13, ControllerInitiated, 1000000,AddressingMode7Bit, "\\_SB_.I2C2",,, , )
          })
          Return(RBUF)
        }
    }
    
    //TP4 1.4 Mhz High Speed, optional target
    Device(TP4) {
        Name (_HID, "STK0004")
        Name (_CID, "WITTTest")
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
            I2CSerialBus ( 0x14, ControllerInitiated, 1400000,AddressingMode7Bit, "\\_SB_.I2C2",,, , )
          })
          Return(RBUF)
        }
    }
    
    //TP5 3.4 Mhz High Speed, optional target
    Device(TP5) {
        Name (_HID, "STK0005")
        Name (_CID, "WITTTest")
        Method(_CRS, 0x0, NotSerialized)
        {
          Name (RBUF, ResourceTemplate ()
          {
            I2CSerialBus ( 0x15, ControllerInitiated, 3400000,AddressingMode7Bit, "\\_SB_.I2C2",,, , )
          })
          Return(RBUF)
        }
    }
    ```

    >[!NOTE]
    >Only TP1-3 are required to run MITT I<sup>2</sup>C tests. TP4 and TP5 are optional targets.

## I<sup>2</sup>C automation tests

1. Create a folder on the system under test.
2. Copy the TAEF binaries to the folder and then add it to your PATH environment variable. The required TAEF binaries are in %ProgramFiles(x86)%\\Windows Kits\\8.1\\Testing\\Runtimes\\TAEF .
3. Copy Muttutil.dll and Mitti2ctest.dll from the MITT software package to the folder.
4. View all MITT I<sup>2</sup>C tests by using the **/list** option:

    `"C:\Program Files (x86)\Windows Kits\10\Testing\Runtimes\TAEF\te" MITTI2CTest.dll /list`

    ```output
    Test Authoring and Execution Framework v3.7k for x64


            C:\Program Files(x86)\MITT\x64\MITTI2CTest.dll
                MITTI2CTest
                    MITTI2CTest::BasicIORead
                    MITTI2CTest::BasicIOWrite
                    MITTI2CTest::BasicIOSeq
                    MITTI2CTest::BasicIOKernel
                    MITTI2CTest::DeviceNACK
                    MITTI2CTest::LockUnlock
                    MITTI2CTest::CancelRead
                    MITTI2CTest::CancelWrite
                    MITTI2CTest::CancelSequence
                    MITTI2CTest::ClockStretching
                    MITTI2CTest::PerfRead
                    MITTI2CTest::PerfWrite
                    MITTI2CTest::PerfSequence
                    MITTI2CTest::BusRecovery
                    MITTI2CTest::Power
                    MITTI2CTest::Stress
    ```

You're now ready to run I<sup>2</sup>C tests. You can run a single test, all tests at once, or run tests manually.

- Run a single test by using the **/name:*&lt;test name&gt;*** option. This command runs the BasicIORead test:

  `"C:\Program Files (x86)\Windows Kits\10\Testing\Runtimes\TAEF\te" MITTI2CTest.dll /name:MITTI2CTest::BasicIORead`

- Run all tests by using this command:

  `"C:\Program Files (x86)\Windows Kits\10\Testing\Runtimes\TAEF\te" MITTI2CTest.dll`

- Run tests manually by using SPBCmd.exe tool included in the MITT software package.

## I<sup>2</sup>C adapter schematic

:::image type="content" source="images/i2c-schematic.png" alt-text="I2C adapter schematic diagram.":::
