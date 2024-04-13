---
title: Generate ACPI Tables by Using AcpiGenFx
description: Use the ACPI Generation Framework (AcpiGenFx) library to write an app that generates ACPI tables.
ms.date: 03/23/2023
---

# Generate ACPI tables by using AcpiGenFx

> [!NOTE]
> Microsoft supports a diverse and inclusive environment. This article contains references to terminology that the Microsoft [style guide for bias-free communication](/style-guide/bias-free-communication) recognizes as exclusionary. The word or phrase is used in this article for consistency because it currently appears in the software. When the software is updated to remove the language, this article will be updated to be in alignment.

## Summary

- Create a .NET app that uses AcpiGenFx to generate ACPI tables

## Applies to

- Windows 10

- Windows SoC and platform bring-up

## Important APIs

- Open AcpiGenFx in Object Browser

- Use the IntelliSense feature in Visual Studio to determine methods and properties

Use the ACPI Generation Framework (AcpiGenFx) library to write an app that generates ACPI tables.

In Windows 10, the new C# library, AcpiGenFx, makes it easier for you to write an app that creates ACPI tables that describe the hardware devices and resources on the platform, such as interrupt controllers, SD host controllers, GPIO, and I<sup>2</sup>C devices. By using the methods and properties exposed by the framework objects, you can describe devices, resources, and dependencies without knowing the exact syntax of the ACPI table or referring to the ACPI specification. Not only does AcpiGenFx generate ACPI Machine Language (ASL) code that is OS-independent, it is also aware of Windows-specific requirements.

The app generates the relevant ACPI table files (\*.aslc and \*.asl) based on those descriptions. At build time, AcpiGenFx statically analyzes the platform description, detecting errors like cyclical or unresolved dependencies, device naming and UUID conflicts, resource to controller mappings, and much more. As a result, the generated ASL code is easier to debug because AcpiGenFx checks for the most common mistakes, and abstracts unique ACPI implementation details.

AcpiGenFx is declarative in nature: its output is static data only, and it is not designed to generate dynamic runtime methods. If a use case is not covered by the framework, such as advanced off-SoC peripheral device power management, the methods must be either implemented in a Windows Platform Extension driver or manually added to the AcpiGenFx-generated ASL code.

## Before you begin

Locate the following files in the **AcpiGenFx** folder of your WDK installation.

AcpiGenFx.dll and associated samples are available in the Tools folder of the WDK. In the Tools directory, navigate to the target architecture folder, then to the AcpiGenFx folder. For example, the x86 version is located in C:\Program Files (x86)\Windows Kits\10\Tools\x86\ACPIGenFx.

- AcpiGenFx.dll

    Required to use ACPIGenFx.

- DSDTSamples

    Use this project as a starting point to design the ACPI firmware for the entire platform. The output is a full set of ACPI tables including the DSDT, FADT, and MADT.

- SSDTSamples

    Use this project as a starting point to add a peripheral device to an existing system. The sample demonstrates how to describe a sensor device and its resources. The output is an ACPI SSDT table in ASL.

Download Windows 10 kits, tools, and code samples.

