---
title: Installing Legacy COM Ports
author: windows-driver-content
description: Installing Legacy COM Ports
ms.assetid: 9cf2a22c-fb4e-4f15-8410-021d2b4f2ce1
keywords: ["legacy COM ports WDK serial devices"]
---

# Installing Legacy COM Ports


## <a href="" id="ddk-installing-legacy-com-ports-kg"></a>


The Serial function driver always configures a legacy serial port as a [COM port](configuration-of-com-ports.md).

Serial detects the presence of legacy ports by reading corresponding COM port subkeys under the **..\\Services\\Serial\\Parameters** key. To install a legacy COM port, you must set a legacy COM port subkey for the device under this key. The COM port subkey contains the [registry settings for a legacy COM port](registry-settings-for-a-legacy-com-port.md).

When Serial is loaded it determines which legacy ports were not previously detected by checking the **LegacyDiscovered** entry value for a legacy port. If this entry value does not exist or is zero, Serial performs the following tasks:

1.  Calls [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597) to report the device to the Plug and Play manager.

2.  Sets the **LegacyDiscovered** entry value for the port to 0x00000001, which indicates that the port has been reported.

3.  Copies some of the entry values under the COM port subkey to the Plug and Play device key for the physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) that is returned by **IoReportDetectedDevice**.

4.  Serial sets the **PortName** entry value under the Plug and Play device key to the value of the **DosDevices** entry value under the legacy COM port subkey. For all other entry values that Serial copies, it retains the same entry value name. For more information about which entry values that Serial copies, see the Serial sample code provided in the Microsoft Windows Driver Kit (WDK).

The **IoReportDetectedDevice** call marks the port as a root-enumerated device. On subsequent system boots, the Plug and Play manager automatically configures the device based on the information in its INF file.

The Plug and Play manager creates the following [compatible IDs](https://msdn.microsoft.com/library/windows/hardware/ff539950) for a legacy COM port: DETECTEDInternal\\Serial and DETECTED\\Serial.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Installing%20Legacy%20COM%20Ports%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


