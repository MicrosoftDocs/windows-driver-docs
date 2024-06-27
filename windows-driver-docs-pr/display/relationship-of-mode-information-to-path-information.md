---
title: Relationship of Mode Information to Path Information
description: Relationship of Mode Information to Path Information
keywords:
- connecting and configuring displays, Windows
- mode and path information, CCD concepts
- virtual mode, connecting and configuring displays
- mode and path information, Windows
ms.date: 06/27/2024
---

# Relationship of Mode Information to Path Information

The connecting and configuring displays (CCD) [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) function always returns path information and source and target mode information for a particular display configuration. The following figure shows an example of how the source and target mode information relates to the path information when the [**DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_info) isn't set; that is, when the path isn't virtual-aware. In this example, the QDC_ALL_PATHS flag was passed to the *Flags* parameter in the call to **QueryDisplayConfig**.

:::image type="content" source="images/displayconfigpathandmode.png" alt-text="Diagram illustrating the relationship between mode information and path information in a display configuration that doesn't support virtual modes.":::

Starting in Windows 10, the [**DISPLAYCONFIG_PATH_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_info), [**DISPLAYCONFIG_PATH_SOURCE_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_source_info), and [**DISPLAYCONFIG_PATH_TARGET_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_target_info) structures are updated to support paths that are virtual-aware:

* The [**DISPLAYCONFIG_PATH_SUPPORT_VIRTUAL_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_info) flag was added as a **flags** value. When this flag is set, it indicates that the path supports virtual modes.

* A union was added to **DISPLAYCONFIG_PATH_SOURCE_INFO**. The **modeInfoIdx** member is used only when the added flag isn't set. When the flag is set, mode information is in the **cloneGroupId** and **sourceModeInfoIdx** members.

* A union was added to **DISPLAYCONFIG_PATH_TARGET_INFO**. The **modeInfoIdx** member is used only when the added flag isn't set. When the flag is set, mode information is in the **desktopModeInfoIdx** and **targetModeInfoIdx** members.
