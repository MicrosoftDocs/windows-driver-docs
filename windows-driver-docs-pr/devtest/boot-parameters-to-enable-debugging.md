---
title: Boot Parameters to Enable Debugging
description: Boot Parameters to Enable Debugging
ms.assetid: acbe2fcd-6f8f-49c8-9de6-1617a1723cf5
keywords: ["boot parameters WDK", "boot entry parameters WDK", "kernel debugging support WDK boot options", "local debugging WDK boot parameters", "single-computer debugging WDK boot parameters", "cable debugging WDK boot parameters", "IEEE 1394 cable WDK boot parameters", "1394 connection WDK boot parameters", "USB 2.0 debugging connection WDK boot parameters", "null-modem cable WDK boot parameters"]
---

# Boot Parameters to Enable Debugging


## <span id="ddk_boot_parameters_to_enable_debugging_tools"></span><span id="DDK_BOOT_PARAMETERS_TO_ENABLE_DEBUGGING_TOOLS"></span>


When a kernel debugging connection is established, the system gives a kernel debugger control over its execution. Also, when a bug check occurs or a kernel-mode program communicates with a debugger, the computer waits for a response from a kernel debugger before it continues.

There are four basic debugging methods that you can configure by using boot parameters:

-   Single-computer (local) debugging

-   Debugging with a null-modem cable

-   Debugging with an IEEE 1394 cable (only if the target computer and the host computer are both running Microsoft Windows 7 or a later version of Windows)

-   Debugging with a USB 2.0 debug cable (only if the target computer and the host computer are both running Microsoft Windows 7 or a later version of Windows)

### <span id="boot_option_for_local_debugging_in_windows_vista_and_later"></span><span id="BOOT_OPTION_FOR_LOCAL_DEBUGGING_IN_WINDOWS_VISTA_AND_LATER"></span>Boot Option for Local Debugging in Windows

To enable kernel debugging on a single computer, use the BCDEdit **/debug** boot option.

To use BCDEdit, open a Command Prompt window with elevated privileges (right-click **Command Prompt** and click **Run as administrator** from the shortcut menu).

The **/debug** option has the following syntax:

```
bcdedit /debug [{ID}] { on | off }
```

The **{***ID***}** is the GUID associated with a boot entry. If an **{***ID***}** is not specified, the settings apply to the current boot entry. The following command enables kernel debugging for the current Windows operating system boot entry:

```
bcdedit /debug on
```

The following command enables kernel debugging for the specified Windows operating system boot entry:

```
bcdedit /debug  {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

You can use the **bcdedit /enum** command to view the current boot entries and their settings, and to identify the GUID associated with each entry.

For more details, see [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191).

### <span id="boot_options_to_debug_with_a_null_modem_cable_in_windows_vista_and_lat"></span><span id="BOOT_OPTIONS_TO_DEBUG_WITH_A_NULL_MODEM_CABLE_IN_WINDOWS_VISTA_AND_LAT"></span>Boot Options to Debug with a Null-Modem Cable in Windows

To enable debugging with a null-modem cable in Windows, use BCDEdit and set the debugging connection type to "SERIAL". You can set this globally by using the [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187) command followed by **serial**, or set it for a specific boot entry by using the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command followed by **debugtype serial**. You must also use the [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) command to enable kernel debugging globally or for the desired operating system.

If BCDEdit has not been used, the default global debug settings are for serial communications, using COM1 and a baud rate of 115,200.

To display the current settings, use the following command:

``` syntax
bcdedit /dbgsettings

debugtype               Serial
debugport               1
baudrate                115200
```

To use BCDEdit, open a Command Prompt window with elevated privileges (right-click **Command Prompt** and click **Run as administrator** from the shortcut menu).

To set the global debug settings to serial communications, use the following syntax:

**bcdedit /dbgsettings serial** \[ **debugport:***port*\] \[ **baudrate:** *baud*\]

The following example shows how to specify serial communications as the global debug setting.

``` syntax
bcdedit /dbgsettings serial debugport:1 baudrate:115200
```

To set the debug settings to serial for a specific boot entry, or for the current entry, use the following syntax:

**bcdedit /set** \[**{***ID***}**\] **debugtype serial**

**bcdedit /set** \[**{***ID***}**\] **debugport** *port*

**bcdedit /set** \[**{***ID***}**\] **baudrate** *baud*

If no **{***ID***}** is specified, the settings apply to the currently active boot entry.

The following example shows how to specify the serial debug settings for a specific boot entry. To enable the debug settings, you must reboot your computer and select that boot entry you have configured for debugging.

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} debugtype serial
```

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} debugport 1
```

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} baudrate 115200
```

