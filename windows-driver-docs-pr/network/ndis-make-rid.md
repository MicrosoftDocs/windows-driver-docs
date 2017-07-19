---
title: NDIS\_MAKE\_RID macro
author: windows-driver-content
description: The NDIS\_MAKE\_RID macro builds an NDIS\_VF\_RID value from PCI Express (PCIe) segment, bus, device, and function numbers. The miniport driver uses this value as a PCIe Requestor ID (RID) for a network adapter's PCIe Virtual Function (VF).
ms.assetid: 908F9DCE-D516-44CE-9FBC-0F2DE3F1A3B8
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
- NDIS_MAKE_RID macro Network Drivers Starting with Windows Vista
---

# NDIS\_MAKE\_RID macro


The NDIS\_MAKE\_RID macro builds an NDIS\_VF\_RID value from PCI Express (PCIe) segment, bus, device, and function numbers. The miniport driver uses this value as a PCIe Requestor ID (RID) for a network adapter's PCIe Virtual Function (VF).

Syntax
------

```ManagedCPlusPlus
 NDIS_MAKE_RID(
   ULONG _Segment,
   ULONG _Bus,
   ULONG _Function
);
```

Parameters
----------

*\_Segment*   
The PCIe segment number for the group of PCIe buses on which the device is attached. A PCIe segment is a set of PCIe buses that share configuration space.

*\_Bus*   
The PCIe bus number of the bus on which the network adapter is attached.

*\_Function*   
The function number of a logical device on the network adapter.

Return value
------------

NDIS\_MAKE\_RID returns an NDIS\_VF\_RID value that is constructed from the parameters.

Remarks
-------

When it handles an OID request of [OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814), the miniport driver for the PCIe Physical Function (PF) uses the NDIS\_MAKE\_RID macro to create a PCIe Requestor ID (RID) value for the VF. The driver retrieves the PCIe segment, bus, device, and function numbers for the VF by calling [**NdisMGetVirtualFunctionLocation**](https://msdn.microsoft.com/library/windows/hardware/hh451487).

**Note**  If an independent hardware vendor (IHV) provides a virtual bus driver (VBD) as part of its SR-IOV [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), its PF miniport driver must not call [**NdisMGetVirtualFunctionLocation**](https://msdn.microsoft.com/library/windows/hardware/hh451487). Instead, the driver must interface with the VBD through a private communication channel, and request that the VBD call [*GetLocation*](https://msdn.microsoft.com/library/windows/hardware/hh451128). This function is exposed from the [GUID\_PCI\_VIRTUALIZATION\_INTERFACE](https://msdn.microsoft.com/library/windows/hardware/hh451143) interface supported by the underlying PCI bus driver.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.30 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


****
[**NdisMGetVirtualFunctionLocation**](https://msdn.microsoft.com/library/windows/hardware/hh451487)

[OID\_NIC\_SWITCH\_ALLOCATE\_VF](https://msdn.microsoft.com/library/windows/hardware/hh451814)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_MAKE_RID%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


