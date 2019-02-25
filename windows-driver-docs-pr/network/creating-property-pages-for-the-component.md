---
title: Creating Property Pages for the Component
description: Creating Property Pages for the Component
ms.assetid: f353844f-56f4-42cd-8f7d-2fa87f469d3c
keywords:
- notify objects WDK networking , property pages
- network notify objects WDK , property pages
- property pages WDK networking
- properties WDK networking
- property-page callback functions WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Property Pages for the Component





A notify object creates custom property pages after the network configuration subsystem calls the notify object's [**INetCfgComponentPropertyUi::MergePropPages**](https://msdn.microsoft.com/library/windows/hardware/ff547746) method. Custom property pages can be merged into the default set of pages on the component's property sheet using the **MergePropPages** method. **MergePropPages** will return the appropriate number of default pages into which the custom pages can be merged.

To create custom property pages, **MergePropPages** calls the COM **CoTaskMemAlloc** function to allocate memory for handles to PROPSHEETPAGE structures. Each of these handles represents a property page to create. If **CoTaskMemAlloc** successfully allocates the memory for the handles, **MergePropPages** will declare and fill **PROPSHEETPAGE** structures for each property page. After **MergePropPages** fills these structures, it calls the Win32 **CreatePropertySheetPage** function for each property page. In this call, **MergePropPages** passes the address of the PROPSHEETPAGE structure to create.

A dialog-box callback function should also be implemented for each property page that **MergePropPages** creates. A dialog-box callback function processes messages that the operating system sends to the property page that is associated with that dialog-box function. To associate a property page with a dialog-box function, **MergePropPages** should point the **pfnDlgProc** member of each PROPSHEETPAGE structure for each page to the dialog-box function for the page.

A dialog-box function processes the following messages:

-   The WM\_INITDIALOG message, which is sent to the dialog-box function immediately before the operating system displays its associated property page. Dialog-box functions typically use this message to initialize the property page and to perform tasks that affect the appearance of the property page.

-   The WM\_NOTIFY message, which is sent to the dialog-box function after an event occurs in the property page. Other information sent with this message identifies what event has occurred. This event information is contained in a pointer to a NMHDR structure. Information that NMHDR can contain for a property sheet includes, for example:
    -   The PSN\_APPLY event, which indicates that a user clicks OK, Close, or Apply on the property page. If the user clicks OK, Close, or Apply, the dialog-box function can call the **PropSheet\_Changed** macro to inform the property sheet that information in the page has changed. In this call, the dialog-box function passes handles to the property sheet and the page. The dialog-box function can call the Win32 **GetParent** function and pass the handle to the page to retrieve the handle to the property sheet.

        After the dialog-box function notifies the property sheet about the change, the network configuration subsystem calls the [**INetCfgComponentPropertyUi::ValidateProperties**](https://msdn.microsoft.com/library/windows/hardware/ff547755) method to check the validity of all changes. If all changes are valid, the subsystem calls the notify object's [**INetCfgComponentPropertyUi::ApplyProperties**](https://msdn.microsoft.com/library/windows/hardware/ff547741) method to cause all changes to take effect. The network configuration subsystem calls **ApplyProperties** before the operating system closes the dialog box.

        The **ApplyProperties** method can be implemented to retrieve information that the user enters and to set the information to the notify object's data members.

    -   The PSN\_RESET event, which indicates that the operating system is about to destroy a property page. A user might click Cancel on the property page to initiate this action. If the user clicks Cancel, the network configuration subsystem calls the [**INetCfgComponentPropertyUi::CancelProperties**](https://msdn.microsoft.com/library/windows/hardware/ff547742) method to cause all changes to be disregarded. The network configuration subsystem calls **CancelProperties** before the dialog box is closed.
    -   The PSN\_KILLACTIVE event, which indicates that a property page is about to become inactive. This event occurs when a user activates another page or clicks OK.

*Property-page callback* functions can also be implemented for each property page that **MergePropPages** creates. A property-page callback function performs initialization and cleanup operations for the page. To associate a property page with a property-page callback function, **MergePropPages** should point the **pfnCallback** member of each PROPSHEETPAGE structure for each page to the property-page callback function for that page.

See the Microsoft Windows SDK documentation For more information about:

-   creating property pages and on structures, functions, and notifications for property pages

-   dialog-box callback procedures, messages, and structures

 

 





