---
title: Importing an SPC into a Certificate Store
description: Importing an SPC into a Certificate Store
ms.assetid: 4640b48c-e56f-4c6b-8943-f8b6fc3e37d7
---

# Importing an SPC into a Certificate Store


Once a Personal Information Exchange (.*pfx*) file is created to store a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) and its private and public keys, the *.pfx* file must be imported into the Personal certificate store on the signing computer. For more information about *.pfx* files, see [Personal Information Exchange (.pfx) Files](personal-information-exchange---pfx--files.md).

To import a *.pfx* file into the local Personal certificate store, do the following:

1.  Start Windows Explorer and double-click the *.pfx* file to open the Certificate Import Wizard.

2.  Follow the procedure in the Certificate Import Wizard to import the code-signing certificate into the Personal certificate store.

The certificate and private key are now available for SignTool to use.

Starting with Windows Vista, an alternative way to import the *.pfx* file into the local Personal certificate store is with the [CertUtil](http://go.microsoft.com/fwlink/p/?linkid=168888) command-line utility. The following command-line example uses CertUtil to import the *abc.pfx* file into the Personal certificate store:

```
certutil -user -p pfxpassword -importPFX abc.pfx
```

Where:

-   The **-user** option specifies "Current User" Personal store.

-   The **-p** option specifies the password for the *.pfx* file (*pfxpassword*).

-   The **-importPFX** option specifies name of the *.pfx* file (*abc.pfx*).

Once the *.pfx* file is imported into the Personal certificate store on the signing computer, you can use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to release-sign [driver packages](driver-packages.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Importing%20an%20SPC%20into%20a%20Certificate%20Store%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




