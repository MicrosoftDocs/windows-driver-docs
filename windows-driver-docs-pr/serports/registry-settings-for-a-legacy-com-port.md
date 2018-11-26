---
title: Registry Settings for a Legacy COM Port
description: Registry Settings for a Legacy COM Port
ms.assetid: 043ac1f5-eeb1-4828-8417-b3c6d76b4322
keywords:
- Serial driver WDK , COM ports
- COM ports WDK serial devices
- serial devices WDK , COM ports
- legacy COM ports WDK serial devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registry Settings for a Legacy COM Port





This topic describes the registry settings that Serial uses with legacy [COM ports](configuration-of-com-ports.md). Serial always configures a legacy serial device as a COM port.

Serial queries these entry values when it enumerates a legacy COM port. If a device-specific entry value is not present, Serial uses a Serial service value.

The registry settings for a legacy COM port are under a corresponding legacy COM port subkey that is under the **..\\Services\\Serial\\Parameters** key.

The following entry values are the same as described for a [Plug and Play serial device](registry-settings-for-a-plug-and-play-serial-device.md):

-   **ClockRate**

-   **PortIndex**

-   **Indexed**

-   **RxFIFO**

-   **TxFIFO**

-   **MaskInverted**

-   **DisablePort**

-   **ForceFifoEnable**

The following additional entry values are used with legacy COM ports:

<a href="" id="portaddress--reg-dword-"></a>**PortAddress** (REG\_DWORD)  
Specifies the untranslated base I/O address for the COM port control registers. Serial reads this value. The value cannot be zero. The default value of **PortAddress** is 0x00000000.

<a href="" id="interrupt--reg-dword-"></a>**Interrupt** (REG\_DWORD)  
Specifies the untranslated interrupt vector, as appropriate for the bus type. Serial reads this value. The value cannot be zero. The default value of **Interrupt** is 0x00000000.

<a href="" id="dosdevices--reg-sz-"></a>**DosDevices** (REG\_SZ)  
Specifies the name of the COM port. The name of a COM port is typically COM<em>&lt;n&gt;,</em> where &lt;*n&gt;* is a COM port number that the installer obtains from the [COM port database](com-port-database.md). However, a COM port name can be set to any non-**NULL** string. Serial uses the port name to create a symbolic link to the COM port that is visible in usermode. The default value of **DosDevices** is a **NULL** string.

<a href="" id="interruptstatus--reg-dword-"></a>**InterruptStatus** (REG\_DWORD)  
Specifies the raw I/O address for the interrupt status register. Serial reads this value. The value is omitted if the port is a stand-alone port. The value cannot be zero if the port is on a multiport device. The default value of **InterruptStatus** is 0x00000000.

<a href="" id="busnumber--reg-dword-"></a>**BusNumber** (REG\_DWORD)  
Specifies the system-wide bus number for the bus type. Serial reads this value. The default value of **BusNumber** is 0x00000000.

<a href="" id="bustype--reg-dword-"></a>**BusType** (REG\_DWORD)  
Specifies the bus type. Serial reads this value. The default value of **BusType** is determined by Serial during driver initialization.

<a href="" id="interruptmode--reg-dword-"></a>**InterruptMode** (REG\_DWORD)  
Specifies the interrupt mode. Serial reads this value. The default value of **InterruptMode** is CM\_RESOURCE\_INTERRUPT\_LATCHED.

<a href="" id="interruptlevel--reg-dword-"></a>**InterruptLevel** (REG\_DWORD)  
Specifies a raw interrupt level value that is appropriate for the bus type. Serial reads this value. The default value of **InterruptLevel** is 0x00000000.

<a href="" id="pnpdeviceid--reg-sz-"></a>**PnPDeviceID** (REG\_SZ)  
Specifies a Plug and Play device identifier for a Plug and Play device. Serial reads this value. The default value of **PnPDeviceID** is a **NULL** string.

<a href="" id="legacydiscovered--reg-dword-"></a>**LegacyDiscovered** (REG\_DWORD)  
Boolean flag that indicates whether Serial has previously reported the device to the Plug and Play manager. Serial reads and sets this value. If **LegacyDiscovered** is nonzero, Serial has previously reported the device and does not report the device again. Otherwise, Serial reports the device and sets the entry value to 0x00000001.

 

 




