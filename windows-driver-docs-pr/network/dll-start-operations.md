---
title: DLL Start Operations
description: DLL Start Operations
ms.assetid: cab7a4f9-35dc-44fc-bdd0-30bac8beb652
keywords:
- IHV Extensions DLL WDK Native 802.11 , start operations
- starting IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , start operations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DLL Start Operations


**Important**  The [Native 802.11 Wireless LAN](native-802-11-wireless-lan4.md) interface is deprecated in Windows 10 and later. Please use the WLAN Device Driver Interface (WDI) instead. For more information about WDI, see [WLAN Universal Windows driver model](wifi-universal-driver-model.md).

 

Immediately after loading the IHV Extensions DLL, the operating system calls the following IHV Handler functions in this sequence.

1.  The operating system calls the [*Dot11ExtIhvGetVersionInfo*](https://msdn.microsoft.com/library/windows/hardware/ff547464) IHV Handler function to determine the interface versions supported by the IHV Extensions DLL. This function is passed a pointer to a [**DOT11\_IHV\_VERSION\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff548645) structure, which the DLL formats with the minimum and maximum interface versions that it supports.
    **Note**  For Windows Vista, the IHV Extensions DLL must set the **dwVerMin** and **dwVerMax** members of the DOT11\_IHV\_VERSION\_INFO structure to zero.

     

2.  If the IHV Extensions DLL supports an interface version that is supported by the operating system, the operating system calls the [*Dot11ExtIhvInitService*](https://msdn.microsoft.com/library/windows/hardware/ff547470) IHV Handler function to initialize the DLL.

The IHV Extensions DLL must follow these guidelines when [*Dot11ExtIhvInitService*](https://msdn.microsoft.com/library/windows/hardware/ff547470) is called.

-   The *pDot11ExtAPI* parameter contains a pointer to a [**DOT11EXT\_APIS**](https://msdn.microsoft.com/library/windows/hardware/ff547617) structure, which is formatted with the addresses of the IHV Extensibility functions supported by the operating system. The IHV Extensions DLL must copy the DOT11EXT\_APIS structure, which is referenced by the *pDot11ExtAPI* parameter, to a globally-declared DOT11EXT\_APIS structure.

-   The *pDot11IHVHandlers* parameter contains a pointer to a [**DOT11EXT\_IHV\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff547625) structure, which the IHV Extensions DLL formats with the addresses of the IHV Handler functions that it supports.
    **Note**  The DLL must not set any of the members of the DOT11EXT\_IHV\_HANDLERS structure to **NULL**.

     

-   The IHV Extensions DLL should perform any internal initialization and resource allocation in preparation for calls to its IHV Handler functions after the DLL returns from [*Dot11ExtIhvInitService*](https://msdn.microsoft.com/library/windows/hardware/ff547470).

For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](https://msdn.microsoft.com/library/windows/hardware/ff560609).

For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](https://msdn.microsoft.com/library/windows/hardware/ff560627).

 

 





