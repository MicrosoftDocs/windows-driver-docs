---
title: Generate ACPI tables by using AcpiGenFx
description: Use the ACPI Generation Framework (AcpiGenFx) library to write an app that generates ACPI tables.
ms.assetid: 46A725C3-609E-45B9-A4BD-033656208E92
ms.date: 06/26/2018
ms.localizationpriority: medium
---

# Generate ACPI tables by using AcpiGenFx


**Summary**

-   Create a .NET app that uses AcpiGenFx to generate ACPI tables

**Applies to**

-   Windows 10
-   Windows SoC and platform bring-up

**Important APIs**

-   Open AcpiGenFx in Object Browser
-   Use the IntelliSense feature in Visual Studio to determine methods and properties

Use the ACPI Generation Framework (AcpiGenFx) library to write an app that generates ACPI tables.

In Windows 10, the new C# library, AcpiGenFx, makes it easier for you to write an app that creates ACPI tables that describe the hardware devices and resources on the platform, such as interrupt controllers, SD host controllers, GPIO, and I²C devices. By using the methods and properties exposed by the framework objects, you can describe devices, resources, and dependencies without knowing the exact syntax of the ACPI table or referring to the ACPI specification. Not only does AcpiGenFx generate ACPI Machine Language (ASL) code that is OS-independent, it is also aware of Windows-specific requirements.

The app generates the relevant ACPI table files (\*.aslc and \*.asl) based on those descriptions. At build time, AcpiGenFx statically analyzes the platform description, detecting errors like cyclical or unresolved dependencies, device naming and UUID conflicts, resource to controller mappings, and much more. As a result, the generated ASL code is easier to debug because AcpiGenFx checks for the most common mistakes, and abstracts unique ACPI implementation details.

AcpiGenFx is declarative in nature: its output is static data only, and it is not designed to generate dynamic runtime methods. If a use case is not covered by the framework, such as advanced off-SoC peripheral device power management, the methods must be either implemented in a Windows Platform Extension driver or manually added to the AcpiGenFx-generated ASL code.

## Before you begin...

Locate the following files in the **AcpiGenFx** folder of your WDK installation.

> [!NOTE]
> AcpiGenFx.dll and associated samples are available in the Tools folder of the WDK. In the Tools directory, navigate to the target architecture folder, then to the AcpiGenFx folder. For example, the x86 version is located in C:\Program Files (x86)\Windows Kits\10\Tools\x86\ACPIGenFx.

-   AcpiGenFx.dll

    Required to use ACPIGenFx.

-   DSDTSamples

    Use this project as a starting point to design the ACPI firmware for the entire platform. The output is a full set of ACPI tables including the DSDT, FADT, and MADT.

-   SSDTSamples

    Use this project as a starting point to add a peripheral device to an existing system. The sample demonstrates how to describe a sensor device and its resources. The output is an ACPI SSDT table in ASL.

Download Windows 10 kits, tools, and code samples.

