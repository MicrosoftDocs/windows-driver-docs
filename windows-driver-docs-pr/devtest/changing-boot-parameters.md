---
title: Changing Boot Parameters
description: Changing Boot Parameters
keywords:
- boot entry parameters WDK
- boot parameters WDK
- boot options WDK , boot parameters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Changing Boot Parameters

To enable and configure boot-related operating system features, such as debugging, you must add boot parameters to a boot entry for the operating system.

To change boot parameters on a system running Windows, you can use BCDEdit.

## <span id="using_bcdedit"></span><span id="USING_BCDEDIT"></span>Using BCDEdit

To add a boot configuration parameter to a boot entry, use the BCDEdit boot entry options to change global settings, such as **/ems**, **/debug**, **/dbgsettings**, or set individual parameters using the [**BCDEdit /set**](./bcdedit--set.md) options. For a complete list of BCDEdit options, at a command prompt, type **BCDEdit /?** or **BCDEdit /?** &lt;command&gt; to find help about a specific command.

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
