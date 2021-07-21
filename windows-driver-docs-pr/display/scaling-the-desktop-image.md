---
title: Scaling the desktop image
description: Describes how desktop image scaling works
keywords:
- connecting displays WDK Windows 7 display , CCD concepts, scaling the desktop image
- connecting displays WDK Windows Server 2008 R2 display , CCD concepts, scaling the desktop image
- configuring displays WDK Windows 7 display , CCD concepts, scaling the desktop image
- configuring displays WDK Windows Server 2008 R2 display , CCD concepts, scaling the desktop image
- CCD concepts WDK Windows 7 display , scaling the desktop image
- CCD concepts WDK Windows Server 2008 R2 display , scaling the desktop image
- scaling the desktop image WDK Windows 7 display
- scaling the desktop image WDK Windows Server 2008 R2 display
ms.date: 03/31/2021
ms.localizationpriority: medium
---

# Scaling the desktop image

This topic applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of the Windows operating system.

## How scaling works

A caller can use the [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) Connecting and Configuring Displays (CCD) function to scale the desktop image to the monitor:

* If the desktop and monitor use the same resolution, **SetDisplayConfig** is not required to scale the desktop image to the monitor. This **SetDisplayConfig** operation is known as *identity scaling*.
* If the desktop and monitor resolution are different, **SetDisplayConfig** applies one of the following types of scaling. The monitor resolution is defined by the [**DISPLAYCONFIG_TARGET_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_mode) structure.

  * **Centered scaling**

    Centered scaling is a mode in which the desktop is displayed on the monitor without any scaling at all. When [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) applies centered scaling, black bands might be visible above and below the desktop. The following figure shows centered scaling.

    ![figure illustrating centered scaling.](images/ccd-center-scale.png)

  * **Stretched scaling**

    Stretched scaling is a mode in which the desktop is horizontally and vertically stretched on the monitor to ensure that the entire display is used. When [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) applies stretched scaling, no black bands are visible above and below the desktop. However, the desktop might appear distorted. The following figure shows stretched scaling.

    ![figure illustrating stretched scaling.](images/ccd-stretch-scale.png)

  * **Aspect-Ratio-Preserving Stretched**

    Aspect-ratio-preserving stretched scaling is a mode in which the desktop is stretched horizontally and vertically as much as possible while maintaining the aspect ratio. When [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) applies aspect-ratio-preserving stretched scaling, black bands might be visible either *above and below* or *left and right of* the desktop. However, black bands cannot be visible both *above and below* and *left and right of* the desktop. Because users are expected to prefer this type of scaling, **SetDisplayConfig** applies this type of scaling as the default. The following figure shows aspect-ratio-preserving stretched scaling.

    ![figure illustrating aspect-ratio-preserving stretched scaling.](images/ccd-arpstretch-scale.png)

Scaling depends on the source and target modes that are used for a path. In addition, the caller can call [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) without specifying the target mode information (that is, setting the *modeInfoArray* parameter is optional and can be set to **NULL**). This means that the caller cannot typically predict if **SetDisplayConfig** must perform any scaling. Furthermore, no API exists to get the full list of scaling types that the graphics adapter supports. The [**EnumDisplaySettings**](/windows/win32/api/winuser/nf-winuser-enumdisplaysettingsa) Win32 function returns DMDFO_DEFAULT in the **dmDisplayFixedOutput** member of the **DEVMODE** structure that the *lpDevMode* parameter points to when the caller requests the Windows 7 scaling types.

The scaling that a caller passes to [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) is a scaling intent rather than an explicit request to perform a scaling operation. If scaling is required (for example, source and target resolutions differ), **SetDisplayConfig** uses the scaling that the caller supplies. If the supplied scaling is not supported, **SetDisplayConfig** uses the graphics adapter's default scaling. When the source and target resolutions that the caller passes to **SetDisplayConfig** are the same, **SetDisplayConfig** always sets identity scaling.

## Scaling requests

The following table shows the different [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) scaling requests, and identifies the abbreviated nomenclature used in the tables found in the sub-sections below.  See [DISPLAYCONFIG_SCALING](/windows/win32/api/wingdi/ne-wingdi-displayconfig_scaling) for definitions of the DISPLAYCONFIG_SCALING_*XXX* values.

| Scaling request | Abbreviated nomenclature used in below tables |
| --------------- | ------- |
| DISPLAYCONFIG_SCALING_IDENTITY | DC_IDENTITY  |
| DISPLAYCONFIG_SCALING_CENTERED | DC_CENTERED  |
| DISPLAYCONFIG_SCALING_STRETCHED |DC_STRETCHED  |
| DISPLAYCONFIG_SCALING_ASPECTRATIOCENTEREDMAX | DC_ASPECTRATIOCENTEREDMAX  |
| DISPLAYCONFIG_SCALING_CUSTOM | DC_CUSTOM  |
| DISPLAYCONFIG_SCALING_PREFERRED | DC_PREFERRED  |
| The adapter default scaling value. Currently, on tablet systems, the default is stretched. On non-tablet systems with graphics adapters that support the [Windows Display Driver Model](windows-vista-display-driver-model-design-guide.md)  (WDDM), the default is defined by the driver. On non-tablet systems with graphics adapters that support WDDM with [features new for Windows 7](../what-s-new-in-driver-development.md), the default is DC_ASPECTRATIOCENTEREDMAX. | AdapterDefault  |
| The scaling value from the database for the current connected monitors | DatabaseValue |

