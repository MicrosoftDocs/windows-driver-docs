---
title: devext
description: The devext extension displays bus-specific device extension information for devices on a variety of buses.
ms.assetid: b4d4f595-9b0b-40e2-8790-2c913a50c8fe
keywords: ["usbhub extension (obsolete)", "hidfdo extension (obsolete)", "hidpdo extension (obsolete)", "device extension", "bus", "devext Windows Debugging"]
ms.author: domars
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
```dbgcmd

## <span id="ddk__devext_dbg"></span><span id="DDK__DEVEXT_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the device extension to be displayed.

<span id="_______TypeCode______"></span><span id="_______typecode______"></span><span id="_______TYPECODE______"></span> *TypeCode*   
Specifies the type of object that owns the device extension to be displayed. Type codes are not case-sensitive. Valid type codes are:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">TypeCode</th>
<th align="left">Object</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>PCI</p></td>
<td align="left"><p>(Windows 2000 only) PCI device extension</p></td>
</tr>
<tr class="even">
<td align="left"><p>ISAPNP</p></td>
<td align="left"><p>ISA PnP device extension</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PCMCIA</p></td>
<td align="left"><p>PCMCIA device extension</p></td>
</tr>
<tr class="even">
<td align="left"><p>HID</p></td>
<td align="left"><p>HID device extension</p></td>
</tr>
<tr class="odd">
<td align="left"><p>USBD</p></td>
<td align="left"><p>(Windows 2000 only) USB bus driver extension</p></td>
</tr>
<tr class="even">
<td align="left"><p>UHCD</p></td>
<td align="left"><p>(Windows 2000 only) UHCD host controller extension</p></td>
</tr>
<tr class="odd">
<td align="left"><p>OpenHCI</p></td>
<td align="left"><p>(Windows 2000 only) Open HCI host controller extension</p></td>
</tr>
<tr class="even">
<td align="left"><p>USBHUB</p></td>
<td align="left"><p>(Windows 2000 only) USB hub extension</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MF</p></td>
<td align="left"><p>(Windows 2000 only) MF device extension</p></td>
</tr>
</tbody>
</table>

 

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

See [Plug and Play Debugging](plug-and-play-debugging.md) for applications of this extension command. For more information about device extensions, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

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

 

 