- [Microsoft Visual Studio](https://visualstudio.microsoft.com/)

- [Windows Driver Kit (WDK) for Windows 10](../download-the-wdk.md)

- [Windows Driver Kit (WDK) samples](https://github.com/Microsoft/Windows-driver-samples)

## Create a platform

1. In Visual Studio, open a new C# console project.

1. Add a reference to the AutoAcpi.dll assembly. Under the **Project** menu, click **Add Reference**. Click **Browse** and navigate to the location of AutoAcpi.dll. Click **OK**.

1. In **Solution Explorer**, expand **References** and select **acpigenfx**. View the objects in Object Browser (**View &gt; Object Browser**).

1. Target .NET Framework 4.5 or later. Open project properties. On the **Application** page, make sure **Target framework** is set to **.NET Framework 4.5**.

1. Add the `Using` directive for the AutoAcpi object at the beginning of the code for the application.

1. Create a platform object. Based on your architecture, instantiate a **Platform** object by calling **Platform.CreateArmPlatform** or **Platform.Createx86Platform**. Specify *OEMID*, *OEMTableID*, *Creator*, *Revision*, and *FileName*.

1. Call **Platform.WriteAsl** to write to a file.

    This example shows how to instantiate the platform.

    ```cs
    using AutoAcpi;

    namespace ACPI
    {
        class Program
        {
            static void Main(string[] args)
            {
                ArmPlatform myPlatform = Platforms.CreateArmPlatform(
                    OEMID: "MSFT",
                    OEMTableID: "EDK2",
                    CreatorID: "MSFT",
                    Revision: 1,
                    FileName: "Platform");

                myPlatform.WriteAsl();
            }
        }
    }
    ```

1. Click **Start** to build and run your app. Visual Studio displays build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.).

1. Open the folder named under *project*\\bin\\*Debug or Release*\\Output. The Output folder contains files generated by the app. View the contents of SSDT.asl.

    Here is the output of the preceding example.

    ```console
    DefinitionBlock ("Platform.aml", "DSDT", 5, "MSFT", "EDK2", 1)
    {
        Scope (\_SB_)
        {
        }

    }
    ```

The app generates two additional folders: Aslc and Bin. Aslc contains all the firmware tables in the aslc format. Bin contains all the firmware tables in the binary blob format.

Compile the ASL code files to an ACPI Machine Language (AML) binary by using the asl.exe compiler provided in the WDK.

## Add devices and resources in the DSDT

You can add components to the platform. Typically, those components include processors, bus controllers, power resources, and so on. Here are some components that are used in DSDTSamples.

| Object type | Creation method | Component |
|--|--|--|
| ACAdapter | Platform.AddACAdapter | Add an AC adapter. |
| BatteryDevice | Platform.AddBatteryDevice<br><br>BatteryDevice.ThermalLimit | Add a battery device and specify its thermal limit. |
| ButtonArrayDevice | Platform.AddButtonArrayDevice<br><br>ButtonArrayDevice.AddBackButton<br><br>ButtonArrayDevice.AddCameraShutterButton<br><br>ButtonArrayDevice.AddCameraAutofocusButton<br><br>ButtonArrayDevice.AddGenericButton<br><br>ButtonArrayDevice.AddPowerButton<br><br>ButtonArrayDevice.AddRotationLockButton<br><br>ButtonArrayDevice.AddSearchButton<br><br>ButtonArrayDevice.AddVolumeDownButton<br><br>ButtonArrayDevice.AddVolumeUpButton<br><br>ButtonArrayDevice.AddWindowsHomeButton | Add buttons such as Windows Home, Back, Volume +/-, Power, Rotation Lock, and Search. |
| DisplaySensor | Platform.AddDisplaySensor | Add a display sensor. |
| GenericDevice | Platform.AddGenericDevice | Add a generic device that can be used to replace any type of internally supported device in the framework. |
| GpioController | Platform.AddGpioController | Add GPIO controllers and associated resources such as interrupts, I/O, and events. |
| HidOverI2C | Platform.AddHidI2CDevice | Add a HID device connected to the I<sup>2</sup>C bus. |
| I2CController | Platform.AddI2CController | Add I<sup>2</sup>C controllers and associated resources such as interrupts, I/O, and events. |
| KDNet2Usb | Platform.AddKDNet2Usb | Add support for kernel debugging by using Kdnet over USB. |
| PEPDevice | Platform.AddPepDevice | Add PEP devices and their resources and methods that return packages and static types. |
| Processor<br><br>ProcessorAggregator | Platform.AddProcessor<br><br>Platform.AddProcessorAggregator | Add processors and processor aggregators. |
| RTCDevice | Platform.AddRTCDevice | Add ACPI time and alarm devices. |
| SdHostController | Platform.AddSdHostController | Add SD host controllers. |
| SerialPort | Platform.AddSerialPort | Add support for serial and UART devices. |
| ThermalZone | Platform.AddThermalZone | Add thermal zones and associated sampling and polling periods. |
| XhciUsbController<br><br>EhciUsbController<br><br>UsbDevice | Platform.AddEhciUsbController<br><br>Platform.AddXhciUsbController<br><br>EhciUsbController.AddUsbDevice<br><br>XhciUsbController.AddUsbDevice<br><br>UsbDevice.AddUsbDevice | Add USB host controllers and the child devices (including hubs). |

To view the complete list, open AcpiGenFx in **Object Browser**. Use IntelliSense to determine the methods (and the parameters) and properties exposed by the objects. For example code that shows how to add the classes and set properties that are listed in the preceding table, refer to the DSDTSamples project.

## Add debug support

To set a port as debuggable, set the **DebugEnabled** property on the object to "true".

For example, you might want to describe an xHCI host controller with USB debug port. In your app, call **Platform.AddXhciUsbController** to get an **XhciUsbController** object and set the **DebugEnabled** property to "true". AcpiGenFx generates a Microsoft DBG2 table that is automatically included in the app's Output\\Aslc folder.

Here is an example of how to add an xHCI host controller and declare it as debuggable.

```cs
XhciUsbController usb1 = Platform.AddXhciUsbController("USB1", "XHCICONT", 0);
usb1.Description = "USB Controller with Debug Support";

Memory32Fixed mem = usb1.AddMemory32Fixed(true, 0xf9000000, 0xfffff, "");
usb1.AddMemory32Fixed(true, 0xf7000000, 0xfffff, "");
usb1.AddInterrupt(InterruptType.Level, InterruptActiveLevel.ActiveHigh, SharingLevel.Shared, 0x8);
usb1.AddInterrupt(InterruptType.Level, InterruptActiveLevel.ActiveHigh, SharingLevel.Shared, 0x9);

usb1.DebugEnabled = true;
mem.DebugAccessSize = DebugAccessSize.DWordAccess;
```

In the preceding snippet, the xHCI host controller has interrupt resources and debug support. It has dependencies on a PEP device and a GPIO controller. To see descriptions of those devices, see DSDTSamples.

This example shows how to add an I<sup>2</sup>C controller to the DSDT.

```cs
I2CController i2c = Platform.AddI2CController("I2C1", "I2CCONTR", 0);
i2c.AddMemory32Fixed(true, 0xf9999000, 0x400, "");
i2c.AddInterrupt(InterruptType.Level, InterruptActiveLevel.ActiveHigh, SharingLevel.Exclusive, 40);
```

Here is the output of the console app with the preceding definition for xHCI host and I<sup>2</sup>C controllers.

```console
DefinitionBlock ("Platform.aml", "DSDT", 5, "MSFT", "EDK2", 1)
{
    Scope (\_SB_)
    {
        //
        // Description: USB Controller with Debug Support
        //

        Device (USB1)
        {
            Name (_HID, "XHCICONT")
            Name (_CID, "PNP0D10")
            Name (_UID, 0x0)
            Method (_STA)
            {
                Return(0xf)
            }
            Method (_CRS, 0x0, NotSerialized) {
                Name (RBUF, ResourceTemplate () {
                    MEMORY32FIXED(ReadWrite, 0xF9000000, 0xFFFFF, )
                    MEMORY32FIXED(ReadWrite, 0xF7000000, 0xFFFFF, )
                    Interrupt(ResourceConsumer, Level, ActiveHigh, Shared) { 0x8 }
                    Interrupt(ResourceConsumer, Level, ActiveHigh, Shared) { 0x9 }
                })
                Return(RBUF)
            }
        }

        //
        // Description: This is an i2cController.
        //

        Device (I2C1)
        {
            Name (_HID, "I2CCONTR")
            Name (_CID, "")
            Name (_UID, 0x0)
            Method (_STA)
            {
                Return(0xf)
            }
            Method (_CRS, 0x0, NotSerialized) {
                Name (RBUF, ResourceTemplate () {
                    MEMORY32FIXED(ReadWrite, 0xF9999000, 0x400, )
                    Interrupt(ResourceConsumer, Level, ActiveHigh, Exclusive) { 0x28 }
                })
                Return(RBUF)
            }
        }

    }

}  
```

After building the project, in the project directory navigate to Output\\Aslc. The Dbg2.aslc file contains the DB2 table shown here:

```asl
// Debug Port Table (DBG2)
// Automatically generated by AutoAcpi

#include "AutoACPI.h"
char DBG2[112] = {
    0x44, 0x42, 0x47, 0x32, 0x70, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x4D, 0x53, 0x46, 0x54, 0x20, 0x20, 0x45, 0x44, 0x4B, 0x32,
    0x20, 0x20, 0x20, 0x20, 0x01, 0x00, 0x00, 0x00, 0x4D, 0x53,
    0x46, 0x54, 0x01, 0x00, 0x00, 0x00, 0x2C, 0x00, 0x00, 0x00,
    0x01, 0x00, 0x00, 0x00, 0x00, 0x44, 0x00, 0x02, 0x0E, 0x00,
    0x36, 0x00, 0x00, 0x00, 0x44, 0x00, 0x02, 0x80, 0x00, 0x00,
    0x00, 0x00, 0x16, 0x00, 0x2E, 0x00, 0x00, 0x00, 0x00, 0x03,
    0x00, 0x00, 0x00, 0xF9, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x01, 0x00, 0x00, 0x00, 0xF7, 0x00, 0x00, 0x00, 0x00,
    0xFF, 0xFF, 0x0F, 0x00, 0xFF, 0xFF, 0x0F, 0x00, 0x22, 0x5C,
    0x5C, 0x5F, 0x53, 0x42, 0x5F, 0x2E, 0x55, 0x53, 0x42, 0x31,
    0x22, 0x00
};

void * ReferenceDBG2Table(void) {
    return (void *) &DBG2;
}
```

## Add an ACPI description for a peripheral device in the SSDT

1. Create a platform object by calling **Platform.CreateArmPlatform** or **Platform.Createx86Platform**.

1. Set the **SSDT** property to true. This indicates to the framework that this table is an SSDT.

1. Create a device and assign resources. For example, for the sensor device shown here, the sample calls **Platform.AddGenericDevice** and specifies the device name, hardware ID, and unique instance. The sensor device that connects to the I<sup>2</sup>C serial bus, I2C1, which is described in the DSDT.

```asl
namespace SSDTSample
{
    class Program
    {
        static void Main(string[] args)
        {

          ArmPlatform Platform = Platforms.CreateArmPlatform(
                OEMID: "MSFT",
                OEMTableID: "EDK2",
                CreatorID: "MSFT",
                Revision: 1,
                FileName: "SSDT"
                );

            platform.SSDT = true;

            var sensor = platform.AddGenericDevice("ADXL", "ACPI\\ADXL345Acc", 1);

            sensor.AddI2CSerialBus(
                SlaveAddress: 0x1d,
                Mode: SlaveMode.ControllerInitiated,
                ConnectionSpeed: 400000,
                addressmode: AddressMode._7Bit,
                controllername: "I2C1"
                );

            platform.WriteAsl();

        }
    }
}
```

Here is the output of the preceding example.

```console
DefinitionBlock ("SSDT.aml", "SSDT", 5, "MSFT", "EDK2", 1)
{
    Scope (\_SB_)
    {

        Device (ADXL)
        {
            Name (_HID, "ACPI\ADXL345Acc")
            Name (_UID, 0x1)
            Method (_STA)
            {
                Return(0xf)
            }
            Method (_CRS, 0x0, NotSerialized) {
                Name (RBUF, ResourceTemplate () {
                    I2CSerialBus(0x1D, ControllerInitiated, 0x61A80, AddressingMode7Bit, "I2C1", 0, ResourceConsumer, , RawDataBuffer() { 0 })
                })
                Return(RBUF)
            }
        }

    }

}
```

## Replacing ACPI firmware during development and testing

In development and test scenarios, you can replace the AML binary that is generated from the asl.exe compiler on the device. To do this, rename the AML binary to acpitabl.dat and move it to %windir%\\system32. At boot time, Windows replaces tables present in the ACPI firmware with those in acpitabl.dat.

Make sure that test signing is enabled with the command:

```console
bcdedit /set testsigning on
```

## Related topics

[ACPI system description tables](acpi-system-description-tables.md)
