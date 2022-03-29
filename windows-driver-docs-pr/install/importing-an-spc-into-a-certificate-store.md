---
title: Importing an SPC into a Certificate Store
description: Importing an SPC into a Certificate Store
ms.date: 04/20/2017
---

# Importing an SPC into a Certificate Store


Once a Personal Information Exchange (.*pfx*) file is created to store a [Software Publisher Certificate (SPC)](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md) and its private and public keys, the *.pfx* file must be imported into the Personal certificate store on the signing computer. For more information about *.pfx* files, see [Personal Information Exchange (.pfx) Files](personal-information-exchange---pfx--files.md).

To import a *.pfx* file into the local Personal certificate store, do the following:

1.  Start Windows Explorer and select and hold (or right-click) the *.pfx* file, then select Open to open the Certificate Import Wizard.

2.  Follow the procedure in the Certificate Import Wizard to import the code-signing certificate into the Personal certificate store.

The certificate and private key are now available for SignTool to use.

Starting with Windows Vista, an alternative way to import the *.pfx* file into the local Personal certificate store is with the [CertUtil](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732443(v=ws.10)) command-line utility. The following command-line example uses CertUtil to import the *abc.pfx* file into the Personal certificate store:

```cpp
certutil -user -p pfxpassword -importPFX abc.pfx
```

Where:

-   The **-user** option specifies "Current User" Personal store.

-   The **-p** option specifies the password for the *.pfx* file (*pfxpassword*).

-   The **-importPFX** option specifies name of the *.pfx* file (*abc.pfx*).

Once the *.pfx* file is imported into the Personal certificate store on the signing computer, you can use [**SignTool**](../devtest/signtool.md) to release-sign [driver packages](driver-packages.md).