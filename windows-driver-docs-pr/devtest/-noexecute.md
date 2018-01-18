---
title: /noexecute
description: The /noexecute parameter enables, disables, and configures Data Execution Prevention (DEP), a set of hardware and software technologies designed to prevent harmful code from running in protected memory locations.For more information about using the /noexecute parameter and the other parameters that affect DEP configuration, see Boot Parameters to Configure DEP and PAE. Note � DEP is a highly effective security feature. Do not disable DEP unless you have no alternative.�
ms.assetid: 7333cac4-91d0-4088-ab5d-4dd5883c9dbc
keywords: ["/noexecute Driver Development Tools"]
topic_type:
- apiref
api_name:
- /noexecute
api_type:
- NA
---

/noexecute
==========

The **/noexecute** parameter enables, disables, and configures Data Execution Prevention (DEP), a set of hardware and software technologies designed to prevent harmful code from running in protected memory locations.

For more information about using the /**noexecute** parameter and the other parameters that affect DEP configuration, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

> [!NOTE]
> DEP is a highly effective security feature. Do not disable DEP unless you have no alternative.

 

``` syntax
    /noexecute={alwayson | optout | optin | alwaysoff}

   
```

## Subparameters


### Subparameter

<a href="" id="-------alwayson------"></a> **alwayson**   
Enables DEP for the operating system and all processes, including the Windows kernel and drivers. All attempts to disable DEP are ignored.

<a href="" id="-------optout------"></a> **optout**   
Enables DEP for the operating system and all processes, including the Windows kernel and drivers. However, administrators can disable DEP on selected executable files by using **System** in Control Panel.

<a href="" id="-------optin------"></a> **optin**   
Enables DEP only for operating system components, including the Windows kernel and drivers. Administrators can enable DEP on selected executable files by using the Application Compatibility Toolkit (ACT).

<a href="" id="-------alwaysoff------"></a> **alwaysoff**   
Disables DEP. Attempts to enable DEP selectively are ignored.

On Windows XP with SP2, this subparameter also disables Physical Address Extension (PAE). This subparameter does not disable PAE on Windows Server 2003 with SP1.

### Comments

### What is DEP?

*Data Execution Prevention* (DEP) consists of hardware and software methods. *Software-enforced DEP*, which protects only user-mode processes, must be supported by the operating system. *Hardware-enforced DEP* sets a bit in the page table entry that prevents code from being executed from a virtual memory page that should contain only data. Hardware-enforced DEP must be supported by the operating system and the processor on the computer. If the operating system supports DEP, but the processor does not, only software-enforced DEP is enabled on the system.

### Operating System Support

DEP is supported in Windows Server 2003 with SP1, Windows XP with SP2, Windows Vista, and later versions of Windows.

The **/noexecute** parameter is supported only on Windows Server 2003 with SP1 and Windows XP with SP2. On Windows Vista and later versions of Windows, use the **NX** element in BCDEdit.

### 32-bit and 64-bit Support

The **/noexecute** parameter is effective only on 32-bit processes. It enables software-enforced DEP and, if the processor supports DEP, it also enables hardware-enforced DEP.

On 64-bit processes, DEP is enabled by default and cannot be disabled (equivalent to **/noexecute=alwayson**). For these processes, the **/noexecute** parameter is ignored. On a 64-bit operating system, the **/noexecute** parameter affects only 32-bit processes running on the system.

### Default Values

On Windows XP with SP2, the installation program adds **/noexecute=optin** to the boot entry.

On Windows Server 2003 with SP1, the installation program adds **/noexecute=optout** to the boot entry.

However, on all operating systems that support DEP, if the **/noexecute** parameter is not present in the boot options, the system behaves as though the setting is **/noexecute=optin**.

### DEP and PAE

On 32-bit operating systems, hardware-enforced DEP requires Physical Address Extension (PAE). Therefore, when DEP is enabled on a computer that supports hardware-enforced DEP, 32-bit versions of the Windows operating system automatically enable PAE and ignores [**/nopae**](-nopae.md).

On Windows XP with SP2, , when you disable DEP by using **/noexecute=alwaysoff**, Windows disables both DEP and PAE. This is the equivalent of using **/noexecute=alwaysoff /nopae**. To enable PAE without DEP on a system with hardware-enforced DEP, use /**noexecute=alwaysoff /pae**. This explicitly enables PAE while disabling DEP.

However, on Windows Server 2003 with SP1, when you disable DEP by using **/noexecute=alwaysoff**, Windows disables only DEP. PAE is still enabled and the system ignores explicit attempts to disable PAE, such as the **/nopae** parameter. To disable both DEP and PAE on Windows Server 2003 with SP1, use [**/execute**](-execute.md).

For a table that describes these parameters and their effects, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

### Setting DEP in Control Panel

To set the **/noexecute=optin** or **/noexecute=optout** policies, or to disable DEP on a particular executable file, open Control Panel, and then double-click **System**. Click the **Advanced** tab and under **Performance**, click **Settings**, and then click the **Data Execution Prevention** tab. To make the new settings effective, you must restart the computer.

For more information about DEP, see [Changes to Functionality in Microsoft Windows XP Service Pack 2, Part 3: Memory Protection Technologies](http://go.microsoft.com/fwlink/p/?linkid=35141).

### Example

```
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect /noexecute=alwayson
```

### Bootcfg command

```
bootcfg /raw "/noexecute=alwayson" /A /ID 1
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/noexecute%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




