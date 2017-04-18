---
title: Exporting and Importing Boot Entries in EFI
description: Exporting and Importing Boot Entries in EFI
ms.assetid: bd019064-cb8c-434c-b471-192168564540
keywords: ["NVRAM boot options WDK , exporting", "EFI NVRAM boot options WDK , exporting", "NVRAM boot options WDK , importing", "EFI NVRAM boot options WDK , importing", "exporting boot entries WDK", "importing boot entries", "boot entry IDs WDK", "EFI boot entry IDs WDK", "identifiers WDK boot options"]
---

# Exporting and Importing Boot Entries in EFI


## <span id="ddk_exporting_and_importing_boot_entries_in_efi_tools"></span><span id="DDK_EXPORTING_AND_IMPORTING_BOOT_ENTRIES_IN_EFI_TOOLS"></span>


Use the **nvrboot x** (export) command to create a backup copy of a boot entry. Design a naming and storage convention that will make it easy to find the backup copy files when you need them.

Use the **nvrboot i** (import) command to import boot entries from the backup copies that you exported or from the Boot*xxxx* boot entry backup files that Setup created.

Imported boot entries always receive new EFI boot entry IDs. For example, if you export a copy of Boot0003, and then import the copy into NVRAM, the imported boot entry receives a new boot entry ID, such as Boot000A.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Exporting%20and%20Importing%20Boot%20Entries%20in%20EFI%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




