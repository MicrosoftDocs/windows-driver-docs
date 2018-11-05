---
title: Content Protection DDI
description: Content Protection DDI
ms.assetid: 770e0fce-d3b5-4599-8165-eadf3f23f9dc
keywords:
- protecting video content WDK Windows 7 display , Content Protection DDI
- protecting video content WDK Windows Server 2008 R2 display , Content Protection DDI
- video content WDK Windows 7 display , Content Protection DDI
- video content WDK Windows Server 2008 R2 display , Content Protection DDI
- video content WDK Windows Server 2008 R2 display , protecting
- Content Protection DDI WDK Windows 7 display
- Content Protection DDI WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Content Protection DDI


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The Content Protection DDI is an extension to the [Direct3D version 9 DDI](https://msdn.microsoft.com/library/windows/hardware/ff552927) to protect video. The Content Protection DDI consists of the entry points that are described in this section.

### <span id="required_content_protection_ddi_functions"></span><span id="REQUIRED_CONTENT_PROTECTION_DDI_FUNCTIONS"></span>Required Content Protection DDI Functions

If content protection is implemented in the user-mode display driver, the driver must support the following Content Protection DDI functions:

-   The [**CreateAuthenticatedChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540591) function creates a channel that the Direct3D runtime and the driver can use to set and query protections.

-   The [**AuthenticatedChannelKeyExchange**](https://msdn.microsoft.com/library/windows/hardware/ff538241) function negotiates the session key.

-   The [**QueryAuthenticatedChannel**](https://msdn.microsoft.com/library/windows/hardware/ff569213) function queries an authenticated channel for capability and state information.

-   The [**ConfigureAuthenticatedChannel**](https://msdn.microsoft.com/library/windows/hardware/ff539572) function sets state within an authenticated channel.

-   The [**DestroyAuthenticatedChannel**](https://msdn.microsoft.com/library/windows/hardware/ff552741) function releases resources for an authenticated channel.

-   The [**CreateCryptoSession**](https://msdn.microsoft.com/library/windows/hardware/ff540609) function creates a crypto session that the Direct3D runtime uses to manage a session key and to perform crypto operations into and out of protected memory.

-   The [**CryptoSessionKeyExchange**](https://msdn.microsoft.com/library/windows/hardware/ff540791) function negotiates the session key.

-   The [**DestroyCryptoSession**](https://msdn.microsoft.com/library/windows/hardware/ff552752) function releases resources for an encryption session.

### <span id="content_protection_capabilities"></span><span id="CONTENT_PROTECTION_CAPABILITIES"></span>Content Protection Capabilities

The user-mode display driver only reports content protection capabilities if it supports each of the preceding required Content Protection DDI functions. The following [**D3DDDICAPS\_TYPE**](https://msdn.microsoft.com/library/windows/hardware/ff544132) values are used by the Direct3D runtime to retrieve information about the content protection capabilities that the user-mode display driver supports. The runtime sets these D3DDDICAPS\_TYPE values in the **Type** member of the [**D3DDDIARG\_GETCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff543148) structure that the *pData* parameter of the driver's [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) function points to when the runtime calls **GetCaps**.

<span id="D3DDDICAPS_GETCONTENTPROTECTIONCAPS"></span><span id="d3dddicaps_getcontentprotectioncaps"></span>D3DDDICAPS\_GETCONTENTPROTECTIONCAPS  
The runtime supplies a pointer to a [**DDICONTENTPROTECTIONCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549568) structure for the specific encryption and decode combination that the driver should use. The driver returns a pointer to a populated D3DCONTENTPROTECTIONCAPS structure that describes the driver's content-protection capabilities for the encryption and decode combination. For more information about D3DCONTENTPROTECTIONCAPS, see the DirectX SDK documentation.

<span id="D3DDDICAPS_GETCERTIFICATESIZE"></span><span id="d3dddicaps_getcertificatesize"></span>D3DDDICAPS\_GETCERTIFICATESIZE  
The driver provides a pointer to a number that specifies the size, in bytes, of the driver's certificate that is used for a channel or crypto type. The Direct3D runtime then uses this size to allocate a buffer to hold the certificate information that the runtime receives when the runtime calls [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) with D3DDDICAPS\_GETCERTIFICATE.

<span id="D3DDDICAPS_GETCERTIFICATE"></span><span id="d3dddicaps_getcertificate"></span>D3DDDICAPS\_GETCERTIFICATE  
The runtime supplies a pointer to a [**DDICERTIFICATEINFO**](https://msdn.microsoft.com/library/windows/hardware/ff549552) structure that describes the certificate that the driver should retrieve.

For an authenticated channel, the driver uses the existing [OPM](opm-features.md) certificate, which is an X.509 certificate that is root signed by Microsoft.

An application can query the driver's certificate to determine the following information:

-   Whether the driver is trusted.

-   Whether the driver is revoked.

-   The driver's public key. The application uses the driver's public key to establish a session key for an authenticated channel that is used for authentication.

A call to [**GetCaps**](https://msdn.microsoft.com/library/windows/hardware/ff566762) with D3DDDICAPS\_GETCERTIFICATE set fails if called for the Direct3D 9 authenticated channel because this channel does not support a certificate or authentication.

For a crypto session, the driver returns its certificate for the given crypto type. Depending on the crypto type and the key exchange that are used, a certificate might or might not be used. It is also possible that different crypto types can use different certificates.

### <span id="optional_content_protection_ddi_functions"></span><span id="OPTIONAL_CONTENT_PROTECTION_DDI_FUNCTIONS"></span>Optional Content Protection DDI Functions

The driver can optionally support the following Content Protection DDI functions:

-   The [**EncryptionBlt**](https://msdn.microsoft.com/library/windows/hardware/ff564153) function reads encrypted data from a protected surface.

-   The [**GetPitch**](https://msdn.microsoft.com/library/windows/hardware/ff566799) function retrieves the pitch of a protected surface.

-   The [**StartSessionKeyRefresh**](https://msdn.microsoft.com/library/windows/hardware/ff569729) function returns a random number that the decoder/application and the driver/hardware can subsequently use to perform an exclusive OR operation (XOR) with the session key.

-   The [**FinishSessionKeyRefresh**](https://msdn.microsoft.com/library/windows/hardware/ff565671) function indicates that all buffers from that point in time will use the updated session key value.

-   The [**GetEncryptionBltKey**](https://msdn.microsoft.com/library/windows/hardware/ff566787) function returns the key that is used to decrypt the data that the driver's [**EncryptionBlt**](https://msdn.microsoft.com/library/windows/hardware/ff564153) function returns.

-   The [**DecryptionBlt**](https://msdn.microsoft.com/library/windows/hardware/ff551823) function writes data to a protected surface.

### <span id="content_protected_resources"></span><span id="CONTENT_PROTECTED_RESOURCES"></span> Content Protected Resources

The following [**D3DDDI\_RESOURCEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544644) flags are used by the Direct3D runtime for protected content. The runtime sets these D3DDDI\_RESOURCEFLAGS flags in the **Flags** member of the [**D3DDDIARG\_CREATERESOURCE**](https://msdn.microsoft.com/library/windows/hardware/ff542963) structure that the *pResource* parameter of the driver's [**CreateResource**](https://msdn.microsoft.com/library/windows/hardware/ff540688) function points to when the runtime calls **CreateResource**.

<span id="RestrictedContent"></span><span id="restrictedcontent"></span><span id="RESTRICTEDCONTENT"></span>**RestrictedContent**  
The resource might contain protected content. An application might or might not have explicitly enabled content protection before the application creates a resource. The driver should ensure that the runtime places the allocation for the resource in a memory pool that can be protected. The driver should allow the creation of lockable protected resources. However, the driver should explicitly fail the calls to its [**Lock**](https://msdn.microsoft.com/library/windows/hardware/ff568213) function to lock these surfaces while content protection is enabled.

<span id="RestrictSharedAccess"></span><span id="restrictsharedaccess"></span><span id="RESTRICTSHAREDACCESS"></span>**RestrictSharedAccess**  
Only specific processes should be allowed access to the shared resource.

The driver should restrict shared access to this resource. The runtime can only call the driver's [**OpenResource**](https://msdn.microsoft.com/library/windows/hardware/ff568611) function to open this resource with display devices (**hDevice**) within the process that created the resource or by those devices that were explicitly granted access via the authenticated channel.

 

 





