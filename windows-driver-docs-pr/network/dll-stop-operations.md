---
title: DLL Stop Operations
description: DLL Stop Operations
keywords:
- IHV Extensions DLL WDK Native 802.11 , stop operations
- unloading IHV Extensions DLL
- stopping IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , stop operations
ms.date: 04/20/2017
---

# DLL Stop Operations




 

The operating system stops and unloads the IHV Extensions DLL whenever.

-   The last wireless LAN (WLAN) adapter managed by the DLL is either removed or disabled.

-   The host computer is reset or shut down.

The operating system follows this sequence when stopping and unloading the IHV Extensions DLL.

1.  The operating system first calls the [*Dot11ExtIhvDeinitAdapter*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_adapter) IHV Handler function for every WLAN adapter managed by the IHV Extensions DLL. For more information about this operation, see [802.11 WLAN Adapter Removal](802-11-wlan-adapter-removal.md).

    After the call to *Dot11ExtIhvDeinitAdapter*, the IHV Extensions DLL must not call any IHV Extensions function related to adapter-specific operations, such as [**Dot11ExtNicSpecificExtension**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_nic_specific_extension).

2.  The operating system then calls the [*Dot11ExtIhvDeinitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_deinit_service) IHV Handler function. When this function is called, the IHV Extensions DLL must free all allocated resources and prepare itself for unloading.

    After the call to *Dot11ExtIhvDeinitService*, the IHV Extensions DLL must not call any IHV Extensions function.

3.  Finally, the operating system calls the *DllMain* function in the IHV Extensions DLL with the *fdwReason* parameter set to DLL\_PROCESS\_DETACH. For more information about *DllMain* and DLLs, refer to the topic "About Dynamic-Link Libraries" within the Microsoft Windows SDK documentation.

For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](./native-802-11-ihv-extensibility-functions.md).

 

 
