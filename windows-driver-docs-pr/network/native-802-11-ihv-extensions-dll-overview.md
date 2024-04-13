---
title: Native 802.11 IHV Extensions DLL Overview
description: Native 802.11 IHV Extensions DLL Overview
keywords:
- IHV Extensions DLL WDK Native 802.11 , about Native 802.11 IHV Extensions DLL
- Native 802.11 IHV Extensions DLL WDK , about Native 802.11 IHV Extensions DLL
ms.date: 04/20/2017
---

# Native 802.11 IHV Extensions DLL Overview




 

Through an IHV Extensions DLL, the independent hardware vendor (IHV) can support the following:

-   Proprietary or non-standard authentication algorithms. Through this support, the IHV Extensions DLL sends and receives all security packets related to the authentication algorithm.

    The IHV Extensions DLL can also support standard authentication algorithms for network configurations that are not supported by the operating system. For example, the DLL can support the Wi-Fi Protected Access with preshared keys (WPA-PSK) authentication algorithm over independent basic service set (IBSS) networks, which is a configuration not supported by Windows Vista.

-   Proprietary or non-standard cipher algorithms. Through this support, the IHV Extensions DLL is responsible for deriving the cipher key and downloading the keys to the Native 802.11 miniport driver.

    The IHV Extensions DLL can also support standard cipher algorithms for network configurations that are not supported by the operating system. For example, the DLL can support the Temporal Key Integrity Protocol (TKIP) over IBSS networks, which is a configuration not supported by Windows Vista.

-   Verification of proprietary extensions to a network profile. For example, the IHV Extensions DLL is responsible for the validation of user settings for IHV-defined security options.

-   Configuration of the Native 802.11 miniport driver. For example, prior to starting a connection operation with the miniport driver, the operating system will call the [*Dot11ExtIhvPerformPreAssociate*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_perform_pre_associate) function so that the IHV Extensions DLL can configure the driver with proprietary extensions related to the connection to a BSS network.

-   Interface to the IHV UI Extensions DLL. Through this interface, the IHV Extensions DLL can request user input or notification. For more information about the IHV UI Extensions DLL, see [Native 802.11 IHV UI Extensions DLL](native-802-11-ihv-ui-extensions-dll2.md).

The Native 802.11 IHV Extensibility Host process loads the IHV Extensions DLL into its process space upon the first arrival and detection of a wireless LAN (WLAN) adapter for which the DLL was installed. For more information about the Native 802.11 IHV Extensibility Host process and Native 802.11 framework, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

The Native 802.11 IHV Extensibility Host process provides an API through its IHV Extensibility functions. Through this API, the IHV Extensions DLL can interface the Native 802.11 miniport driver or IHV UI Extensions DLL. For more information about the IHV Extensibility functions, see [Native 802.11 IHV Extensibility Functions](./native-802-11-ihv-extensibility-functions.md).

Similarly, the IHV Extensions DLL provides an API through its IHV Handler functions. The Native 802.11 IHV Extensibility Host process uses this API for various operations, such as initiating pre- or post-association operations. For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](./native-802-11-ihv-handler-functions.md).

 

 
