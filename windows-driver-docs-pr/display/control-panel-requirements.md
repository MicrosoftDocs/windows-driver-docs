---
title: Control Panel Requirements
description: Control Panel Requirements
ms.assetid: ad700594-b58c-4f6c-b594-e880612923b7
keywords:
- Control Panel WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





