---
title: Supporting Brightness Controls on Integrated Display Panels
description: Supporting Brightness Controls on Integrated Display Panels
keywords:
- brightness WDK display
- ACPI-based brightness hot-keys WDK display
- notifying brightness hot keys WDK display
- BIOS brightness control WDK display
- automatic brightness WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Brightness Controls on Integrated Display Panels

Brightness controls are implemented in the monitor driver, Monitor.sys, supplied by the operating system. The monitor driver implements a Windows Management Instrumentation (WMI) interface to allow applications (such as the operating system's brightness slider) to interact with the brightness level. The monitor driver registers with the Device Power Policy Engine (DPPE) so that brightness levels respond to changes in power policy. The monitor driver registers with the Advanced Configuration and Power Interface (ACPI) to process ACPI-based brightness shortcut keys. For compatibility with the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md), the monitor driver implements the IOCTL-based brightness controls.

Either the display miniport driver or ACPI methods that are exposed by the system basic input/output system (BIOS) can support changing the brightness of an integrated display panel. For the first video target that is marked as having output technology that connects internally in a computer ([**D3DKMDT_VOT_INTERNAL**](/windows-hardware/drivers/ddi/d3dkmdt/ne-d3dkmdt-_d3dkmdt_video_output_technology)), the monitor driver calls the display miniport driver's [**DxgkDdiQueryInterface**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_interface) function to query for both of the following:

* The [Brightness Control Interface](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_brightness_interface) that is identified by GUID_DEVINTERFACE_BRIGHTNESS_2 and DXGK_BRIGHTNESS_INTERFACE_VERSION_1
* The [Brightness Control Interface V.2](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-dxgk_brightness_interface_2) that is identified by GUID_DEVINTERFACE_BRIGHTNESS and DXGK_BRIGHTNESS_INTERFACE_VERSION_2

If the display miniport driver does not support at least the Brightness Control Interface, the monitor driver uses ACPI to query for the \_BCL, \_BCM, and _BQC methods on the child device. For more information about these methods, see the ACPI specification on the [ACPI website](https://go.microsoft.com/fwlink/p/?linkid=57185).

> [!NOTE]
> In the Windows Display Driver Model (WDDM), an ACPI identifier is not used to identify an integrated display panel. This is different from the [Windows 2000 Display Driver Model](windows-2000-display-driver-model-design-guide.md), which supports only display panels with an identifier of 0x0110.

If either the display miniport driver or BIOS-exposed ACPI methods support brightness controls, the monitor driver registers for ACPI notifications of brightness shortcut keys. No alternative mechanism exists to signal the monitor driver about shortcut key notifications. If the monitor driver cannot use either brightness-control mechanism or if the display miniport driver supplies the brightness control interface but fails a call to the [**DxgkDdiGetPossibleBrightness**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgk_brightness_get_possible) function, the monitor driver does not support brightness controls.

## Brightness Levels

Brightness levels are represented as single-byte values in the range from zero to 100 where zero is off and 100 is the maximum brightness that a laptop computer supports. Every laptop computer must report a maximum brightness level of 100; however, a laptop computer is not required to support a level of zero. The only requirement for values from zero to 100 is that larger values must represent higher brightness levels. The increment between levels is not required to be uniform, and a laptop computer can support any number of distinct values up to the maximum of 101 levels. You must decide how to map hardware levels to the range of brightness level values. However, a call to the display miniport driver's [**DxgkDdiGetPossibleBrightness**](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgk_brightness_get_possible) function should not report more brightness level values than the hardware supports.

## Disabling Automatic Brightness Changes by the BIOS

To avoid problems that might occur if the system BIOS and the monitor driver both control display panel brightness, the display miniport driver should set bit 2 of the argument to the \_DOS method. For more information about the _DOS method and its arguments, see the ACPI specification. By setting bit 2, the system BIOS is informed that it should not perform any automatic brightness changes.

## BIOS Requirements to Support Brightness Controls

For the display miniport driver to support controlling integrated panel brightness in an optimum way, the system BIOS must provide the following items through the ACPI.

### Brightness control methods

An integrated panel device should support the ACPI brightness control methods (\_BCL, \_BCM, and \_BQC). \_BCL and \_BCM are unchanged since version 1.0b of the ACPI specification; you can find their definitions in the ACPI 3.0 specification in sections B.6.2 and B.6.3. _BQC is optional and is defined in the ACPI 3.0 specification in section B.6.4. For definitions of brightness levels, see Brightness Levels.

The following are the aliases for the ACPI brightness control methods defined in Dispmprt.h:

* ACPI_METHOD_OUTPUT_BCLÂ - Allows Windows to query a list of brightness levels supported by the display output devices. This method is required if an integrated LCD is present and supports brightness levels.
* ACPI_METHOD_OUTPUT_BCMÂ - Allows Windows to set the brightness level of the display output device. Windows will only set levels that were reported by the ACPI_METHOD_OUTPUT_BCL method. The ACPI_METHOD_OUTPUT_BCM method is required if the ACPI_METHOD_OUTPUT_BCL method is implemented.

### Disabling the automatic system BIOS brightness control

The system BIOS should support setting bit 2 of the argument to the _DOS method on the graphics adapter to allow automatic system BIOS brightness changes to be disabled. This bit is an addition to the previously defined values for the bits in this method. For details about this bit, see section B.4.1 in the ACPI 3.0 specification. If this bit is not supported, the monitor driver and the system BIOS can both change the brightness level, which results in a flicker of brightness and can potentially leave the brightness set to a value that is not what the user requested.

The following alias for the ACPI automatic brightness control method is defined in Dispmprt.h:

* ACPI_METHOD_DISPLAY_DOSÂ - Indicates that the system BIOS is capable of automatically switching the active display output or controlling the brightness of the LCD. The following are the allowed parameters:

  * ACPI_ARG_ENABLE_AUTO_LCD_BRIGHTNESS. States that the system BIOS should automatically control the brightness level of the LCD when the power changes from AC to DC.
  * ACPI_ARG_DISABLE_AUTO_LCD_BRIGHTNESS. States that the system BIOS should not automatically control the brightness level of the LCD when the power changes from AC to DC.

### Notifications of brightness shortcut keys

Brightness shortcut key notifications should be targeted to the integrated display panel device, not to the graphics adapter.

The following notifications are supported as defined in Dispmprt.h:

* ACPI_NOTIFY_CYCLE_BRIGHTNESS_HOTKEY - The user has pressed the hotkey for cycling display brightness.
* ACPI_NOTIFY_INC_BRIGHTNESS_HOTKEY - The user has pressed the hotkey for increasing display brightness.
* ACPI_NOTIFY_DEC_BRIGHTNESS_HOTKEY - The user has pressed the hotkey for decreasing display brightness.
* ACPI_NOTIFY_ZERO_BRIGHTNESS_HOTKEY - The user has pressed the hotkey for reducing display brightness to zero.

These shortcut key notifications are new to the ACPI 3.0 specification and are described in section B.7. Typically, a laptop computer would not support all of these shortcut key notifications.

The default behavior of the monitor driver for the ACPI_NOTIFY_INC_BRIGHTNESS_HOTKEY and ACPI_NOTIFY_DEC_BRIGHTNESS_HOTKEY notifications is to increment (or decrement) brightness by at least 5 percent more (or less) than the previous brightness level, until the next available 5-percent step level is reached (5, 10, 15, ..., 95, 100). Incrementing or decrementing with shortcut keys can create asymmetrical patterns in brightness levels, as the following examples show.

* Available _BCL brightness control levels specified as 0, 1, 5, 10, ..., 95, 100

  * Results using the ACPI_NOTIFY_INC_BRIGHTNESS_HOTKEY notification:  
        0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100

  * Results using the ACPI_NOTIFY_DEC_BRIGHTNESS_HOTKEY notification:  
        100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0

  * Available _BCL brightness control levels specified as 1, 5, 10, ..., 95, 100

    * Results using the ACPI_NOTIFY_INC_BRIGHTNESS_HOTKEY notification:  
        1, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100

    * Results using the ACPI_NOTIFY_DEC_BRIGHTNESS_HOTKEY notification:  
        100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 1

  In the latter example, 1 is the last available value, so the driver sets the brightness level to 1 even though it is less than 5 percentage units different from the previous value of 5.

This default monitor driver behavior can be overridden by changing the value of the DWORD. **MinimumStepPercentage** in the following registry key:

```cpp
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\`*Monitor*`\Parameters\
```

## Related topics

[Supporting Display Output and ACPI Events](supporting-display-output.md)
