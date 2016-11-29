---
title: Changing the Default Boot Entry
description: Changing the Default Boot Entry
ms.assetid: 0dce10d4-f73a-49bd-8a24-a4aa14c82233
keywords: ["default boot entries", "Boot.ini files WDK , default boot entries", "boot options WDK , default boot entries", "identifying boot entry", "current boot entry WDK", "NVRAM boot options WDK , default boot entries", "EFI NVRAM boot options WDK , default boot entries"]
---

# Changing the Default Boot Entry


## <span id="ddk_changing_the_default_boot_entry_tools"></span><span id="DDK_CHANGING_THE_DEFAULT_BOOT_ENTRY_TOOLS"></span>


The default boot entry is the entry that the boot loader selects when the boot menu time-out expires. You can change the default boot entry to ensure that the operating system configuration that you prefer is loaded automatically.

For Windows, you can use BCDEdit to change the default boot entry.

### <span id="using_bcdedit"></span><span id="USING_BCDEDIT"></span>Using BCDEdit

You can specify the default boot entry using the **/default** option. The syntax to specify the default operating system is as follows:

```
bcdedit /default <ID>
```

The *&lt;ID&gt;* is the GUID for the Windows boot loader boot entry that is associated with the operating system that you want to designate as the default. You must include the braces (**{ }**) around the GUID, for example:

```
bcdedit /default {cbd971bf-b7b8-4885-951a-fa03044f5d71}
```

To change the default boot entry to the earlier Windows operating system loader on a multiboot computer, set *&lt;ID&gt;* to **{ntldr}**, which is the reserved name for the GUID that is associated with Ntldr. This might present another menu depending on entries in Boot.ini file.

```
bcdedit /default {ntldr}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Changing%20the%20Default%20Boot%20Entry%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




