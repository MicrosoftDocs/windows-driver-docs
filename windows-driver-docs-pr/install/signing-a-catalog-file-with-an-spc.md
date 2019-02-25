---
title: Signing a Catalog File with an SPC
description: Signing a Catalog File with an SPC
ms.assetid: 8fe1fc32-73c9-4c09-96bd-93effb35c061
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Signing a Catalog File with an SPC


Use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command to sign the [catalog file](catalog-files.md) of a kernel-mode [driver package](driver-packages.md) with a [Software Publisher Certificate (SPC)](software-publisher-certificate.md). For 64-bit versions of Windows Vista and later versions of Windows, kernel-mode driver packages that do not have a [WHQL release signature](whql-release-signature.md) must be signed with an SPC signature to comply with both the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md).

```cpp
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

```cpp
SignTool sign /v /ac c:\lab\rsacertsrvcross.cer /s my /n contoso.com /t http://timestamp.verisign.com/scripts/timstamp.dll tstamd64.cat 
```

 

 