-   [Microsoft Visual Studio](https://go.microsoft.com/fwlink/p/?LinkId=533470)
-   [Windows Driver Kit (WDK) for Windows 10](https://go.microsoft.com/fwlink/p/?LinkId=733614)

## Create a platform


1.  In Visual Studio, open a new C# console project.
2.  Add a reference to the AutoAcpi.dll assembly. Under the **Project** menu, click **Add Reference**. Click **Browse** and navigate to the location of AutoAcpi.dll. Click **OK**.
3.  In **Solution Explorer**, expand **References** and select **acpigenfx**. View the objects in Object Browser (**View &gt; Object Browser**).
4.  Target .NET Framework 4.5 or later. Open project properties. On the **Application** page, make sure **Target framework** is set to **.NET Framework 4.5**.
5.  Add the `Using` directive for the AutoAcpi object at the beginning of the code for the application.
6.  Create a platform object. Based on your architecture, instantiate a **Platform** object by calling **Platform.CreateArmPlatform** or **Platform.Createx86Platform**. Specify *OEMID*, *OEMTableID*, *Creator*, *Revision*, and *FileName*.
7.  Call **Platform.WriteAsl** to write to a file.

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

8.  Click **Start** to build and run your app. Visual Studio displays build progress in the **Output** window. (If the **Output** window is not visible, choose **Output** from the **View** menu.).
9.  Open the folder named under *project*\\bin\\*Debug or Release*\\Output. The Output folder contains files generated by the app. View the contents of SSDT.asl.

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

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Object type</th>
<th>Creation method</th>
<th>Component</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ACAdapter</strong></td>
<td><strong>Platform.AddACAdapter</strong></td>
<td>Add an AC adapter.</td>
</tr>
<tr class="even">
<td><strong>BatteryDevice</strong></td>
<td><p><strong>Platform.AddBatteryDevice</strong></p>
<p><strong>BatteryDevice.ThermalLimit</strong></p></td>
<td>Add a battery device and specify its thermal limit.</td>
</tr>
<tr class="odd">
<td><strong>ButtonArrayDevice</strong></td>
<td><p><strong>Platform.AddButtonArrayDevice</strong></p>
<p><strong>ButtonArrayDevice.AddBackButton</strong></p>
<p><strong>ButtonArrayDevice.AddCameraShutterButton</strong></p>
<p><strong>ButtonArrayDevice.AddCameraAutofocusButton</strong></p>
<p><strong>ButtonArrayDevice.AddGenericButton</strong></p>
<p><strong>ButtonArrayDevice.AddPowerButton</strong></p>
<p><strong>ButtonArrayDevice.AddRotationLockButton</strong></p>
<p><strong>ButtonArrayDevice.AddSearchButton</strong></p>
<p><strong>ButtonArrayDevice.AddVolumeDownButton</strong></p>
<p><strong>ButtonArrayDevice.AddVolumeUpButton</strong></p>
<p><strong>ButtonArrayDevice.AddWindowsHomeButton</strong></p></td>
<td>Add buttons such as Windows Home, Back, Volume +/-, Power, Rotation Lock, and Search.</td>
</tr>
<tr class="even">
<td><strong>DisplaySensor</strong></td>
<td><strong>Platform.AddDisplaySensor</strong></td>
<td>Add a display sensor.</td>
</tr>
<tr class="odd">
<td><strong>GenericDevice</strong></td>
<td><strong>Platform.AddGenericDevice</strong></td>
<td>Add a generic device that can be used to replace any type of internally supported device in the framework.</td>
</tr>
<tr class="even">
<td><strong>GpioController</strong></td>
<td><strong>Platform.AddGpioController</strong></td>
<td>Add GPIO controllers and associated resources such as interrupts, I/O, and events.</td>
</tr>
<tr class="odd">
<td><strong>HidOverI2C</strong></td>
<td><strong>Platform.AddHidI2CDevice</strong></td>
<td>Add a HID device connected to the I²C bus.</td>
</tr>
<tr class="even">
<td><strong>I2CController</strong></td>
<td><strong>Platform.AddI2CController</strong></td>
<td>Add I²C controllers and associated resources such as interrupts, I/O, and events.</td>
</tr>
<tr class="odd">
<td><strong>KDNet2Usb</strong></td>
<td><strong>Platform.AddKDNet2Usb</strong></td>
<td>Add support for kernel debugging by using Kdnet over USB.</td>
</tr>
<tr class="even">
<td><strong>PEPDevice</strong></td>
<td><strong>Platform.AddPepDevice</strong></td>
<td>Add PEP devices and their resources and methods that return packages and static types.</td>
</tr>
<tr class="odd">
<td><p><strong>Processor</strong></p>
<p><strong>ProcessorAggregator</strong></p></td>
<td><p><strong>Platform.AddProcessor</strong></p>
<p><strong>Platform.AddProcessorAggregator</strong></p></td>
<td>Add processors and processor aggregators.</td>
</tr>
<tr class="even">
<td><strong>RTCDevice</strong></td>
<td><strong>Platform.AddRTCDevice</strong></td>
<td>Add ACPI time and alarm devices.</td>
</tr>
<tr class="odd">
<td><strong>SdHostController</strong></td>
<td><strong>Platform.AddSdHostController</strong></td>
<td>Add SD host controllers.</td>
</tr>
<tr class="even">
<td><strong>SerialPort</strong></td>
<td><strong>Platform.AddSerialPort</strong></td>
<td>Add support for serial and UART devices.</td>
</tr>
<tr class="odd">
<td><strong>ThermalZone</strong></td>
<td><strong>Platform.AddThermalZone</strong></td>
<td>Add thermal zones and associated sampling and polling periods.</td>
</tr>
<tr class="even">
<td><p><strong>XhciUsbController</strong></p>
<p><strong>EhciUsbController</strong></p>
<p><strong>UsbDevice</strong></p></td>
<td><p><strong>Platform.AddEhciUsbController</strong></p>
<p><strong>Platform.AddXhciUsbController</strong></p>
<p><strong>EhciUsbController.AddUsbDevice</strong></p>
<p><strong>XhciUsbController.AddUsbDevice</strong></p>
<p><strong>UsbDevice.AddUsbDevice</strong></p></td>
<td>Add USB host controllers and the child devices (including hubs).</td>
</tr>
</tbody>
</table>



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

This example shows how to add an I²C controller to the DSDT.

```cs
I2CController i2c = Platform.AddI2CController("I2C1", "I2CCONTR", 0);
i2c.AddMemory32Fixed(true, 0xf9999000, 0x400, "");
i2c.AddInterrupt(InterruptType.Level, InterruptActiveLevel.ActiveHigh, SharingLevel.Exclusive, 40);
```

Here is the output of the console app with the preceding definition for xHCI host and I²C controllers.

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


1.  Create a platform object by calling **Platform.CreateArmPlatform** or **Platform.Createx86Platform**.
2.  Set the **SSDT** property to true. This indicates to the framework that this table is an SSDT.
3.  Create a device and assign resources. For example, for the sensor device shown here, the sample calls **Platform.AddGenericDevice** and specifies the device name, hardware ID, and unique instance. The sensor device that connects to the I²C serial bus, I2C1, which is described in the DSDT.

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

**Note**  Make sure that test signing is enabled.
**bcdedit /set testsigning on**

## Related topics

[ACPI system description tables](acpi-system-description-tables.md)  
