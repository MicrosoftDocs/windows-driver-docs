---
title: 802.11 WLAN Adapter Removal
description: 802.11 WLAN Adapter Removal
keywords:
- adapters WDK 802.11 WLAN , removing
- WLAN adapters WDK , removing
- removing WLAN adapters
ms.date: 04/20/2017
---

# 802.11 WLAN Adapter Removal




 

When a wireless LAN (WLAN) adapter is removed or disabled, the operating system calls [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) to notify the IHV Extensions DLL of the adapter's removal. The operating system also calls the *Dot11ExtIhvDeinitAdapter* function for every adapter managed by the IHV Extensions DLL before the operating system unloads the DLL.

When [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) is called, the IHV Extensions DLL must follow these guidelines.

-   The IHV Extensions DLL must free any allocated resources for the WLAN adapter. In particular, all memory allocated through calls to [**Dot11ExtAllocateBuffer**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_allocate_buffer) must be freed through calls to [**Dot11ExtFreeBuffer**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_free_buffer).

-   The handle used by the operating system to reference the WLAN adapter is no longer valid when [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) is called. The operating system passes its handle to the IHV Extensions DLL through the *hDot11SvcHandle* parameter when [*Dot11ExtIhvInitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_adapter) is called.

    Within the call to the *Dot11ExtIhvDeinitAdapter* function and after returning from the call, the DLL must not use the handle value when calling any IHV Extensibility function that declares an *hDot11SvcHandle* parameter, such as [**Dot11ExtSendPacket**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_packet).

-   If the IHV Extensions DLL had a pending pre-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) IHV Handler function, the operating system regards the operation as canceled through the call to the [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) function. Within the call, the DLL must cancel the pre-association operation internally but must not call [**Dot11ExtPreAssociateCompletion**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_pre_associate_completion) to complete the pre-association operation.

    For more information about the pre-association operation, see [Pre-Association Operations](pre-association-operations.md).

-   If the IHV Extensions DLL had a pending post-association operation, which was initiated through a call to the [*Dot11ExtIhvPerformPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_post_associate) IHV Handler function, the operating system cancels the operation by calling the [*Dot11ExtIhvStopPostAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_stop_post_associate) function before it calls [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter).

    For more information about the post-association operation, see [Post-Association Operations](post-association-operations.md).

-   The operating system calls the [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) function for every adapter managed by the IHV Extensions DLL before the operating system unloads the DLL. In this situation, the operating system calls the [*Dot11ExtIhvDeinitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_service) IHV Handler function after the last WLAN adapter has been halted through a call to *Dot11ExtIhvDeinitAdapter*.

    For more information about this operation, see [DLL Stop Operations](dll-stop-operations.md).

 

 
