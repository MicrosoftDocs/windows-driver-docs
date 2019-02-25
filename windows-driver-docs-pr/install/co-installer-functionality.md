---
title: Co-installer Functionality
description: Co-installer Functionality
ms.assetid: ce8a5ab4-d5ce-4255-a959-9619ff736e37
keywords:
- co-installers WDK device installations , functionality
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Co-installer Functionality





A co-installer is a user-mode Win32 DLL that typically writes additional configuration information to the registry, or performs other installation tasks that require information that is not available when an INF is written.

A co-installer might do some or all of the following:

-   Handle one or more of the [device installation function codes](https://msdn.microsoft.com/library/windows/hardware/ff541307) (DIF codes) received by the [co-installer entry point](co-installer-interface.md#co-installer-entry-point) function.

-   Perform operations before the associated class or device installer is called, after the class or device installer is called, or both, as described in [Co-installer Operation](co-installer-operation.md).

-   [Provide device property pages](providing-device-property-pages.md), which are displayed by Device Manager so users can modify device parameters.

-   Starting with Windows Vista, provide [finish-install actions](finish-install-actions--windows-vista-and-later-.md) (in response to a [**DIF_FINISHINSTALL_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request) to install applications.

When called for postprocessing, a co-installer must check the **InstallResult** member of the [COINSTALLER_CONTEXT_DATA](co-installer-interface.md#coinstaller-context-data) structure. If its value is not NO_ERROR, the co-installer must do any necessary clean up operations and return an appropriate value for **InstallResult**.

Co-installers can sometimes obtain information from the user. Such information might include additional device parameters, or whether the user wants device-specific applications installed. Co-installers can create user interfaces by providing "finish install" pages and device property pages. No other form of user interface is allowed. Windows displays "finish install" pages at the end of the installation (within the Found New Hardware or Hardware Update). Device Manager displays property pages, and allows users with administrator privilege to modify parameters displayed on these pages.

 

 





