---
title: Personal Information Exchange (.pfx) Files
description: Personal Information Exchange (.pfx) Files
ms.assetid: 58849ccc-c86f-4c49-b848-8926febb5521
---

# Personal Information Exchange (.pfx) Files


To be used for release signing, a Software Publisher Certificate (SPC), and its private and public keys, must be stored in a Personal Information Exchange (.*pfx*) file. However, some certificate authorities (CAs) use different file formats to store this data. For example, some CAs store the certificate's private key in a Private Key (.*pvk*) file and store the certificate and public key in a *.spc* or *.cer* file.

If the CA issued an *.spc* and its keys in non-*.pfx* files, you must convert and store the files in a *.pfx* file before they can be used for release-signing. The [**Pvk2Pfx**](https://msdn.microsoft.com/library/windows/hardware/ff550672) tool is used to perform this conversion.

The following command-line example converts a *.pvk* file that is named *abc.pvk* and a *.spc* that is named *abc.spc* into a *.pfx* file that is named *abc.pfx*:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Personal%20Information%20Exchange%20%28.pfx%29%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




