---
title: Release-Signing a Driver File
description: Release-Signing a Driver File
ms.assetid: 3da0377d-57cf-4bd4-b3ce-6ba4ebbc3ceb
keywords: ["public release driver signing WDK , driver files", "driver file release signing WDK"]
---

# Release-Signing a Driver File


Use the following [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) command to embed a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) signature in a driver file. To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md), [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) for 64-bit versions of Windows Vista and later versions of Windows must have an embedded SPC signature.

```
SignTool sign /v /ac CrossCertificateFile /s SPCCertificateStore /n SPCCertificateName /t http://timestamp.verisign.com/scripts/timstamp.dll DriverFileName.sys
```

Where:

-   The **sign** command configures SignTool to embed a signature in the file *DriverFileName.sys*.

-   The **/v** verbose option configures SignTool to print execution and warning messages.

-   The **/ac** *CrossCertificateFile* option specifies the cross-certificate *.cer* file that is associated with the SPC that is specified by *SPCCertificateName*.

-   The **/s** *SPCCertificateStore* option specifies the name of the Personal certificate store that holds the SPC that is specified by *SPCCertificateName*. As described in [Software Publisher Certificate (SPC)](software-publisher-certificate.md), the certificate information must be contained in a *.pfx* file, and the information in the *.pfx* file must be added to the Personal certificate store of the local computer. The Personal certificate store is specified by the option **/s my**.

-   The **/n** *SPCCertificateName* option specifies the name of the certificate in the *SPCCertificateStore* certificate store.

-   The **/t** *http://timestamp.verisign.com/scripts/timstamp.dll* option supplies the URL to the publicly-available time-stamp server that VeriSign provides.

-   *DriverFileName.sys* is the name of the driver file.

The following command embeds a signature in *Toaster.sys* that is generated from a certificate named "contoso.com" in the Personal "my" certificate store and the corresponding cross-certificate *Rsacertsvrcross.cer*. In addition, the signature is time-stamped by the time stamp service http://timestamp.verisign.com/scripts/timstamp.dll. In this example, *Toaster.sys* is in the *amd64* subdirectory under the directory in which the command is run.

```
SignTool sign /v /ac c:\lab\rsacertsrvcross.cer /s my /n contoso.com /t http://timestamp.verisign.com/scripts/timstamp.dll amd64\toaster.sys
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Release-Signing%20a%20Driver%20File%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




