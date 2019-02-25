---
title: Property Page Callback Function
description: Property Page Callback Function
ms.assetid: 3f4d7247-2a12-4889-9fc0-a28f58046c7b
keywords:
- device property pages WDK device installations , callback functions
- property pages WDK device installations , callback functions
- custom property pages WDK device installations , callback functions
- callback functions WDK property page
- PSPCB_CREATE
- PSPCB_RELEASE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Property Page Callback Function





When a provider creates a property page for its device or device class, it supplies a pointer to a callback function. The callback function is called one time when the property page is created and again when it is about to be destroyed.

The callback is a **PropSheetPageProc** function that is described in the Windows SDK documentation. This function must be able to handle the PSPCB_CREATE and PSPCB_RELEASE actions.

The callback is called with a PSPCB_CREATE message when a property page is being created. In response to this message, the callback can allocate memory for data that is associated with the page. The function should return **TRUE** to continue to create the page or **FALSE** if the page should not be created.

Property pages for a device are destroyed when the user clicks **OK** or **Cancel** on the page's dialog box or clicks **Uninstall** on the **Drivers** tab.

When a property page is destroyed, the callback is called with a PSPCB_RELEASE message. The function should free any data that was allocated when the property page was created. Typically, this involves freeing the data referenced by the **lParam** member of the PROPSHEETPAGE structure. The return value is ignored when the page is being destroyed.

 

 





