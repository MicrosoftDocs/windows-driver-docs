---
title: Accessing Profile and Context Data
description: Accessing Profile and Context Data
keywords:
- custom UI WDK Native 802.11 IHV UI Extensions DLL , profile data
- custom UI WDK Native 802.11 IHV UI Extensions DLL , context data
- context data WDK networking
- profile data WDK networking
ms.date: 04/20/2017
---

# Accessing Profile and Context Data




 

A custom user interface (UI) that is supported by the Native 802.11 IHV UI Extensions DLL can be displayed through either:

-   A call to [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) made by the Native 802.11 IHV Extensions DLL. For more information about this process, see [Requesting the Display of a Custom UI](requesting-the-display-of-a-custom-ui.md).

-   A call to the Native 802.11 IHV Extensions DLL's *Dot11ExtQueryUIRequest* IHV Handler function made by the operating system. For more information about this process, see [Querying for the Display of a Custom UI](querying-for-the-display-of-a-custom-ui.md).

Regardless of whether the UI request is displayed through either a balloon notification or the operating system's Network Connection Wizard, the Native 802.11 IHV UI Extensions DLL can access the following data:

<a href="" id="network-connection-profile-data"></a>**Network connection profile data**  
If the custom UI is displayed within the Network Connection Wizard, the Native 802.11 IHV UI Extensions DLL can access the IHV-defined portion of the current network connection profile. This data is formatted as an XML fragment bounded by the &lt;IHV&gt; &lt;/IHV&gt; XML tags. The XML data within these tags is specific to the IHV's implementation and is opaque to the operating system.

Access to the profile data is through the **Read** and **Write** methods of the [IPropertyBag COM interface](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768196(v=vs.85)) for a property named **IHV\_PROFILE\_DATA**.

<a href="" id="context-data"></a>**Context data**  
The Native 802.11 IHV Extensions DLL specifies a custom UI through a [**DOT11EXT\_IHV\_UI\_REQUEST**](/windows-hardware/drivers/ddi/wlanihv/ns-wlanihv-_dot11ext_ihv_ui_request) structure, which is passed as an argument in both the [**Dot11ExtSendUIRequest**](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11ext_send_ui_request) and [*Dot11ExtIhvQueryUIRequest*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_query_ui_request) functions. Within the DOT11EXT\_IHV\_UI\_REQUEST structure, the IHV can provide (through the **pvUIRequest** member) context data specific to the custom UI. Typically, the IHV formats this data with default settings for the custom UI.

Access to the profile data is through the **Read** and **Write** methods of the [IPropertyBag COM interface](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768196(v=vs.85)) for a property named **IHV\_NOTIFICATION\_DATA**.

The Native 802.11 IHV UI Extensions DLL accesses the [IPropertyBag COM interface](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768196(v=vs.85)) through the *IUnknown* pointer returned through the [**IObjectWithSite::SetSite**](/windows/win32/api/ocidl/nf-ocidl-iobjectwithsite-setsite) method. For more information, see [**IObjectWithSite**](/windows/win32/api/ocidl/nn-ocidl-iobjectwithsite).

As an alternative to the IPropertyBag COM interface, the Native 802.11 IHV UI Extensions DLL can access the **IHV\_PROFILE\_DATA** and **IHV\_NOTIFICATION\_DATA** properties through the [**GetProp**](/windows/win32/api/winuser/nf-winuser-getpropa) Win32 function. In this situation, the DLL must use the handle of the parent window, as shown in the following example:

```C++
LPWSTR lpszBuffer = (LPWSTR) GetProp(GetParent(hwndDlg), L"IHV_PROFILE_DATA");
```

 

 
