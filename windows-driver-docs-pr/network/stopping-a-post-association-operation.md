---
title: Stopping a Post-Association Operation
description: Stopping a Post-Association Operation
keywords:
- post-association operations WDK Native 802.11 IHV Extensions DLL
- stopping post-association operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stopping a Post-Association Operation




 

The operating system terminates the post-association operation by calling the [*Dot11ExtIhvStopPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate) IHV Handler function whenever one of the following occurs.

-   The wireless LAN (WLAN) adapter completes a disassociation operation with the AP. In this situation, the Native 802.11 station, which manages the adapter, makes a media-specific [NDIS\_STATUS\_DOT11\_DISASSOCIATION](/previous-versions/windows/hardware/wireless/ndis-status-dot11-disassociation) indication. For more information about the disassociation operation, see [Disassociation Operations](/previous-versions/windows/hardware/wireless/disassociation-operations).

-   The WLAN adapter is disabled or removed. In this situation, the operating system calls the [*Dot11ExtIhvStopPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate) function before it calls the [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) function.

The operating system calls the [*Dot11ExtIhvStopPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate) function to notify the IHV Extensions DLL that the data port created for the association with an AP is down. The operating system calls this function regardless of whether the DLL has completed the post-association operation through a call to [**Dot11ExtPostAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion).

When [*Dot11ExtIhvStopPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate) is called, the IHV Extensions must release all of the resources allocated for the data port. If the post-association operation was not completed with a call to [**Dot11ExtPostAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion), the IHV Extensions DLL must cancel the operation internally but must not call **Dot11ExtPostAssociateCompletion**.

 

 
