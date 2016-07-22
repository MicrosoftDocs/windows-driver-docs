---
title: Appendix 4 Driver Signing Issues
description: Two known driver signing issues are described below.
ms.assetid: EC244022-A02B-4AAD-93EE-B9AE3E72A674
---

# Appendix 4: Driver Signing Issues


Two known driver signing issues are described below.

## Signing issue with previous OS


Every new release of Windows and subsequently in the released Service Packs, root certificates from Microsoft certified CA vendors, new or existing vendors with new certificates are added to the OS image. For example, Vista, XP, etc. OSes may have unknown signing issues or driver not signed issues if the computer under test is not connected to the internet. If the computer under test is connected to the internet, then the new certificates are automatically downloaded when a driver is installed and there will not be any issues. Sometimes the CA vendors are also able to help out in resolving the issues when the computer under test is not connected to the internet.

## Code 52 error


There is a known bug for Windows 7 x64 OS, when a catalog file (.cat) is signed using a new VeriSign released signing certificate which uses the SHA256 has algorithm. If you open the signed cat file and view signature and select the Details tab you will notice the following:

![screen shot showing the signature's hash algorithm](images/tutorialcertsignaturehashalg.png)

To resolve the issue, you may ask VeriSign to provide a replacement certificate at no cost signed with the SHA1 hash algorithm.

Alternatively, you can buy another SHA1 certificate and sign the file with two signatures as shown below if you want to keep both certificates. Note that only .sys files can be dual signed because they are PE files.

```
Signtool sign /fd sha256 /ac C:\MyCrossCert\Crosscert.cer /s my /n “MyCompany Inc. “ /ph /as /sha1 XX...XX C:\DriverDir\toaster.SYS
```

Where XX...XX is the hash of the certificate you are using for the secondary signature. Add /tr to timestamp signing.

**Note**  Please review Microsoft Security Advisory ([2880823](https://technet.microsoft.com/library/security/2880823)) "Deprecation of SHA-1 Hashing Algorithm for Microsoft Root Certificate Program" which describes a policy change wherein Microsoft will no longer allow root certificate authorities to issue X.509 certificates using the SHA-1 hashing algorithm for the purposes of SSL and code signing after January 1, 2016.

 

Use of SHA1 certificate will be deprecated by Microsoft starting from January 1, 2016. All CA vendors must to issue signing certificates with the SHA256 hash algorithm.

Windows will stop accepting SHA1 code signing certificates without time stamps after 1 January 2016.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Appendix%204:%20Driver%20Signing%20Issues%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




