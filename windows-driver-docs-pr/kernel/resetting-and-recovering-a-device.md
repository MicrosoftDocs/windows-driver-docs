---
title: Resetting and recovering a device
description: The GUID_DEVICE_RESET_INTERFACE_STANDARD interface defines a standard way for function drivers to attempt to reset and recover a malfunctioning device.
ms.assetid: 507192FF-77BB-4446-AAA0-3F44E1CB2E72
keywords: [GUID_DEVICE_RESET_INTERFACE_STANDARD]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Resetting and recovering a device

The GUID_DEVICE_RESET_INTERFACE_STANDARD interface defines a standard way for function drivers to attempt to reset and recover a malfunctioning device.

Two types of device resets are available through this interface:

-    Function-level device reset. In this case, the reset operation is restricted to a specific device, and is not visible to other devices. The device stays connected to the bus throughout the reset and returns to a valid state (initial state) after the reset. This type of reset has the least impact on the system. 

        This type of reset can be implemented either by the bus driver or by ACPI firmware. The bus driver can implement a function-level reset if the bus specification defines an in-band reset mechanism that meets the requirement. ACPI firmware can optionally override a bus driver-defined function-level reset with its own implementation.

-    Platform-level device reset. In this case, the reset operation causes the device to be reported as missing from the bus. The reset operation affects a specific device and all other devices that are connected to it via the same power rail or reset line. This type of reset has the most impact on the system. The OS will tear down and rebuild the stacks of all affected devices to ensure that everything restarts from a blank state.

        Starting in Windows 10, these registry entries under the HKLM\SYSTEM\CurrentControlSet\Control\Pnp key configures the reset operation: 

        -    DeviceResetRetryInterval: Time period before the reset operation starts. Default value is 3 seconds. Minimum value is 100 milliseconds; maximum value is 30 seconds. 
        -    DeviceResetMaximumRetries: Number of times the reset operation is attempted. 

Note  The GUID_DEVICE_RESET_INTERFACE_STANDARD interface is available starting in Windows 10.
 

## Using the device reset interface

If a function driver detects that the device is not functioning correctly, it should first attempt a function-level reset. If a function-level reset does not fix the issue, then the driver may choose to attempt a platform-level reset. However, a platform-level reset should only be used as the final option.

To query for this interface, a device driver sends an IRP_MN_QUERY_INTERFACE IRP down the driver stack. For this IRP, the driver sets the InterfaceType input parameter to GUID_DEVICE_RESET_INTERFACE_STANDARD. On successful completion of the IRP, the Interface output parameter is a pointer to a DEVICE_RESET_INTERFACE_STANDARD structure. This structure contains a pointer to the DeviceReset routine, which can be used to request a function-level or platform-level reset.


## Supporting the device reset interface in function drivers

To support the device reset interface, the device stack must meet the following requirements.

The function driver must properly handle IRP_MN_QUERY_REMOVE_DEVICE, IRP_MN_REMOVE_DEVICE and IRP_MN_SURPRISE_REMOVAL. 

In most cases, when the driver receives IRP_MN_QUERY_REMOVE_DEVICE, it should return a success so that the device can be safely removed. However, there may be cases where the device cannot be safely stopped, such as if the device is stuck in a loop writing to a memory buffer. In such cases, the driver should return STATUS_DEVICE_HUNG to IRP_MN_QUERY_REMOVE_DEVICE. The PnP manager will continue the IRP_MN_QUERY_REMOVE_DEVICE and IRP_MN_REMOVE_DEVICE process, but that particular stack will not receive IRP_MN_REMOVE_DEVICE. Instead, the device stack will receive IRP_MN_SURPRISE_REMOVAL after the device has been reset.

For more information about these IRPs, see: 

[Handling an IRP_MN_QUERY_REMOVE_DEVICE Request](handling-an-irp-mn-query-remove-device-request.md)

[Handling an IRP_MN_REMOVE_DEVICE Request](handling-an-irp-mn-remove-device-request.md)

[Handling an IRP_MN_SURPRISE_REMOVAL Request](handling-an-irp-mn-surprise-removal-request.md)

## Supporting the device reset interface in filter drivers

Filter drivers may intercept IRP_MN_QUERY_INTERFACE IRPs that have the GUID_DEVICE_RESET_INTERFACE_STANDARD interface type. By doing so, they can continue to delegate to the GUID_DEVICE_RESET_INTERFACE_STANDARD interface but perform device-specific operations before or after the reset operation. Alternatively, they can override the GUID_DEVICE_RESET_INTERFACE_STANDARD interface returned by the bus driver with its own interface in order to provide its own reset operation.

## Supporting the device reset interface in bus drivers

