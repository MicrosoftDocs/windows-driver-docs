---
title: Native 802.11 IHV UI Extensions COM Interfaces
description: Native 802.11 IHV UI Extensions COM Interfaces
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , COM interfaces
- COM interfaces WDK Native 802.11 IHV UI Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Native 802.11 IHV UI Extensions COM Interfaces




 

The Native 802.11 IHV UI Extensions DLL implements one or more of the following COM interfaces:

<a href="" id="idot11extui"></a>**IDot11ExtUI**  
Through the **IDot11ExtUI** COM interface, the operating system's Native 802.11 Network Configuration UI can interact with the Native 802.11 IHV UI Extensions DLL. For example, this COM interface provides the methods used by the Native 802.11 Network Configuration UI to query the DLL for the **IDot11ExtUIProperty** COM interfaces that are used to extend the operating system's 802.11 connection and security properties.

The Native 802.11 IHV UI Extensions DLL must provide an implementation of the **IDot11ExtUI** COM interface.

For more information about this COM interface, see [IDot11ExtUI COM Interface](/previous-versions/windows/hardware/wireless/ff553769(v=vs.85)).

<a href="" id="idot11extuiproperty"></a>**IDot11ExtUIProperty**  
Through the **IDot11ExtUIProperty** COM interface, the Native 802.11 IHV UI Extensions DLL can extend the connection and security properties that are displayed by the Native 802.11 Network Configuration UI.

The **IDot11ExtUIProperty** COM interface is optional and is only required if the Native 802.11 IHV UI Extensions DLL supports extensions to the operating system's 802.11 connection and security properties.

The Native 802.11 IHV UI Extensions DLL can provide one or more implementations of the **IDot11ExtUIProperty** COM interface, with each implementation representing an IHV-defined extension to a Native 802.11 property. The DLL can provide one or more property extensions for security settings. For Windows Vista, the DLL can add no more than one property extension for connection settings.

For more information about this COM interface, see [IDot11ExtUIProperty COM Interface](/previous-versions/windows/hardware/wireless/ff553746(v=vs.85)).

<a href="" id="iwizardextension"></a>**IWizardExtension**  
The Native 802.11 IHV UI Extensions DLL can provide one or more implementations of the **IWizardExtension** COM interface. Each implementation supports the display of one or more custom UI pages. These UI pages are displayed through one of the following:

-   An external request made by the Native 802.11 IHV Extensions DLL. For more information about this process, see [Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md).

-   A query made by the operating system to determine whether the Native 802.11 IHV Extensions DLL has a custom UI to display. For more information about this process, see [Querying for the Display of a Custom UI](querying-for-the-display-of-a-custom-ui.md).

-   An internal request made by a component of the Native 802.11 IHV UI Extensions DLL.

For more information about the **IWizardExtension** COM interface, see [IWizardExtension COM Interface](/windows/win32/api/shobjidl/nn-shobjidl-iwizardextension).

For more information about the Native 802.11 Network Configuration UI component, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

 

 
