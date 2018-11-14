---
title: Personal Information Exchange (.pfx) Files
description: Personal Information Exchange (.pfx) Files
ms.assetid: 58849ccc-c86f-4c49-b848-8926febb5521
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Personal Information Exchange (.pfx) Files


To be used for release signing, a Software Publisher Certificate (SPC), and its private and public keys, must be stored in a Personal Information Exchange (.*pfx*) file. However, some certificate authorities (CAs) use different file formats to store this data. For example, some CAs store the certificate's private key in a Private Key (.*pvk*) file and store the certificate and public key in a *.spc* or *.cer* file.

If the CA issued an *.spc* and its keys in non-*.pfx* files, you must convert and store the files in a *.pfx* file before they can be used for release-signing. The [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672) tool is used to perform this conversion.

The following command-line example converts a *.pvk* file that is named *abc.pvk* and a *.spc* that is named *abc.spc* into a *.pfx* file that is named *abc.pfx*:

```cpp
Pvk2Pfx -pvk abc.pvk -pi pvkpassword -spc abc.spc -pfx abc.pfx -po pfxpassword -f
```

Where:

-   The **-pvk** option specifies a *.pvk* file (*abc.pvk*).

-   The **-pi** option specifies the password for the .*pvk* file (*pvkpassword*).

-   The **-spc** option specifies the name and extension of the SPC file that contains the certificate. The file can be either an *.spc* file or a *.cer* file. In this example, the certificate and public key are in the *abc.spc* file.

-   The **-pfx** option specifies the name of the *.pfx* file (*abc.pfx*). If this option is not specified, Pvk2Pfx opens an Export Wizard and ignores the -po and -f arguments.

-   The **-po** option specifies a password for the *.pfx* file (*pfxpassword*). If this option is not specified, the specified *.pfx* file is assigned the same password that is associated with the specified *.pvk* file.

-   The **-f** option configures Pvk2Pfx to replace an existing *.pfx* file if one exists.

For more information about SPCs and their management, see [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

 

 





