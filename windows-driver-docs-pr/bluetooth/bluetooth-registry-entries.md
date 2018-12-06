---
title: Bluetooth Registry Entries
description: Bluetooth Registry Entries
ms.assetid: a4d2848d-cb3c-4413-b06f-fe4695448f6a
keywords:
- Bluetooth WDK , registry entries
- registry WDK Bluetooth
- COD_Type subkey
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bluetooth Registry Entries


This section describes the class-of-device (CoD) registry subkeys and entries that apply to the Bluetooth driver stack.

### <span id="cod_type_subkey"></span><span id="COD_TYPE_SUBKEY"></span>"COD Major" and "COD Type" Values

Original equipment manufacturer (OEMs) can use the **COD Major** and **COD Type** values to indicate the Class of Device for a Bluetooth-enabled Windows device. After the Bluetooth class installer sets the Class of Device based on these registry values, a remote device can determine whether it is connecting to a portable computer, a desktop computer, a phone, and so on.

The registry path to the **COD Major** and **COD Type** values is:

HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\BTHPORT\\Parameters

Note that setting these values changes the Bluetooth Class of Device for the system, regardless of which Bluetooth radio may be attached. You can set the **COD Major** and **COD Type** to `DWORD` values as defined for the Class of Device field values in the [Bluetooth SIG Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/baseband).

The Bluetooth profile driver, BthPort.sys, reads the **COD Major** and **COD Type** values to determine how it should respond to a device inquiry. These values affect only the `COD_MAJOR_XXX` and `COD_XXX_MINOR_XXX` bits of the Class of Device. The `COD_SERVICE_XXX` bits are not affected by this registry entry.

If the **COD Major** and **COD Type** values are not set or are set to invalid values, the Bluetooth class installer will set these values to `COD_MAJOR_COMPUTER` and `COD_COMPUTER_MINOR_DESKTOP`, respectively.

### <span id="Scanning_Parameterization_Settings"></span><span id="scanning_parameterization_settings"></span><span id="SCANNING_PARAMETERIZATION_SETTINGS"></span>Scanning Parameterization Settings

Profile drivers can specify scanning parameters settings for their device(s) in their profile driver's INF file to tailor to the specific needs of a given device scenario.

You can override the default system scanning parameters by providing one or more of the following scanning parameters listed below into the AddReg directive. More information on how to use this directive can be found in [INF AddReg Directive](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addreg-directive).

|                           |               |           |                                                                                |
|---------------------------|---------------|-----------|--------------------------------------------------------------------------------|
| Value Name                | Type          | Min Value | Max Value                                                                      |
| HighDutyCycleScanWindow   | DWORD 0x10001 | 0x0004    | 0x4000. Shall be equal or smaller than the HighDutyCycleScanInterval parameter |
| HighDutyCycleScanInterval | DWORD 0x10001 | 0x0004    | 0x4000                                                                         |
| LowDutyCycleScanWindow    | DWORD 0x10001 | 0x0004    | 0x4000. Shall be smaller than the LowDutyCycleScanInterval parameter           |
| LowDutyCycleScanInterval  | DWORD 0x10001 | 0x0004    | 0x4000                                                                         |
| LinkSupervisionTimeout    | DWORD 0x10001 | 0x000A    | 0x0C80                                                                         |
| ConnectionLatency         | DWORD 0x10001 | 0x0000    | 0x01F4                                                                         |
| ConnectionIntervalMin     | DWORD 0x10001 | 0x0006    | 0x0C80. Shall be smaller or equal to ConnectionIntervalMax                     |
| ConnectionIntervalMax     | DWORD 0x10001 | 0x0006    | 0x0C80                                                                         |

 

**Note**  Changes to scanning parameters make a global impact on the performance of the Bluetooth stack. Making changes to scanning parameters programmatically is not permitted. Using Low Duty Cycle scanning parameters that are too aggressive can not only have a negative impact to the available bandwidth for other Bluetooth Low Energy connections, but also for Bluetooth BR/EDR connections.

 

 

 





