---
title: Authenticode Signing of Third-party CSPs
description: Third-party Authenticode signing for custom Cryptographic Service Providers (CSPs) has been available beginning with Windows Vista, and has been back ported to Windows XP SP3 and Windows Server 2003 SP2 as of May, 2013 via this download.
ms.assetid: DBAA575A-F0B5-4725-A7B1-D6EA84977212
---

# Authenticode Signing of Third-party CSPs


Third-party Authenticode signing for custom Cryptographic Service Providers (CSPs) has been available beginning with Windows Vista, and has been back ported to Windows XP SP3 and Windows Server 2003 SP2 as of May, 2013 via [this download](http://support.microsoft.com/kb/2836198).

Consequently, Microsoft will no longer sign CSPs, and the manual CSP signing service has been retired. Emails and CSPs sent to cspsign@microsoft.com or cecspsig@microsoft.com to be signed will no longer be processed by Microsoft.

Instead, all third-party CSPs can now be self-signed by following this procedure:

1.  Purchase a code-signing certificate from a Certificate Authority (CA) for which Microsoft also issues a cross-certificate. The [Cross-Certificates for Kernel Mode Code Signing](cross-certificates-for-kernel-mode-code-signing.md) topic provides a list of CAs for which Microsoft also provides cross-certificates and the corresponding cross-certificates. Note that these are the only cross-certificates that chain up to the “Microsoft Code Verification Root” issued by Microsoft, which will enable Windows to run third-party CSPs.
2.  After you have a certificate from the CA and the matching cross-certificate, you can use [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) to sign all your CSP binaries.
3.  SignTool is included in the latest versions of Visual Studio. It is also included in the WDK version 7.0 and newer versions. Note that the SignTool that ships with earlier versions of the WDK is not compatible with cross-certificates and cannot be used to sign your binaries.

**Note**  Starting with Windows 8, it is no longer a requirement that CSPs must be signed.

 

You can sign binaries from a command-line, or sign as an integrated build step in Visual Studio 2012 and newer.

The command to [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) is:

``` syntax
signtool.exe sign /ac <cross-certificate_from_ms> /sha1 <sha1_hash> /t <timestamp_server> /d <”optional_description_in_double_quotes”> <binary_file.ext>
```

-   &lt;cross-certificate\_from\_ca&gt; is the cross-certificate file you downloaded from Microsoft
-   &lt;sha1\_hash&gt; is the SHA1 thumbprint that corresponds to the code signing certificate
-   &lt;timestamp\_server&gt; is the server used to timestamp the signing operation
-   &lt;”optional\_description\_in\_double\_quotes”&gt; is an optional friendly-name description
-   &lt;binary\_file.ext&gt; is the file to sign

For example:

``` syntax
signtool.exe sign /ac certificate.cer /sha1 553e39af9e0ea8c9edcd802abbf103166f81fa50 /t "http://timestamp.verisign.com/scripts/timstamp.dll" /d "My Cryptographic Service Provider" csp.dll
```

**Note**  It is unnecessary to include resource ID \#666 in the CSP DLL, or the signature in the registry, as was required for older CSP signatures.

 

## Additional Help and Support


Consult the [MSDN troubleshooting and support](http://msdn.microsoft.com/hh361695) page for additional help and support.

You can also check the [MSDN Application Security for Windows Desktop](http://social.msdn.microsoft.com/Forums/en-US/home?forum=windowssecurity) forum for assistance.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Authenticode%20Signing%20of%20Third-party%20CSPs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




