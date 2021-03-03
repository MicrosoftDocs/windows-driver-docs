---
title: Standardized INF keywords for VMMQ
description: The *RssOnHostVPorts standardized INF keyword is defined to enable or disable support for VMMQ.
ms.date: 02/28/2021
ms.localizationpriority: medium
---

# Standardized INF keywords for VMMQ

The **\*RssOnHostVPorts** standardized INF keyword is defined to enable or disable support for the network adapter [Virtual Machine Multiple Queues (VMMQ)](overview-of-virtual-machine-multiple-queues.md) feature.

The **\*RssOnHostVPorts** INF keyword is an enumeration keyword. Enumeration standardized INF keywords have the following attributes:

SubkeyName: The name of the keyword that you must specify in the INF file.

ParamDesc: The display text that is associated with the SubkeyName. 

Value: The enumeration integer value that is associated with each SubkeyName in the list. 

EnumDesc: The display text that is associated with each value that appears in the menu.

Default: The default value for the menu.

The following table describes the possible INF entries for the **\*RssOnHostVPorts** INF keyword.

| SubkeyName       | ParamDesc          | Value       | EnumDesc |
|-------------------|--------------------|-------------|----------|
| \*RssOnHostVPorts | Virtual Switch RSS | 0 (Default) | Disabled |
|                   |                    | 1           | Enabled  |

During miniport adapter initialization, the miniport driver must examine the **\*RssOnHostVPorts** keyword to determine if it should enable the VMMQ feature on the NIC.

## Handling RSS INF keywords for VMMQ

If a NIC supports VMMQ, all [Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md) should also be supported to provide future compatibility even if the OS doesn't not currently use them all.
You should use the keywords as normal for RSS functionality except for:

-   **\*RSSProfile**: The “ClosestProcessor” profile should be supported and used as a policy for VMMQ.

-   **\*MaxRssProcessors**: When VMMQ is active, this keyword should not restrict the number of MSIx interrupt messages reported in [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities).