---
title: /execute
description: The /execute parameter disables Data Execution Prevention (DEP) and Physical Address Extension (PAE).Note � DEP is a highly effective security feature.
ms.assetid: 2d275a80-5d7f-4b6d-ba82-2bb6801d1d56
keywords: ["/execute Driver Development Tools"]
topic_type:
- apiref
api_name:
- /execute
api_type:
- NA
---

/execute
========

The **/execute** parameter disables Data Execution Prevention (DEP) and Physical Address Extension (PAE).

> [!IMPORTANT]
> DEP is a highly effective security feature. Do not disable DEP unless you have no other alternative.

> [!NOTE]
> The **/execute** parameter is supported in in Windows Server 2003 with SP1 to disable both DEP and PAE . To disable DEP and PAE in Windows XP with Service Pack 2 (SP2), use **/noexecute=alwaysoff**. For more information, see [**/noexecute**](-noexecute.md). 

For more information about using the /**execute** parameter and the other parameters that affect DEP configuration, see [Boot Parameters to Configure DEP and PAE](https://msdn.microsoft.com/library/windows/hardware/ff542275).

``` syntax
    /execute   
```

### Comments

### What is DEP?

DEP consists of hardware and software methods. *Software-enforced DEP*, which protects only user-mode processes, must be supported by the operating system. *Hardware-enforced DEP* sets a bit in the page table entry that prevents code from being executed from a virtual memory page that should contain only data. Hardware-enforced DEP must be supported by the operating system and the processor on the computer. If the operating system supports DEP, but the processor does not, only software-enforced DEP is enabled on the system.

### Operating System Support

DEP is supported in Windows Server 2003 with SP1, Windows XP with SP2, Windows Vista, and later versions of Windows. The **/execute** option is supported only on Windows Server 2003 with SP1 and Windows XP with SP2. On Windows Vista and later versions of Windows, use the **NX** element in BCDEdit.

### 32-bit and 64-bit Support

The **/execute** parameter is effective only on 32-bit processes. On 64-bit processes, DEP is enabled by default and cannot be disabled. For these processes, the **/execute** parameter is ignored. On a 64-bit operating system, the **/execute** parameter affects only on 32-bit processes running on the system.

### Enabling and Configuring DEP

To enable, disable, and configure DEP on Windows Server 2003 with SP1 and Windows XP with SP2, use the[**/noexecute**](-noexecute.md) boot parameter.

### DEP and PAE

On 32-bit operating systems, hardware-enforced DEP requires PAE. Therefore, when DEP is enabled on a computer that supports hardware-enforced DEP, 32-bit versions of the Windows operating system automatically enable PAE (see [**/pae**](-pae.md)).

The **/execute** parameter disables both DEP and PAE.

On Windows XP, Windows Vista and later versions of Windows when you disable DEP, Windows also disables PAE. On Windows XP, the **/execute** parameter has the same effect as the **/noexecute=alwaysoff** and **noexecute=alwaysoff /nopae** parameters; they all disable both DEP and PAE.

However, on Windows Server 2003 with SP1, the **/noexecute=alwaysoff** parameter disables DEP, but it does not disable PAE, and the system ignores [**/nopae**](-nopae.md). To disable both DEP and PAE on Windows Server 2003 with SP1, you must use **/execute**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20/execute%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




