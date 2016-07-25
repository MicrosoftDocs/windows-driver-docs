---
title: Co-installer Functionality
description: Co-installer Functionality
ms.assetid: ce8a5ab4-d5ce-4255-a959-9619ff736e37
keywords: ["co-installers WDK device installations , functionality"]
---

# Co-installer Functionality


## <a href="" id="ddk-co-installer-functionality-dg"></a>


A co-installer is a user-mode Win32 DLL that typically writes additional configuration information to the registry, or performs other installation tasks that require information that is not available when an INF is written.

A co-installer might do some or all of the following:

-   Handle one or more of the [device installation function codes](https://msdn.microsoft.com/library/windows/hardware/ff541307) (DIF codes) received by the [co-installer entry point](co-installer-interface.md#co-installer-entry-point) function.

-   Perform operations before the associated class or device installer is called, after the class or device installer is called, or both, as described in [Co-installer Operation](co-installer-operation.md).

-   [Provide device property pages](providing-device-property-pages.md), which are displayed by Device Manager so users can modify device parameters.

-   Starting with Windows Vista, provide [finish-install actions](finish-install-actions--windows-vista-and-later-.md) (in response to a [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request) to install applications.

When called for postprocessing, a co-installer must check the **InstallResult** member of the [COINSTALLER\_CONTEXT\_DATA](co-installer-interface.md#coinstaller-context-data) structure. If its value is not NO\_ERROR, the co-installer must do any necessary clean up operations and return an appropriate value for **InstallResult**.

Co-installers can sometimes obtain information from the user. Such information might include additional device parameters, or whether the user wants device-specific applications installed. Co-installers can create user interfaces by providing "finish install" pages and device property pages. No other form of user interface is allowed. Windows displays "finish install" pages at the end of the installation (within the Found New Hardware or Hardware Update). Device Manager displays property pages, and allows users with administrator privilege to modify parameters displayed on these pages.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Co-installer%20Functionality%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




