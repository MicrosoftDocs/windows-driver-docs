---
title: Exporting and Importing Boot Entries in EFI
description: Exporting and Importing Boot Entries in EFI
keywords:
- NVRAM boot options WDK , exporting
- EFI NVRAM boot options WDK , exporting
- NVRAM boot options WDK , importing
- EFI NVRAM boot options WDK , importing
- exporting boot entries WDK
- importing boot entries
- boot entry IDs WDK
- EFI boot entry IDs WDK
- identifiers WDK boot options
ms.date: 07/02/2018
---

# Exporting and Importing Boot Entries in EFI

Use the **nvrboot x** (export) command to create a backup copy of a boot entry. Design a naming and storage convention that will make it easy to find the backup copy files when you need them.

Use the **nvrboot i** (import) command to import boot entries from the backup copies that you exported or from the Boot*xxxx* boot entry backup files that Setup created.

Imported boot entries always receive new EFI boot entry IDs. For example, if you export a copy of Boot0003, and then import the copy into NVRAM, the imported boot entry receives a new boot entry ID, such as Boot000A.
