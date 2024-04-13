---
title: Registry Settings for the Serial Service
description: Registry Settings for the Serial Service
keywords:
- Serial service WDK
ms.date: 04/20/2017
---

# Registry Settings for the Serial Service

This topic describes the registry settings that Serial applies to all serial devices for which Serial is the function driver or a lower-level device filter driver.

> [!NOTE]
> This topic describes programming traditional COM ports. For information on USB attached serial ports, see [USB serial driver (Usbser.sys)](../usbcon/usb-driver-installation-based-on-compatible-ids.md).

Serial queries the service entry values after it is loaded. If an entry value is not present, Serial adds the service entry value. Serial sets the entry value to the default value that is statically defined in the system-supplied Serial.sys driver. If a service entry value is changed after Serial is loaded, the new value is used the next time Serial is loaded.

Serial uses the following service entry values that are under the **..\\Services\\Serial** registry key:

For general information on how to locate and work with Windows drivers registry keys, see [Registry Trees for Devices and Drivers](../install/overview-of-registry-trees-and-keys.md).

<a href="" id="forcefifoenable--reg-dword-"></a>**ForceFifoEnable** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether to force Serial to use FIFOs. If **ForceFifofEnable** is nonzero, FIFOs are used, regardless of whether Serial can detect the presence of FIFOs. Otherwise, FIFOs are used only if Serial can detect them. The default value of is nonzero. If the entry value is not present, Serial sets a **ForceFifoEnable** entry value to the default value. For more information about the method of detection, see the [Serial driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serial) on GitHub.

<a href="" id="rxfifo--reg-dword-"></a>**RxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the receive FIFO that triggers a port interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serial) on GitHub. The default value of **RxFIFO** is eight bytes. If the entry value is not present, Serial sets an **RxFIFO** entry value to the default value.

<a href="" id="txfifo--reg-dword-"></a>**TxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the transmit FIFO that triggers a port interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](https://github.com/Microsoft/Windows-driver-samples/tree/main/serial/serial) on GitHub. The default value of **TxFIFO** is 14 bytes. If the entry value is not present, Serial sets a **TxFIFO** entry value to the default value.

<a href="" id="permitshare--reg-dword-"></a>**PermitShare** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether to permit the system to share the interrupt that a port uses. If **PermitShare** is nonzero, the interrupt can be shared; otherwise, the interrupt cannot be shared. The default value of **PermitShare** is 0x00000000. If the entry value is not present, Serial sets a **PermitShare** entry value to the default value.

<a href="" id="breakonentry--debuglevel--and-logfifo"></a>**BreakOnEntry**, **DebugLevel**, and **LogFifo**  
Specify entry values that are used for debugging. For more information about these entry values, see the Serial sample code that is included in the WDK.
