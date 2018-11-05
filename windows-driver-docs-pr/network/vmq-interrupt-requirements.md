---
title: VMQ Interrupt Requirements
description: VMQ Interrupt Requirements
ms.assetid: 7ECC9031-D41B-4664-963D-F1C20B297B7C
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# VMQ Interrupt Requirements


A miniport driver that supports the virtual machine queue (VMQ) functionality must also support the following interrupt allocation requirements:

-   The miniport driver must support MSI-X. The driver must set the **NDIS\_RECEIVE\_FILTER\_MSI\_X\_SUPPORTED** flag in the **SupportedQueueProperties** member of the [**NDIS\_RECEIVE\_FILTER\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566864) structure.

    The driver returns this structure in the [**NDIS\_MINIPORT\_ADAPTER\_HARDWARE\_ASSIST\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565924) structure that the driver uses in its call to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

-   The miniport driver must call the [**NdisGetRssProcessorInformation**](https://msdn.microsoft.com/library/windows/hardware/ff562669) function to obtain processor information for allocating interrupt vectors. It must not rely on registry keys or information obtained from other sources for interrupt allocation.

    [**NdisGetRssProcessorInformation**](https://msdn.microsoft.com/library/windows/hardware/ff562669) returns information about the set of processors that a miniport driver can use for RSS and VMQ. This information is contained in an [**NDIS\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567274) structure.

-   The miniport driver should allocate only one interrupt vector for each processor that is specified in the [**NDIS\_RSS\_PROCESSOR\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567274) structure.

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

     

 

 





