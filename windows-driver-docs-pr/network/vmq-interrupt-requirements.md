---
title: VMQ Interrupt Requirements
description: VMQ Interrupt Requirements
ms.date: 04/20/2017
---

# VMQ Interrupt Requirements


A miniport driver that supports the virtual machine queue (VMQ) functionality must also support the following interrupt allocation requirements:

-   The miniport driver must support MSI-X. The driver must set the **NDIS\_RECEIVE\_FILTER\_MSI\_X\_SUPPORTED** flag in the **SupportedQueueProperties** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_filter_capabilities) structure.

    The driver returns this structure in the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_hardware_assist_attributes) structure that the driver uses in its call to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

-   The miniport driver must call the [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation) function to obtain processor information for allocating interrupt vectors. It must not rely on registry keys or information obtained from other sources for interrupt allocation.

    [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation) returns information about the set of processors that a miniport driver can use for RSS and VMQ. This information is contained in an [**NDIS\_RSS\_PROCESSOR\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_processor_info) structure.

-   The miniport driver should allocate only one interrupt vector for each processor that is specified in the [**NDIS\_RSS\_PROCESSOR\_INFO**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_rss_processor_info) structure.

    The miniport driver should allocate no more than two interrupt vectors for other events that are not related to send or receive packet operations. For example, the driver could allocate an IDT for link status events.

-   The miniport driver must support the minimum number of MSI-X interrupt vectors as defined in the following table:

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Number of queues</th>
    <th align="left">Minimum number of required MSI-X interrupt vectors</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>1–16</p></td>
    <td align="left"><p>1–16</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>17–64</p></td>
    <td align="left"><p>16–32</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>65 or more</p></td>
    <td align="left"><p>32 or more</p></td>
    </tr>
    </tbody>
    </table>

     

 

