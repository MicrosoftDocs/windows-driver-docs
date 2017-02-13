---
title: Supporting Path-Independent Rotation
description: Starting with Windows 8.1 Update, the operating system supports cloning portrait-first displays on landscape-first displays with the greatest possible resolution.
ms.assetid: 136CEDA5-2839-4E6E-A032-1A9222C769C6
---

# <span id="display.supporting_path-independent_rotation"></span>Supporting Path-Independent Rotation


Starting with Windows 8.1 Update, the operating system supports cloning portrait-first displays on landscape-first displays with the greatest possible resolution. The display miniport driver must set the proper offset values in the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705) structure for the *primary clone path* and *secondary clone path*, as described in [Supporting Rotation in a Display Miniport Driver](supporting-rotation-in-a-display-miniport-driver.md#clone-mode-requirements).

These Device driver interfaces (DDIs) are new in Windows 8.1 Update:

-   [VidPN Path-Independent Rotation Interface](https://msdn.microsoft.com/library/windows/hardware/dn653366)

These DDIs are updated in Windows 8.1 Update:

-   [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705)

-   [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff546700)

## <span id="Cloning_a_portrait-first_device"></span><span id="cloning_a_portrait-first_device"></span><span id="CLONING_A_PORTRAIT-FIRST_DEVICE"></span>Cloning a portrait-first device


When a driver of a portrait-first device is requested to clone to a landscape-first monitor, it should report source-mode (*x*,*y*) resolutions that match the resolutions in the primary clone path. The secondary clone path could then support 90- and 270-degree offset values ([**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705).**Offset90** or .**Offset270** are **TRUE**). So when a VidPN is committed with an [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff546700) enumeration value that indicates a 90- or 270-degree offset, this means that the (*x*,*y*) resolutions are flipped in this particular path.

By default the operating system chooses the secondary clone path to be the internal display panel. In the case that the internal panel is portrait-first, the operating system expects [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705).**Offset270** to be set on this path in order to display on the internal display panel in landscape mode. In the case of a landscape-first external monitor in the secondary clone path, the operating system expects the driver to support **D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**.**Offset90**, although this is likely to be a rare scenario.

## <span id="Example_clone_scenarios"></span><span id="example_clone_scenarios"></span><span id="EXAMPLE_CLONE_SCENARIOS"></span>Example clone scenarios


Here's a typical scenario where a portrait-first device with native resolution 800 (width) x 1280 pixels (height) is connected in clone mode to a landscape-first TV with height 1080 pixels. The driver would report this info to the operating system:

<span id="source_mode"></span><span id="SOURCE_MODE"></span>source mode  
1280 x 800

<span id="TV_target_mode"></span><span id="tv_target_mode"></span><span id="TV_TARGET_MODE"></span>TV target mode  
1920 x 1080 (aspect-ratio preserved scaling)

<span id="device_target_mode"></span><span id="DEVICE_TARGET_MODE"></span>device target mode  
800 x 1280 (identity scaling)

<span id="primary_clone_path__TV_"></span><span id="primary_clone_path__tv_"></span><span id="PRIMARY_CLONE_PATH__TV_"></span>primary clone path (TV)  
driver supports only [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705).**Offset0**, as well as normal rotation support

<span id="secondary_clone_path__device_"></span><span id="SECONDARY_CLONE_PATH__DEVICE_"></span>secondary clone path (device)  
driver supports only [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION\_SUPPORT**](https://msdn.microsoft.com/library/windows/hardware/ff546705).**Offset270**, as well as normal rotation support

<span></span>  

The call to the [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597) function then returns with these path settings from the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff546700) enumeration:

<span id="primary_clone_path__TV_"></span><span id="primary_clone_path__tv_"></span><span id="PRIMARY_CLONE_PATH__TV_"></span>primary clone path (TV)  
**D3DKMDT\_VPPR\_IDENTITY**

<span id="secondary_clone_path__device_"></span><span id="SECONDARY_CLONE_PATH__DEVICE_"></span>secondary clone path (device)  
**D3DKMDT\_VPPR\_IDENTITY\_OFFSET270**

The operating system expects the driver to rotate the provided content 270 degrees.

If, in the **Display** control panel's **Orientation** drop-down box, the user chooses the **Landscape (flipped)** option, the call to the [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597) function returns with these path settings from the [**D3DKMDT\_VIDPN\_PRESENT\_PATH\_ROTATION**](https://msdn.microsoft.com/library/windows/hardware/ff546700) enumeration:

<span id="primary_clone_path__TV_"></span><span id="primary_clone_path__tv_"></span><span id="PRIMARY_CLONE_PATH__TV_"></span>primary clone path (TV)  
**D3DKMDT\_VPPR\_ROTATE180**

<span id="secondary_clone_path__device_"></span><span id="SECONDARY_CLONE_PATH__DEVICE_"></span>secondary clone path (device)  
**D3DKMDT\_VPPR\_ROTATE180\_OFFSET270**

If the Desktop Window Manager (DWM) has already rotated the content 180 degrees, the driver must still rotate it another 270 degrees in the secondary clone path. Otherwise, the driver must rotate the content 180 degrees for the TV and 90 degrees for the device. Note that to rotate the content, the driver must set the **Rotate** member of the [**DXGK\_PRESENTFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff562005) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Path-Independent%20Rotation%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




