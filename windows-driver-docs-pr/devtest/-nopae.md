---
title: /nopae
description: The /nopae parameter disables Physical Address Extension (PAE) and forces the boot loader to load the non-PAE version of the Windows kernel.For more information about using the /nopae parameter and the other parameters that affect PAE configuration, see Boot Parameters to Configure DEP and PAE.
ms.assetid: 36e5a520-ae58-43e6-8a73-dd0c5a6ede4e
keywords: ["/nopae Driver Development Tools"]
topic_type:
- apiref
api_name:
- /nopae
api_type:
- NA
---

/nopae
======

The **/nopae** parameter disables Physical Address Extension (PAE) and forces the boot loader to load the non-PAE version of the Windows kernel.

For more information about using the **/nopae** parameter and the other parameters that affect PAE configuration, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

``` syntax
    /nopae 

   
```

### Comments

This parameter is valid only on boot entries for 32-bit versions of Windows that run on computers with x86 and x64-based processors.

The **/nopae** option is supported only on Windows Server 2003 with SP1 and Windows XP with SP2. On Windows Vista and later versions of Windows, use the **PAE** element in BCDEdit with a value of **ForceDisable**.

Consider using this parameter on systems on which a device does not operate properly when PAE is enabled.

Typically, this parameter is not necessary because PAE is not enabled unless you use the [**/pae**](-pae.md) boot parameter. However, on computers with x86 processors, Windows automatically enables PAE when the computer is configured for hot-add memory devices in memory ranges beyond the 4 GB region, as defined by the Static Resource Affinity Table (SRAT). *Hot-add memory* supports memory devices that you can add without rebooting or turning off power to the computer. In this case, because PAE must be enabled when the system starts, it is enabled automatically so that the system can immediately address extended memory that is added between restarts. (Disabling PAE on these systems disables hot-add memory.) Hot-add memory is supported only on Windows Server 2003, Datacenter Edition; Windows Server 2003, Enterprise Edition; Windows Server 2008, Datacenter Edition; Windows Server 2008 for Itanium-Based Systems; and on the datacenter and enterprise editions of all later versions of Windows Server. Moreover, for versions of Windows prior to Windows Server 2008, hot-add memory is supported only on computers with an ACPI BIOS, an x86 processor, and specialized hardware. For Windows Server 2008 and later versions of Windows Server, it is supported for all processor architectures.

On a computer that supports hardware-enabled Data Execution Protection (DEP) and is running a 32-bit version of the Windows operating system that supports DEP, PAE is automatically enabled when DEP is enabled, even if **/nopae** is set. On all 32-bit versions of Windows that support DEP, except Windows Server 2003 with SP1, when you disable DEP, Windows automatically disables PAE, but you can use **/pae** to enable it. For information about DEP, see [**/noexecute**](-noexecute.md).

PAE is supported in Windows 2000 and later versions of Windows.

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Windows Server 2003, Enterprise" /fastdetect /nopae
```

### Bootcfg Command

```
bootcfg /raw "/nopae" /A /ID 1
```

See also
--------

[**/pae**](-pae.md)
 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/nopae%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




