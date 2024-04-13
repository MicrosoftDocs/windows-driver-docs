---
title: OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES
ms.topic: reference
description: As a query, overlying drivers use the OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES OID to get the PCI custom properties of a device.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PCI_DEVICE_CUSTOM_PROPERTIES Network Drivers Starting with Windows Vista
---

# OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES


As a query, overlying drivers use the OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES OID to get the PCI custom properties of a device.

## Remarks

NDIS handles OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES and miniport drivers do not receive an OID query.

This query is optional for other NDIS drivers.

NDIS returns an [**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pci_device_custom_properties) structure that contains the PCI custom properties.

For non-PCI miniport adapters, NDIS fails OID\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES with the NDIS\_STATUS\_INVALID\_DEVICE\_REQUEST status code.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pci_device_custom_properties)

 

