---
title: Using SetupAPI To Verify Driver Authenticode Signatures
description: Using SetupAPI To Verify Driver Authenticode Signatures
ms.assetid: 2019d77d-2d98-4bae-8d9d-aa41e47f3811
keywords: ["SetupAPI functions WDK , verifying signatures", "Authenticode signatures WDK", "signatures WDK , Authenticode", "digital signatures WDK , Authenticode", "verifying Authenticode signatures", "checking Authenticode signatures"]
---

# Using SetupAPI To Verify Driver Authenticode Signatures


## <a href="" id="ddk-using-setupapi-to-verify-driver-authenticode-signatures-dg"></a>


You can use the following procedures to verify that a driver has a valid Authenticode [digital signature](digital-signatures.md). These procedures are supported starting with Microsoft Windows Server 2003.

### To determine whether a driver has a valid Authenticode signature

Check the DNF\_AUTHENTICODE\_SIGNED flag.

If a driver has a valid Authenticode signature, Windows sets this flag in the **Flags** member of the driver node's [**SP\_DRVINSTALL\_PARAMS**](https://msdn.microsoft.com/library/windows/hardware/ff553290) structure. (Also be aware that Windows sets the DNF\_INF\_IS\_SIGNED flag if the driver has a [WHQL release signature](whql-release-signature.md), if it is a system-supplied driver, or if it has an Authenticode signature.)

### To verify that an INF file has a valid Authenticode signature

1.  Call the [INF file processing function](inf-file-processing-functions.md) **SetupVerifyInfFile**.

2.  Check the error code that was returned by the function.

    If the INF file is not system-supplied and does not have a valid WHQL digital signature, but it does have a valid Authenticode signature, **SetupVerifyInfFile** returns **FALSE** and [GetLastError](http://go.microsoft.com/fwlink/p/?linkid=169416) returns one of the following error codes:

    <a href="" id="error-authenticode-trusted-publisher"></a>ERROR\_AUTHENTICODE\_TRUSTED\_PUBLISHER  
    Indicates that the publisher is trusted because the publisher's certificate is installed in the [Trusted Publishers certificate store](trusted-publishers-certificate-store.md).

    <a href="" id="error-authenticode-trust-not-established"></a>ERROR\_AUTHENTICODE\_TRUST\_NOT\_ESTABLISHED  
    Indicates that trust cannot be automatically established because the publisher's signing certificate is not installed in the trusted publisher certificates store. However, this does not necessarily indicate an error. Instead it indicates that the caller must apply a caller-specific policy to establish trust in the publisher.

If the INF file has a valid Authenticode signature, **SetupVerifyInfFile** also returns the following information in the SP\_INF\_SIGNER\_INFO output structure:

-   The **DigitalSigner** member is set to the name of the signer.

-   The **CatalogFile** member is set to the full path of the corresponding signed catalog file.

However, be aware that **SetupVerifyInfFile** does not return the version in the **DigitalSignerVersion** member.

### To verify that a file has a valid Authenticode signature

Call the SetupAPI function **SetupScanFileQueue** by using the SPQ\_SCAN\_USE\_CALLBACK\_SIGNERINFO flag.

**SetupScanFileQueue** sends an SPFILENOTIFY\_QUEUESCAN\_SIGNERINFO request to the caller's callback routine and passes a pointer to a FILEPATHS\_SIGNERINFO structure. If a file is signed with a valid Authenticode signature, the function sets the error code to the appropriate ERROR\_AUTHENTICODE\_Xxx value before calling the callback routine for a file. The function also sets the following information in the FILEPATHS\_SIGNERINFO structure:

-   The **DigitalSigner** member is set to the name of the signer.

-   The **CatalogFile** member is set to the full path of the corresponding signed catalog file.

However, be aware that the version is not set in the **Version** member.

**SetupScanFileQueue** sets the ERROR\_AUTHENTICODE\_Xxx error code in the same way as described earlier in this topic for **SetupVerifyInfFile**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Using%20SetupAPI%20To%20Verify%20Driver%20Authenticode%20Signatures%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




