---
title: Installing Legacy COM Ports
description: Installing Legacy COM Ports
ms.assetid: 9cf2a22c-fb4e-4f15-8410-021d2b4f2ce1
keywords:
- legacy COM ports WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Legacy COM Ports





The Serial function driver always configures a legacy serial port as a [COM port](configuration-of-com-ports.md).

Serial detects the presence of legacy ports by reading corresponding COM port subkeys under the **..\\Services\\Serial\\Parameters** key. To install a legacy COM port, you must set a legacy COM port subkey for the device under this key. The COM port subkey contains the [registry settings for a legacy COM port](registry-settings-for-a-legacy-com-port.md).

When Serial is loaded it determines which legacy ports were not previously detected by checking the **LegacyDiscovered** entry value for a legacy port. If this entry value does not exist or is zero, Serial performs the following tasks:

1.  Calls [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597) to report the device to the Plug and Play manager.

2.  Sets the **LegacyDiscovered** entry value for the port to 0x00000001, which indicates that the port has been reported.

3.  Copies some of the entry values under the COM port subkey to the Plug and Play device key for the physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) that is returned by **IoReportDetectedDevice**.

4.  Serial sets the **PortName** entry value under the Plug and Play device key to the value of the **DosDevices** entry value under the legacy COM port subkey. For all other entry values that Serial copies, it retains the same entry value name. For more information about which entry values that Serial copies, see the Serial sample code provided in the Microsoft Windows Driver Kit (WDK).

The **IoReportDetectedDevice** call marks the port as a root-enumerated device. On subsequent system boots, the Plug and Play manager automatically configures the device based on the information in its INF file.

The Plug and Play manager creates the following [compatible IDs](https://msdn.microsoft.com/library/windows/hardware/ff539950) for a legacy COM port: DETECTEDInternal\\Serial and DETECTED\\Serial.

 

 




