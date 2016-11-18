---
title: Changing Boot Parameters
description: Changing Boot Parameters
ms.assetid: e835e1e9-ad80-462b-b55f-2fa0e55009a5
keywords: ["boot entry parameters WDK", "boot parameters WDK", "boot options WDK , boot parameters"]
---

# Changing Boot Parameters


## <span id="ddk_changing_boot_parameters_tools"></span><span id="DDK_CHANGING_BOOT_PARAMETERS_TOOLS"></span>


To enable and configure boot-related operating system features, such as debugging, you must add boot parameters to a boot entry for the operating system.

To change boot parameters on a system running Windows, you can use BCDEdit.

### <span id="using_bcdedit"></span><span id="USING_BCDEDIT"></span>Using BCDEdit

To add a boot configuration parameter to a boot entry, use the BCDEdit boot entry options to change global settings, such as **/ems**, **/debug**, **/dbgsettings**, or set individual parameters using the [**BCDEdit /set**](https://msdn.microsoft.com/library/windows/hardware/ff542202) options. For a complete list of BCDEdit options, at a command prompt, type **BCDEdit /?** or **BCDEdit /?** &lt;command&gt; to find help about a specific command.

For example, the following command enables PAE for a specified boot entry:

```
bcdedit /set {802d5e32-0784-11da-bd33-000476eba25f} pae forceenable
```

To turn the kernel debugger on or off, use the **/debug** option with the following syntax:

```
bcdedit /debug <ID> [on | off]
```

The &lt;ID&gt; is the GUID that is associated with the boot entry. If you do not specify an &lt;ID&gt;, the command modifies the operating system that is currently active. The following command turns on the kernel debugger for a boot entry, called DebugEntry:

```
bcdedit /debug {49916baf-0e08-11db-9af4-000bdbd316a0} on
```

To view the current boot entries, type **bcdedit** at the command prompt. The boot entry for DebugEntry shows that the kernel debugger is turned on.

```
## Windows Boot Loader
-------------------
identifier              {49916baf-0e08-11db-9af4-000bdbd316a0}
device                  partition=C:
path                    \Windows\system32\winload.exe
description             DebugEntry
locale                  en-US
inherit                 {bootloadersettings}
osdevice                partition=C:
systemroot              \Windows
resumeobject            {3e3a9f69-024a-11db-b5fc-a50a1ad8a70e}
nx                      OptIn
pae                     ForceEnable
debug                   Yes
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Changing%20Boot%20Parameters%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




