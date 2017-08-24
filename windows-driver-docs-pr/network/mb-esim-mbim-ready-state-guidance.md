---
title: MB eSIM MBIM ready state guidance
description: MB eSIM MBIM ready state guidance
ms.assetid: E7EB5E6D-1858-4B94-AF91-05333CC93D8B
ms.author: windowsdriverdev
ms.date: 08/10/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MB eSIM MBIM ready state guidance

This topic provides guidance on the expected MBIM ready state for eSIM scenarios on Windows 10, version 1709 and later. Conforming to the correct ready state ensures that the OS handles all changes properly for that scenario. 

> [!IMPORTANT]
> All scenarios and states in this topic assume that the eSIM capable card is mapped to the default executor, executor 0, and is powered ON.

| Scenario | MBIM_MS_UICCSLOT_STATE | MBIM_SUBSCRIBER_READY_STATE |
| --- | --- | --- |
| eSIM with MF only (no profiles) | MBIMMsUICCSlotStateActiveEsimNoProfiles | MBIMSubscriberReadyStateNoEsimProfile |
| eSIM with no enabled profiles | MBIMMsUICCSlotStateActiveEsimNoProfiles | MBIMSubscriberReadyStateNoEsimProfile |
| eSIM with profile enabled | MBIMMsUICCSlotStateActiveEsim | MBIMSubscriberReadyStateInitialized |
| eSIM in passthrough mode | MBIMMsUICCSlotStateActiveEsimNoProfiles | MBIMSubscriberReadyStateNotInitialized |

When a change in both MBIM_MS_UICCSLOT_STATE and MBIM_SUBSCRIBER_READY_STATE is needed, the slot state change should precede the ready state change. 

When enabling a new profile or switching between profiles, the ready state should have the following flow:

![eSIM MBIM ready state flow when switching profiles](images/esim_mbim_ready_state_flow.png "eSIM MBIM ready state flow when switching profiles")

For more info about MBIM_MS_UICCSLOT_STATE, see the MBIM_MS_UICCSLOT_STATE table on [MB Multi-SIM Operations (MBIM_CID_MS_SLOT_INFO_STATUS)](mb-multi-sim-operations.md#mbimcidmsslotinfostatus).-ndis-status-dot11-wfd-group-operating-channel.md

For more info about MBIM_SUBSCRIBER_READY_STATE, see Section 10.5.2.3 of [the public USB MBIM standard](https://go.microsoft.com/fwlink/p/?linkid=842064).

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")