### SetDisplayConfig scaling requests

The following table shows the values that are saved in the database and the values that are actually set, where:

* "Set (same)" and "Store (same)" are the set and store values when the resultant source mode and target mode have the same resolution
* "Set (different)" and "Store (different)" are the set and store values when the resultant source mode and target mode have different resolutions

| Scaling flag passed to SetDisplayConfig | Set (same) | Store (same) | Set (different) | Set (different) |
| - | - | - | - | - |
| DC_IDENTITY current config not in Db | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DC_IDENTITY current config in Db | DC_IDENTITY | DatabaseValue | DatabaseValue |DatabaseValue |
| DC_CENTERED | DC_IDENTITY | DC_CENTERED | DC_CENTERED | DC_CENTERED |
| DC_STRETCHED | DC_IDENTITY | DC_STRETCHED | DC_STRETCHED | DC_STRETCHED |
| DC_ASPECTRATIOCENTEREDMAX on WDDM with Windows 7 features driver |DC_IDENTITY | DC_ASPRATIOMAX | DC_ASPRATIOMAX | DC_ASPRATIOMAX |
| DC_ASPECTRATIOCENTEREDMAX on WDDM driver | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DC_CUSTOM on WDDM with Windows 7 features driver that does support custom scaling on the path | DC_CUSTOM | DC_CUSTOM | DC_CUSTOM | DC_CUSTOM |
| DC_CUSTOM on WDDM with Windows 7 features driver that does not support custom scaling on the path | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DC_CUSTOM on WDDM driver | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DC_PREFERRED current config not in Db | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DC_PREFERRED current config in Db | DC_IDENTITY | DatabaseValue | DatabaseValue |DatabaseValue |

### Legacy ChangeDisplaySettingsEx scaling requests

The following table shows how the scaling that a caller can pass to the legacy  [**ChangeDisplaySettingsEx**](/windows/win32/api/winuser/nf-winuser-changedisplaysettingsexa) API maps to the scaling set, where:

* "Set (same)" and "Store (same)" are the set and store values when the resultant source mode and target mode have the same resolution
* "Set (different)" and "Store (different)" are the set and store values when the resultant source mode and target mode have different resolutions

| Scaling flag passed to ChangeDisplaySettingsEx | Set (same) | Store (same) | Set (different) | Set (different) |
| - | - | - | - | - |
| DMDFO_DEFAULT with current config not in CCD database | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DMDFO_DEFAULT with current config in CCD database | DC_IDENTITY | DatabaseValue | DatabaseValue |DatabaseValue |
| DMDFO_STRETCH| DC_IDENTITY | DC_STRETCHED | DC_STRETCHED | DC_STRETCHED |
| DMDFO_CENTER | DC_IDENTITY | DC_CENTERED | DC_CENTERED | DC_CENTERED |
| DM_DISPLAYFIXEDOUTPUT not set, current config not in CCD database | DC_IDENTITY | AdapterDefault | AdapterDefault | AdapterDefault |
| DM_DISPLAYFIXEDOUTPUT not set, current config in CCD database | DC_IDENTITY | DatabaseValue | DatabaseValue |DatabaseValue |

### Legacy EnumDisplaySettings scaling translation

The following table shows how display configuration scaling is translated and returned from [**EnumDisplaySettings**](/windows/win32/api/winuser/nf-winuser-enumdisplaysettingsa).

| Current active scaling | GDI scaling values returned from legacy EnumDisplaySettings(ENUM_CURRENT_SETTINGS) |
| - | - |
| DC_IDENTITY  | DMDFO_DEFAULT |
| DC_CENTERED  | DMDFO_CENTER |
| DC_STRETCHED  | DMDFO_STRETCH |
| DC_ASPRATIOMAX  | DMDFO_DEFAULT |
| DC_CUSTOM  | DMDFO_DEFAULT |
| DC_PREFERRED  | DMDFO_DEFAULT |

## DirectX games and scaling

Microsoft DirectX 9L and earlier runtimes require that applications always call the [**ChangeDisplaySettingsEx**](/windows/win32/api/winuser/nf-winuser-changedisplaysettingsexa) function without DM_DISPLAYFIXEDOUTPUT set in the **dmFields** member of the DEVMODE structure that the *lpDevMode* parameter points to. DirectX 10 and later runtimes allow applications to choose the scaling that those applications pass to **ChangeDisplaySettingsEx**. The following table shows the mapping of scaling values to scaling flags that are passed to **ChangeDisplaySettingsEx**.

| DXGI flip chain scaling value | Scaling flags that are passed to ChangeDisplaySettingsEx |
| - | - |
| DXGI_MODE_SCALING_UNSPECIFIED  | DMDFO_DEFAULT, DMDFO_CENTER, or DMDFO_STRETCH. The scaling that applications use depends on several factors, which include the current desktop scaling and the mode list that the driver exposes. |
| DXGI_MODE_SCALING_CENTERED  | DMDFO_CENTER |
| DXGI_MODE_SCALING_STRETCHED  | DMDFO_STRETCH |

By using this information in combination with the preceding scaling tables, you can determine the expected scaling from a DirectX application.
