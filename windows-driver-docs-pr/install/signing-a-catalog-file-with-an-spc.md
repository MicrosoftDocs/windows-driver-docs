---
title: Signing a Catalog File with an SPC
description: Signing a Catalog File with an SPC
ms.assetid: 8fe1fc32-73c9-4c09-96bd-93effb35c061
---

# Signing a Catalog File with an SPC


Use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command to sign the [catalog file](catalog-files.md) of a kernel-mode [driver package](driver-packages.md) with a [Software Publisher Certificate (SPC)](software-publisher-certificate.md). For 64-bit versions of Windows Vista and later versions of Windows, kernel-mode driver packages that do not have a [WHQL release signature](whql-release-signature.md) must be signed with an SPC signature to comply with both the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

```
SignTool sign /v /ac CrossCertificateFile /s SPCCertificateStore /n SPCCertificateName /t http://timestamp.verisign.com/scripts/timstamp.dll CatalogFileName.cat
```

Where:

-   The **sign** command configures SignTool to sign the catalog file *CatalogFileName.cat*.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/ac** *CrossCertificateFile* option specifies the cross-certificate *.cer* file that is associated with the Software Publisher Certificate (SPC) that is specified by *SPCCertificateName*.

-   The **/s** *SPCCertificateStore* option specifies the name of the certificate store that holds the Software Publisher Certificate that is specified by *SPCCertificateName*. As described in [Software Publisher Certificate (SPC)](software-publisher-certificate.md), the certificate information must be contained in *.pfx* file, and the information in the *.pfx* file must be added to the Personal certificate store of the local computer. The Personal certificate store is specified by the option **/s my**.

-   The **/n** *SPCCertificateName* option specifies the name of the certificate in the *SPCCertificateStore* certificate store.

-   The **/t** *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *CatalogFileName.cat* is the name of the catalog file.

For example, the following command signs the *Tstamd64.cat* catalog file with the SPC named "contoso.com" in the Personal "my" certificate store and the corresponding cross-certificate *Rsacertsvrcross.cer*. The signature is time-stamped by the service http://timestamp.verisign.com/scripts/timstamp.dll. In this example, the catalog file is in the same directory in which the command is run.

```
SignTool sign /v /ac c:\lab\rsacertsrvcross.cer /s my /n contoso.com /t http://timestamp.verisign.com/scripts/timstamp.dll tstamd64.cat 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Signing%20a%20Catalog%20File%20with%20an%20SPC%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




