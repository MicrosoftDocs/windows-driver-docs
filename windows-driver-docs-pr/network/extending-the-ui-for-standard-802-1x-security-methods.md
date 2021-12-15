---
title: Extending the UI for Standard 802.1X Security Methods
description: Extending the UI for Standard 802.1X Security Methods
keywords:
- standard 802.1X security WDK IHV UI Extensions DLL
ms.date: 04/20/2017
---

# Extending the UI for Standard 802.1X Security Methods




 

If the Native 802.11 IHV Extensions DLL supports proprietary encryption extensions that can be used with the operating system's 802.1X security methods, the Native 802.11 IHV UI Extensions DLL can extend the Network Configuration user interface's (UI')s **Security** tab to allow user configuration of the these extensions. For more information about extending the Native 802.11 802.1X module, see [Interface to the Native 802.11 802.1X Module](interface-to-the-native-802-11-802-1x-module.md).

For more information about the Network Configuration UI and other Native 802.11 components, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

Before it displays the **Security** tab,the operating system does the following:

1.  Queries the Native 802.11 IHV UI Extensions DLL for its security property extensions through a call to the [**IDot11ExtUI::GetDot11ExtUIProperties**](/previous-versions/windows/hardware/wireless/ff553776(v=vs.85)) method. The operating system passes a value of **DOT11\_EXT\_UI\_KEYEXTENSION** to the method's *ExtType* parameter.

    Property extensions of type **DOT11\_EXT\_UI\_KEYEXTENSION** do not provide security settings that are mutually exclusive to the standard Microsoft security settings. Instead, this type of security property extension provides IHV-defined 802.1X settings that are used together with the Microsoft 802.1X settings.

2.  Queries the friendly name of the 802.1X security extension by calling the extension's [**IDot11ExtUIProperty::GetDot11ExtUIPropertyFriendlyName**](/previous-versions/windows/hardware/wireless/ff553768(v=vs.85)) method.

3.  Queries the extension's [**IDot11ExtUIProperty::Dot11ExtUIPropertyIsStandardSecurity**](/previous-versions/windows/hardware/wireless/ff553760(v=vs.85)) method to determine whether the extension supports a security type extension. If the method sets the *fIsStandardSecurity* parameter to **TRUE**, the operating system will not add the extension's friendly name to the **Security type** list on the **Security** tab.

    In this situation, the extension adds functionality to the security settings that are supported by the operating system. The method specifies the type of security setting it extends through the *dot11ExtUISecurityType* parameter.

4.  When the end user selects an item from the **Security type** list, the operating system responds by calling the [**IDot11ExtUIProperty::Dot11ExtUIPropertyGetSelected**](/previous-versions/windows/hardware/wireless/ff553753(v=vs.85)) method for each extension to match the selection of the end user. The first extension that returns a value of **TRUE** for the method's *pfIsSelected* parameter is determined to be the selected extension. After this is confirmed, the operating system highlights the selection made by the end user.

5.  When the end user selects an item for a standard security setting from the **Security type** list, the operating system calls the [**IDot11ExtUIProperty::Dot11ExtUIPropertyGetDisplayInfo**](/previous-versions/windows/hardware/wireless/ff553752(v=vs.85)) method of the property extension that extends the security method. Through the **IDot11ExtUIProperty::Dot11ExtUIPropertyGetDisplayInfo** method, the Native 802.11 IHV UI Extensions DLL can return other items to be added to the **Security** tab of the Native 802.11 Network Configuration UI.

    The **IDot11ExtUIProperty::Dot11ExtUIPropertyGetDisplayInfo** method returns a list of the extended display properties that are supported by the property extension. Each item in the list is formatted as a [**DOT11\_EXT\_UI\_PROPERTY\_DISPLAY\_INFO**](/previous-versions/windows/hardware/drivers/ff548637(v=vs.85)) structure.

    For Windows Vista, the Native 802.11 IHV UI Extensions DLL can only add items to the **Encryption** list on the **Security** tab. As a result, each entry within the list of [**DOT11\_EXT\_UI\_PROPERTY\_DISPLAY\_INFO**](/previous-versions/windows/hardware/drivers/ff548637(v=vs.85)) structures must have a **DOT11\_EXT\_UI\_DISPLAY\_INFO\_TYPE** of **DOT11\_EXT\_UI\_DISPLAY\_INFO\_CIPHER** in order to be included in the **Encryption** list.

6.  When the end user selects from the **Encryption** list, the operating system will call the property extension's [**IDot11ExtUIProperty::Dot11ExtUIPropertySetDisplayInfo**](/previous-versions/windows/hardware/wireless/ff553763(v=vs.85)) method to process the profile data that is associated with the end user's selection.

 

 
