---
title: Extending Wireless Security Properties
description: Extending Wireless Security Properties
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , security properties
- security properties WDK Native 802.11 IHV UI Extensions DLL
ms.date: 04/20/2017
---

# Extending Wireless Security Properties




 

This topic describes how a Native 802.11 IHV UI Extensions DLL extends the properties of the **Security** tab that is displayed through the Network Configuration user interface (UI). In this situation, the Native 802.11 IHV UI Extensions DLL adds properties to the **Security** tab for proprietary security settings that are mutually exclusive from the Native 802.11 802.1X module.

The Native 802.11 IHV UI Extensions DLL can also extend the security and encryption methods that are supported by the Native 802.11 802.1X module. For more information about how the DLL does this, see [Extending Microsoft 802.1X Security Settings](extending-microsoft-802-1x-security-settings.md).

For more information about the Network Configuration UI and other Native 802.11 components, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

Before it displays the **Security** tab, the operating system does the following:

1.  Queries the Native 802.11 IHV UI Extensions DLL for its security property extensions through a call to the [**IDot11ExtUI::GetDot11ExtUIProperties**](/previous-versions/windows/hardware/wireless/ff553776(v=vs.85)) method. The operating system passes a value of **DOT11\_EXT\_UI\_SECURITY** to the method's *ExtType* parameter.

    If the Native 802.11 IHV UI Extension DLL supports one or more properties of type **DOT11\_EXT\_UI\_SECURITY**, the DLL returns (through the method's *ppDot11ExtUIProperty* parameter) a list of [IDot11ExtUIProperty COM interfaces](/previous-versions/windows/hardware/wireless/ff553746(v=vs.85)) for the security property extensions that are supported by the DLL. For more information about the COM interfaces used to extend security properties, see [Native 802.11 IHV UI Extensions COM Interfaces](native-802-11-ihv-ui-extensions-com-interfaces.md).

2.  Queries the friendly name of the security extension by calling the extension's [**IDot11ExtUIProperty::GetDot11ExtUIPropertyFriendlyName**](/previous-versions/windows/hardware/wireless/ff553768(v=vs.85)) method. The operating system adds the friendly name to the list of proprietary security settings at the bottom of the **Security** tab.

3.  If the end user selects an item from this list, the operating system will call the [**IDot11ExtUIProperty::Dot11ExtUIPropertyGetSelected**](/previous-versions/windows/hardware/wireless/ff553753(v=vs.85)) method of each security extension's [IDot11ExtUIProperty COM interfaces](/previous-versions/windows/hardware/wireless/ff553746(v=vs.85)). The first extension that returns with a value of **TRUE** for the method's *pfIsSelected* parameter is determined to be the selected extension. The selected entry in the list will then be highlighted.

4.  Queries the selected setting's [**IDot11ExtUIProperty::Dot11ExtUIPropertyHasConfigurationUI**](/previous-versions/windows/hardware/wireless/ff553756(v=vs.85)) method to determine whether it has a custom UI property page that can be displayed. If the method returns with the *fHasConfigurationUI* parameter set to **TRUE**, the operating system will add a **Configure** button next to the list of proprietary security settings.

If the selected proprietary security setting supports a configuration UI and the end user clicks the **Configure** button, the operating system calls the setting's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method to launch the custom UI. The operating system passes the current profile data for the setting through the method's *bstrIHVProfile* argument.

The profile data is formatted as an XML fragment bounded by the &lt;IHV&gt; &lt;/IHV&gt; XML tags. The XML data within these tags is specific to the IHV's implementation and is opaque to the operating system. For more information about the format of the Native 802.11 profile data, refer to the documentation within the Microsoft Windows SDK.

If the profile data is changed through the custom UI, the setting's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method must do the following before returning:

-   Allocate a string buffer for the modified profile data and return a pointer to the buffer through the method's *bstrModifiedIHVProfile* parameter.
    **Note**  The setting's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method must not modify the data that is referenced by the *bstrIHVProfile* argument.

     

-   Set the *pbIsModified* argument to **TRUE**.

 

 
