---
title: 802.11 WLAN Adapter Reset
description: 802.11 WLAN Adapter Reset
keywords:
- adapters WDK 802.11 WLAN , resetting
- WLAN adapters WDK , resetting
- resetting WLAN adapters
ms.date: 04/20/2017
---

# 802.11 WLAN Adapter Reset




 

The operating system calls [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) whenever it becomes necessary to restore the wireless LAN (WLAN) adapter to its initialized state. The operating system calls this function whenever one of the following events occurs.

-   The WLAN adapter performs a disconnection operation. For more information about this operation, see [Disconnection Operations](/previous-versions/windows/hardware/wireless/disconnection-operations).

-   The operating system resets the Native 802.11 miniport driver, which manages the adapter, through a set request of [OID\_DOT11\_RESET\_REQUEST](/previous-versions/windows/hardware/wireless/oid-dot11-reset-request).

When [*Dot11ExtIhvAdapterReset*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_adapter_reset) is called, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL must restore its state to the same state it was in after the [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) function was called. If the DLL configured proprietary settings on the WLAN adapter, it must restore these settings to the same state they were in after *Dot11ExtIhvInitAdapter* was called.

-   If the IHV Extensions DLL had a pending pre-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) IHV Handler function, the DLL must call [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion) to cancel the operation. In this situation, the DLL sets the *dwWin32Error* parameter of **Dot11ExtPreAssociateCompletion** to ERROR\_CANCELLED.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

-   If the DLL had a pending post-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate) IHV Handler function, the DLL must call [**Dot11ExtPostAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_post_associate_completion) to cancel the operation. In this situation, the DLL sets the *dwWin32Error* parameter of **Dot11ExtPostAssociateCompletion** to ERROR\_CANCELLED.

    For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

 

 
