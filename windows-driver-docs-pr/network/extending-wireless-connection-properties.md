---
title: Extending Wireless Connection Properties
description: Extending Wireless Connection Properties
keywords:
- IHV UI Extensions DLL WDK Native 802.11 , wireless connection properties
- wireless connection properties WDK Native 802.11 IHV UI Extensions DLL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extending Wireless Connection Properties




 

This topic describes how a Native 802.11 IHV UI Extensions DLL extends the properties on the **Connection** tab that are displayed through the Network Configuration user interface (UI). In this situation, the Native 802.11 IHV UI Extensions DLL adds properties to the **Connection** tab for proprietary connection settings.

For more information about the Network Configuration UI and other Native 802.11 components, see [Native 802.11 Software Architecture](/previous-versions/windows/hardware/wireless/native-802-11-software-architecture).

Before it displays the **Connection** tab, the operating system does the following:

1.  Queries the Native 802.11 IHV UI Extensions DLL for its connection properties through a call to the [**IDot11ExtUI::GetDot11ExtUIProperties**](/previous-versions/windows/hardware/wireless/ff553776(v=vs.85)) method. The operating system passes a value of **DOT11\_EXT\_UI\_CONNECTION** to the method's *ExtType* parameter.

    If the Native 802.11 IHV UI Extension DLL supports a property of type **DOT11\_EXT\_UI\_CONNECTION**, the DLL returns (through the method's *ppDot11ExtUIProperty* parameter) the address of the [IDot11ExtUIProperty COM interface](/previous-versions/windows/hardware/wireless/ff553746(v=vs.85)), which implements the connection property extension. For more information about the COM interfaces that are used to extend connection properties, see [Native 802.11 IHV UI Extensions COM Interfaces](native-802-11-ihv-ui-extensions-com-interfaces.md).

    **Note**  For Windows Vista, the Native 802.11 IHV UI Extensions DLL must not return more than one [IDot11ExtUI COM Interface](/previous-versions/windows/hardware/wireless/ff553769(v=vs.85)) for a connection property extension.

     

2.  If the Native 802.11 IHV UI Extensions DLL supports a connection property, the operating system queries the friendly name of the property extension by calling the extension's [**IDot11ExtUIProperty::GetDot11ExtUIPropertyFriendlyName**](/previous-versions/windows/hardware/wireless/ff553768(v=vs.85)) method. The operating system inserts the friendly name within the text "Enable *xxx* connection settings," where "*xxx*" is the friendly name of the property extension. The operating system displays this text along with a check box on the **Connection** tab.

3.  Queries the extension to determine whether it has a custom UI property that can be displayed. The operating system does this by calling the extension's [**IDot11ExtUIProperty::Dot11ExtUIPropertyHasConfigurationUI**](/previous-versions/windows/hardware/wireless/ff553756(v=vs.85)) method. If the connection property extension supports a custom UI property, the operating system adds a **Configure** button below the check box for the property.

If the selected proprietary connection setting supports a configuration UI and the end user clicks the **Configure** button in the**Connection** tab, the operating system calls the connection property extension's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method to launch the custom UI. The operating system passes the current profile data for the extension through the method's *bstrIHVProfile* argument.

The profile data is formatted as an XML fragment bounded by the &lt;IHV&gt; &lt;/IHV&gt; XML tags. The XML data within these tags is specific to the IHV's implementation and is opaque to the operating system. For more information about the format of the Native 802.11 profile data, refer to the documentation within the Microsoft Windows SDK.

If the profile data is changed through the custom UI, the extension's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method must do the following before returning:

-   Allocate a string buffer for the modified profile data and return a pointer to the buffer through the method's *bstrModifiedIHVProfile* parameter.
    **Note**  The extension's [**IDot11ExtUIProperty::DisplayDot11ExtUIProperty**](/previous-versions/windows/hardware/wireless/ff553749(v=vs.85)) method must not modify the data referenced by the *bstrIHVProfile* argument.

     

-   Set the *pbIsModified* argument to **TRUE**.

 

 
