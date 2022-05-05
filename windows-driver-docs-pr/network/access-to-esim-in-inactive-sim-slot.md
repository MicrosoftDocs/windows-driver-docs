---
title: Access an eSIM in an inactive SIM slot
description: MBIMEx 4.0 supports full access to an eSIM in the inactive SIM slot of a DSSA modem.
keywords:
- Access to eSIM in inactive SIM slot
ms.date: 05/04/2022
---

# Access an eSIM in the inactive SIM slot

Before the Windows 11 2022 OS release, all eSIM access related CIDs in the MBIM interface target the SIM in the active SIM slot in DSSA modems. The active SIM slot is the slot currently mapped to the executor, as supplied in MBIM_CID_MS_DEVICE_SLOT_MAPPINGS (or the only SIM slot in a single-SIM modem). As a result, eSIM functionality is only applicable if an eSIM resides in the active SIM slot in a DSSA modem. If an eSIM resides in the inactive slot in a DSSA modem, there is no access to the eSIM. 

In the Windows 11 Insider Preview Build 22610 release, [MBIMEx 4.0](mbimex-4.0-5g-sa-phase-2-support.md) introduces access to an eSIM in the inactive SIM slot. MBIMEx 4.0 extends the following CIDs with a slot ID element (and other necessary information) to support full access to an eSIM in the inactive slot of a DSSA modem, in addition to the eSIM in the active SIM slot.

* MBIM_CID_MS_UICC_ATR
* MBIM_CID_MS_UICC_OPEN_CHANNEL
* MBIM_CID_MS_UICC_CLOSE_CHANNEL
* MBIM_CID_MS_UICC_APDU
* MBIM_CID_MS_UICC_TERMINAL_CAPABILITY
* MBIM_CID_MS_UICC_RESET
* MBIM_CID_SUBSCRIBER_READY_STATUS

[Download the MBIMEx 4.0 specification here](https://download.microsoft.com/download/d/8/a/d8ad97b9-83bd-4ab2-bcea-7500dfaf22b4/MBIMEx%204.0%20spec%20and%20Errata%20to%20MBIMEx%203.0%20Rev%201.46%2020220426.docx).

For general information about MBIMEx 4.0, see [MBIMEx 4.0 – 5G SA Phase 2 support](mbimex-4.0-5g-sa-phase-2-support.md).