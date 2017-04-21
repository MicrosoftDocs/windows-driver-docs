---
title: Control Panel Requirements
description: Control Panel Requirements
ms.assetid: ad700594-b58c-4f6c-b594-e880612923b7
keywords:
- Control Panel WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Control Panel Requirements


## <span id="ddk_control_panel_requirements_gg"></span><span id="DDK_CONTROL_PANEL_REQUIREMENTS_GG"></span>


The following are requirements for extensions to the display Control Panel:

-   Existing property pages must remain unchanged. Any Microsoft-provided property page (including **Settings**) must not be disabled, modified, removed, or replaced.

-   Custom property pages can be added only under **Advanced Properties**. The features exposed at the top level are commonly accessed features that are included in every Windows system. Because Windows 2000 and later operating system versions support multiple displays, custom property pages cannot be added to the top-level property page set in the Display Control Panel.

-   Control Panel extensions must be able to operate with existing Windows Control Panel elements.

-   Custom property pages must be labeled with an icon in addition to the text name. In order to prevent conflicts with future operating system or shell releases, third-party tabs must contain, in addition to the page label, either an icon (with the company's logo) or text with the name of the vendor. For example, "Acme Video Controls" is acceptable; "Video Controls" is not.

-   Control panel extensions must not initialize if the necessary hardware/driver combination is not present. If the display hardware that ships with the custom Control Panel extensions is not present, the extensions should not load. Likewise, if a custom property page has features that are dependent on proprietary driver extensions (for example, extensions that are not guaranteed to be present in every other display driver), those features must disable themselves, or the property page must not load when the necessary driver is not installed.

-   Control Panel extension must respect the **Hide modes that this monitor cannot display** check box on the **Monitor** tab. If the check box is selected, then Control Panel extension must not display any modes that are not enumerated by **EnumDisplaySettings** (described in the Microsoft Windows SDK documentation).

-   Control panel state must be stored in the registry. No *.ini* files are allowed. Any state that is maintained by your Control Panel extension must be stored in the SOFTWARE key in the registry, accessible through HKR in the INF file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Control%20Panel%20Requirements%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




