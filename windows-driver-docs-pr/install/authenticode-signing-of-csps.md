---
title: Authenticode Signing of Third-party CSPs
description: Third-party Authenticode signing for custom Cryptographic Service Providers (CSPs) has been available beginning with Windows Vista, and has been back ported to Windows XP SP3 and Windows Server 2003 SP2 as of May, 2013 via this download.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Authenticode Signing of Third-party Cryptographic Service Providers (CSPs)

Third-party Authenticode signing for custom Cryptographic Service Providers (CSPs) is available in Windows Vista and later.

Consequently, Microsoft will no longer sign CSPs, and the manual CSP signing service has been retired. Emails and CSPs sent to cspsign@microsoft.com or cecspsig@microsoft.com to be signed will no longer be processed by Microsoft.

Instead, all third-party CSPs can now be self-signed by following this procedure:

1. Purchase a code-signing certificate from a Certificate Authority (CA) for which Microsoft also issues a cross-certificate. The [Cross-Certificates for Kernel Mode Code Signing](cross-certificates-for-kernel-mode-code-signing.md) topic provides a list of CAs for which Microsoft also provides cross-certificates and the corresponding cross-certificates. Note that these are the only cross-certificates that chain up to the “Microsoft Code Verification Root” issued by Microsoft, which will enable Windows to run third-party CSPs.
2. After you have a certificate from the CA and the matching cross-certificate, you can use [**SignTool**](../devtest/signtool.md) to sign all your CSP binaries.
3. SignTool is included in the latest versions of Visual Studio. It is also included in the WDK version 7.0 and newer versions. Note that the SignTool that ships with earlier versions of the WDK is not compatible with cross-certificates and cannot be used to sign your binaries.

>[!NOTE]
>Starting with Windows 8, it is no longer a requirement that CSPs must be signed.

You can sign binaries from a command-line, or sign as an integrated build step in Visual Studio 2012 and newer.

The command to [**SignTool**](../devtest/signtool.md) is:

```cpp
signtool.exe sign /ac <cross-certificate_from_ms> /sha1 <sha1_hash> /t <timestamp_server> /d <”optional_description_in_double_quotes”> <binary_file.ext>
```

- <cross-certificate_from_ca> is the cross-certificate file you downloaded from Microsoft
- <sha1_hash> is the SHA1 thumbprint that corresponds to the code signing certificate
- <timestamp_server> is the server used to timestamp the signing operation
- <"optional_description_in_double_quotes"> is an optional friendly-name description
- <binary_file.ext> is the file to sign

For example:

```cpp
signtool.exe sign /ac certificate.cer /sha1 553e39af9e0ea8c9edcd802abbf103166f81fa50 /t "http://timestamp.digicert.com" /d "My Cryptographic Service Provider" csp.dll
```

>[!NOTE]
>It is unnecessary to include resource ID \#666 in the CSP DLL, or the signature in the registry, as was required for older CSP signatures.

## Additional Help and Support

You can try the [Application Security for Windows Desktop](https://social.msdn.microsoft.com/Forums/home?forum=windowssecurity) forum for assistance.
