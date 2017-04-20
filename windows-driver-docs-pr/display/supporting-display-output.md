---
title: Supporting Display Output and ACPI Events
description: A comprehensive approach to system configuration and device power control is built into Windows, based on the Advanced Configuration and Power Interface (ACPI) specification.
ms.assetid: CD5BC59A-4C15-4111-BF4F-13DC04F6874F
keywords:
- ACPI display WDK display
- ACPI-based display hot-keys WDK display
- display hot-keys WDK display
- BIOS display control WDK display
- automatic display switch WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Supporting Display Output and ACPI Events


A comprehensive approach to system configuration and device power control is built into Windows, based on the Advanced Configuration and Power Interface (ACPI) specification. Windows supports capabilities that can be used by drivers to manage the configuration and power of display output devices. For more information, see the ACPI specification on the [ACPI website](http://go.microsoft.com/fwlink/p/?linkid=57185).

## <span id="BIOS_Requirements_to_Support_Display_Output_Devices"></span><span id="bios_requirements_to_support_display_output_devices"></span><span id="BIOS_REQUIREMENTS_TO_SUPPORT_DISPLAY_OUTPUT_DEVICES"></span>BIOS Requirements to Support Display Output Devices


The display miniport driver or ACPI methods that are exposed by the system BIOS support display output devices configuration. The [**DxgkDdiNotifyAcpiEvent**](https://msdn.microsoft.com/library/windows/hardware/ff559695) function is called to notify the display miniport driver about ACPI events. For example, when the user presses the keyboard shortcut for the output device switch, the **DxgkDdiNotifyAcpiEvent** function is called with ACPI\_NOTIFY\_CYCLE\_DISPLAY\_HOTKEY notification and a request type of DXGK\_ACPI\_CHANGE\_DISPLAY\_MODE. As a result, the operating system calls the [**DxgkDdiRecommendFunctionalVidPn**](https://msdn.microsoft.com/library/windows/hardware/ff559775) function to query the selected display output device.

The following aliases for the ACPI display output are defined in Dispmprt.h:

-   ACPI\_METHOD\_DISPLAY\_DOD - Enumerates all the devices attached to the display adapter. This method is required if the integrated controller supports switching of output devices. This is the alias name for the DOD\_ method defined by the ACPI specification.
-   ACPI\_METHOD\_DISPLAY\_DOS - Indicates that the system firmware is capable of automatically switching the active display output. This is the alias name for the SOD\_ method defined by the ACPI specification. The following are the allowed parameters:
    -   ACPI\_ARG\_ENABLE\_SWITCH\_EVENT. States that the system firmware should not automatically switch the active display output device. Instead, it must save the desired change in state variables associated with each display output device and generate a display switch event. The operating system can query the active status of a device by calling the ACPI\_METHOD\_OUTPUT\_DGS method.
    -   ACPI\_ARG\_ENABLE\_AUTO\_SWITCH. States that the system firmware should automatically switch the active display output device without interacting with the operating system. It does not generate a display switch event.
    -   ACPI\_ARG\_DISABLE\_SWITCH\_EVENT. States that the system firmware should not perform any action; that is, neither switch the output device nor notify the operating system. The values returned by the ACPI\_METHOD\_OUTPUT\_DGS method are locked.
-   ACPI\_METHOD\_OUTPUT\_DCS - Returns the status of a display output device. This is the alias name for the CSD\_ method defined by the ACPI specification.
-   ACPI\_METHOD\_OUTPUT\_DGS - Checks whether the status of a display output device is active. This is the alias name for the SGD\_ method defined by the ACPI specification.
-   ACPI\_METHOD\_OUTPUT\_DSS - Sets the status of a display output device to active or inactive. This is the alias name for the SSD\_ method defined by the ACPI specification. The operating system manages this action to avoid flickering.
-   ACPI\_METHOD\_DISPLAY\_GPD - Queries the CMOS entry to determine which video device is posted at boot time. This is the alias name for the DPG\_ method defined by the ACPI specification.
-   ACPI\_METHOD\_DISPLAY\_SPD - Updates the CMOS entry that determines which video device is posted at boot time. This is the alias name for the DPS\_ method defined by the ACPI specification.
-   ACPI\_METHOD\_DISPLAY\_VPO - Determines what video options are implemented. This is the alias name for the OPV\_ method defined by the ACPI specification.

## <span id="External_Asynchronous_Events"></span><span id="external_asynchronous_events"></span><span id="EXTERNAL_ASYNCHRONOUS_EVENTS"></span>External Asynchronous Events


The operating system must be notified about external, asynchronous events that affect the display output devices. The following notifications and related request types are defined in Dispmprt.h and used in the [**DxgkDdiNotifyAcpiEvent**](https://msdn.microsoft.com/library/windows/hardware/ff559695) function.

-   ACPI\_NOTIFY\_CYCLE\_DISPLAY\_HOTKEY - Notifies the operating system that the user has pressed the cycle display keyboard shortcut.
-   ACPI\_NOTIFY\_NEXT\_DISPLAY\_HOTKEY - Notifies the operating system that the user has pressed the next display keyboard shortcut.
-   ACPI\_NOTIFY\_PREV\_DISPLAY\_HOTKEY - Notifies the operating system that the user has pressed the previous display keyboard shortcut.

**Note**  The previous notifications depend on the handling of the event caused by the user when pressing the keyboard shortcuts.

 

The following are the types of requests that the display miniport driver can make to the operating system.

-   DXGK\_ACPI\_CHANGE\_DISPLAY\_MODE - Requests to initiate a mode change to the new recommended active video present network (VidPN).
-   DXGK\_ACPI\_POLL\_DISPLAY\_CHILDREN - Requests to poll the connectivity of the children of the display adapter.

**Note**  The previous requests are the values of the *AcpiFlags* parameter returned by the [**DxgkDdiNotifyAcpiEvent**](https://msdn.microsoft.com/library/windows/hardware/ff559695) function.

 

## <span id="related_topics"></span>Related topics


[Supporting Brightness Controls on Integrated Display Panels](supporting-brightness-controls-on-integrated-display-panels.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Display%20Output%20and%20ACPI%20Events%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