Bus drivers that participate in the device reset process (that is, bus drivers that are associated with the device that is requesting the reset and bus drivers that are associated with devices that are responding to the reset request) must meet one of the following requirements:

-    Be hot plug capable. The bus driver must be able to detect a device being removed from the bus without notice, and a device being plugged into the bus.

-    Alternatively, it must implement the GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface. This simulates a device being pulled from a bus and being plugged back in. Built-in bus drivers (such as PCI and SDBUS) support this interface. Therefore, if the device being reset uses one of these buses, no bus driver modifications should be necessary.

        For WDF-based bus drivers, the WDF framework registers the GUID_REENUMERATE_SELF_INTERFACE_STANDARD interface on behalf of the drivers. Therefore, registering this interface is not necessary for those drivers. If the bus driver needs to do perform some operations before its child devices are re-enumerated, it must register for the EvtChildListDeviceReenumerated callback routine and perform the operations in that routine. Because this callback routine may be called in parallel for all PDO’s, the code in the routine may need to protect against race conditions.

## ACPI firmware: Function-level reset

To support function-level device reset, there must be an _RST method defined inside the Device scope. If present, this method will override the bus driver's implementation of function-level device reset (if present) for that device. When executed, the _RST method must reset only that device, and must not affect other devices. In addition, the device must stay connected on the bus.

## ACPI firmware: Platform-level reset
To support platform-level device reset, there are two options:

-    The ACPI firmware can define a PowerResource that implements the _RST method, and all devices that are affected by this reset method can refer to this PowerResource through a _PRR object defined under their Device scope.

-    The device can declare a _PR3 object. In this case, the ACPI driver will use D3cold power cycling to perform the reset, and reset dependencies between devices will be determined from the _PR3 object.

If the _PRR object exists in the Device scope, the ACPI driver will use the _RST method in the referenced PowerResource to perform the reset. If no _PRR object is defined but the _PR3 object is defined, then the ACPI driver will use D3cold power cycling to perform the reset. If neither the _PRR or _PR3 object is defined, then the device does not support a platform-level reset and the ACPI driver will report that the platform-level reset is not available.

## Verifying ACPI firmware on the test system
To test your driver that supports device reset and recovery, follow this procedure. This procedure assumes you are using this example ASL file. 

```cpp
DefinitionBlock("SSDT.AML", "SSDT", 0x01, "XyzOEM", "TestTabl", 0x00001000)
{
    Scope(\_SB_)
       {
        PowerResource(PWFR, 0x5, 0x0)
        {
            Method(_RST, 0x0, NotSerialized)    { }
            
            // Placeholder methods as power resources need _ON, _OFF, _STA.
            Method(_STA, 0x0, NotSerialized)
            {
                Return(0xF)
            }

            Method(_ON_, 0x0, NotSerialized)    { }

            Method(_OFF, 0x0, NotSerialized)    { }

        } // PowerResource()
    } // Scope (\_SB_)

    // Assumes WiFi device is declared under \_SB.XYZ.
    Scope(\_SB_.XYZ.WIFI)
        {

        // Declare PWFR as WiFi reset power rail
        Name(_PRR, Package(One)
            {
                \_SB_.PWFR
            })
        } // Scope (\_SB)
}
```
 


1. Compile the test ASL file to an AML by using an ASL compiler, such as Asl.exe. The executable in included in the Windows Driver Kit (WDK). 
Asl <test>.asl

    The preceding command generates SSDT.aml.

2. Rename SSDT.aml to acpitabl.dat. 
3. Copy acpitabl.dat to %systemroot%\system32 on the test system. 
4. Enable test signing on the test system. 
      Bcdedit /set GUID_DEVICE_RESET_INTERFACE_STANDARD testsigning on

5. Reboot the test system. 
6. Verify that the table is loaded. In Windows Debugger, use these commands. 

```cpp
!acpicache 
dt _DESCRIPTION_HEADER address of the SSDT table 

0: kd> !acpicache
Dumping cached ACPI tables...
  SSDT @(ffffffffffd03018) Rev: 0x1 Len: 0x000043 TableID: TestTabl
  XSDT @(ffffffffffd05018) Rev: 0x1 Len: 0x000114 TableID: HSW-FFRD
       ...
       ...
 
0: kd> dt _DESCRIPTION_HEADER ffffffffffd03018
ACPI!_DESCRIPTION_HEADER
   +0x000 Signature        : 0x54445353
   +0x004 Length           : 0x43
   +0x008 Revision         : 0x1 ''
   +0x009 Checksum         : 0x37 '7'
   +0x00a OEMID            : [6]  "XyzOEM"
   +0x010 OEMTableID       : [8]  "TestTabl"
   +0x018 OEMRevision      : 0x1000
   +0x01c CreatorID        : [4]  "MSFT"
   +0x020 CreatorRev       : 0x5000000
```
