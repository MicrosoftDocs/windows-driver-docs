---
title: EFI\_USBFN\_PORT\_TYPE
description: EFI\_USBFN\_PORT\_TYPE
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 2596dd4f-26bd-454b-9550-a89c7e1f790b
---

# EFI\_USBFN\_PORT\_TYPE


This enumeration specifies the USB port type.

## Syntax


``` syntax
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20EFI_USBFN_PORT_TYPE%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


