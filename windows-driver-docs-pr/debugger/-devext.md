---
title: devext
description: The devext extension displays bus-specific device extension information for devices on a variety of buses.
keywords: ["usbhub extension (obsolete)", "hidfdo extension (obsolete)", "hidpdo extension (obsolete)", "device extension", "bus", "devext Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- devext
api_type:
- NA
ms.localizationpriority: medium
---

# !devext


The **!devext** extension displays bus-specific device extension information for devices on a variety of buses.

```dbgcmd
!devext Address TypeCode
```

## <span id="ddk__devext_dbg"></span><span id="DDK__DEVEXT_DBG"></span>Parameters

###  *Address*   
Specifies the hexadecimal address of the device extension to be displayed.

#### *TypeCode*   
Specifies the type of object that owns the device extension to be displayed. Type codes are not case-sensitive. Valid type codes are:

|TypeCode|Object|
|--- |--- |
|ISAPNP|ISA PnP device extension|
|PCMCIA|PCMCIA device extension|
|HID|HID device extension|
 

### <span id="DLL"></span><span id="dll"></span>DLL

Kdexts.dll
 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For more information about device extensions, see the Windows Driver Kit (WDK) documentation.

## Remarks

The **!usbhub**, **!hidfdo**, and **!hidpdo** extensions are obsolete; their functionality has been integrated into **!devext**.

For those object types that are no longer supported by **!devext**, use the [**dt (Display Type)**](dt--display-type-.md) debugger command.

Here is an example for an ISA PnP device extension:

```dbgcmd
kd> !devext e0000165fff32190 ISAPNP
ISA PnP FDO @ 0x00000000, DevExt @ 0xe0000165fff32190, Bus # 196639
Flags (0x854e2530)  DF_ACTIVATED, DF_QUERY_STOPPED, 
                    DF_STOPPED, DF_RESTARTED_NOMOVE, 
                    DF_BUS
                    Unknown flags 0x054e2000

NumberCSNs           - -536870912
ReadDataPort         - 0x0000000d (mapped)
AddressPort          - 0x00000000 (not mapped)
CommandPort          - 0x00000000 (not mapped)
DeviceList           - 0xe000000085007b50
CardList             - 0x00000000
PhysicalBusDevice    - 0x00000000
AttachedDevice       - 0x00000000
SystemPowerState     - Unspecified
DevicePowerState     - Unspecified
```

Here is an example for a PCI device:

```dbgcmd
kd> !devext e0000000858c31b0 PCI
PDO Extension, Bus 0x0, Device 0, Function 0.
  DevObj 0xe0000000858c3060 PCI Parent Bus FDO DevExt 0xe0000000858c4960
  Device State = PciNotStarted
  Vendor ID 8086 (INTEL)  Device ID 123D
  Class Base/Sub 08/00  (Base System Device/Interrupt Controller)
  Programming Interface: 20, Revision: 01, IntPin: 00, Line Raw/Adj 00/00
  Enables ((cmd & 7) = 106): BM   Capabilities Pointer = <none>
  CurrentState:          System Working,  Device D0
  WakeLevel:             System Unspecified,  Device Unspecified
  Requirements: <none>
```

 

 