``` syntax
bcdedit /debug {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

You can use the **bcdedit /enum** command to view the current boot entries and their settings.

For more details, see [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) and [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187).

### <span id="boot_parameters_to_debug_with_a_1394_cable_in_windows_vista_and_later"></span><span id="BOOT_PARAMETERS_TO_DEBUG_WITH_A_1394_CABLE_IN_WINDOWS_VISTA_AND_LATER"></span>Boot Parameters to Debug with a 1394 Cable in Windows

To enable debugging with an IEEE 1394 cable in Windows, use BCDEdit and set the debugging connection type to "1394". You can set this globally by using the [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187) command followed by **1394**, or set it for a specific boot entry by using the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command followed by **debugtype 1394**. You must also use the [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) command to enable kernel debugging globally or for the desired operating system.

To use BCDEdit, open a Command Prompt window with elevated privileges (right-click **Command Prompt** and click **Run as administrator** from the shortcut menu).

To set the debug settings for 1394 globally, use the following syntax:

**bcdedit /dbgsettings 1394** \[ **channel:***channel* \]

The following example shows how to specify 1394 as the global debug setting.

``` syntax
bcdedit /dbgsettings 1394 channel:32 
```

To set the debug settings to 1394 for a specific boot entry, or for the current entry, use the following syntax:

**bcdedit /set** \[**{***ID***}**\] **debugtype 1394**

**bcdedit /set** \[**{***ID***}**\] **channel** *channel*

If an **{***ID***}** is not specified, the settings apply to the current boot entry.

The following example shows how to specify the 1394 debug settings for a specific boot entry, and how to use the **/debug** option to enable kernel debugging for that boot entry. Note that to enable the debug settings, you must reboot your computer and select the boot entry you have configured for debugging.

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} debugtype 1394
```

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} channel 32
```

``` syntax
bcdedit /debug {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

You can use the **bcdedit /enum** command to view the current boot entries and their settings.

For more details, see [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) and [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187).

### <span id="boot_parameters_to_debug_with_a_usb_2_0_debugging_cable_in_windows_vis"></span><span id="BOOT_PARAMETERS_TO_DEBUG_WITH_A_USB_2_0_DEBUGGING_CABLE_IN_WINDOWS_VIS"></span>Boot Parameters to Debug with a USB 2.0 Debugging Cable in Windows

To enable debugging with a USB cable in these versions of Windows, use BCDEdit and set the debugging connection type to "USB". You can set this globally by using the [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187) command followed by **usb**, or set it for a specific boot entry by using the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command followed by **debugtype usb**. You must also use the [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) command to enable kernel debugging globally or for the desired operating system.

To use BCDEdit, open a Command Prompt window with elevated privileges (right-click **Command Prompt** and click **Run as administrator** from the shortcut menu).

To set the debug settings for USB globally, use the following syntax:

**bcdedit /dbgsettings usb** \[**targetname:***name*\]

The following example shows how to specify USB as the global debug setting.

``` syntax
bcdedit /dbgsettings usb targetname:U1
```

To set the debug settings to USB for a specific boot entry, or for the current entry, use the following syntax:

**bcdedit /set** \[**{***ID***}**\] **debugtype usb**

**bcdedit /set** \[**{***ID***}**\] **targetname** *name*\]

If no **{***ID***}** is specified, the settings apply to the current boot entry.

The following example shows how to specify the USB debug settings for a specific boot entry, and how to use the **/debug** command to enable kernel debugging for that boot entry. Note that to enable the debug settings, you must reboot your computer and select the boot entry you have configured for debugging.

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} debugtype usb
```

``` syntax
bcdedit /set {18b123cd-2bf6-11db-bfae-00e018e2b8db} targetname u2
```

``` syntax
bcdedit /debug {18b123cd-2bf6-11db-bfae-00e018e2b8db} on
```

You can use the **bcdedit /enum** command to view the current boot entries and their settings.

For more details, see [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) and [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187).

### <span id="boot_parameters_to_debug_the_boot_process_in_windows_vista_and_later"></span><span id="BOOT_PARAMETERS_TO_DEBUG_THE_BOOT_PROCESS_IN_WINDOWS_VISTA_AND_LATER"></span>Boot Parameters to Debug the Boot Process in Windows

To enable boot debugging, use the [**BCDEdit /bootdebug**](https://msdn.microsoft.com/library/windows/hardware/ff542183) command and specify the appropriate boot component. If you wish to perform kernel debugging after Windows starts, use the [**BCDEdit /debug**](https://msdn.microsoft.com/library/windows/hardware/ff542191) command as well.

You must also select a debugging connection (serial, 1394, or USB 2.0). This can be done with either the [**BCDEdit /dbgsettings**](https://msdn.microsoft.com/library/windows/hardware/ff542187) or [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) command, just as in normal kernel debugging.

For more details, see [**BCDEdit /bootdebug**](https://msdn.microsoft.com/library/windows/hardware/ff542183).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Boot%20Parameters%20to%20Enable%20Debugging%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




