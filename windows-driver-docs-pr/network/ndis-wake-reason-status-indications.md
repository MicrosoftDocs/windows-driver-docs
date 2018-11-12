---
title: NDIS Wake Reason Status Indications
description: NDIS Wake Reason Status Indications
ms.assetid: 0229A4F3-8CC1-4A81-9AF4-33BAEBDAE954
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Wake Reason Status Indications


Starting with NDIS 6.30, miniport drivers issue an NDIS wake reason status indication ([**NDIS\_STATUS\_PM\_WAKE\_REASON**](https://msdn.microsoft.com/library/windows/hardware/hh439808)) to notify NDIS and overlying drivers about the reason for a system wake-up event. If the network adapter generates a wake-up event, the miniport driver immediately issues this NDIS status indication when the system resumes to a full-power state.

**Note**  Support for NDIS wake reason status indications is optional for Mobile Broadband (MB) miniport drivers.

 

This section includes the following topics:

[Overview of NDIS Wake Reason Status Indications](overview-of-ndis-wake-reason-statue-indications.md)

[Reporting Wake Reason Status Indication Capabilities](reporting-wake-reason-status-indication-capabilities.md)

[Issuing NDIS Wake Reason Status Indications](issuing-ndis-wake-reason-indications.md)

 

 





