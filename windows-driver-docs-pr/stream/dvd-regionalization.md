---
title: DVD Regionalization
description: DVD Regionalization
keywords:
- DVD decoder minidrivers WDK
- regionalization WDK DVD decoder
ms.date: 04/20/2017
---

# DVD Regionalization





The DVD decoder minidriver should not be involved in any part of the regionalization process. Other parts of the streaming architecture enforce regionalization. Under most circumstances, the decoder minidriver does not implement the [**KS\_DVDCOPY\_REGION**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-_ks_dvdcopy_region) property.

If the decoder is limited to a certain region (by hardware or other considerations), then it may respond to the **KS\_DVDCOPY\_REGION** property to override all other system regions. The DVD decoder minidriver should set exactly one bit corresponding to the region that the decoder is designated for. Note that the logic is *inverted* from the region coding on the media. For example, a decoder designed to work only in Region 1 (USA) returns 0x01 to the **KS\_DVDCOPY\_REGION** property.

If the decoder provides a region, the system region change application still functions. It changes the system region in case there are other decoders in the system. Note that Windows DVD playback only functions if the system region and the decoder region match.

 

