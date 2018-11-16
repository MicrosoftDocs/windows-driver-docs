---
title: EFI_USBFN_PORT_TYPE
description: EFI_USBFN_PORT_TYPE
ms.assetid: 2596dd4f-26bd-454b-9550-a89c7e1f790b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# EFI\_USBFN\_PORT\_TYPE


This enumeration specifies the USB port type.

## Syntax


```cpp
typedef enum _EFI_USBFN_PORT_TYPE 
{
    EfiUsbUnknownPort = 0,
    EfiUsbStandardDownstreamPort,
    EfiUsbChargingDownstreamPort,
    EfiUsbDedicatedChargingPort,
    EfiUsbInvalidDedicatedChargingPort
} EFI_USBFN_PORT_TYPE;
```

## Constants


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>EfiUsbUnknownPort</strong></p></td>
<td><p>Unknown Port - Driver internal default port type; this is never returned by the driver with a success status code.</p></td>
</tr>
<tr class="even">
<td><p><strong>EfiUsbStandardDownstreamPort</strong></p></td>
<td><p>Standard Downstream Port - Standard USB host.for more information, see <strong>Remarks</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>EfiUsbChargingDownstreamPort</strong></p></td>
<td><p>Charging Downstream Port - Standard USB host. For more information, see <strong>Remarks</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>EfiUsbDedicatedChargingPort</strong></p></td>
<td><p>Dedicated Charging Port – A wall-charger, not USB host. For more information, see <strong>Remarks</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>EfiUsbInvalidDedicatedChargingPort</strong></p></td>
<td><p>Invalid Dedicated Charging Port – Not a USB host or dedicated charging port.</p></td>
</tr>
</tbody>
</table>

 

## Remarks


Refer to "Battery Charging Specification, Revision 1.1” on the [USB.org](http://go.microsoft.com/fwlink/p/?linkid=64124) website.

## Requirements


**Header:** User generated

 

 




