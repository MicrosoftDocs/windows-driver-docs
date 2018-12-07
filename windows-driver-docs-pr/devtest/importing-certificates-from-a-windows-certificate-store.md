---
title: Importing Certificates from a Windows Certificate Store
description: Importing Certificates from a Windows Certificate Store
ms.assetid: abdf19c7-2cea-4af3-8a86-37fc4a9e7c3d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Importing Certificates from a Windows Certificate Store


You can use the Enhanced Storage Certificate Management tool to import certificates from your private certificate store in the computer to an IEEE 1667-compliant USB storage device.

To import a certificate from a private certificate store, you must specify the certificate name by using the **-Store** parameter of the [**/Add**](enhstor-add-switch.md) and [**/Replace**](-replace-switch.md) switches of the Enhanced Storage Certificate Management tool. The tool searches all of your private certificate stores for the specified certificate and (if found) imports it to a specified USB storage device.

**Note**  The tool does not import a certificate from the Windows root certificate store.

 

 

 





