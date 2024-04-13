---
title: GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES
description: WMI clients can use the GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES method GUID to determine the current link state.
ms.date: 03/02/2023
keywords: 
 -GUID_NDIS_GEN_PCI_DEVICE_CUSTOM_PROPERTIES Network Drivers Starting with Windows Vista
---

# GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES


WMI clients can use the GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES method GUID to determine the current link state.

## Remarks

NDIS handles this GUID and miniport drivers do not receive an OID query.

When a WMI client issues a GUID\_NDIS\_GEN\_PCI\_DEVICE\_CUSTOM\_PROPERTIES WMI method request, NDIS returns the PCI custom properties of a PCI device for the miniport adapter. The WMI method identifier should be NDIS\_WMI\_DEFAULT\_METHOD\_ID, and the WMI input buffer should contain an [**NDIS\_WMI\_METHOD\_HEADER**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_method_header) structure.

The data buffer that NDIS returns with this GUID contains an [**NDIS\_PCI\_DEVICE\_CUSTOM\_PROPERTIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pci_device_custom_properties) structure.

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

[**NDIS\_WMI\_METHOD\_HEADER**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_method_header)

 

