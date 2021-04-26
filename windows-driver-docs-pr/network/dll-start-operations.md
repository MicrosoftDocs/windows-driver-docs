---
title: DLL Start Operations
description: DLL Start Operations
keywords:
- IHV Extensions DLL WDK Native 802.11 , start operations
- starting IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , start operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DLL Start Operations




 

Immediately after loading the IHV Extensions DLL, the operating system calls the following IHV Handler functions in this sequence.

1.  The operating system calls the [*Dot11ExtIhvGetVersionInfo*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_get_version_info) IHV Handler function to determine the interface versions supported by the IHV Extensions DLL. This function is passed a pointer to a [**DOT11\_IHV\_VERSION\_INFO**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11_ihv_version_info) structure, which the DLL formats with the minimum and maximum interface versions that it supports.
    **Note**  For Windows Vista, the IHV Extensions DLL must set the **dwVerMin** and **dwVerMax** members of the DOT11\_IHV\_VERSION\_INFO structure to zero.

     

2.  If the IHV Extensions DLL supports an interface version that is supported by the operating system, the operating system calls the [*Dot11ExtIhvInitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) IHV Handler function to initialize the DLL.

The IHV Extensions DLL must follow these guidelines when [*Dot11ExtIhvInitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) is called.

-   The *pDot11ExtAPI* parameter contains a pointer to a [**DOT11EXT\_APIS**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_apis) structure, which is formatted with the addresses of the IHV Extensibility functions supported by the operating system. The IHV Extensions DLL must copy the DOT11EXT\_APIS structure, which is referenced by the *pDot11ExtAPI* parameter, to a globally-declared DOT11EXT\_APIS structure.

-   The *pDot11IHVHandlers* parameter contains a pointer to a [**DOT11EXT\_IHV\_HANDLERS**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_ihv_handlers) structure, which the IHV Extensions DLL formats with the addresses of the IHV Handler functions that it supports.
    **Note**  The DLL must not set any of the members of the DOT11EXT\_IHV\_HANDLERS structure to **NULL**.

     

-   The IHV Extensions DLL should perform any internal initialization and resource allocation in preparation for calls to its IHV Handler functions after the DLL returns from [*Dot11ExtIhvInitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service).

For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](./native-802-11-ihv-extensibility-functions.md).

For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](./native-802-11-ihv-handler-functions.md).

 

 
