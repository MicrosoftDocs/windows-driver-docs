---
title: General discard reasons
description: This section describes General discard reasons for Windows Filtering Platform callout drivers.
keywords:
- General discard reasons network drivers
ms.date: 11/09/2017
ms.localizationpriority: medium
---

# General discard reasons

The identifiers for the possible reasons that the data is discarded by the filter engine are as follows. These identifiers are constant values in the FWPS_GENERAL_DISCARD_REASON enumeration that is defined in Fwpstypes.h.

| Discard reason identifier | Discard reason description |
| --- | --- |
| FWPS_DISCARD_FIREWALL_POLICY | An FWP_ACTION_BLOCK action was returned from a filtering decision. |
| FWPS_DISCARD_IPSEC | Reserved. |

