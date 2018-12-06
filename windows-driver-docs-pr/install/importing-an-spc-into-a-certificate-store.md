---
title: Importing an SPC into a Certificate Store
description: Importing an SPC into a Certificate Store
ms.assetid: 4640b48c-e56f-4c6b-8943-f8b6fc3e37d7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Importing an SPC into a Certificate Store


Once a Personal Information Exchange (.*pfx*) file is created to store a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and its private and public keys, the *.pfx* file must be imported into the Personal certificate store on the signing computer. For more information about *.pfx* files, see [Personal Information Exchange (.pfx) Files](personal-information-exchange---pfx--files.md).

To import a *.pfx* file into the local Personal certificate store, do the following:

1.  Start Windows Explorer and double-click the *.pfx* file to open the Certificate Import Wizard.

2.  Follow the procedure in the Certificate Import Wizard to import the code-signing certificate into the Personal certificate store.

The certificate and private key are now available for SignTool to use.

Starting with Windows Vista, an alternative way to import the *.pfx* file into the local Personal certificate store is with the [CertUtil](http://go.microsoft.com/fwlink/p/?linkid=168888) command-line utility. The following command-line example uses CertUtil to import the *abc.pfx* file into the Personal certificate store:

```cpp
certutil -user -p pfxpassword -importPFX abc.pfx
```

Where:

-   The **-user** option specifies "Current User" Personal store.

-   The **-p** option specifies the password for the *.pfx* file (*pfxpassword*).

-   The **-importPFX** option specifies name of the *.pfx* file (*abc.pfx*).

Once the *.pfx* file is imported into the Personal certificate store on the signing computer, you can use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to release-sign [driver packages](driver-packages.md).

 

 





